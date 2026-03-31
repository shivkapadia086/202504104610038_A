from flask import Flask,render_template,request,redirect

app = Flask(__name__)

tasks=[]

@app.route('/')
def home():
    return render_template('index.html',tasks=tasks)

@app.route('/add',methods=['POST'])
def add():

    task=request.form['task']

    if task!="":
        tasks.append(task)

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):

    if len(tasks)>id:
        tasks.pop(id)

    return redirect('/')

@app.route('/update/<int:id>',methods=['POST'])
def update(id):

    newtask=request.form['task']

    if newtask!="":
        tasks[id]=newtask

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)