from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = f"<h1><a href={url_for('godzilla')}>Vasii Alexandru 441D - Godzilla</a></h1>"
    return ret


@app.route('/godzilla', methods=['GET'])
def godzilla():
    return render_template('/Gabriel/godzilla.html')

@app.route('/description')
def description():
    return render_template('/Gabriel/description.html')

@app.route('/trailer')
def trailer():
    return render_template('/Gabriel/trailer.html')

if __name__ == '__main__':
    app.run(debug=True)


