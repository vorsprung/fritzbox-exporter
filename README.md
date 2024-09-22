Fritzbox DSL speed monitor exporter for prometheus
--------------------------------------------------
![Alt text](https://i.postimg.cc/hjmfH8LC/Screenshot-from-2024-09-22-19-22-09.png "Example Grafana")


This simple thing gets the bytes metrics for send and receive and makes them available as prometheus metrics
Tested on a rasberry pi running Debian 11

Installing
----------
See installer.sh

Setup Prometheus
----------------
Add localhost:8000 to static_configs targets

Setup Grafana
-------------
Add a panel with two queries, one for irate(sent[5m]) and one for irate(received[5m])
Then you will see graphs for 5 minute send /receive rates

