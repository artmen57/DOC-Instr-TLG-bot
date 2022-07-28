from telegram import MessageEntity
from telegram.ext import (  Updater,
                            CallbackContext,
                            CommandHandler,
                            MessageHandler,
                            Filters         )
from telegram.update import Update
import check2
    

id="1285601447:AAGIhhPP4v6EPADkrcdKR1L9YjW-z7UZstU"
upd=Updater(id,use_context=True)
         
def start(update:Update,context:CallbackContext):
    update.message.reply_text("HELLO Wolrd")

def help(update:Update,context:CallbackContext):
    update.message.reply_text("Your mssg")

def unknw(update:Update,context:CallbackContext):
   #if update.message.text=="wtf" or update.message.text == "argh" :
    match update.message.text:
        case "wtf":
            path="guides\guide1"
            check2.img_extract(path+"\Bot.docx",path+"\img")
            check2.text_exctact(path+"\Bot.docx")
            """    
                    Created Image extractor.   
                    Created text extractor & copy in buffer
                    Need to save formation of the text 
                    Need to check existence of extraacted images for guide
            """        
            with open(path+"\Bot.docx","r",encoding="unicode_escape") as line:
                idk=line.read()
            context.bot.send_photo(chat_id=update.effective_chat.id,photo=open("guides\guide1\img","rb"),caption=idk)

        case _:    
            update.message.reply_text("sry, I cannot understand '%s'"%update.message.text)


upd.dispatcher.add_handler(CommandHandler('start',start))
upd.dispatcher.add_handler(CommandHandler('help',help))
upd.dispatcher.add_handler(MessageHandler(Filters.text,unknw))
#upd.dispatcher.add_handler(CommandHandler('stop', stop))
if __name__=="__main__":
    upd.start_polling()
    

#print(f"{start}Hi ")
""" 
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
 """
""" 
def stop():
    threading.Thread(target=shutdown).start()

def shutdown():
    upd.stop()
    upd.is_idle = False
 """