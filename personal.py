import asyncio
from telethon.sync import TelegramClient


# List of group names to monitor
group_names = ["@django", "@djangouz"]  # Replace with your group names


def get_new_unread_messages_from_groups(group_names):
    from main import client
    from telethon import functions, types

    try:
        client.start()
        chat_entity = client.get_entity("@django")
        dialog = client(functions.messages.GetPeerDialogsRequest(peers=[chat_entity]))
        if dialog.dialogs:
            dialog = dialog.dialogs[0]
            unread_count = dialog.unread_count
            messages = client.get_messages(dialog, limit=unread_count)

            print(f"Unread messages in {chat_entity.title}: {unread_count}")
            for message in messages:
                if isinstance(message, types.MessageEmpty):
                    continue
                if message:
                    print(f"Message {message.id}: {message.message}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_new_unread_messages_from_groups(group_names)
