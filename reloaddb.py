from time import sleep
import sqloperations
import random

def cleardbTables():
    sqloperations.SqlOperation().cleardbTable("english_songs")
    sqloperations.SqlOperation().cleardbTable("hindi_songs")
    # pass

def repopulatedbTables():
    # Refreshing English Songs
    fp = open("eng_pls.txt")
    le=fp.readlines()
    random.shuffle(le)
    for u in le:
        sqloperations.SqlOperation().insertData('english_songs',u[:len(u)-1])
    fp.close()

    #Refreshing Hindi Songs
    fp = open("hin_pls.txt")
    lh=fp.readlines()
    random.shuffle(lh)
    for u in lh:
        print(u[:len(u)-1])
        sqloperations.SqlOperation().insertData('hindi_songs',u[:len(u)-1])
    fp.close()


if __name__ == "__main__":
    while True:
        cleardbTables()
        repopulatedbTables()
        print("sleeping....  *_*")
        sleep(60*60*6)   