import telebot
import json

from decouple import config



token=config("TELEGRAM_BOT_TOKEN")
group_id=config("GROUP_ID")

bot = telebot.TeleBot(token)

# bot.send_message(
#     group_id, text="O bot do vídeo ta funcionando"
# )


# @bot.message_handler(commands=["start"])
# def enviar_ola(message):
#     bot.reply_to(message, "Olá, bem vindo!")

def message_to_dict(message):
    message_dict = {
        "content_type": message.content_type,
        "id": message.message_id,
        "message_id": message.message_id,
        "from_user": {
            "id": message.from_user.id,
            "is_bot": message.from_user.is_bot,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
            "username": message.from_user.username,
            "language_code": message.from_user.language_code,
            "can_join_groups": message.from_user.can_join_groups,
            "can_read_all_group_messages": message.from_user.can_read_all_group_messages,
            "supports_inline_queries": message.from_user.supports_inline_queries,
            "is_premium": message.from_user.is_premium,
            "added_to_attachment_menu": message.from_user.added_to_attachment_menu,
            "can_connect_to_business": message.from_user.can_connect_to_business
        },
        "date": message.date,
        "chat": {
            "id": message.chat.id,
            "type": message.chat.type,
            "title": message.chat.title,
            "username": message.chat.username,
            "first_name": message.chat.first_name,
            "last_name": message.chat.last_name,
            "is_forum": message.chat.is_forum,
            "max_reaction_count": message.chat.max_reaction_count,
            "photo": message.chat.photo,
            "bio": message.chat.bio,
            "join_to_send_messages": message.chat.join_to_send_messages,
            "join_by_request": message.chat.join_by_request,
            "has_private_forwards": message.chat.has_private_forwards,
            "has_restricted_voice_and_video_messages": message.chat.has_restricted_voice_and_video_messages,
            "description": message.chat.description,
            "invite_link": message.chat.invite_link,
            "pinned_message": message.chat.pinned_message,
            "permissions": message.chat.permissions,
            "slow_mode_delay": message.chat.slow_mode_delay,
            "message_auto_delete_time": message.chat.message_auto_delete_time,
            "has_protected_content": message.chat.has_protected_content,
            "sticker_set_name": message.chat.sticker_set_name,
            "can_set_sticker_set": message.chat.can_set_sticker_set,
            "linked_chat_id": message.chat.linked_chat_id,
            "location": message.chat.location,
            "active_usernames": message.chat.active_usernames,
            "emoji_status_custom_emoji_id": message.chat.emoji_status_custom_emoji_id,
            "has_hidden_members": message.chat.has_hidden_members,
            "has_aggressive_anti_spam_enabled": message.chat.has_aggressive_anti_spam_enabled,
            "emoji_status_expiration_date": message.chat.emoji_status_expiration_date,
            "available_reactions": message.chat.available_reactions,
            "accent_color_id": message.chat.accent_color_id,
            "background_custom_emoji_id": message.chat.background_custom_emoji_id,
            "profile_accent_color_id": message.chat.profile_accent_color_id,
            "profile_background_custom_emoji_id": message.chat.profile_background_custom_emoji_id,
            "has_visible_history": message.chat.has_visible_history,
            "unrestrict_boost_count": message.chat.unrestrict_boost_count,
            "custom_emoji_sticker_set_name": message.chat.custom_emoji_sticker_set_name,
            "business_intro": message.chat.business_intro,
            "business_location": message.chat.business_location,
            "business_opening_hours": message.chat.business_opening_hours,
            "personal_chat": message.chat.personal_chat,
            "birthdate": message.chat.birthdate
        },
        "sender_chat": message.sender_chat,
        "is_automatic_forward": message.is_automatic_forward,
        "reply_to_message": message.reply_to_message,
        "via_bot": message.via_bot,
        "edit_date": message.edit_date,
        "has_protected_content": message.has_protected_content,
        "media_group_id": message.media_group_id,
        "author_signature": message.author_signature,
        "text": message.text,
        "entities": message.entities,
        "caption_entities": message.caption_entities,
        "audio": message.audio,
        "document": message.document,
        "photo": message.photo,
        "sticker": message.sticker,
        "video": message.video,
        "video_note": message.video_note,
        "voice": message.voice,
        "caption": message.caption,
        "contact": message.contact,
        "location": message.location,
        "venue": message.venue,
        "animation": message.animation,
        "dice": message.dice,
        "new_chat_members": message.new_chat_members,
        "left_chat_member": message.left_chat_member,
        "new_chat_title": message.new_chat_title,
        "new_chat_photo": message.new_chat_photo,
        "delete_chat_photo": message.delete_chat_photo,
        "group_chat_created": message.group_chat_created,
        "supergroup_chat_created": message.supergroup_chat_created,
        "channel_chat_created": message.channel_chat_created,
        "migrate_to_chat_id": message.migrate_to_chat_id,
        "migrate_from_chat_id": message.migrate_from_chat_id,
        "pinned_message": message.pinned_message,
        "invoice": message.invoice,
        "successful_payment": message.successful_payment,
        "connected_website": message.connected_website,
        "reply_markup": message.reply_markup,
        "message_thread_id": message.message_thread_id,
        "is_topic_message": message.is_topic_message,
        "chat_background_set": message.chat_background_set,
        "forum_topic_created": message.forum_topic_created,
        "forum_topic_closed": message.forum_topic_closed,
        "forum_topic_reopened": message.forum_topic_reopened,
        "has_media_spoiler": message.has_media_spoiler,
        "forum_topic_edited": message.forum_topic_edited,
        "general_forum_topic_hidden": message.general_forum_topic_hidden,
        "general_forum_topic_unhidden": message.general_forum_topic_unhidden,
        "write_access_allowed": message.write_access_allowed,
        "users_shared": message.users_shared,
        "chat_shared": message.chat_shared,
        "story": message.story,
        "external_reply": message.external_reply,
        "quote": message.quote,
        "link_preview_options": message.link_preview_options,
        "giveaway_created": message.giveaway_created,
        "giveaway": message.giveaway,
        "giveaway_winners": message.giveaway_winners,
        "giveaway_completed": message.giveaway_completed,
        "forward_origin": message.forward_origin,
        "boost_added": message.boost_added,
        "sender_boost_count": message.sender_boost_count,
        "reply_to_story": message.reply_to_story,
        "sender_business_bot": message.sender_business_bot,
        "business_connection_id": message.business_connection_id,
        "is_from_offline": message.is_from_offline,
        "json": {
            "message_id": message.message_id,
            "from": {
                "id": message.from_user.id,
                "is_bot": message.from_user.is_bot,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name,
                "username": message.from_user.username
            },
            "chat": {
                "id": message.chat.id,
                "title": message.chat.title,
                "type": message.chat.type,
                "all_members_are_administrators": True  # Este é um exemplo; ajuste conforme necessário
            },
            "date": message.date,
            "text": message.text
        }
    }
    return message_dict

def impar_par(message_text):
    if message_text.isdigit():     
        msg=int(message_text)
        if msg%2==0:
            return "é par"
        else:
            return "é impar"
    else:
        return "formato errado"


@bot.message_handler()
def echo_all(message):
	msg=impar_par(message.text)
	bot.reply_to(message, msg)

bot.infinity_polling()