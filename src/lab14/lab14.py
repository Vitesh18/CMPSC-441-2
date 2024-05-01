import datetime
from transformers import pipeline
from openai import Dalle

class Journal:
    def __init__(self, filename="game_journal.log"):
        self.filename = filename
        self.text_generator = pipeline('text-generation', model='gpt-3')
        self.image_generator = Dalle()

    def log(self, message, level="INFO"):
        """Log a message with a timestamp and a log level."""
        with open(self.filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} [{level}]: {message}\n")

    def generate_text_entry(self, context):
        """Generate text based on the given context."""
        return self.text_generator(f"Reflecting on today's adventures: {context}", max_length=150)[0]['generated_text']

    def generate_image(self, description):
        """Generate an image from text description."""
        return self.image_generator.generate_image(description)

global_journal = Journal()
