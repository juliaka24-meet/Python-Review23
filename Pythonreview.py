def create_youtube_video(title, description):
    dict_video = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}, "hashtag":[]}
    return dict_video

def like(dict_video):
    if "likes" in dict_video:
        dict_video["likes"]+=1
    return dict_video


def dislike(dict_video):
    if "dislikes" in dict_video:
        dict_video["dislikes"]+=1
    return dict_video

def add_comment(dict_video, username, comment_text):
    dict_video["comments"][username] = comment_text
    return dict_video


def add_list_desc(dict_video, list_desc):
    dict_video["hashtag"] = list_desc
    return dict_video


def compare_videos(list_dicts_video):
    list1 = list_dicts_video[0]["hashtag"]
    list2 = list_dicts_video[1]["hashtag"]
    similarity = 0
    for adj in list1:
        if adj in list2:
            similarity += 1
    sim_perc = similarity * 20
    sim_perc = str(sim_perc) + "%"
    return sim_perc


list_dicts_video = []

for i in range(2):
    list_desc = []
    username = input("username: ")
    title = input("title:")
    description = input("description: ")
    dict_video = create_youtube_video(title, description)
    for liking in range(495):
        dict_video = like(dict_video)
    dict_video = dislike(dict_video)
    comment_text = input("comment: ")
    dict_video = add_comment(dict_video, username, comment_text)
    for i in range(5):
        adj = input("describe the video in one word: ")
        list_desc.append(adj)
    dict_video = add_list_desc(dict_video, list_desc)
    list_dicts_video.append(dict_video)

print(list_dicts_video)

perc = compare_videos(list_dicts_video)
print("the similarity between the video is:",perc)




