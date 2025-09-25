from core.database import execute_query
main_menu = """
1. Contact 
2. Message
3. Exit
"""
contact_manager = """
1. Add contact
2. Read contact
3. Update contact
4. Delete contact
5. Exit
"""

sms_manager = """
1. Send message
2. Delete message
3. Show messages 
4. Exit
"""

def get_user_option(menu: str, max_option: int):
    while True:
        print(menu)
        option = input("Enter your option: ")
        if not (1 <= int(option) <= max_option):
            print("Invalid option number!")
        else:
            return option


def execute_tables():
    from apps.contact.models import contact_query
    from apps.message.model import sms_query

    execute_query(query=contact_query)
    execute_query(query=sms_query)
