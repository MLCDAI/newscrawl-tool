from flask import Flask, Response, render_template, request, send_from_directory
from news_crawler import NewsCrawler
from flask_wtf import FlaskForm
from wtforms import StringField, validators
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
os.environ['FLASK_DEBUG'] = '1'
# Assuming you'd add this back later
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

class LinkForm(FlaskForm):
    link = StringField('Link', [validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    crawler = NewsCrawler('urls.yaml', 'my_datasets')  # Define this outside the if block
    show_table = True
    rows = []
    if form.validate_on_submit():
        print("Form is validated.")
        links = form.link.data.split(',')  # split by lines to support multiple links
        for link in links:
            print(f"Crawling: {link}")
            crawler.urls.append(link.strip())
        crawler.crawl_news()
        crawler.update_urls_to_yaml()

        filename = "news.csv"
        crawler.to_csv(filename)

        # Reading the CSV to show in the HTML table
        with open(os.path.join("my_datasets", filename), 'r') as file:
            csv_data = file.read()
        rows = [row.split(",") for row in csv_data.split("\n")]
        if rows:
            show_table = True
    else:
        print(form.errors)
    return render_template('index.html', form=form, rows=rows, show_table=show_table)

@app.route('/download-csv')
def download_csv():
    return send_from_directory(directory='my_datasets', filename="news.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
