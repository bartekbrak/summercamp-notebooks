import wimq
from workers import WorkerX


def main():
    config_provider = wimq.INIConfigProvider(
        config={
            'wimq.locker_host': 'localhost:11211',
            'wimq.host': 'localhost',
            'wimq.user': 'sc',
            'wimq.password': 'sc',
            'wimq.vhost': 'sc',
        })
    app = wimq.App(config_provider)
    app.register_worker(WorkerX)
    return app
