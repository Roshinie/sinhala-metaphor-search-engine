import json

with open('./all_songs.json') as fp:
    data = json.load(fp)

with open('./test_song_corpus.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
