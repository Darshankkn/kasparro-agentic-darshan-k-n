# Kasparro Agentic Content Generation System

This project is a **multi-agent, event-driven system** that automatically generates structured JSON content pages for products. It was developed as part of the Applied AI Engineer assignment at Kasparro.

The system uses **autonomous agents**, a **shared message bus**, and **template-driven rendering** to produce machine-readable outputs.

---

## Objective

- Demonstrate a **true multi-agent system** with autonomous, decision-making agents  
- Ensure **dynamic coordination** via an event-driven architecture  
- Generate **JSON outputs** for FAQs, product pages, and comparisons  
- Maintain **clean, reusable code and templates**  

---

## How It Works

- **Data Agent**: Loads product data and publishes it to the bus  
- **Question Agent**: Generates questions and publishes them  
- **FAQ Agent**: Creates FAQ JSON based on questions  
- **Product Agent**: Generates product page JSON  
- **Comparison Agent**: Decides if a comparison page is needed and creates JSON  

> Agents communicate **only through the message bus**. The orchestrator **starts the system** but does not control agent logic.

---

## How to Run

1. Ensure **Python 3.9+** is installed  
2. Open a terminal at the project root  
3. Run:

```bash
python orchestrator.py
