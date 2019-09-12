from flask import Flask, render_template, request, redirect
app = Flask(__name__, template_folder='.')

@app.route('/')
def helloWorld():
    return 'Hello, World!'

# @app.route('/index')
# def index():
#     return render_template('index.html')

@app.route('/index')
@app.route('/index/<name>')
def useVariable(name=None): 
    return render_template('index.html', name=name)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        return redirect('/index/' + name)
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run()