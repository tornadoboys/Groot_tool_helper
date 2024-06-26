import json
import sys
import requests
import logging

from tqdm import tqdm

def log_message(level, message):
    if level >= logging.ERROR:
        stream = sys.stderr
    else:
        stream = sys.stdout
    logging.basicConfig(stream=stream, level=logging.DEBUG, format='%(levelname)s: %(message)s', force=True)
    logger = logging.getLogger('MyLogger')
    logger.log(level, message)

def handle_exception(e):
    # 当试图打开一个不存在的文件时，将会捕捉到FileNotFoundError异常。
    # 如果文件不存在，则打印错误信息到标准错误输出（通常是控制台），指明文件找不到。
    if isinstance(e, FileNotFoundError):
        log_message(logging.ERROR,f"File not found: {e}")

    # 当试图对一个目录执行文件操作（如尝试打开一个目录作为文件）时，将会捕捉到IsADirectoryError异常。
    # 如果指定的路径是一个目录而不是文件，同样将错误信息输出到标准错误。
    elif isinstance(e, IsADirectoryError):
        log_message(logging.ERROR,f"Specified path is a directory, not a file: {e}")

    # 当程序没有足够的权限执行文件操作时，将会捕捉到PermissionError异常。
    # 如果由于权限问题操作失败，则输出权限被拒绝的错误信息到标准错误。
    elif isinstance(e, PermissionError):
        log_message(logging.ERROR, f"Permission denied: {e}")

    # 当发生其他输入/输出错误时，将会捕捉到IOError异常。这可能包括硬件故障或外部IO问题。
    # 输出具体的I/O错误信息到标准错误。
    elif isinstance(e, IOError):
        log_message(logging.ERROR, f"An I/O error occurred: {e}")

    elif isinstance(e, requests.exceptions.RequestException):
        log_message(logging.ERROR, f"An error occurred while making the request: {e}")
    else:
        log_message(logging.ERROR, f"An unexpected error occurred: {e}")

def getConfig():
    with open(sys.argv[1], 'r') as file:
        config = json.load(file)
        return config

def create_processbar():
    pbar = tqdm(total=100, file=sys.stdout, bar_format='{desc}: {percentage:3.0f}%')
    print("\n")
    return pbar

