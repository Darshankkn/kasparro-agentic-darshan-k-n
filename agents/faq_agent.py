from core.agent_base import Agent
from rendering.template_loader import load_template
from rendering.template_renderer import render
import json, os

class FAQAgent(Agent):
    def handle(self, event, questions):
        if event != "questions_ready":
            return

        faq_items = []
        for k in questions:
            faq_items.append({
                "question": questions[k][0],
                "answer": "Based on product information."
            })

        template = load_template("templates/faq.json")
        output = render(template, {"items": faq_items})

        os.makedirs("outputs", exist_ok=True)
        with open("outputs/faq.json", "w") as f:
            json.dump(output, f, indent=2)
