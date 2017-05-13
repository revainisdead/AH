import src.db.db

import client


class AHServer:
    def __init__(self, host):
        self.host = host
        self.db = src.db.db.DBManager()


    def run():
        # server loop
        pass

    def clean_auctions():
        # Search for bought auctions
        # remove them by talking to DBManager
        pass


def main():
    # manage server
    ah = AHServer("localhost")

    ahc = client.AHClient()

    # test db


if __name__ == "__main__":
    main()
