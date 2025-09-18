from core.database import execute_query

main_menu = """
1. Add contact
2. Read contact
3. Update contact
4. Delete contact
5. Exit
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
    from apps.admin.models import contact_query

    execute_query(query=contact_query)