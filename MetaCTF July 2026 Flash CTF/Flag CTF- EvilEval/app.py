import socket
import time
import os
import random
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def animate_text(client_socket, text, delay=0.05):
    for char in text:
        client_socket.sendall(char.encode())
        time.sleep(delay)
    client_socket.sendall(b"\n")

def log_message(client_socket, message):
    client_socket.sendall(f"{get_current_time()} {message}\n".encode())

def check_black_list(inp):
    for item in black_list:
        if item in inp:
            return True
    return False

def check_number(inp):
    for i in range(10):
        if str(i) in inp:
            return True
    return False

def check_rce(inp):
    rce_keywords = ['os', 'sys', 'subprocess', 'shutil', 'tempfile', 'pickle', 
                    'marshal', 'exec', 'eval', 'compile', 'globals', 'locals', 
                    'import', '__', '{', '}']
    for keyword in rce_keywords:
        if keyword in inp:
            return True
    return False

FLAG = os.getenv("FLAG", "MetaCTF{Fake_Flag_For_Testing}")
ct = time.ctime().encode()
key = int((b"flag" + ct).hex(), 16) % 255
black_list = ['+', '-', '*', '/', '%', '==', '!=', '[', ']', '>', '<', '>=', '<=', 
              '~', 'and', 'or', 'not', 'in', 'lambda', 'print', 'input', 'open', 
              'eval', 'compile', 'os', 'sys', 'subprocess', 'shutil', 'tempfile', 
              'pickle', 'marshal', '__', 'import']

HOST, PORT = os.getenv("HOST", "0.0.0.0"), int(os.getenv("PORT", 1337))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[INFO] Server is listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"[INFO] Connection from {client_address}")

    try:
        log_message(client_socket, "Welcome to EvilEval challenge!")
        animate_text(client_socket, "Keep trying to unlock the secret password...\n", 0.07)

        attempts = 0
        while True:
            client_socket.sendall(f"{get_current_time()} > Enter your input: ".encode())
            inp = client_socket.recv(1024).decode().strip()
            attempts += 1

            try:
                if check_number(inp) or check_black_list(inp) or check_rce(inp):
                    log_message(client_socket, "Nope! This input is not allowed.")
                elif eval(inp) != key:
                    log_message(client_socket, f"Incorrect! You have tried {attempts} times. Keep going!")
                else:
                    log_message(client_socket, FLAG)
                    break
            except Exception as e:
                log_message(client_socket, f"Error in your input: {e}")
                log_message(client_socket, "Please try again.")
                continue
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client_socket.close()
        print(f"[INFO] Connection with {client_address} closed.")
