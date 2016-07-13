from flask import Flask
import data
import threading
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worddddld!"

@app.route("/table")
def table():
    tabela = ''
    for e in list(reversed(data.prices))[:10]:
        tabela += '''
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
                 ''' % e
    sablon = '''
    <html>
    <head>
    <meta http-equiv="refresh" content="5">
    <style>
    table, th, td {
        border: 2px dotted blue;
    }
    </style>
    </head>
    <body>
    <table align="center">
          <tr>
            <th>Date</th>
            <th>Symbol</th>
            <th>Price</th>
          </tr>
          % s        
    </table>
    </body>
    </html>
    '''
    return sablon % tabela

@app.route("/graph")
def graph():
    return "...graph html..."

@app.route("/getdata")
def getdata():
    data.get_data()
    return "OK\n"

@app.route("/data")
def returndata():
    s = '''
    <html>
	<head>
	<meta http-equiv="refresh" content="5">
	</head>
    <body>
    %r
    </body>
    </html>
    '''
    return s % data.prices

def poller():
    while True:
        data.get_data()
        time.sleep(10)

t = threading.Thread(target=poller)
t.setDaemon(True)
t.start()

if __name__ == "__main__":
    app.run(debug=True)


