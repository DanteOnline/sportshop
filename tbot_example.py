from unittest.mock import patch


class Message:

    def __init__(self):
        self.text = ''

    def reply_text(self, text):
        self.text = text


class Update:

    def __init__(self):
        self.message = Message()


class Context:
    pass


class ContextTypes:
    pass


def help_command(update: Update, context) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help!")


update = Update()
context = Context()

#
# with patch.object(update.message, 'reply_text') as mock:
#     help_command(update, context)
#     mock.assert_called_once_with()

help_command(update, context)
assert update.message.text == 'Help!'

