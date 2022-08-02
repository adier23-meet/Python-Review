def creat_youtube_channel(title, description):
	dict1 = {"title": title,
	"description": description, 
	"likes": 0, 
	"dislikes": 0, 
	"comments": {}}
	return dict1


def like (dict1):
	if "likes" in dict1:
		dict1["likes"] += 1
	return dict1


def dislike(dict1):
	if "dislikes" in dict1:
		dict1["dislikes"] += 1
	return dict1


def add_comment(youtubevideo, username, comment):
	youtubevideo["comments"][username] = comment
	return youtubevideo



newvid = creat_youtube_channel("v", "j")

newvid = like(newvid) 
print(newvid)