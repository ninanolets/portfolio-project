'''
$ sudo systemctl edit --full gunicorn.service
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn && systemctl status gunicorn

$ sudo systemctl start gunicorn.socket
$ sudo systemctl enable gunicorn.socket
$ sudo systemctl status gunicorn.socket

$ sudo nano /etc/systemd/system/gunicorn.service
$ sudo systemctl list-unit-files | grep gunicorn


Path Error:

Go back into your virtualenv with $ source [your_project_env]/bin/activate 
and then $ which gunicorn
That will return the path to your gunicorn exectuable.

Paste that into the path section of the ‘ExecStart’ value inside the file
$ sudo nano /etc/systemd/system/gunicorn.service
and run commands to restart your daemon
$ sudo systemctl daemon-reload 
$ sudo systemctl restart gunicorn

Whenever you make changes on your Django project on the VPS from 
now on <after installing Gunicorn> you have to restart gunicorn with
$ sudo systemctl restart gunicorn

Whenever you make changes to an nginx path file, you need to restart ngix with
$ sudo nginx -t && sudo systemctl restart nginx
that first tests than restart nginx

'''
