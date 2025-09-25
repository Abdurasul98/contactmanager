from core.database import execute_query


class ContactQueries:
    @staticmethod
    def read_contact():
        query = "SELECT * FROM contacts"

        return execute_query(query=query, fetch='all')

    @staticmethod
    def add_contact(params: tuple) -> None | bool:
        try:
            query = """INSERT INTO contacts (name,phone)
                       VALUES (%s, %s)
                    """

            execute_query(query=query, params=params)
            print("Added contact")
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_contact(name,phone):
        query = "UPDATE contacts SET name = %s WHERE phone = %s"
        params = (name, phone)
        execute_query(query=query, params=params)
        print("Updated contact")
        return True

    @staticmethod
    def delete_contact(phone):
        query = "DELETE FROM contacts WHERE phone = %s"
        params = (phone,)
        execute_query(query=query, params=params)
        print("Deleted contact")
        return True