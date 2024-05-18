from prometheus_client import start_http_server, Summary, Gauge
import time
import os

from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzServiceError



def process_request(fc):
    action = 'GetAddonInfos'
    service = 'WANCommonIFC1'
    try:
            result = fc.call_action(service, action)
    except FritzServiceError:
            return {}
    return {"received": result['NewX_AVM_DE_TotalBytesReceived64'],
            "sent": result['NewX_AVM_DE_TotalBytesSent64']}

if __name__ == '__main__':

    address=os.environ["FRITZ_IP"]
    password=os.environ["FRITZ_PASS"]
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # get fritz connection
    fc = FritzConnection(address=address, password=password)
    r = Gauge('received', 'received')
    s = Gauge('sent', 'sent')


    while True:
        time.sleep(10) 
        data=process_request(fc)
        r.set_function(lambda: data['received'])
        s.set_function(lambda: data['sent'])
