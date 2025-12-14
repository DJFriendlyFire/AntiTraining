class Notification:
    def __init__(self, user_id: str, message: str):
        self.user_id = user_id
        self.message = message
        self.sending = False


class Scheduler:
    def __init__(self):
        self.list_notifications = []

    def schedule(self, notification: Notification):
        self.list_notifications.append(notification)

    def run_pending(self):
        for message in self.list_notifications:
            if not message.sending:
                print(f' INFO: Sending notification to user_id="{message.user_id}": "{message.message}"')
        else:
            print(f' INFO: все сообщения были отправлены адресатам.')

if __name__ == '__main__':
    notification = Notification('123', 'Пора кушать')
    scheduler = Scheduler()
    scheduler.schedule(notification)
    scheduler.run_pending()