# All the game models will go here

from peewee import *
import datetime


DATABASE = SqliteDatabase('games.sqlite')


# Background-image, ratings, name, released, 'platforms' = that will be a string(For my model)
class Game(Model):
    name = CharField()
    background_image = CharField()
    ratings = DecimalField()
    released = DateTimeField(default=datetime.datetime.now)
    platforms = CharField()

    # convert game model to dictionary
    def json(self):
        return {
            "name": self.name,
            "background_image": self.background_image,
            "ratings": self.ratings,
            "released": self.released,
            "platforms": self.platforms
        }


    class Meta:
        database = DATABASE  #Connects to the Sqlite DATABASE
        # fields = ('name', 'background_image', 'ratings', 'released', 'platforms')

def initialize():
    DATABASE.connect()


    # need to create tables based on the Schema
    DATABASE.create_tables([Game], safe=True)
    print("Connected to the DB and created tables if they don't already exist")

    DATABASE.close()  # Don't leave DB connection open







# https://api.rawg.io/api/games?key=cc7a20c2a9db45bc8a0eb2994afda720&dates=2019-09-01,2019-09-30&platforms=18,1,7

# API Key = cc7a20c2a9db45bc8a0eb2994afda720
