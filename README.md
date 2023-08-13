# Python Web Crawler newscrawl-tool
a simple Python function using the Newspaper3k library that would crawl a given URL or list of URLs, extracting all the relevant attributes.

This repository contains a simple web crawler implemented in Python, using the Newspaper3k library.

## Description

The crawler function can take either a single URL or a list of URLs and crawls each one, extracting various attributes such as authors, publish date, headline, text, top image, movies, keywords, summary, and the link itself. The extracted data is returned as a list of dictionaries, where each dictionary corresponds to an article.
## Features

- Extracts a variety of attributes from each article:
  - Authors
  - Publish date
  - Headline
  - Text
  - Image
  - Movies (if any)
  - Keywords
  - Summary
  - Link
- Reads URLs from a YAML file, which can have separate sections for input and history URLs.
- Stores crawled URLs in history section to avoid re-crawling in future runs.
- Writes extracted data to a CSV file for further analysis.

## Output 

- Test example: [News - Victoria announces ban on gas connections to new homes from January 2024](https://www.theguardian.com/australia-news/2023/jul/28/victoria-announces-ban-on-gas-connections-to-new-homes-from-january-2024)



- Demo <br>![logging output](/images/repo/image_flask.png)

- CSV file output: <br>![csv output](/images/repo/image_2.png)

## Usage 
Insert news link or a list of news link into `urls.yaml` file.
![Example](/images/repo/image_1.png)
```shell
#python
python main.py -o my_output.csv

```

```shell
#flask 
python app.py
```
## Prerequisites

Python 3.6 or higher is required to use this crawler. You also need to install the a few library, which can be done via pip:

```shell
pip: -r requirements.txt
```
