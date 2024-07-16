from flask import Flask, request, render_template_string, redirect, url_for, session
import process_bill

app = Flask(__name__)
app.secret_key = '255e4f1849aa3412e170ad559d2c4cb8'  # Required for session management

# HTML template with form and results
template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>POS System</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
    <h1>Foodies Express POS System</h1>
    <p> First <b>Add Payment</b> then click on <b>Finalize bill</b> to get Final bill Thank you</p>
    <form method="POST" >
      <label for="amount">Enter Amount (before tax):</label><br>
      <input type="text" id="amount" name="amount"><br>
      <label for="payment_method">Enter Method of Payment [CASH/DEBIT/CREDIT]:</label><br>
      <input type="text" id="payment_method" name="payment_method"><br>
      
      <input type="submit" value="Add Payment">
    </form>

    <form method="POST" action="{{ url_for('finalize') }}">
      <input type="submit" style="margin-top:6px;" value="Finalize Bill">
    </form>

    {% if payments %}
        <h2>Current Payments:</h2>
        <ul>
        {% for payment in payments %}
            <li>Amount: {{ payment['amount'] }} - Method: {{ payment['payment_method'] }}</li>
        {% endfor %}
        </ul>
    {% endif %}

    {% if result %}
        <h2>Final Bill:</h2>
        <p>{{ result|safe }}</p>
    {% endif %}
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'payments' not in session:
        session['payments'] = []

    if request.method == 'POST':
        amount = request.form['amount']
        payment_method = request.form['payment_method'].upper()
        session['payments'].append({'amount': amount, 'payment_method': payment_method})
        session.modified = True

    return render_template_string(template, payments=session['payments'])

@app.route('/finalize', methods=['POST'])
def finalize():
    payments = session.get('payments', [])
    results = [process_bill.process_payment(p['amount'], p['payment_method']) for p in payments]
    result = "<br>".join(results)
    session.pop('payments', None)  # Clear the session after finalizing

    return render_template_string(template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
