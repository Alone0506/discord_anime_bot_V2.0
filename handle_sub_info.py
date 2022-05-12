from collections import defaultdict


class Handle_sub_info():
    def __init__(self):
        self.info_dict = defaultdict(list)

    def txt2dict(self):
        with open('sub_info.txt', 'r', encoding="utf-8") as f:
            infos = f.readlines()

            for info in infos:
                user_id = info.strip().split(" ", 2)[0]
                episode = info.strip().split(" ", 2)[1]
                anime_name = info.strip().split(" ", 2)[2]
                self.info_dict[user_id].append([episode, anime_name])
                

    def dict2txt(self, _dict: dict):
        with open('sub_info.txt', 'w+', encoding="utf-8") as f:
            f.read()
            f.seek(0)
            f.truncate(0)
            for user_id in _dict:
                for episode, anime_name in _dict[user_id]:
                    f.write(f"{user_id} {episode} {anime_name}\n")
                    

    def issub(self, user_id: str, episode: str, anime_name: str):
        self.txt2dict()
        if user_id in self.info_dict and [episode, anime_name] in self.info_dict[user_id]:
            return True
        return False
