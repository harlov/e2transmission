# Email2Transmission service

Daemon, what check email box(over IMAP) for new messages with torrents file's - and send them to transmission daemon.

## Install

1. `pip install e2transmission`
2. configure `/etc/e2transmission.json` - pass you email and daemon settings
3. `e2transmission-cli start` - run daemon