import psutil
import socket
import pickle

def scrape_ram():
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        s.sendall(pickle.dumps(data))

if __name__ == "__main__":
    data = scrape_ram()
    send_data(data)
