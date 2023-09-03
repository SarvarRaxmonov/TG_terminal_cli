from telethon.sync import TelegramClient
import sys
from rich import pretty
from utility import main_logo_print
from rich.prompt import Prompt
from db_control import (
    display_all_names,
    add_name_to_channel_table,
    add_name_to_group_table,
)


pretty.install()
client = TelegramClient(
    "name", api_id=28036966, api_hash="49ba518c255dd3df214d876c92cbc72f"
)


def start():
    ans = Prompt.ask(
        "\n[bold green]Welcome [/bold green]\n"
        "Choose an option:\n"
        "[cyan][ p: [/cyan]getting the personal folder\n"
        "[magenta][ gr: [/magenta]getting the selected groups\n"
        "[yellow][ ch: [/yellow]getting the selected channels\n"
        "[blue][ h: [/blue]for help \n"
        "[cyan]add_ch/[/cyan]to add a new channel to selected\n"
        "[magenta]add_gr/[/magenta]to add a new group to selected\n"
        "[bold]Your choice:[/bold] "
    )
    if ans == "add_ch/":
        display_all_names(table_name="channel_table")
        add = add_name_to_channel_table()

    elif ans == "add_gr/":
        display_all_names(table_name="group_table")
        add = add_name_to_group_table()

    elif ans == "e/":
        sys.exit()

    # elif ans == "p:":
    #     client.loop.run_until_complete(print_unread_personal_messages())


if __name__ == "__main__":
    main_logo_print()
    start()
