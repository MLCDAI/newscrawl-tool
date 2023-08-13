import os


from dotenv import load_dotenv

from flask import Flask, render_template,send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from news_crawler import NewsCrawler, Timer

# 加载环境变量
load_dotenv()

app = Flask(__name__)
os.environ['FLASK_DEBUG'] = '1'
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

# 定义表单类
class LinkForm(FlaskForm):
    link = StringField('Link', [validators.DataRequired()])



@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    rows = []
    elapsed_time = 0
    filename = "default.csv"
    

    # 创建新闻爬虫实例
    crawler = NewsCrawler('urls.yaml', 'my_datasets')
    
    if form.validate_on_submit():
        links = [link.strip() for link in form.link.data.split(',')]
        for link in links:
            crawler.urls.append(link)

        timer = Timer()
        crawler.crawl_news()
        crawler.update_urls_to_yaml()
        
        # Save the result data to CSV
        rows,filename = crawler.to_index()  
        print(filename)

        elapsed_time = "{:.4f}".format(timer.stop())
    return render_template('index.html', form=form, 
                           rows=rows, show_table=bool(rows), 
                           filename = filename,
                           elapsed_time=elapsed_time, 
                           max_time=600)

@app.route('/download-csv/<filename>')
def download_csv(filename):
    return send_from_directory('my_datasets', filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
