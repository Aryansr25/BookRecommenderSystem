from flask import Flask, render_template
import pickle

popular_df = pickle.load(open('popular.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=popular_df['Book-Title'].to_list(),
                           author_name=popular_df['Book-Author'].to_list(),
                           image=popular_df['Image-URL-M'].to_list(),
                           votes=popular_df['num_ratings'].to_list(),
                           ratings=popular_df['avg_ratings'].to_list()
                           )


@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

if __name__ == '__main__':
    app.run(debug=True)
