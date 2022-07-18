
class Channel:
    def __init__(self, name):
        self.channel_name = name
        self.__subscribers = []
        self.__videos = []

    def add_sub(self, sub):
        self.__subscribers.append(sub)
        
    def delete_sub(self, sub):
        self.__subscribers.remove(sub)

    def upload_video(self, name):
        self.__videos.append(name)
        self.send_notification()

    def send_notification(self):
        if len(self.__subscribers) > 0:
            print()
            for sub in self.__subscribers:
                sub.update(self.__videos[-1])


class Subscriber:
    def __init__(self, name):
        self.subscriber_name = name
        self.following = None

    def subscribe(self, channel):
        self.following = channel
        self.following.add_sub(self)

    def unsubscribe(self):
        self.following.delete_sub(self)
        self.following = None

    def update(self, new_video):
        print(f'Hello {self.subscriber_name}, {self.following.channel_name} has uploaded \'{new_video}\'')


myChannel = Channel("echoaj")
myChannel.upload_video("Intro to Python3")

sub1 = Subscriber("Amy")
sub2 = Subscriber("Joe")
sub3 = Subscriber("Liz")
sub4 = Subscriber("Tim")

sub1.subscribe(myChannel)
sub2.subscribe(myChannel)
sub3.subscribe(myChannel)
sub4.subscribe(myChannel)
sub2.unsubscribe()

myChannel.upload_video("x86 assembly intro")
