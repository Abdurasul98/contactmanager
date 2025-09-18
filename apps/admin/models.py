contact_query = """
    CREATE TABLE IF NOT EXISTS contacts
    (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    phone VARCHAR(32) NOT NULL
    )
"""