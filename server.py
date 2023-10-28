from flask import Flask , render_template ,url_for , request , redirect
import csv
app = Flask(__name__)
print((__name__))

@app.route("/")
def my_home():
    return render_template('index.html')

#here we can go for every page
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt' , mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write( f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv' ,newline='', mode = 'a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',' ,quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
#when  we have a problem my server and my database in the some location
#so when the server stops ,my file stay saved
#but what happens if maybe this  computer brokes or something happens to 'it and i can't turn it any more
#i've lost my files or mybe we have so much data that we want to store .
#well, this is actualyy database come in
#databases specialize in storing information
#Large scale applications can use databases to store large amounts of data and then do really intresting
#thing with them
#so that we're guaranteed not to lose that data .
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data) this from write to database.txt
            write_to_csv(data) #this is for csv File
            return redirect('/thankyou.html')
        except:
           return 'did not save in database'
    else:
        return 'somthing are wrong. try again!'



#@app.route("/works.html")
#def work():
#    return render_template('works.html')

#@app.route("/contact.html")
#def contact():
 #   return render_template('contact.html')






#to run app Falsk you should doing this :
#in terminal "set FLASK_APP=name_your_file(i named server).py"
#then : falsk run
#when Falsk run not worked
#Put this //$env:FLASK_APP = "server.py"//
#then flask run

#127.0.0.1 ==> it's what we call local host // this the url or the addrr of the laptop i'm working on
# with Port 5000
#render_template #==> this libraies allow us to send The Html file

#Flask uses this idea of templates to add multiple HTML files
#css and js The file has to be stored on the filesystem as static folder
#and when we use this two file we change the location in index.html to static/..js/.css

#localhost{#127.0.0.1} simply mean your comuter













