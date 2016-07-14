from flask import Flask
import data
import threading
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Wordddld!"

@app.route("/get_data")
def get_data():
    data.get_data()
    #print data.prices
    return "%s" % data.prices

@app.route("/table")
def table():
    tableHTML = ""
    for e in reversed(data.prices):
        tableHTML += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
        ''' %e
    tabela = '''
    <html>
	<head>
	<meta http-equiv="refresh" content="5">
	</head>
    <body>
    <TABLE  BORDER="5"; WIDTH=50%%>
   <TR>
      <TH COLSPAN="3">
         <H3><BR>Podaci s burza</H3>
      </TH>
   </TR>
      <TH>Symbol</TH>
      <TH>Date</TH>
      <TH>Price</TH>
   <TR>
    %s
   </TR>
</TABLE>
    </body>
    </html>
    '''

    return tabela % tableHTML

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

@app.route("/graph")
def graph():
    return "...graph html..."


def puller():
    while True:
        print "polling"
        data.get_data()
        time.sleep(10)


t = threading.Thread(target=puller)
t.setDaemon(True)
t.start()


if __name__ == "__main__":
    app.run(debug=True)

