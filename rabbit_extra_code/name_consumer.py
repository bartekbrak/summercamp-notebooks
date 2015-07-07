import time
from kombu import Connection, Exchange, Queue

name_queue = Queue('name', exchange='', routing_key='name')

place = 1

def show_name(body, message):
    global place
    try:
        print place, '\t', time.strftime('%X'), '\t', body['name']
    except TypeError, KeyError:
        print place, '\t', time.strftime('%X'), '\t', body
    message.ack()
    place += 1
    
with Connection('amqp://guest:guest@localhost//') as conn:
    with conn.Consumer(name_queue, callbacks=[show_name]) as consumer:
        while True:
            conn.drain_events()

