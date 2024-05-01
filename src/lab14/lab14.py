import datetime

class Journal:
    def __init__(self, filename="game_journal.log"):
        self.filename = filename

    def log(self, message, level="INFO"):
        """Log a message with a timestamp and a log level."""
        with open(self.filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} [{level}]: {message}\n")

    def debug(self, message):
        self.log(message, "DEBUG")

    def info(self, message):
        self.log(message, "INFO")

    def error(self, message):
        self.log(message, "ERROR")

global_journal = Journal()
