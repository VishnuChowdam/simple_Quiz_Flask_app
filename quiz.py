from flask import *
app=Flask(__name__)
data={}
class questions:
    q_no=-1
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    correct_ans=-1
    def __init__(self,q_no,question, option1, option2, option3, option4,correct_ans):
     self.q_no = q_no
     self.question = question
     self.option1 = option1
     self.option2 = option2
     self.option3 = option3
     self.option4 = option4
     self.correct_ans=correct_ans
    def correct_option(self):
     if(self.correct_ans==1):
      return self.option1
     elif (self.correct_ans == 2):
       return self.option2
     elif (self.correct_ans == 3):
            return self.option3
     elif (self.correct_ans == 4):
            return self.option4
q1=questions(1,"1.which of the following is not an OOPS based programming language?","Java","C","C++","None of the above",2)
q2=questions(2,"2.Who invented the python programming language?","Dennies Ritchie","Guido van Rossum","james Goosling","steve jobs",2)
q3=questions(3,"3.What is the full form of HTML?","HyperText Markup Language","HyperText Markup Listing","HyperTransfer Markup Language","HyperText Management Language",1)
q4=questions(4,"4.Who is the founder of facebook?","Steve Jobs","Sundar Pichai","Mark Zukerberg","sam altaman",3)
q5=questions(5,"5.Who is the father of the AI?","sam Altman","Marvin Minsky","Geoffrey Hinton","John McCarthy",4)
Questions=[q1,q2,q3,q4,q5]
@app.route('/')
def home():
    return render_template('home.html',info='Register to take a quiz')
@app.route('/home')
def home1():
    return render_template('home.html',info='Register to take a quiz')
@app.route('/register_page')
def register():
   return render_template('register.html')
@app.route('/register_page',methods=['POST','GET'])
def registered_details():
    key=request.form.get('user')
    value=request.form.get('password')
    if key and value and len(value)>8:
        data[key]=value
        return render_template('login1.html')
    else:
        return render_template('register.html', text="Password must be above 8 characters")
@app.route('/login_page',methods=['POST'])
def login():
    key1=request.form.get('username')
    value1=request.form.get('password')
    if(key1 in data and value1==data[key1]):
        return render_template('quiz_page.html',Questions=Questions)
    else:
        if (key1 not in data):
            return render_template('login1.html', info1='Incorrect username')
        elif (value1 != data[key1]):
            return render_template('login1.html', info1='Incorrect password')
@app.route('/submit_quiz',methods=['POST','GET'])
def submit():
        correct = 0
        for question in Questions:
            q_id = str(question.q_no)
            picked_option = request.form[q_id]
            correct_option = question.correct_option()
            if(picked_option == correct_option):
                correct = correct+1
            if(correct==len(Questions)):
                t=True
            else:
                t=False
        count=str(correct)
        return render_template('score.html',inf=count+'/'+'5',condition=t)
@app.route('/logout')
def logout():
   return render_template('home.html')
if(__name__=='__main__'):
    app.run(debug=True,port=3000)