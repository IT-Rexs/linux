
main.py: файл подключается к БД, запущенной в compose-docker.yaml, создает внутри нее (если ранее не была создана) таблицу users
и выводит всех пользователей из данной таблицы

test.py: подключается к методу  main.py и проверяет наличие пользователя в таблице.

Вставка пользователей была произведена в терминале postgreSQL след.командами:
sudo docker exec -it postgr_db_1 bash
psql -Ukubsu -dkubsu
INSERT INTO users (NAME, SURNAME, AGE) VALUES ('John', 'Doe', 30), ('Jane', 'Smith', 25), ('Bob', 'Johnson', 40);
