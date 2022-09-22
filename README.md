# Steps
1. Clone this repos
2. Create virtual enviroment and enable it.
3. install packages in requirement.txt
4. run command **python manage runserver**
run worker: **celery -A konigle worker -l info -P eventlet**     
run beat: **celery -A konigle beat -l info**      


admin page: admin/admin

![Views](assets/view.JPG)   

<hr>

![worker](assets/worker.JPG)

<hr>

![beat](assets/celery_beat.JPG)





