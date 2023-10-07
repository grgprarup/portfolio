# Portfolio
This is a portfolio website made using Django. It is a simple website that can be used to showcase your projects and skills.

## Install dependencies
- Python 3.10.12 can be installed from [here](https://www.python.org/downloads/)
- Django 4.2.6 can be installed from [here](https://www.djangoproject.com/download/)
- Install Pip 23.2.1 using the following command
    ```
    python -m pip install --upgrade pip
    ```
- Install Conda 4.12.0 using the following command
    ```
    pip install conda
    ```

## Create/Remove a virtual environment
- Create a virtual environment using conda
    ```
    conda create --name portfolio python=3.10.12
    ```
- Delete the virtual environment using conda
    ```
    conda remove --name portfolio --all
    ```

## Activate/Deactivate the virtual environment
- Activate the virtual environment using conda
    ```
    conda activate portfolio
    ```
- Deactivate the virtual environment using conda
    ```
    conda deactivate
    ```

## Install the requirements
- Install the requirements using pip
    ```
    pip install -r requirements.txt
    ```

## Set up the project
- Clone the project using the following command
  1. Github
      ```
      git clone https://github.com/grgprarup/portfolio.git
      ```
  2. Gitlab
     ```
     git clone https://gitlab.com/grgprarup/portfolio.git
     ```
- Change the directory to the project directory
    ```
    cd portfolio
    ```

### Make migrations
- Make migrations using the following command
    ```
    python manage.py makemigrations
    ```

### Migrate the database
- Migrate the database using the following command
    ```
    python manage.py migrate
    ```

### Create a superuser
- Create a superuser using the following command
    ```
    python manage.py createsuperuser
    ```

### Run the server
- Run the server using the following command
    ```
    python manage.py runserver
    ```

### Create a new app
- Create a new app using the following command
    ```
    python manage.py startapp <app_name>
    ```
  
### Add the app to the project
- Add the app to the project by adding the following code to the INSTALLED_APPS list in settings.py
    ```
    '<app_name>.apps.<App_name>Config',
    ```
