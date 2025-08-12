from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html', page='home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"📩 New message from {name} ({email}): {message}")
        return render_template('main.html', page='success', name=name)
    return render_template('main.html', page='contact')

if __name__ == '__main__':
    app.run(debug=True)
