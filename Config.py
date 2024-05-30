import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "RahulReviews")
  # Postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", "")
  API_HASH = os.environ.get("API_HASH", "")
  # Emter Your ID
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1255023013").split()))
  SUDO_USERS.append(1255023013)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**ᴅᴇᴠᴇʟᴏᴘᴇᴅ  ʙʏ**  [ʀᴀʜᴜʟ](https://youtube.com/@RahulReviews)"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**[{}](tg://user?id={})**,\n𝙸  𝙲𝙰𝙽  𝙵𝙾𝚁𝙲𝙴  𝙼𝙴𝙼𝙱𝙴𝚁𝚂  𝚃𝙾  𝙹𝙾𝙸𝙽  𝙰  𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲  𝙲𝙷𝙰𝙽𝙽𝙴𝙻  𝙱𝙴𝙵𝙾𝚁𝙴  𝚆𝚁𝙸𝚃𝙸𝙽𝙶  𝙼𝙴𝚂𝚂𝙰𝙶𝙴  𝙸𝙽  𝚃𝙷𝙴  𝙶𝚁𝙾𝚄𝙿.\n\n𝙲𝙷𝙴𝙲𝙺𝙾𝚄𝚃  /help  𝙵𝙾𝚁  𝙼𝙾𝚁𝙴..."