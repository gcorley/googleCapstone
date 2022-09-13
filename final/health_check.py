#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails


def check_disk_usage():
    du = shutil.disk_usage('/')
    free = du.free / du.total * 100
    return free


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage


def send_error_email(sbj):
    sender = 'automation@example.com'
    recipient = '<username>@example.com'
    body = 'Please check your system and resolve the issue as soon as possible.'
    msg = emails.generate_error_report(sender, recipient, sbj, body)
    emails.send_email(msg)


def resolves():
    ip_address = socket.gethostbyname('localhost')
    return ip_address


if __name__ == "__main__":
    if check_cpu_usage() > 80:
        subject = 'Error - CPU usage is over 80%'
        send_error_email(subject)
    if check_disk_usage() < 20:
        subject = 'Error - Available disk space is less than 20%'
        send_error_email(subject)
    memory_info = psutil.virtual_memory()
    available_memory = memory_info.available/1024
    if available_memory < 500:
        subject = 'Error - Available memory is less than 500MB'
        send_error_email(subject)
    if resolves() != '127.0.0.1':
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
        send_error_email(subject)
