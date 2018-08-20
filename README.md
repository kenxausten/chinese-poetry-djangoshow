# chinese-poetry-djangoshow
chinese-poetry , show in django using mysql database

1. install the requirements
   pip install -r requirements.txt
2. create database
   a) under mysql mode: create database chinese_poetry CHARACTER SET utf8 COLLATE utf8_general_ci;
   b) python manager.py makemigrations;
   c) python manager.py migrate;
   
3. run the server: python manager.py runserver localhost:8001

4. open the URL: http://localhost:8001/admin

5. import the Shijing to mysql db
![Alt text](djangoshow/images/shijing_admin.jpg?raw=true "诗经后台管理页面")
