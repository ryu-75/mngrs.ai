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

Now, navigate to the project directory and execute the following command:
```bash
cd project
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

