from core.agent_base import Agent
from rendering.template_loader import load_template
from rendering.template_renderer import render
import json, os

class ComparisonAgent(Agent):
    def handle(self, event, data):
        if event != "product_loaded":
            return

        if data["price"] >= 800:
            return  # agent DECIDES not to act

        product_b = {
            "name": "RadiancePlus Serum",
            "price": 799,
            "ingredients": ["Vitamin C"]
        }

        comparison = {
            "product_a": data,
            "product_b": product_b,
            "summary": "GlowBoost offers better value"
        }

        template = load_template("templates/comparison.json")
        output = render(template, comparison)

        os.makedirs("outputs", exist_ok=True)
        with open("outputs/comparison_page.json", "w") as f:
            json.dump(output, f, indent=2)
