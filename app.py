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
        response = requests.get('https://emojihub.yurace.pro/api/random')
        response.raise_for_status()
        # saves json response into variable
        data = response.json()
        category = data['category']
        unicode_list = data['unicode']
        emoji = chr(int(unicode_list[0].lstrip('U+'), 16))



    # Catches Error 500
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500

    # Catchall for other errors
    except Exception as err:
        return jsonify({'ERR':f'Other error occurred: {err}'}), 500

    # Returns data to the webpage
    return render_template('data.html', data=data, category=category, emoji=emoji, mimetype='text/html')

# Runs the app
if __name__ == '__main__':
    app.run(debug=True)