import json

with open('./output_1.json') as fp:
    data = json.load(fp)

with open('./song_lyrics_1.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
