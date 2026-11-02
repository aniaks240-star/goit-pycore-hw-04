from decimal import Decimal, InvalidOperation
from pathlib import Path


def total_salary(path):
    salaries = []
    try:
        with open(path, encoding="utf-8-sig") as file:
            for number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    name, amount = line.strip().split(",")
                    salary = Decimal(amount.strip())
                    if not name.strip() or not salary.is_finite() or salary < 0:
                        raise ValueError
                except (ValueError, InvalidOperation) as error:
                    raise ValueError(f"Invalid salary record at line {number}.") from error
                salaries.append(salary)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Cannot read salary data: {error}")
        return 0, 0

    if not salaries:
        return 0, 0
    total = sum(salaries)
    return float(total), float(total / len(salaries))


if __name__ == "__main__":
    total, average = total_salary(Path(__file__).parent / "data" / "salaries.txt")
    print(f"Total salary: {total}, Average salary: {average}")
