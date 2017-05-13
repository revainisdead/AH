from ah.db import DBManager

from ah.auctionhouse.client import AHClient


class AHServer:
    def __init__(self, host):
        self.host = host
        self.db = DBManager()


    def run():
        # server loop
        pass

    def clean_auctions():
        # Search for bought auctions
        # remove them by talking to DBManager
        pass


def main():
    print("Creating AH server . . .")
    server = AHServer("localhost")

    client = AHClient()

    # test db


if __name__ == "__main__":
    main()
