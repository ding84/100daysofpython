from flask import Flask
import time


app = Flask(__name__)

# export FLASK_APP=main.py
# terminal: flask run


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye_world():
    return 'Bye, World!'


def delay_decorater(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function


@delay_decorater
def say_hello():
    print("Hello")


@delay_decorater
def say_bye():
    print("bye")


say_hello()

decorated_function = delay_decorater(say_bye)
decorated_function()

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()


if __name__ == "__main__":
    app.run()