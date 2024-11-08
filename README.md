# Instruction

First of all, before running the app.

You need to install all the dependencies, to do so, simply execute the `init.sh` script.
```bash
source init.sh
```
If you have already installed the dependencies and activated the virtual environment, run:
```bash
source django_venv/bin/activate
```
Once the installation is complete, you will be redirected in the environment.

Now, you need to create and configure an `.env` file inside the `project/` folder.
The `.env` file take:
```
DB_NAME    = 
DB_USER    = 
DB_PWD     = 
DB_PORT    = 
DB_HOST    = 
```

Then, execute the following command to configure the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

Now we need to settings parameters to be sure the sending email work correctly.

Make sure to already have installed `redis server` in your system.
If not, you will need to install it.

Run the following commands :
```bash
sudo apt-get install redis-server
sudo service redis-server start
```

Then, access the **Redis CLI** to be ensure the message broker is working correctly.
Run the following command: 
```bash
redis-cli
127.0.0.1:6379> ping
```

You should receive a `PONG` response if **Redis** working correctly.

Once you have configured and restarted the broker, restart Celery with: 
```bash
celery -A project worker -l info
```

Finally, in the project root directory, run:
```bash
python manage.py runserver
```

## How to used the app
Once the server is running, you can create a project !

To do this, you need to :
1. Navigate to the `create` link.
2. Fill out the form (Only the `title` is required).
3. Concerning tags, you can add multiple tags by separating each tag with a comma.
4. Once form is correctly filled, click on `New project`.
You will be redirected to the `projects` page.

To update a project, simply :
1. Click on the `yellow` button at the top right of the project card.
2. You will redirected to the `update/` url.
3. Apart from the `title` which is required, any field you leave unchanged will keep its oldest value.
4. Then, click on `Edit`

And now, for deleted a project, you just need to:
1. Simply click on the `red` button next to the `yellow` button. That's all !

You can also sort projects with the dropdown at the top right of the page.

It sorts projects by `Completed` or `due date` status.

### Good to know: 
When you create a new project, the program creates a folder called `emails` in the project root.
Similarly, when your add an image to your project, a folder called `uploads` is also created in the project root.

## Test
If you want to execute tests for views, models and services.
You just need to run the following command:
```bash
python manage.py test
```

## Command
To delete all the projects from Project table, you need to run the following command:
```bash
python manage.py delete_all_projects
```
Then type `yes` to delete all.

I hope you will be satisfied with my practical case !
