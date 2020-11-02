# vectorAITest

To start developing you must ensure that you have installed docker and docker-compose.

After you clone the repo, in the root directory of the proyect you must run the following commands:

* docker volume create --name=vectorai-data 
* docker-compose build 
* docker-compose run back alembic upgrade head
* docker-compose up

Now, you can go to your favourite browser and hit the following url:

http://localhost:3001