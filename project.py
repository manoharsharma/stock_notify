from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to Stock Notifier App!'


def get_stock_data(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}'
    response = requests.get(url)
    # TODO: Process the response and return the stock data.


def send_notification(ticker, threshold, frequency, notification_type):
    # TODO: Retrieve stock data and process it to check if the stock's price reaches the threshold.
    # TODO: If the condition is met, send the notification via the specified notification type.
    pass


@app.route('/notify', methods=['GET', 'POST'])
def notify():
    if request.method == 'POST':
        ticker = request.form['ticker']
        threshold = request.form['threshold']
        frequency = request.form['frequency']
        notification_type = request.form['notification_type']

        send_notification(ticker, threshold, frequency, notification_type)

        return f'Notification has been set for {ticker} stock at {threshold} threshold with {frequency} frequency via {notification_type}.'

    return '''
        <form method="post">
            <label for="ticker">Enter Ticker Symbol:</label>
            <input type="text" id="ticker" name="ticker"><br><br>
            <label for="threshold">Enter Price Threshold:</label>
            <input type="text" id="threshold" name="threshold"><br><br>
            <label for="frequency">Select Frequency:</label>
            <select id="frequency" name="frequency">
                <option value="hourly">Hourly</option>
                <option value="daily">Daily</option>
            </select><br><br>
            <label for="notification_type">Select Notification Type:</label>
            <select id="notification_type" name="notification_type">
                <option value="email">Email</option>
                <option value="text_message">Text Message</option>
            </select><br><br>
            <input type="submit" value="Set Notification">
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
