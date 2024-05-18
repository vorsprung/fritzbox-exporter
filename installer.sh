#!/bin/bash

python venv /opt/fritz-exporter
cp exporter.py /opt/fritz-exporter/
/opt/fritz-exporter/bin/pip -r requirements.txt
cp fritz-exporter.env /etc/default/fritz-exporter
cp fritz-exporter.service /lib/systemd/system/
systemctl enable fritz-exporter.service
systemctl start fritz-exporter.service
systemctl status fritz-exporter.service

