# by Pastel (some of the code was made by Karma/Jax/Nix too!), also make sure you have "requests" installed on your system.
import requests
import json

print("SandParser, by Pastel (Some of the code by Labbo-Lab)")
query = str(input("Search Keywords: "))

responsetext = requests.get("https://us-central1-sandtable-8d0f7.cloudfunctions.net/api/creations?title="+query).text
responsedict = json.loads(responsetext)

titleList = []
idList = []
urlList = []
timeStampList = []

i = 0
for item in responsedict:
    i += 1
    itemtitle = item["data"]["title"]
    itemid = item["data"]["id"]
    itemurl = "https://sandspiel.club/#"+item["data"]["id"]
    itemtimestamp = item["data"]["timestamp"]
    titleList.append(itemtitle)
    idList.append(itemid)
    urlList.append(itemurl)
    timeStampList.append(itemtimestamp)

i = 0
for item in titleList:
    print("Post "+str(i))
    print("  Title: "+item)
    print("  Post ID: "+idList[i])
    print("  Post URL: "+urlList[i])
    print("  Post date: "+timeStampList[i][:10])
    print("  Post time: "+timeStampList[i][12:19])
    print("\n")
    i+=1

input("Press enter to exit.")
