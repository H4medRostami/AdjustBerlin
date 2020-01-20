******
Adjust
******
+++++++++++
Simple Test
+++++++++++

* install dependencies::

    pip3 install -r requirement.txt

* transfer dataset.csv to datatable(Postgresql example)::

    COPY  "dataset"(id, date, channel, country, os, impressions, clicks, installs, spend, revenue)
    FROM '\adjust\dataset.csv' DELIMITER ',' CSV HEADER;

* create superuser and run server::

    >>>manage.py createsuperuser
    Success

    >>>manage.py runserver
    Success



* try full documentation with swagger on browser::

    [ip:port]/v1/swagger/


========================
requested use cases url:
========================
1:v1/Filter/?sort_by=-clicks&group_by=channel,country&date_to=2017-06-01

2:v1/Filter/?sort_by=date&group_by=date&os=ios&date_from=2017-05-01&date_to=2017-05-31

3:v1/Filter/?sort_by=-revenue&group_by=os&country=us&date_from=2017-06-01&date_to=2017-06-01

4:v1/Filter/?sort_by=-CPI&group_by=channel&country=CA

