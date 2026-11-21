def apply_discount(amount: float, percent: float) -> float:
    return round(amount * (1 - percent / 100), 2)


def add_tax(amount: float, rate: float) -> float:
    return round(amount * (1 + rate / 100), 2)
