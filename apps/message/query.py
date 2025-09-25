from core.database import execute_query


class MessageQueries:
    @staticmethod
    def show_all_messages():
        query = """
            SELECT m.id,c.name,m.phone,m.u_message FROM messages AS m
            LEFT JOIN contacts AS c ON m.contact_id = c.id
        """
        rows =  execute_query(query=query,fetch="all")
        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]}: {row[3]}")
        return rows

    @staticmethod
    def send_message(params:tuple) -> None|bool:
        try:
            query = "INSERT INTO messages (contact_id,u_message,phone) VALUES((SELECT id FROM contacts WHERE phone = %s),%s,%s)"
            execute_query(query=query,params=params)
            print("Message sent")
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def delete_message(message_id):
        query = "DELETE FROM messages WHERE id = %s"
        params = (message_id,)
        execute_query(query=query, params=params)
        print("Deleted message")
        return True