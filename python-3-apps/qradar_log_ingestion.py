import socket
import logging
import logging.handlers
import requests
import json



def send_to_qradar(data_recv):
    my_logger = logging.getLogger("LogSender")
    my_logger.setLevel(logging.INFO)
    ip_address = '192.168.86.129'
    #ip_address = '23.217.138.110'
    #ip_address = '172.29.164.102'
    #ip_address = '169.63.156.196'
    port = 514
    socket.setdefaulttimeout(1000.0)

    logging.handlers.SysLogHandler()
    # if tcp_enabled:
    #     handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_STREAM)
    # else:
    #     handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_DGRAM)

    handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_STREAM)
    # handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_DGRAM)
    my_logger.addHandler(handler)

    my_logger.info(data_recv)

def main():
    headers = {
        'X-Auth-Token': 'EEBQG94FQP35MDMWVDZ37FTP/IHNZU5FLA3',
        'Content-Type': 'application/json',
    }

    data = '{"criteria": {"group_results": true,"minimum_severity": 3,"create_time": {"start": "2020-01-27T23:10:20.814Z","end": "2020-01-27T23:10:25.814Z"}},"sort": [{"field": "first_event_time","order": "DESC"}],"rows": 10,"start": 0}'

    response = requests.post('https://defense.conferdeploy.net/appservices/v6/orgs/7DESJ9GN/alerts/_search',
                                 headers=headers, data=data)

    data_recv = response.content
    data_recv_json = json.loads(data_recv)

    print(type(data_recv_json))

    send_to_qradar(data_recv_json)
    print(data_recv_json)


if __name__ == "__main__":
    main()
