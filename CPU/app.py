from flask import Flask, render_template, jsonify
import datetime
import math
import psutil

app = Flask(__name__)

def calculate_factorial(n):
    return math.factorial(n)

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    return f'CPU: {cpu_percent:.2f}%, Memory: {memory_percent:.2f}%'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_hour, current_minute, current_second = map(int, current_time.split(':'))
    factorial = calculate_factorial(current_hour) * calculate_factorial(current_minute) * calculate_factorial(current_second)
    system_info = get_system_info()
    data = {'current_time': current_time, 'factorial': factorial, 'system_info': system_info}
    with open('system_monitor.txt', 'a') as file:
        file.write(f'{current_time}: {system_info}\n')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
