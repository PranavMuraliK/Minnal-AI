import random

class HooksGenerator:
    def __init__(self):
        # In a real system, this calls OpenAI API.
        self.templates = [
            "You've been doing {topic} wrong your entire life.",
            "This secret {topic} trick will make you rich.",
            "Stop scrolling if you want to master {topic}.",
            "Here are 3 tools that feel illegal to know for {topic}."
        ]
        self.topics = ["e-commerce", "side hustles", "dropshipping", "AI tools", "productivity"]

    def generate_daily_hooks(self, count=3):
        hooks = []
        for _ in range(count):
            template = random.choice(self.templates)
            topic = random.choice(self.topics)
            hooks.append(template.format(topic=topic))
        return hooks

if __name__ == "__main__":
    gen = HooksGenerator()
    print(gen.generate_daily_hooks())
