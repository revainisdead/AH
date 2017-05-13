# Goal: let app run in any directory
#
# set BASE_DIR = "current directory"
# os.getcwd = setup



class DBManager:
    """ Allowed to talk to the Db
    Clients must communicate with the Manager.
    """
    def __init__(self):
        db = Database()


    def add_auction(self): pass



class Database:
    """ Database for auction house

    Uses text files
    """
    def __init__(self):
        pass

    # should access files directly
    def retrieve(self, item):
        pass

    def remove(self, name):
        pass




# Let "auction" determine buyout
# Set bought on item
# 
# Update item in database
