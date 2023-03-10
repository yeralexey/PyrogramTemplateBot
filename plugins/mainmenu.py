from main import *


@Client.on_message(filters.private & filters.command(['start']))
async def send_welcome_on_command(client, message):
    user = await User.get_user(user_id=message.chat.id, user_name=message.from_user.username, set_active=True)
    text = plate("mainmenu_welcome_message", user.chosen_language)
    keyboard = kb([[(plate("registration_button", user.chosen_language), 'proceed_lastname')]])
    await Client.send_message(client, chat_id=message.chat.id, text=text, reply_markup=keyboard)


@Client.on_callback_query(filters.regex(pattern='main_start'))
async def send_welcome_on_call(client, call):
    user = await User.get_user(call.message.chat.id)
    await user.set_attribute("current_step", None)
    text = plate("mainmenu_welcome_message", user.chosen_language)
    keyboard = kb([[(plate("registration_button", user.chosen_language), 'proceed_lastname')]])
    await Client.edit_message_text(client, chat_id=call.message.chat.id, message_id=call.message.id,
                                   text=text, reply_markup=keyboard)
