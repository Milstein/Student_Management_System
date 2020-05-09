===================================
# Student Management System
===================================

`git clone` this repository.

`cd Student_Management_System`.

Create a virtual environment by running `py -3 -m venv venv`.

## Activate the virtual environment by running:

  * on Linux/Mac: `source venv/bin/activate`

  * on Windows: `venv\Scripts\activate`

Install the necessary python packages by running `pip install -r requirements.txt`.

Run the migrations by running `./manage.py makemigrations` or `python manage.py makemigrations`.

Run the migrations by running `./manage.py migrate` or `python manage.py migrate`.

Run the migrations by running `./manage.py collectstatic` or `python manage.py collectstatic`.

Start the web server by running `./manage.py runserver` or `python manage.py runserver`.

To see the website, go to `http://localhost:8000`.

## To change the Layout and Theme:

* `templates\student_management_system_app`    
    * `index.html` is used as the home page inheriting the `base.html`.
    
 - Change the Template pages as required to customize.
 
## Features

* Bulk Upload
* Toast Messaging
* 3 different user types - HOD(admin), Staff and Student
* AJAX enabled functions
* Customized Template

## Contribute

If you'd like to contribute, simply fork [`the repository`](https://github.com/Milstein/Student_Management_System), commit your
changes to the **develop** branch (or branch off of it), and send a pull
request. Make sure you add yourself to [AUTHORS](https://github.com/Milstein/Student_Management_System/blob/master/AUTHORS).

As most projects, we try to follow [PEP8](https://www.python.org/dev/peps/pep-0008/) as closely as possible. Please bear
in mind that most pull requests will be rejected without proper unit testing.

## Feedback
Any suggestion and feedback is welcome. You can message me on facebook or my personal website
- [Milstein on Facebook](https://fb.com/milsonmun)
- [Milstein's Personal Site](https://milstein.me)
