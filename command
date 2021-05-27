docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1 -d mysql
docker exec -i some-mysql mysql -p1 mysql < script/db.sql
docker exec -it some-mysql mysql -uroot -p
alembic revision --autogenerate -m "update"
alembic upgrade head
export PYTHONPATH="${PYTHONPATH}:/home/vladimir/PythonProjects/pharmacy"