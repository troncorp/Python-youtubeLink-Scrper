import json
import os

def getSteamLink(link_id):
    link=f"https://youtu.be/{link_id}"
    try:
        os.system(f"youtube-dl -s -g --get-duration --get-thumbnail {link} > streamLink.txt")
        fp = open('streamLink.txt')
        tempLinks = fp.readlines()
        fp.close()
        os.system("rm -rf streamLink.txt")
        return tempLinks[2],tempLinks[1],tempLinks[3]
    except:
        return "None","NOT FOUND"


class VideoUrls():
    def getmetaData(self,url):
        link = url
        if link.find("watch?")!=-1:
            print("Please enter Proper Playlist link\nsimply the shareable link of complete playlist")
            exit(0)
        print("fetching metadata from youtube server...")
        try:
            os.system(f"youtube-dl -s --print-json --flat-playlist {link} > metadata.txt")
        except:
            print("Failed !!!")
            exit()
        print('Fetched... :-)')
        
        try:
            fp = open('metadata.txt')
            totalLinks = len(fp.readlines())
            fp.seek(0)
            processed = 0
            linkId=[]
            for line in fp:
                d = json.loads(str(line))
                title=d['title'].replace("'","").replace('"',"").replace("(","").replace(")","").replace("[","").replace("]","")
                if title == "Deleted video":continue
                print(f"Getting Audio stearm Link for :- {title} ;-)")
                print(f"{processed} out of {totalLinks}")
                thumbnailLink,audioStremLink,duration = getSteamLink(d['id'])
                processed+=1
                if thumbnailLink!="None" and audioStremLink!="NOT FOUND":
                    dataReq = [d['id'],title,thumbnailLink,audioStremLink,duration]
                    linkId.append(dataReq)
                else:
                    print("Invalid link or Video is removed form the youtube!!!")
            print(f"total link found:- {len(linkId)} ")
            fp.close()
            # os.system("rm -rf metadata.txt")
            return linkId
        except:
            print("Unable to Complet operation")
            return linkId