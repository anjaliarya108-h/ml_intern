import json

def load_kb():
    with open("data/knowledge_base.json", "r") as f:
        return json.load(f)

def get_pricing():
    kb = load_kb()
    return kb["pricing"]

def get_policies():
    kb = load_kb()
    return kb["policies"]

def format_pricing():
    pricing = get_pricing()

    return f"""
Basic Plan:
- Price: {pricing['basic']['price']}
- Videos: {pricing['basic']['videos']}
- Quality: {pricing['basic']['quality']}

Pro Plan:
- Price: {pricing['pro']['price']}
- Videos: {pricing['pro']['videos']}
- Quality: {pricing['pro']['quality']}
- Features: {pricing['pro']['features']}
"""