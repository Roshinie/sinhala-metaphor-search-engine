import json

with open('./output2.json') as fp:
    data = json.load(fp)

with open('./song_lyrics2.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
