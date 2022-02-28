import socket
import logging
import logging.handlers
import requests
import json
import subprocess
import os
import sys

# def get_stream(url):
#     s = requests.Session()
#
#     with s.get(url, headers=None, stream=True) as resp:
#         for line in resp.iter_lines():
#             if line:
#                 print(line)


def send_to_qradar(data_recv):
    my_logger = logging.getLogger("LogSender")
    my_logger.setLevel(logging.INFO)
    ip_address = '192.168.86.129'

    port = 514
    socket.setdefaulttimeout(1000.0)

    logging.handlers.SysLogHandler()
    # if tcp_enabled:
    #     handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_STREAM)
    # else:
    #     handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_DGRAM)

    #handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_STREAM)
    handler = logging.handlers.SysLogHandler(address=(ip_address, port), socktype=socket.SOCK_DGRAM)
    my_logger.addHandler(handler)

    s = ""
    for row in data_recv:
        s += row
        try:
            my_logger.info(s + "\n")
            my_logger.handlers[0].flush()
            print("Sent to appliance: {}".format(s))
        except Exception as e:
            print("Something went wrong: {}".format(e))
            break

def main():
    command = 'curl -i --no-buffer -H "Connection: Upgrade" -H "Upgrade: websocket" -H "Host: logstream.proofpoint.com:443" -H "Authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1ODI1NzQ4MTUsImlzcyI6IlByb29mcG9pbnQgSW5jLiIsImNsdXN0ZXJJZCI6InBoYW5uaWZpbl9ob3N0ZWQiLCJ1c2VySWQiOiJwaGFubmlmaW5faG9zdGVkXzEifQ.F2RfRc1a3ax62rnNAWNnyWT0pPHew1qEYfuXm96KX9prXd_lDZfvDd7_didwLZ547ZWI2_HTIsf7TwtrCH6lCw" -H "Sec-WebSocket-Key: phannifin_hosted_1" -H "Sec-WebSocket-Version: 13" "https://logstream.proofpoint.com:443/v1/stream?cid=phannifin_hosted&type=message&sinceTime=2020-05-25T11:11:11-0400&toTime=2020-05-26T11:11:12-0400"'
    #p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    for line in iter(p.stdout.readline, ''):
        send_to_qradar(line)

    # try:
    #     for line in iter(p.stdout.readline, b''):
    #         send_to_qradar(line)
    #     sys.stdout.flush()
    # except BrokenPipeError:
    #     devnull = os.open(os.devnull, os.O_WRONLY)
    #     os.dup2(devnull, sys.stdout.fileno())
    #     sys.exit(1)

        # #print(line)
        # print(">>> " + str(line.rstrip()))
        # p.stdout.flush()
        #send_to_qradar(line)

    # while True:
    #     output = p.stdout.readline()
    #     if output == '' and p.poll() is not None:
    #         break
    #     if output:
    #         send_to_qradar(output)
    #         print (output.strip())
    # rc = p.poll()
    # print (rc)


if __name__ == "__main__":
    main()
