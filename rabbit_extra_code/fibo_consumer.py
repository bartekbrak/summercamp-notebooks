import math
from kombu import Connection


conn = Connection('amqp://summercamp:summercamp@localhost/summercamp')

grzegorz_queue = conn.SimpleQueue('grzegorz')
results_queue = conn.SimpleQueue('fibo_results')


def fibo(n):
    phi = 0.5 *(1 + 5**0.5)
    return round(phi**n/5**0.5)


with conn:
    while True:
        message = grzegorz_queue.get(block=True)
        n = message.payload # get deserialized message
        fn = fibo(n)
        print n, fn
        results_queue.put({'n': n, 'fn': fn, 'name': 'greg'})
        message.ack()