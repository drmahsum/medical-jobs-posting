# Medical Jobs Openings
### Demo Video : [Youtube Demo Video](https://youtu.be/1jzAqelL9Kw)
### Description : Medical Job Opening for Healthcare professionals. You can check job openings and make api calls
### Demo link: [Medical Jobs](https://medical-jobs.onrender.com/)

In this website healthcare professional specifically doctors can look for jobs. For backend I used python,flask and mysql and for frontend I used bootstrap.It has a simple user interface and fully responsive so it users can apply jobs easily on their small devices such as mobile phones.

To apply a job user can click on apply button and it will open email client so that user can send application email to job poster. To add a job I have to insert a row to jobs table in database.In database there title,location,salary and email columns which is email of job poster.

Static folder contains the images that I used for my website. I found images on Unsplash which provides royalty-free images that you don't have pay for it to use them.

In templates folder there are jinja templates for website such as home.html which is for home page and jobs.html for list of job posting which uses for loop with help of jinja template.

In app.py folder there is backend part of website there 2 route one of them is for home page and the other one is for api calls to get json object of job listings.

In database.py file there are configurations for database.To connect database and send command to database I used sqlalchemy library which is easy to use and there a lot of documentation about how to use it.

To test it locally on your machine, clone this repository and install requirements with  `pip install -r requirements.txt` and to run server you should run `flask run` command in terminal to run it in debug mode you can use ` flask run --debug` command.You need to use your own database creditentials in app.py file change `DB_CRED` with your own creditentials. I used [Planetscale](https://app.planetscale.com/) free database service and to host demo I used [Render](https://dashboard.render.com/).You can sign up to server your own version of website. Both of them have free services(but limited functionalities).

Feel free to contribute to this project and make pull requests.