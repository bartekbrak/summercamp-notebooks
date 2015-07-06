from kombu import Connection, Exchange, Queue

introduction_queue = Queue('number', exchange='', routing_key='number')

# connections
with Connection('amqp://guest:guest@localhost//') as conn:

    # produce
    producer = conn.Producer(serializer='json')
	
    producer.publish({'name': 'Jan Kowalski'},
	    exchange='', routing_key='name',
            declare=[introduction_queue])

