import re
from datetime import datetime

def parse_expense(text):
    try:
        amount_match = re.search(r"\$?(\d+(\.\d{1,2})?)", text)
        category_match = re.search(r"for (\w+)", text)
        date = datetime.now().strftime("%Y-%m-%d")
        amount = float(amount_match.group(1)) if amount_match else None
        category = category_match.group(1) if category_match else "general"
        return {"amount": amount, "category": category, "date": date}
    except:
        return None