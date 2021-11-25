from flask import Flask, request

app = Flask(__name__)


@app.route('/service', methods=['POST'])
def service():
    incoming_msg = request.values.get('Body', '').lower().strip()
    print(incoming_msg)


if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
