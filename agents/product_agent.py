from core.agent_base import Agent
from rendering.template_loader import load_template
from rendering.template_renderer import render
import json, os

class ProductAgent(Agent):
    def handle(self, event, data):
        if event != "product_loaded":
            return

        template = load_template("templates/product.json")
        output = render(template, data)

        os.makedirs("outputs", exist_ok=True)
        with open("outputs/product_page.json", "w") as f:
            json.dump(output, f, indent=2)
