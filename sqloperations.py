import util
import scrapLinks

sqlobj = util.ConnectToDB().connect()
cur = sqlobj.cursor()

class SqlOperation():
    def cleardbTable(self, tableName):
        print(f"Clearing Table {tableName}...")
        cur.execute(f"TRUNCATE TABLE {tableName}")
        sqlobj.commit()
        print("cleared #_#")

    def insertData(self, tableName, url):
        
        dataToBeEntered = scrapLinks.VideoUrls().getmetaData(url)
        
        for i in dataToBeEntered:
                try:
                    #delete from streamer.english_songs where english_songs.id = "_83KqwEEGw4";
                    query = f"DELETE FROM {tableName} WHERE id = '{i[0]}'"
                    cur.execute(query)
                    query = f"INSERT INTO {tableName} VALUES ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}')"
                    cur.execute(query)
                except Exception as e:
                    print("Link Already exist or Unable to enter ;-)")
                    print(e)

        sqlobj.commit()
        print("All changes save to Database ^_^ \nEnjoy your Day!!!")