from core.agent_base import Agent

class QuestionAgent(Agent):
    def handle(self, event, data):
        if event != "product_loaded":
            return

        questions = {
            "usage": ["How to use GlowBoost?"],
            "safety": ["Does it cause irritation?"],
            "benefits": ["What are the benefits?"],
            "price": ["Is it affordable?"],
            "comparison": ["How is it better than others?"]
        }

        if len(questions) < 5:
            questions["general"] = ["Is it good for oily skin?"]

        self.bus.publish("questions_ready", questions)
