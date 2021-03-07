from flask import Flask, render_template


app = Flask(__name__)

@app.route('/auto_answer')
@app.route('/answer')
def index():
    params = {}
    params['surname'] = 'Романов'
    params['name'] = 'Сергей'
    params['education'] = 'Высшее'
    params['profession'] = 'штурман марсохода'
    params['sex'] = 'Мужской'
    params['motivation'] = 'Побывать на другой планете'
    params['ready'] = 'Да'
    return render_template('list_val.html', params=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')