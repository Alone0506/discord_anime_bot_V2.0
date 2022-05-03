# web_spider_dict to txt and txt to web_spider_dict
from web_spider import Web_info


class Web_info2txt():
    def __init__(self):
        self.newanime_info = Web_info().newanime_info()
        self.renewlist_info = Web_info().renew()

    def newanime_info2txt(self):
        with open('newanime_info.txt', 'w+', encoding='utf-8') as f:
            for anime_name, info in self.newanime_info.items():
                f.write(anime_name+'\n')
                for i in range(len(info)):
                    f.write(info[i]+'\n')

    def renewlist_info2txt(self):
        with open('renewlist_info.txt', 'w+', encoding='utf-8') as f:
            for update_day, update_info in self.renewlist_info.items():
                f.write(update_day+'\n')
                for i in range(len(update_info)):
                    for j in update_info[i]:
                        f.write(j+'\n')


class Txt2web_info():
    def __init__(self):
        self.day = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']

    def txt2newanime_info(self):
        newanime_info_dict = {}
        with open('newanime_info.txt', 'r', encoding='utf-8') as f:
            info = f.readlines()
            for i in range(0, len(info), 6):
                values = [info[i+j].strip() for j in range(1, 6)]
                newanime_info_dict[info[i].strip()] = values
        print(newanime_info_dict)

    def txt2renewlist_info(self):
        renewlist_info_dict = {}
        with open('renewlist_info.txt', 'r', encoding='utf-8') as f:
            info = f.readlines()
            for i in range(len(info)):
                info[i] = info[i].strip()
                if info[i] in self.day:
                    values = []
                    j = 1
                    while info[i+j].strip() not in self.day:
                        values.append(info[i+j].strip())
                        j += 1
                        if i+j == len(info) - 1:
                            break
                    values = values
                    renewlist_info_dict[info[i]] = values

        print(renewlist_info_dict)


# a = Web_info2txt().newanime_info2txt()
# b = Web_info2txt().renewlist_info2txt()
# c = Txt2web_info().txt2newanime_info()
d = Txt2web_info().txt2renewlist_info()
