#Ethan Monnin and Paxton Caldwell
#Implement Later
from twitch import TwitchClient

client = TwitchClient(client_id='s81q68ulo4c8y5s9iqvobsole69ck9')
channel = client.channels.get_by_id(44322889)

print(channel.id)
print(channel.name)
print(channel.display_name)

# Gets top games
games = client.games.get_top()
#Gets top game name
games[0]['game']['name']
#Gets top games names total viewers
games[0]['game']['popularity']


# Gets all featured streams
allchannels = client.streams.get_featured()
allchannels[0]['title']

#Gets all live streams
liveStreams = client.streams.get_live_streams()
#game
liveStreams[0]['game']
#viewers
liveStreams[0]['viewers']
#channel and name
liveStreams[0]['channel']['name']


# Gets all total number of viewers and streams across twitch
summary = client.streams.get_summary()
print(summary)

#top Videos will get the top VIDEO of the last week
topVideos = client.videos.get_top(10, 0)
#Gets title of video
topVideos[0]['title']
# # of views on the video
topVideos[0]['views']
# name of game in the video
topVideos[0]['game']

for i in range (0,10):
	print(topVideos[i]['game'])
	print(topVideos[i]['views'])
	print(topVideos[i]['title'])

#Gets top clips
topClips = client.clips.get_top()
#game
topClips[0]['game']
#number of views
topClips[0]['views']
#duration of video
topClips[0]['duration']
#title
topClips[0]['title']
#Name of person/account
topClips[0]['broadcaster']

for i in range (0,10):
	print(topClips[i]['game'])
	print(topClips[i]['views'])
	print(topClips[i]['title'])
	print(topClips[i]['duration'])
	print(topClips[i]['broadcaster'])
	print("")
