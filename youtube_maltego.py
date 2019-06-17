#!/usr/bin/env python
import sys
from googleapiclient import discovery

# Google API Key
DEVELOPER_KEY = ""

def getResults(videoId, pageToken=""):

    api_service_name = "youtube"
    api_version = "v3"

    youtube = discovery.build(
        api_service_name,
        api_version,
        developerKey=DEVELOPER_KEY,
    )

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=videoId,
        pageToken=pageToken,
        maxResults=100
    )

    response = request.execute()

    return response

def processResults(data, response):

    for entry in response["items"]:

        authorDisplayName = entry["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        authorChannelUrl = entry["snippet"]["topLevelComment"]["snippet"]["authorChannelUrl"]
        textDisplay = entry["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

        if authorChannelUrl not in data:
            data[authorChannelUrl] = {"authorDisplayName": authorDisplayName,
                                      "textDisplay": textDisplay}

    return data

def CLIMessage(data):

    for entry in data:
        print("%s|||%s|||%s" % (entry,data[entry]["authorDisplayName"],data[entry]["textDisplay"]))

    return

def maltegoMessage(data):

    # Header
    print("""<MaltegoMessage>
        <MaltegoTransformResponseMessage>
            <Entities>
    """)

    for entry in data:
        print("""                    <Entity Type="maltego.Alias">
                    <Value>%s</Value>
                    <Weight>100</Weight>
                </Entity>
        """ % (entry,
               #data[entry]["textDisplay"],
               #data[entry]["authorDisplayName"]
               )
        )

    print("""            </Entities>
            <UIMessages>
            </UIMessages>
        </MaltegoTransformResponseMessage>
    </MaltegoMessage>
    """)

    return

def main():

    videoId = sys.argv[1].split("=")[1]

    data = {}

    response = getResults(videoId)
    data = processResults(data, response)

    while "nextPageToken" in response:
        response = getResults(videoId, response["nextPageToken"])
        data = processResults(data, response)

    # For Maltego ->
    maltegoMessage(data)

    # For general CLI (if too many nodes, this is ideal) ->
    #CLIMessage(data)

    return

if __name__ == "__main__":
    main()