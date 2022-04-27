from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
    return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
  <li><a href='/animals/dogs'>Dogs</a></li>
  <li><a href='/animals/cats'>Cats</a></li>
  <li><a href='/animals/rabbits'>Rabbits</a></li>
  <ul>

  '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
    tmp = '<ul>'

    for i, v in enumerate(pets[pet_type]):
        url = '/animals/' + pet_type + '/' + str(i)
        tmp += '<li><a href=' + url + '>' + v['name'] + '</a></li>'
    tmp += '</ul>'

    html = f'''{tmp}'''

    return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]

    return f'''
  <h1>{pet['name']}</h1>
  <img src={pet['url']}>
  <p>{pet['description']}</p>
  <ul>
  <li>{pet['breed']}</li>
  <li>{pet['age']}</li>
  </ul>
  '''

if __name__ == '__main__':
    app.run()
