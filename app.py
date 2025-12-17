from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

# - Homepage
@app.route('/')
def home():
    return "This is some example data :)"

# WRN: App routes must start with a forward slash
# - Data page that displays data from the API
@app.route('/api/data')
def get_data():
    try:
        # Attempts to get the data from the API link
        # https://www.themoviedb.org/u/nickscrumpets
        # 22548726

        url = "https://api.themoviedb.org/3/account/YOUR_ACCOUNT_ID_HERE"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer PUT_YOUR_API_KEY_HERE"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        username = data['username']
        name = data['name']
        img = data['avatar']['tmdb']['avatar_path']
        #tmdb = data['tmdb']
        profile_url = "https://media.themoviedb.org/t/p/w300_and_h300_face"

        theimage = profile_url + img

        print(theimage)



        #response = requests.get('https://api.themoviedb.org/3/movie/latest?api_key=a2aca971ecc30ef8a0cc14d8e1895ab8')

        # saves json response into variable
        #data = response.json()
        #title = data['title']



    # Catches Error 500
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500

    # Catchall for other errors
    except Exception as err:
        return jsonify({'ERR':f'Other error occurred: {err}'}), 500

    # Returns data to the webpage
    return render_template('data.html',name=name,img=img,theimage=theimage, username=username, data=data, mimetype='text/html')

# Runs the app
if __name__ == '__main__':
    app.run(debug=True)