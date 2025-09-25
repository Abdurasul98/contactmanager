sms_query = """
    CREATE TABLE IF NOT EXISTS messages
    (
    id SERIAL PRIMARY KEY,
    contact_id INT NULL,
    FOREIGN KEY (contact_id) REFERENCES contacts(id) ON DELETE CASCADE,
    u_message TEXT,
    phone VARCHAR(32) NOT NULL
    )
"""