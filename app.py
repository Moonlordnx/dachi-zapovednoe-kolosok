from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/zapovednoe')
def zapovednoe():
    return render_template('zapovednoe.html')

@app.route('/kolosok')
def kolosok():
    return render_template('kolosok.html')

if __name__ == '__main__':
    print('\n' + '='*50)
    print('✅ САЙТ ЗАПУЩЕН!')
    print('📱 Открой в браузере: http://localhost:5000')
    print('='*50 + '\n')
    app.run(debug=True, port=5000)