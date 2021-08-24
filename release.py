from fast import execute_sql


def prepare_db():
    execute_sql(
        """
        CREATE TABLE IF NOT EXISTS numbers(
            name text NOT NULL UNIQUE,
            n integer NOT NULL DEFAULT 0
        )
        ;
        """
    )

    print(2131232131)


if __name__ == "__main__":
    prepare_db()