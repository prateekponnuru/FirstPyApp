from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
#app = Flask(__name__, template_folder=r'./Scripts/Templates/')
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capture_lead', methods=['get', 'post'])
def capture_lead():
    if methods == 'get':
        return render_template('lead_capture.html')
    else:
        ##return render_template('lead_capture.html')
        FName = request.form['nme']
        ##Gender = request.form['gender']
        ##phone = request.form['Mobile']
        ##email = request.form['email']
        ##HighestQualification = request.form['HighestQualification']
        ##Bkgrnd_in_computers = request.form['comptrBkgrnd']
        ##Working = request.form['working']
        ##Experience = request.form['exp']
        ##Earnings = request.form['earn']
        ##Interest = request.form['InterestedIn']
        ##time2convert = request.form['Time2Join']
        flash( 'FName')
        return render_template('lead_capture.html')

@app.route('/construction_page', methods=['get'])
def construction_page():
    return 'Page Under Construction!'
 
@app.route('/create_lead', methods=['POST'])
##FName VARCHAR, LName, Gender, phone, email, HighestQualification, Bkgrnd_in_computers, Working, Experience, Earnings, Interest, time2convert
def submit_lead():
    ##return render_template('lead_capture.html')
    FName = request.form['Name']
    ##Gender = request.form['gender']
    ##phone = request.form['Mobile']
    ##email = request.form['email']
    ##HighestQualification = request.form['HighestQualification']
    ##Bkgrnd_in_computers = request.form['comptrBkgrnd']
    ##Working = request.form['working']
    ##Experience = request.form['exp']
    ##Earnings = request.form['earn']
    ##Interest = request.form['InterestedIn']
    ##time2convert = request.form['Time2Join']
    flash( 'FName')
    return home()
    
   ##     session['logged_in'] = True
    ##else:
      ##  flash('wrong password!')
    ##return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    ##app.run(debug=True, host='0.0.0.0', port=4000)
    app.run(debug = True)