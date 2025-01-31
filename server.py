from flask import Flask, render_template, request
from weather import  get_current_weather_byCity
# waitress is package help to deploy the flask in production mode
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])

def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    
    # check for empty string / string with spaces
    if not bool(city):
        city = "Mysore"
          
    weather_data = get_current_weather_byCity(city)
    return render_template('weather.html', 
                           title=city, 
                           status=weather_data['weather'][0]['main'], 
                           temp=f"{weather_data['main']['temp']:.1f}", 
                           feels_like=f"{weather_data['main']['feels_like']:.1f}")


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8000) # this is for development only
    serve(app, host='0.0.0.0', port=8000)

