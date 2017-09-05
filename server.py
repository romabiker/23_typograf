from flask import (
                   Flask,
                   render_template,
                   request,
                   )


import typograf


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    incoming = request.form.get('text')
    res_text = ''
    if incoming:
        res_text = typograf.prepare_text(incoming)
    return render_template('form.html', result_text=res_text)


if __name__ == "__main__":
    app.run(debug=True)
