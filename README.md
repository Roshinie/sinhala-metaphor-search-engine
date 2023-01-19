# Sinhala Metaphor Search Engine

This repository includes all the implmentation codes for the sinhala metaphor search engine. This is implemented with elastic search, Flask API, python, HTML, Bootstrap. 

This repository is structured as follows

- Final Corpus
- Search Engine 
- Lyrics Crawler
- Utils for data processing

## Data Corpus
---
The final data corpus contains the following data fields
1. Song Title in Sinhala
2. Song Title in English
3. Singer in Sinhala
4. Singer in English
5. Lyricits in Sinhala
6. Lyricits in English
7. Composer in Sinhala
8. Composer in English
9. Song Lyrics
10. Metaphor
11. Metaphor source domain in Sinhala
12. Metaphor source domain in English
13. Metaphor target domain in Sinhala
14. Metaphor target domain in English
15. Interpretation
16. Views

## Web Crawler
---
For the web crawling Scrapy is used. Songs are crawled from the following sites and manually processed further

1. [http://lyricslk.com/](http://lyricslk.com/)
2. [https://sinhalasongbook.com](https://sinhalasongbook.com)

## Search Engine
---
For building the search engine Elastic Search and Kibana is used. Elasticsearch is a RESTful distributed search engine. It is Java-based and can search and index document files in diverse formats. Kibana is an open-source data visualization and exploration tool that is specialized for large volumes of streaming and real-time data.
