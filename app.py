from flask import Flask,render_template,request,Response    #importing Flask
from macanalysis import macAnalysis     #import our mac processing python file
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        try:
            file = request.files['File']
            if file.filename.split('.')[1] == 'pcapng' or file.filename.split('.')[1] == 'pcap':
                file.save(file.filename)
                result = macAnalysis(file.filename)
            else:
                return render_template('home.html',v='',resultv='hidden')
        except:
            return render_template('home.html',v='',resultv='hidden')
        os.system(f'rm *.pcapng');os.system(f'rm *.pcap');os.system(f'rm *.csv')
        return render_template('home.html',outputs = result,v='hidden',resultv='')

    return render_template('home.html',v='hidden',resultv='hidden')

@app.route('/result')
def yahoo():
    return render_template('results.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',debug=True,port=port)