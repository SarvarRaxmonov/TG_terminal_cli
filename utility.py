from rich.text import Text
from datetime import datetime
from rich import print


current_year = datetime.now().year
ascii_art = f"""
╔╦╗╔═╗  ┌┬┐┌─┐┬─┐┌┬┐┬┌┐┌┌─┐┬    ┌─┐┬  ┬
 ║ ║ ╦   │ ├┤ ├┬┘│││││││├─┤│    │  │  │   
 ╩ ╚═╝   ┴ └─┘┴└─┴ ┴┴┘└┘┴ ┴┴─┘  └─┘┴─┘┴  © {current_year}  1.0.0 version
_________________________________________________                                                                     
 """


def main_logo_print():
    main_logo = Text(ascii_art)
    main_logo.stylize("bold bright_white")
    small_font_style = "font-size: 4px"
    main_logo.stylize(small_font_style, 0, 0)
    intro_text = (
        "\n Our first and ultimate goal is to achieve distraction free ecosystems and softwares which are"
        " has to work for humanity not humanity work for them . This green systems can influence to"
        " our daily life in a positive way , and I believe this distraction free tools to be more effective "
        " than our current apps .\n"
        "\n[italic]Embark on your journey[/italic] by harnessing the [green]TG terminal CLI[/green] to conquer your tasks.\n\n"
    )

    return print(main_logo, intro_text)


async def check_group_exists(name):
    from main import client

    try:
        await client.start()
        await client.get_dialogs(limit=None)
        entity = await client.get_entity(name)
        if entity.megagroup:
            return True
        return print(f"🚫 An error occurred while checking the group: please only group")
    except Exception as e:
        print(f"🚫 An error occurred while checking the group: {e}")
        return False


async def check_channel_exists(name):
    from main import client

    try:
        await client.start()
        await client.get_dialogs(limit=None)
        entity = await client.get_entity(name)
        if entity.broadcast:
            return True
        return print(
            f"🚫 An error occurred while checking the channel: please only channel"
        )
    except Exception as e:
        print(f"🚫 An error occurred while checking the channel: {e}")
        return False
