import sys
from flask import Flask, url_for
from flask import render_template
import app.lib.description as dscr
import app.lib.rating as rate
import app.tests.test_Lotr as tst
import pytest

#from app.lib import network
#from app.lib import linux
#from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

print(tst.test_rating())

from app.lib import biblioteca_filme

actiune_iron_man = biblioteca_filme.actiune_iron_man()
distributie_iron_man = biblioteca_filme.distributie_iron_man()

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TESTING'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/index_Lotr")
def home():
    description = dscr.returneaza_descriere()
    rating = rate.returneaza_rating()
    return render_template("index_Lotr.html", description = description, rating = rating)


@app.route("/cast_Lotr")
def cast():
    return render_template("cast_Lotr.html")

@app.route("/description_Lotr")
def description():
    return render_template("description_Lotr.html")

@app.route("/iron_man", methods=['GET'])
def iron_man():
  ret = "<h1>Iron Man</h1><br>"
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"  
  ret += f"<h2><a href={url_for('distributie')}>Distributie</a></h2>"
  return ret  
	
@app.route("/iron_man/distributie", methods=["GET"])
def distributie():
  ret = "<h1>Distributie</h1>"
  ret += f"<h2><a href={url_for('iron_man')}>Iron Man</a></h2> "
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"
  ret += distributie_iron_man
  return ret
  
@app.route("/iron_man/actiune", methods=["GET"])
def actiune():
  ret = "<h1>Actiune</h1>"
  ret += f"<h2><a href={url_for('iron_man')}>Iron Man</a></h2>"
  ret += f"<h2><a href={url_for('distributie')}>Distrinutie</a></h2>"
  ret += actiune_iron_man
  return ret

@app.route("/mazerunner", methods=['GET'])
def maze_runner():
    return render_template('/Octavian/mazerunner.html')

@app.route("/mazerunner/trailer", methods=['GET'])
def maze_runner_trailer():
    return render_template('/Octavian/mazerunner-trailer.html')

@app.route("/mazerunner/description", methods=['GET'])
def maze_runner_description():
    return render_template('/Octavian/mazerunner-description.html')

## Vasii Gabriel
@app.route('/godzilla', methods=['GET'])
def godzilla():
    return render_template('/Gabriel/godzilla.html')

@app.route('/description')
def description_godzilla():
    return render_template('/Gabriel/description.html')

@app.route('/trailer')
def trailer():
    return render_template('/Gabriel/trailer.html')

@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """

    errno = pytest.main(["-x", "app/tests"])
    sys.exit(errno)
    #sys.exit(pytest.main(["."]))

if __name__ == '__main__':
   app.run(debug=True)
   sys.exit(pytest.main(["app/tests"]))
