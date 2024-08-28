import websocket
import json
import urllib.request
import uuid
import time
import threading
from tabulate import tabulate

class QueueMonitor:
    def __init__(self):
        self.queue_status = {}
        self.client_id = str(uuid.uuid4())
        self.websockets = {}

    def add_url(self, url):
        if url not in self.queue_status:
            self.queue_status[url] = {'running': 0, 'pending': 0}
            self._start_websocket(url)

    def get_queue_status(self, url):
        try:
            with urllib.request.urlopen(f"http://{url}/queue") as response:
                data = json.loads(response.read())
                running = len(data.get('queue_running', []))
                pending = len(data.get('queue_pending', []))
                return running, pending
        except Exception as e:
            print(f"Error getting queue status for {url}: {e}")
            return 0, 0

    def update_status(self, url):
        running, pending = self.get_queue_status(url)
        self.queue_status[url]['running'] = running
        self.queue_status[url]['pending'] = pending

    def print_status(self):
        headers = ["URL", "Running", "Pending", "Total"]
        table_data = []
        for url, status in self.queue_status.items():
            total = status['running'] + status['pending']
            table_data.append([url, status['running'], status['pending'], total])
        
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))
        print(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def get_least_busy_url(self):
        if not self.queue_status:
            return None
        return min(self.queue_status, key=lambda x: sum(self.queue_status[x].values()))

    def _on_message(self, ws, message):
        data = json.loads(message)
        if data['type'] == 'status':
            url = ws.url.split('/')[2]
            self.update_status(url)

    def _on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def _on_close(self, ws, close_status_code, close_msg):
        print(f"WebSocket connection closed for {ws.url}")

    def _on_open(self, ws):
        print(f"WebSocket connection opened for {ws.url}")

    def _run_websocket(self, url):
        ws_url = f"ws://{url}/ws?clientId={self.client_id}"
        ws = websocket.WebSocketApp(ws_url,
                                    on_message=self._on_message,
                                    on_error=self._on_error,
                                    on_close=self._on_close,
                                    on_open=self._on_open)
        ws.url = ws_url
        while True:
            try:
                ws.run_forever()
            except Exception as e:
                print(f"WebSocket connection failed for {url}: {e}")
            print(f"Attempting to reconnect to {url} in 5 seconds...")
            time.sleep(5)

    def _start_websocket(self, url):
        thread = threading.Thread(target=self._run_websocket, args=(url,))
        thread.daemon = True
        thread.start()
        self.websockets[url] = thread

def create_monitor(urls):
    monitor = QueueMonitor()
    for url in urls:
        monitor.add_url(url)
    return monitor

def get_least_busy_url(monitor):
    return monitor.get_least_busy_url()