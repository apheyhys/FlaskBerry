from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


def log_request(req, res):
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase = phrase, the_letters = letters, the_results = results, the_title = title,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)