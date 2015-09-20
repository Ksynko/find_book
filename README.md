# Find book

#Installation
1. Create virtualenv if neccesary
2. Install requirements from requirements.txt
3. Provide connection to database(change settings.py file)
4. Migrate database (python ./manage.py migrate)
5. Run Elasticsearch server
6. Create indexes (python ./manage.py rebuild_index)
7. Set email PASSWORD variable to enviorument
8. Run (python ./manage.py runserver)  
