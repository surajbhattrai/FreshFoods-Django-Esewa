
> FreshFoods is a online food & grocery delivery service app built with Django with Esewa payment integration.

We have used ``Faker`` to generate fake data automatically.

## Getting Started  

To get a local copy up and running follow these simple example steps.

1. To get started, fork this repository to your GitHub account.

2. Clone the repo :
    ```sh
     git clone https://github.com/1hanzla100/flutter-yumniastic
    ```
3. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).

4. Install dependencies:
    ```sh
     pip install -r requirements.txt
    ```
    
5. Create a development database:
    ```sh
      python manage.py migrate
    ```

6. If everything is alright, you should be able to start the Django development server:
    ```sh
      python manage.py runserver
    ```

7. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.


## Generate fake data

Make use of management command `python manage.py createdata`  to generate fake categories and products automatically.


