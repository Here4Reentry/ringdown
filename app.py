from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    resp = twilio.twiml.Response()

    with resp.gather(numDigits=1, action='/handle_category', method='POST') as g:
        g.say('Press 1 for food, 2 for housing, 3 for resources.')

    return str(resp)


@app.route('/handle_category', methods=['GET', 'POST'])
def handle_category():
    digit_pressed = request.values.get('Digits', None)
    resp = twilio.twiml.Response()
    if digit_pressed == '1':
        pass
    elif digit_pressed == '2':
        pass
    elif digit_pressed == '3':
        pass
    else:
        return redirect('/')

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
