import time
from kombu import Connection, Exchange, Queue

name_queue = Queue('name', exchange='', routing_key='name')

def show_name(body, message):
    print body['name'], time.strftime('%X')
    message.ack()
    
with Connection('amqp://guest:guest@localhost//') as conn:
    with conn.Consumer(name_queue, callbacks=[show_name]) as consumer:
        while True:
            conn.drain_events()

