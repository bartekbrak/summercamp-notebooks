from kombu import Connection
from kombu.simple import SimpleQueue

connection = Connection('amqp://guest:guest@localhost//')

karol_queue = connection.SimpleQueue('karol')
adam_queue = connection.SimpleQueue('adam')
mikaeil_queue = connection.SimpleQueue('mikaeil')
tomasz_queue = connection.SimpleQueue('tomasz')
elena_queue = connection.SimpleQueue('elena')
rafal_queue = connection.SimpleQueue('rafal')
jakub_k_queue = connection.SimpleQueue('jakub_k')
aleksandra_queue = connection.SimpleQueue('aleksandra')
krzysztof_queue = connection.SimpleQueue('krzysztof')
jakub_m_queue = connection.SimpleQueue('jakub_m')

summercamp_queues = [
    karol_queue,
    adam_queue,
    mikaeil_queue,
    tomasz_queue,
    elena_queue,
    rafal_queue,
    jakub_k_queue,
    aleksandra_queue,
    krzysztof_queue,
    jakub_m_queue,
]

numbers = range(5, 50, 5) + range(50, 1000, 50) + range(1000, 1000000, 1000)

with connection:
    for n in numbers:
        for queue in summercamp_queues:
            queue.put(n)