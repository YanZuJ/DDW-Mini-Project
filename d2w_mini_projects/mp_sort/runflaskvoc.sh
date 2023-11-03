#!/bin/bash

port=`voc_get_proxied_server_port` 
flask run -h localhost -p $port

/voc/work/DDW-Mini-Project/d2w_mini_projects/mp_calc