
from flask import Flask, flash, redirect, request, render_template, get_flashed_messages
from crypt import methods
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so_secret'
# app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route('/forex-converter')
def home():
    return render_template ('forex_conv.html')

@app.route('/forex-converter/converted', methods = ['POST'])
def convert():
    c = CurrencyRates()
    cc = CurrencyCodes()
    amount = request.form['amount']
    currency_from = request.form['currencyA']
    currency_to = request.form['currencyB']
    symbol = cc.get_symbol(currency_to)
        
    # if isinstance(amount, float) == False:
    #     flash('Not a valid number')
    
    conversion_rate = c.get_rate(currency_from, currency_to)
    converted = int(amount) * float(conversion_rate)
    result = symbol + str(converted)
    flash('Your new amount is: ' + result)
    return redirect('/forex-converter')


