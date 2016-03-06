import imaplib
import json
from email import parser
from .transmission_rpc import TransmissionRpc
from threading import Thread
import time
from .daemon import Daemon


class TorrentParser(Daemon, Thread):
    def __init__(self, config_path, is_daemon=False):
        if is_daemon:
            Daemon.__init__(self, pidfile='/tmp/e2transmission.pid')

        Thread.__init__(self)
        self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path) as conf_file:
            self.conf = json.load(conf_file)

    def run(self):
        print("running")
        self.transmission = TransmissionRpc(self.conf)
        self.connect_to_mail()
        while True:
            time.sleep(self.conf["email_check_interval"])
            self.run_update()

    def run_update(self):
        print("check email...")
        self.read_mails()

    def connect_to_mail(self):
        print('connect to %s' % (self.conf["email_host"], ))
        self.imap_conn = imaplib.IMAP4_SSL(
            self.conf["email_host"],
            self.conf["email_port"])
        self.imap_conn.login(
            self.conf["email_user"],
            self.conf["email_password"])
        self.imap_conn.select(self.conf["email_input_folder"])

    def read_mails(self):
        result, data = self.imap_conn.uid('SEARCH', None, '(UNSEEN)')
        ids = data[0]
        id_list = ids.split()
        for mid in id_list:
            result, data = self.imap_conn.fetch(mid, "(RFC822)")
            raw_email = data[0][1]
            self.proc_email(raw_email, mid.decode("utf-8"))

    def proc_email(self, message, mail_id):
        msg = parser.Parser().parsestr(message.decode("utf-8"))
        for part in msg.walk():
            if part.get_content_type() == 'application/x-bittorrent':
                torrent_data_64 = part.get_payload()
                self.transmission.request(
                    "torrent-add",
                    {"metainfo": torrent_data_64}
                )
                print(" torrent added")
