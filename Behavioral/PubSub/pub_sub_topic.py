

class MessageBroker:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish(self, topic, message):
        for subscriber in self.subscribers:
            if topic in subscriber.topics:
                subscriber.update(message)
        print('-' * 20)


class Subscriber:
    def __init__(self, name, broker):
        self.topics = set()
        self.name = name
        self.message_broker = broker
        self.message_broker.subscribe(self)

    def add_topic(self, topic):
        self.topics.add(topic)

    def update(self, message):
        print(f'{self.name} received this message: {message}')

    def __del__(self):
        self.message_broker.unsubscribe(self)


class Publisher:
    def __init__(self, name, broker):
        self.name = name
        self.message_broker = broker

    def publish(self, topic, message):
        self.message_broker.publish(topic, message)


message_broker = MessageBroker()
subscriber1 = Subscriber('subscriber1', message_broker)
subscriber2 = Subscriber('subscriber2', message_broker)
subscriber3 = Subscriber('subscriber3', message_broker)
subscriber4 = Subscriber('subscriber4', message_broker)
subscriber5 = Subscriber('subscriber5', message_broker)

subscriber1.add_topic('topic/cats')
subscriber1.add_topic('topic/dogs')
subscriber1.add_topic('topic/jokes')
subscriber2.add_topic('topic/cats')
subscriber3.add_topic('topic/jokes')
subscriber4.add_topic('topic/jokes')
subscriber4.add_topic('topic/dogs')
subscriber5.add_topic('topic/programming')


publisher = Publisher('publisher', message_broker)
publisher.publish('topic/cats', 'I love cats (1,2)')
publisher.publish('topic/dogs', 'I love dogs (1,4)')
publisher.publish('topic/jokes', 'I love jokes (1,3,4)')
publisher.publish('topic/programming', 'I love programming (5)')

