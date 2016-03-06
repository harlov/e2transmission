import sys
from .e_parser import TorrentParser


def main():
    if len(sys.argv) < 2:
        sys.exit('no enough args')

    if len(sys.argv) > 2:
            conf_path = sys.argv[2]
    else:
        conf_path = '/etc/e2transmission.json'

    if sys.argv[1] == 'start':
        parser = TorrentParser(is_daemon=True, config_path=conf_path)
        parser.start()

    if sys.argv[1] == 'stop':
        parser = TorrentParser(is_daemon=True, config_path=conf_path)
        parser.stop()

    if sys.argv[1] == 'run':
        parser = TorrentParser(config_path=conf_path)
        parser.run()
        parser.join()

if __name__ == '__main__':
    main()
