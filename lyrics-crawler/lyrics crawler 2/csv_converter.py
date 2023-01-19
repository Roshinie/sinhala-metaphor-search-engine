import pandas as pd

input_json_file='song_lyrics_1.json'
output_csv_file='csv_file_1.csv'
with open(input_json_file, 'r', encoding="utf-8") as inputfile:
    df = pd.read_json(inputfile)

df.to_csv(output_csv_file, index=False) 