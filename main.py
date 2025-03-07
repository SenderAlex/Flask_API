from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
   api_key = "ced3e5c2863a4637600d2d79c46177e4"
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   response = requests.get(url)
   return response.json()


def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])

def get_quotes():
   api_key = '2n6k3t/l+cDixm04d1JDZQ==Em46FSMeSW7BTkxV'
   url = 'https://api.api-ninjas.com/v1/quotes'
   response = requests.get(url, headers={'X-Api-Key': api_key})
   return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
   weather = None  # создаем функцию с переменной weather, где мы будем сохранять погоду
   news = []
   quotes = []
   if request.method == 'POST':
       city = request.form['city']  # этот определенный город мы будем брать для запроса API
       weather = get_weather(city)
       news = get_news()
       quotes = get_quotes()
   return render_template("index.html", weather=weather, news=news, quotes=quotes)


if __name__ == '__main__':
   app.run(debug=True)