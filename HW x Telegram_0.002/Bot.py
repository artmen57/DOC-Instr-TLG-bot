import glob
from itertools import zip_longest
from telegram import BotCommand
from telegram.ext import (  Updater,
                            CallbackContext,
                            CommandHandler,
                            MessageHandler,
                            Filters         )
from telegram.update import Update
import check2, os,re


id="" #Enter your Telegram Token
upd=Updater(id,use_context=True)
command = [BotCommand("start","to start something"),
            BotCommand("help", "Узнать про функционал бота"),
            ("bye", "to show doc")]

ext=(".jpeg", ".jpg",".png")

def start(update:Update,context:CallbackContext):
    update.message.reply_text("HELLO Wolrd")

def help(update:Update,context:CallbackContext):
    update.message.reply_text("Your mssg")

def unknw(update:Update,context:CallbackContext):
    
    
    if update.message.text.find("VPN")!=-1 or update.message.text.find("ВПН")!=-1:
        path="D:\HW x Telegram\guides\guide1"
        check2.img_extract(path+"\\bot.docx",path+"\img")
        txt, step=check2.text_extract(path+"\\bot.docx")
        img_list=check2.img_sender(path,step)
        img_ar=glob.glob(path+"\img\*")
        img_ar.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
        for img,do in zip_longest(img_ar, step):    
            if img.endswith(ext):
                context.bot.send_photo(chat_id = update.effective_chat.id, photo=open(img,"rb"),caption=do)


    elif update.message.text.find("КСПД")!=-1 :
        path="D:\HW x Telegram\guides\guide2"
        check2.img_extract(path+"\\bot.docx",path+"\img")
        txt, step=check2.text_extract(path+"\\bot.docx")
        img_list=check2.img_sender(path,step)
        img_ar=glob.glob(path+"\img\*")
        img_ar.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
        for img,do in zip_longest(img_ar, step):    
            if img.endswith(ext):
                context.bot.send_photo(chat_id = update.effective_chat.id, photo=open(img,"rb"),caption=do)
    else:
        update.message.reply_text(f"sry, I cannot understand '{update.message.text}'")

upd.dispatcher.add_handler(CommandHandler('start',start))
upd.dispatcher.add_handler(CommandHandler('help',help))
upd.dispatcher.add_handler(MessageHandler(Filters.text,unknw))

if __name__=="__main__":
    upd.start_polling()
    upd.bot.set_my_commands(command)
    


"""    
                Created Image extractor.   
                Created text extractor & copy in buffer
                Saved formation of the text 
                Checked existence of extraacted images for guide
                Need to claim keywords to send instructions  
"""        


#upd.dispatcher.add_handler(CommandHandler('stop', stop))
""" 
def stop():
    threading.Thread(target=shutdown).start()

def shutdown():
    upd.stop()
    upd.is_idle = False
"""
