from kombu import Connection, Exchange, Queue

exch = Exchange('fibo_results', 'direct', durable=True)
fibo_queue = Queue('fibo_results', exchange=exch, routing_key='fibo_results')


def fibo(n):
    phi = 0.5 *(1 + 5**0.5)
    return round(phi**n/5**0.5)


def correct_fibo(n, fn):
    return fibo(n) == fn


def process_message(body, message):
    correct = correct_fibo(body['n'], body['fn'])
    if correct:
        print body
        message.ack()
    else:
        print body, 'INCORRECT'

    
with Connection('amqp://summercamp:summercamp@localhost/summercamp') as conn:
    with conn.Consumer(fibo_queue, callbacks=[process_message]) as consumer:
        while True:
            conn.drain_events()