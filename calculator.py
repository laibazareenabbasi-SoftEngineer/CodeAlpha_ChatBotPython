import re

def calculator(user_ques):
    """
    Takes the full text typed by the user (e.g. "5 + 3", "what is 10 * 2")
    finds a simple math expression inside it, and returns a reply string.
    Supports: + - * / % **
    """
    # Look for a pattern like: number operator number  (spaces optional)
    # ** must be checked before * so it isn't split as two '*' operators
    match = re.search(r'(-?\d+\.?\d*)\s*(\*\*|[+\-*/%])\s*(-?\d+\.?\d*)', user_ques)

    if not match:
        return "🤖 Robot: I found a math symbol but couldn't read the numbers. Try like: 5 + 3"

    num1 = float(match.group(1))
    op = match.group(2)
    num2 = float(match.group(3))

    try:
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        elif op == "**":
            result = num1 ** num2
        else:
            return "🤖 Robot: I don't know that operator yet."

        # show whole numbers without a trailing .0
        if result == int(result):
            result = int(result)

        return f"🤖 Robot: {match.group(1)} {op} {match.group(3)} = {result}"

    except ZeroDivisionError:
        return "🤖 Robot: You can't divide by zero!"
