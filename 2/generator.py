import itertools


queries = [
    {
        "rental": ["staff_id", "rental_id", "customer_id", "last_update"],
        "payment": ["rental_id", "payment_date"],
        "customer": ["customer_id"]
    },
    {
        "film": ["title", "release_year", "rental_rate"]
    }
]


def add_inex(name, table, columns):
    return f"CREATE INDEX {name} ON {table} ({','.join(columns)});"


for q, query in enumerate(queries):
    indexes = {}

    for table, columns in query.items():
        for i in range(1, len(columns) + 1):
            for combination in itertools.combinations(columns, i):
                indexes[f"query_{q}_{len(indexes)}"] = \
                    table + f" ({', '.join(combination)});"

    for name, index in indexes.items():
        print(f"CREATE INDEX {name} ON {index}")

    print()
    [print("DROP INDEX " + name) for name in indexes]
    print("----------")