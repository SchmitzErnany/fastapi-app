#%%
import os
import mongoengine


class Mongodb():

    def __init__(self):
        user = os.environ.get('MONGODB_USER')
        password = os.environ.get('MONGODB_PASSWORD')
        url = os.environ.get('MONGODB_URL')
        port = os.environ.get('MONGODB_PORT')
        database = os.environ.get('MONGODB_DATABASE')

        self.host = f"mongodb://{user}:{password}@{url}:{port}/{database}"

    def create_connection(self):
        try:
            mongoengine.connect(host=self.host)
            print("MongoDB Connection Succeeded.")
        except:
            print(f"Error in DB connection.")
            
        print(self.host)
        return self.host
