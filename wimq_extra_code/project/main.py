import wimq
from .workers import WorkerX


def main():
    config_provider = wimq.INIConfigProvider(
        config={
            'wimq.host': 'localhost',
            'wimq.user': 'test',
            'wimq.password': 'test',
            'wimq.vhost': 'test',
            'wimq.locker_host': 'localhost:11211',
        })
    app = wimq.App(config_provider)
    app.register_worker(WorkerX)
    return app
