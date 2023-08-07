# newscrawl-tool
a simple Python function using the Newspaper3k library that would crawl a given URL or list of URLs, extracting all the relevant attributes.
# Python Web Crawler with Newspaper3k

This repository contains a simple web crawler implemented in Python, using the Newspaper3k library.

## Description

The crawler function can take either a single URL or a list of URLs and crawls each one, extracting various attributes such as authors, publish date, headline, text, top image, movies, keywords, summary, and the link itself. The extracted data is returned as a list of dictionaries, where each dictionary corresponds to an article.

## Prerequisites

Python 3.6 or higher is required to use this crawler. You also need to install the Newspaper3k library, which can be done via pip:

```shell
pip install newspaper3k
```

## Usage 
```shell
crawler = NewsCrawler(['https://example.com/news/article1', 'https://example.com/news/article2'], 'my_datasets')
crawler.crawl_news()
crawler.to_csv('output.csv')
```

