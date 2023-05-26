from flask import Flask,render_template,jsonify
from database import load_jobs
app = Flask(__name__)
@app.route("/")
def home():
    jobs = load_jobs()
    return render_template("home.html",name="Medical Job Openings",jobs=jobs)

@app.route("/api")
def job_portal():
    jobs = load_jobs()
    return jsonify(jobs)
if __name__=="__main__":
    app.run(host="0.0.0.0"d)