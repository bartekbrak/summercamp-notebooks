from kombu import Connection, Exchange, Queue

number_exchange = Exchange('number', 'direct', durable=True)
number_queue = Queue('number', exchange=number_exchange, routing_key='number')

# connections
with Connection('amqp://guest:guest@localhost//') as conn:

    # produce
    producer = conn.Producer(serializer='json')
	
    for i in xrange(100000):
        number = i
        producer.publish({'number': number},
	    exchange=number_exchange, routing_key='number',
            declare=[number_queue])
