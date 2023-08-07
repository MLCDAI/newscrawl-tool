import os
import pandas as pd
from newspaper import Article
from typing import Union, List
import yaml
import nltk
import argparse


class NewsCrawler:
    def __init__(self, yaml_file: str, output_dir='datasets'):
        self.urls = []
        self.yaml_file = yaml_file
        self.output_dir = output_dir
        self._create_output_dir()

    def _create_output_dir(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def read_urls_from_yaml(self):
        with open(self.yaml_file, 'r') as file:
            data = yaml.safe_load(file)
            self.urls = data.get('input', [])
            self.history_urls = data.get('history', [])

    def crawl_news(self):
        data = []
        try:
            for url in self.urls:
                article = Article(url)
                article.download()
                article.parse()
                article.nlp()

                data.append({
                    "authors": article.authors,
                    "publish_date": article.publish_date,
                    "headline": article.title,
                    "text": article.text,
                    "image": article.top_image,
                    "movies": article.movies,
                    "keywords": article.keywords,
                    "summary": article.summary,
                    "link": url,
                })
        except Exception as e:
            print(f"Failed to process url {url}. Error: {str(e)}")

        self.data = data

    def update_urls_to_yaml(self):
        # Move input urls to history and sort
        self.history_urls += self.urls
        self.history_urls = sorted(list(set(self.history_urls)))

        # Clear input urls
        self.urls = []

        # Update yaml file
        data = {
            "input": self.urls,
            "history": self.history_urls
        }
        with open(self.yaml_file, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)

    def to_csv(self, filename):
        if hasattr(self, 'data'):
            df = pd.DataFrame(self.data)
            file_path = os.path.join(self.output_dir, filename)
            df.to_csv(file_path, index=False)
        else:
            print("No data to write. Use crawl_news method to get data.")

    def download_nltk_packages(self):
        """
            Download necessary NLTK packages for Newspaper3k library.
        """
    try:
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
        print("NLTK packages downloaded successfully.")
    except Exception as e:
        print(f"Error during NLTK packages download: {str(e)}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NewsCrawler for extracting news article data.")
    
    # Add argument for the output CSV filename
    parser.add_argument('--output', '-o', type=str, default='example.csv', 
                        help='Name of the output CSV file. Default is "example.csv".')
    
    # Parse the arguments
    args = parser.parse_args()
    
    crawler = NewsCrawler('urls.yaml', 'my_datasets')
    #crawler.download_nltk_packages()
    crawler.read_urls_from_yaml()
    crawler.crawl_news()
    crawler.update_urls_to_yaml()
    crawler.to_csv('args.output')
