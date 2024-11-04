from flask import Flask,render_template,redirect,url_for,request
from certificate.cretificate import certificategenerator

app=Flask(__name__)



@app.route('/')
def index():
  return render_template('certificate_form.html')

@app.route('/generate',methods=['POST'])
def generate():
  name = request.form.get('name')
  course = request.form.get('course')
  all_classes = request.form.get('all_classes')
  all_assignments = request.form.get('all_assignment')
  if all_classes.lower()=='yes' and all_assignments.lower() =='yes':
    certificate=certificategenerator(name,course,all_classes,all_assignments)
    result_dict=certificate.generatecertificate()
    return render_template('certificate.html',name=result_dict['name'],course=result_dict['course'])
  else :
    return render_template('not_completed.html')
if __name__ == '__main__':
    app.run(debug=True)
    
  
    
  