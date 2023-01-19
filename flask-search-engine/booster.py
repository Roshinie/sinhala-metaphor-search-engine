import json

def read_unique_vals(path):
    with open(path,'r') as f:
        json_data = json.loads(f.read())
        res_list = [i for n, i in enumerate(json_data) if i not in json_data[n + 1:]]
        return res_list

Lyricist_en = read_unique_vals("summary-corpus/Lyricist_en.json") #2
Lyricist_sn = read_unique_vals("summary-corpus/Lyricist_sn.json") #6
Composer_en = read_unique_vals("summary-corpus/Composer_en.json") #3
Composer_sn = read_unique_vals("summary-corpus/Composer_sn.json") #7
Singer_en = read_unique_vals("summary-corpus/Singer_en.json") #1
Singer_sn = read_unique_vals("summary-corpus/Singer_sn.json") #5

all_unique_data = [Lyricist_en,Lyricist_sn,Composer_en,Composer_sn,Singer_en,Singer_sn]
position_arr = [2,6,3,7,1,5]

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def boost_field(phrase):

    boost_array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1]

    if (isEnglish(phrase)):
        for field in range(0,4):
            boost_array[field] = 2
        boost_array[11] = 2
        boost_array[13] = 2
    else:
        for field in range(4,11):
            boost_array[field] = 2
        boost_array[12] = 2
        boost_array[14] = 2

    phrase_list = phrase.strip().split()

    for word in phrase_list:
        print(word)
        for i in range(0,6):
            if (any(word.lower() in x.lower()  for x in all_unique_data[i])):
                boost_array[position_arr[i]] = boost_array[position_arr[i]] + 1

    print(boost_array)

    return boost_array