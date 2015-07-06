# Exercise 1
# part b - number_consumer.py
from kombu import Connection, Exchange, Queue

number_exchange = Exchange('number', 'direct', durable=True)
number_queue = Queue('number', exchange=number_exchange, routing_key='number')

def process_number(body, message):
    n = body['number']
    print n
    message.ack()
    
with Connection('amqp://guest:guest@localhost//') as conn:
    # consume
    with conn.Consumer(number_queue, callbacks=[process_number]) as consumer:
        # Process messages and handle events on all channels
        while True:
            conn.drain_events()
