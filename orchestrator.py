from core.message_bus import MessageBus
from agents.data_agent import DataAgent
from agents.question_agent import QuestionAgent
from agents.faq_agent import FAQAgent
from agents.product_agent import ProductAgent
from agents.comparison_agent import ComparisonAgent

bus = MessageBus()

data_agent = DataAgent("DataAgent", bus)
question_agent = QuestionAgent("QuestionAgent", bus)
faq_agent = FAQAgent("FAQAgent", bus)
product_agent = ProductAgent("ProductAgent", bus)
comparison_agent = ComparisonAgent("ComparisonAgent", bus)

question_agent.subscribe("product_loaded")
faq_agent.subscribe("questions_ready")
product_agent.subscribe("product_loaded")
comparison_agent.subscribe("product_loaded")

data_agent.start()

print("✅ Agentic system executed successfully")
