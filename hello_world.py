from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:80px;'>
            <center>
                <image height="600" width="531" src="https://i.pinimg.com/originals/22/e0/4e/22e04e26bf80cc666c5fc2e7a1e0818d.jpg">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = 'SA Tarea7 201314733'
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)