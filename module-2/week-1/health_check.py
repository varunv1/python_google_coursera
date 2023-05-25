#!usr/bin/env python3
import shutil
import psutil


def check_disk_usage(disk):
    """Returns true if more that 20% of disk is available"""
    du = shutil.disk_usage(disk)
    return (du.free / du.total * 100) > 20


def check_cpu_usage(interval):
    """Returns true if more than 75% of cpu is available"""
    cu = psutil.cpu_percent(interval)
    return cu < 75


if not check_cpu_usage(1) or not check_disk_usage("/"):
    print("Not healthy!")
else:
    print("Everything is ok!")
