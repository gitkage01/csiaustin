from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def load():
   return render_template('index.html')

@app.route('/autopsy',methods = ['POST', 'GET'])
def autopsy():
   return render_template('autopsy-report.html')


@app.route('/incident',methods = ['POST', 'GET'])
def incident():
   return render_template('police-report.html')

if __name__ == '__main__':
   app.run(debug = True)