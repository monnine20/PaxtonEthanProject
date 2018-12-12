#Ethan Monnin and Paxton Caldwell
#This code takes a python version of the twitch api, grabs information and performs
#different queries to manipualte the data into something more meaningful
from twitch import TwitchClient

#Grabs twitch client object
client = TwitchClient(client_id='s81q68ulo4c8y5s9iqvobsole69ck9')

#Gets top 100 games
games = client.games.get_top(limit = 100)

#Gets all total number of viewers and streams across twitch
summary = client.streams.get_summary()

#Gets up to 100 featured streams
featured = client.streams.get_featured(limit = 100)

#Gets top 100 live streams
liveStreams = client.streams.get_live_streams(limit = 100)

#Gets top 100 clips from past week
topClips = client.clips.get_top(limit = 100)

#Gets top 100 videos from past week
topVideos = client.videos.get_top(limit = 100)

#1
#This first section will make a dictionary of the top 100 games and get a ratio 
#compared to all of twitch for viewers and channels
totalViewers = summary['viewers']
totalStreams = summary['channels']
ratio_dict ={}
for i in range(0,len(games)):
	gameid = games[i]['game']['name']
	gameviewers = games[i]['game']['popularity']
	ratiov = gameviewers / totalViewers * 100
	ratiov = round(ratiov, 2)
	gamestreams = games[i]['channels']
	ratioc = gamestreams / totalStreams * 100
	ratioc = round(ratioc, 2)
	ratio_dict[gameid] = {str(ratiov) + '%' + " of viewers", str(ratioc) + "%" + " of streams"}
print("\nratio_dict:")
print(ratio_dict)

#2
#This next section will compare the top 100 games in Videos/Streams/Clips in each category

#CountIncategory gets a dictionary of one of Videos/Clips/Streams and returns a dictionary
#With the amount of times a game appears in each
def countIncategory(gamedict):
	returndict = {}
	for i in range(0,100):
		cursor = gamedict[i]['game']
		if cursor in returndict.keys():
			returndict[cursor] = returndict[cursor] + 1
		else:
			returndict[cursor] = 1
	return returndict

#codenseNames takes 3 dictionary and narrows their keys into one list
def condenseNames(gamedict1,gamedict2,gamedict3):
	returndict = []
	for name in gamedict1.keys():
		returndict.append(name)
	for name in gamedict2.keys():
		if name not in returndict:
			returndict.append(name)
	for name in gamedict3.keys():
		if name not in returndict:
			returndict.append(name)
	return returndict

#checkValid takes a string and a dict and check whether that string is a key in the dict
#if it is it will return the value at that dict which is an int otherwise
# it will return a string 0 since it is not in the dictionary
def checkvalid(name, dict):
	if name in dict.keys():
		return str(dict[name])
	else:
		return str(0)


top100compare = {}
videoDict = countIncategory(topVideos)
clipDict = countIncategory(topClips)
streamDict = countIncategory(liveStreams)
allNames = condenseNames(videoDict,clipDict,streamDict)

for name in allNames:
	top100compare[name] = {checkvalid(name,videoDict) + " videos", 
							checkvalid(name,clipDict) + " clips", 
							checkvalid(name,streamDict) + " streams"}
print("\ntop100compare:")
print(top100compare)

#3
#This next session will take the 100 streams and clips and return a list of people who
#appear in both

#collects the number of time a channel is in the top 100 videos of the week
videoChannelCount = {}
for i in range(0,100):
	cursor = topVideos[i]['channel']['name']
	if cursor in videoChannelCount.keys():
		videoChannelCount[cursor] = videoChannelCount[cursor] + 1
	else:
		videoChannelCount[cursor] = 1

#collects the number of time a channel is in the top 100 clips of the week
clipChannelCount = {}
for i in range(0,100):
	cursor = topClips[i]['broadcaster']['name']
	if cursor in clipChannelCount.keys():
		clipChannelCount[cursor] = clipChannelCount[cursor] + 1
	else:
		clipChannelCount[cursor] = 1

appearsmorethanonce = {}
allChannelNames = condenseNames(clipChannelCount, videoChannelCount, {})
for name in allChannelNames:
	if ((1 <= int(checkvalid(name,clipChannelCount))) and (1 <= int(checkvalid(name, videoChannelCount)))):
		appearsmorethanonce[name] = {str(checkvalid(name,clipChannelCount)) + " Clips",
									str(checkvalid(name,videoChannelCount)) + " videos"}
print("\nappearsmorethanonce:")
print(appearsmorethanonce)

#4 part 1
#This next section compare the up to 100 featured streams to the top 100 livestreams
#The first part will compute the average viewers of the featured
#The second part will compute a dictionary of a Lists that holds the total number
#of streams in a game in the top 100 and featured,
#the number of total viewers in the top 100 and featured of a game
#and the average number of viewers in the top 100 and featured for game

totalViewersFeatured  = 0
for cursor in featured:
	addVal = cursor['stream']['viewers']
	totalViewersFeatured = totalViewersFeatured + int(addVal)

totalViewersTopStreams = 0
for cursor in liveStreams:
	addVal = cursor['viewers']
	totalViewersTopStreams = totalViewersTopStreams + int(addVal)

avgValStream = (totalViewersTopStreams / 100)
avgValFeatured = (totalViewersFeatured / len(featured))
print("\navgValStream:")
print(avgValStream)
print("\navgValFeatured:")
print(avgValFeatured)

#4 part 2
#this function takes two dictionaries and combines the total number of streams
#in a game 
def countNames(topStreamDict ,featuredDict):
	returndict = {}
	for i in range(0,100):
		cursor = topStreamDict[i]['game']
		if cursor in returndict.keys():
			returndict[cursor] = returndict[cursor] + 1
		else:
			returndict[cursor] = 1
	for i in range(0,len(featuredDict)):
		cursor = featuredDict[i]['stream']['game']
		if cursor in returndict.keys():
			returndict[cursor] = returndict[cursor] + 1
		else:
			returndict[cursor] = 1
	return returndict

#gets the total number of views for games in the top 100 and featured
def countViews(topStreamDict ,featuredDict):
	returndict = {}
	for i in range(0,100):
		cursor = topStreamDict[i]
		if cursor['game'] in returndict.keys():
			returndict[cursor['game']] = returndict[cursor['game']] + int(cursor['viewers'])
		else:
			returndict[cursor['game']] = int(cursor['viewers'])
	for i in range(0,len(featuredDict)):
		cursor = featuredDict[i]['stream']
		if cursor['game'] in returndict.keys():
			returndict[cursor['game']] = returndict[cursor['game']] + int(cursor['viewers'])
		else:
			returndict[cursor['game']] = int(cursor['viewers'])
	return returndict

#This function will output a list with
#(# of streams with name, # of viewers on streams with game name, avg viewers with game name )
def ComputesAvgList(totalG, totalV, names):
	returndict = {}
	for name in names:
		list = ['Total streams: ' + str(totalG[name]),
				'Total views: ' + str(totalV[name]),
				'Average views a stream: ' + str(totalV[name] / totalG[name])]
		returndict[name] = list
	return returndict

totalGames = countNames(liveStreams,featured)
totalViews = countViews(liveStreams,featured)
nameList = condenseNames(totalGames,totalViews,{})
gameinfodict = ComputesAvgList(totalGames,totalViews,nameList)
print("\ngameinfodict:")
print(gameinfodict)
