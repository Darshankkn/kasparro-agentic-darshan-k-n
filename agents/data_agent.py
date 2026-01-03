from core.agent_base import Agent

class DataAgent(Agent):
    def start(self):
        product_data = {
            "name": "GlowBoost Vitamin C Serum",
            "price": 699,
            "ingredients": ["Vitamin C", "Hyaluronic Acid"],
            "benefits": ["Brightening", "Fades dark spots"],
            "usage": "Apply 2–3 drops before sunscreen",
            "side_effects": "Mild tingling",
            "skin_type": ["Oily", "Combination"]
        }
        self.bus.publish("product_loaded", product_data)
