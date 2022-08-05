
<pre><code>
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ export FLASK_RUN_PORT=8000
$ export FLASK_RUN_HOST=0.0.0.0
</code></pre>

<pre><code>
python manage.py db init
python manage.py db migrate --message 'initial database migration'
python manage.py db upgrade
</code></pre>

<pre><code>
pip3 freeze > requirements.txt
</code></pre>