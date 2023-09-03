import asyncio
import sqlite3
from tabulate import tabulate
from rich import print
from utility import check_group_exists, check_channel_exists

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


def add_name_to_group_table():
    ans = input("Enter a name to add to the group table or d/id , < : ")
    if ans.startswith("d/"):
        delete_item_by_id(table_name="group_table", item_id=ans[2:])
        return add_name_to_group_table()
    elif ans == "<":
        from main import start

        return start()
    loop = asyncio.get_event_loop()
    checking = loop.run_until_complete(check_group_exists(ans))
    if checking:
        cursor.execute("INSERT INTO group_table (name) VALUES (?)", (ans,))
        conn.commit()
        print(f"Added '{ans}' to the group table ✅")
        return add_name_to_group_table()
    return add_name_to_group_table()


def add_name_to_channel_table():
    ans = input("Enter a name to add to the channel table or d/id , < : ")
    if ans.startswith("d/"):
        delete_item_by_id(table_name="channel_table", item_id=ans[2:])
        return add_name_to_channel_table()
    elif ans == "<":
        from main import start

        return start()
    loop = asyncio.get_event_loop()
    checking = loop.run_until_complete(check_channel_exists(ans))
    if checking:
        cursor.execute("INSERT INTO channel_table (name) VALUES (?)", (ans,))
        conn.commit()
        print(f"Added '{ans}' to the channel table ✅")
        return add_name_to_channel_table()
    return add_name_to_channel_table()


def delete_item_by_id(table_name, item_id):
    checking = cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (item_id,))
    if checking.fetchone():
        cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (item_id,))
        conn.commit()
        print(f"Deleted item with ID {item_id} from the {table_name} ✔")
    else:
        print(f"[red]In {table_name} , this {item_id} id not found  ❌ !!! [/red] ")


def display_all_names(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    if rows:
        headers = ["ID", "Name"]
        table_data = [[row[1], row[0]] for row in rows]
        table = tabulate(table_data, headers, tablefmt="fancy_grid")
        print(f"\n[bold]All Names in the {table_name} Table:[/bold]\n")
        print(table)
    else:
        print(f"\n[bold]No names found in the {table_name} Table.[/bold]\n")
