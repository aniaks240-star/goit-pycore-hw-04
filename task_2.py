from pathlib import Path


def get_cats_info(path):
    cats = []
    identifiers = set()
    try:
        with open(path, encoding="utf-8-sig") as file:
            for number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    cat_id, name, age = [part.strip() for part in line.split(",")]
                    if not cat_id or not name or not age.isdecimal():
                        raise ValueError
                    if cat_id in identifiers:
                        raise ValueError
                except ValueError as error:
                    raise ValueError(f"Invalid cat record at line {number}.") from error
                cats.append({"id": cat_id, "name": name, "age": age})
                identifiers.add(cat_id)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Cannot read cat data: {error}")
        return []
    return cats


if __name__ == "__main__":
    print(get_cats_info(Path(__file__).parent / "data" / "cats.txt"))
