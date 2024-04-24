"""File imports"""

import json

LANGUAGE = "en"

with open("text.json", "r", encoding="utf-8") as file:
    MSG = json.load(file)


def prompt(text):
    """Add to front of text a arrow to program outputs"""
    return f"==> {text}"


def get_bill_calculations(bill, tip, split):
    """Calculates the bill amount after tip"""
    tip *= 0.01
    total = (bill + (bill * tip)) / split
    return total


def main():
    bill = float(input(prompt(MSG[LANGUAGE]["questions"]["bill"])))
    tip = float(input(prompt(MSG[LANGUAGE]["questions"]["tip"])))
    bill_split = float(input(prompt(MSG[LANGUAGE]["questions"]["split"])))
    result = get_bill_calculations(bill, tip, bill_split)
    print(f'{prompt(MSG[LANGUAGE]['result'])}{result}')


main()
