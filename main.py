#PYTHON code 
#FILE NAME : main.py
#DESCRIPTION : Technical analysis bot from TendingView  
#Required libs  : telebot json tradingview_ta
#* : Telegram : [@Akil828 - @ffffffm] , Github : AKILXXX
#* : If you are  bitch  change the rights  
#2021/9/19


from tradingview_ta import TA_Handler, Interval, Exchange
import json
from telebot import types
import telebot



bot = telebot.TeleBot(input("Enter Your telegram bot Token : "))
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def send_wel(message):
    inline = types.InlineKeyboardMarkup(row_width=3)
 #   rf = types.InlineKeyboardButton("♻️تحديث",callback_data="tt")
 
 
    m1 = types.InlineKeyboardButton("1M🕛",callback_data="1m")
    m5 = types.InlineKeyboardButton("5M🕑",callback_data="5m")
    m15 = types.InlineKeyboardButton("15M🕓",callback_data="15m")
    m30 = types.InlineKeyboardButton("30M🕔",callback_data="30m")
    h1 = types.InlineKeyboardButton("1H🕕",callback_data="1h")
    h4 = types.InlineKeyboardButton("4H🕖",callback_data="4h")
    inline.add(m1,m5)
    inline.add(m15,m30)
    inline.add(h1,h4)
     
    sc = '*Choose The Frame ⌚ : * \n\n\n 📕 : 𝐍𝐎𝐓𝐄 ->\n*The bot fetches analytics from 𝚃𝚛𝚊𝚍𝚒𝚗𝚐𝚅𝚒𝚎𝚠* \n(*I am not asking you to follow any analysis*) 🌐 \n\n 𝗕𝐨𝐭 𝗗𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : [𝙰𝚔𝚒𝚕](t.me/akil828) 📈'
    bot.reply_to(message,sc,reply_markup=inline,parse_mode='markdown',disable_web_page_preview=True)    
                        
@bot.callback_query_handler(func=(lambda call:True))
def call(call):
    if call.data == "5m": #5m
      eu = TA_Handler(
      symbol="EURUSD",
      screener="forex",
      exchange="FX_IDC",
      interval=Interval.INTERVAL_5_MINUTES)

      ea = TA_Handler(
      symbol="EURAUD",
      screener="forex",
      exchange="FX_IDC",
      interval=Interval.INTERVAL_5_MINUTES
      )

      ec = TA_Handler(
      symbol="EURCAD",
      screener="forex",
      exchange="FX_IDC",
      interval=Interval.INTERVAL_5_MINUTES
      )

      ech = TA_Handler(
      symbol="EURCHF",
      screener="forex",
      exchange="FX_IDC",
      interval=Interval.INTERVAL_5_MINUTES
      )
      eusd = eu.get_analysis().summary
      eusd1 = eusd['RECOMMENDATION']
      eusd2 = eusd['BUY']
      eusd3 = eusd['NEUTRAL']
      eusd4 = eusd['SELL']
      eusd2b = int(eusd2/0.26)
      eusd2n = int(eusd3/0.26)
      eusd2s  = int(eusd4/0.26)
      xu = f'%{eusd2b}✅ %{eusd2n}☑ %{eusd2s}❗'
    
    
    
      eaud = ea.get_analysis().summary
      eaud1 = eaud['RECOMMENDATION']
      eaud2 = eaud['BUY']
      eaud3 = eaud['NEUTRAL']
      eaud4 = eaud['SELL']
      eaud2b = int(eaud2/0.26)
      eaud2n = int(eaud3/0.26)
      eaud2s = int(eaud4/0.26)
      xa = f'%{eaud2b}✅ %{eaud2n}☑ %{eaud2s}❗'
      
    
      ecad = ec.get_analysis().summary
      ecad1 = ecad['RECOMMENDATION']
      ecad2 = ecad['BUY']
      ecad3 = ecad['NEUTRAL']
      ecad4 = ecad['SELL']
      ecad2b = int(ecad2/0.26)
      ecad2n = int(ecad3/0.26)
      ecad2s = int(ecad4/0.26)
      xc = f'%{ecad2b}✅ %{ecad2n}☑ %{ecad2s}❗'

      echf = ech.get_analysis().summary
      echf1 = echf['RECOMMENDATION']
      echf2 = echf['BUY']
      echf3 = echf['NEUTRAL']
      echf4 = echf['SELL']
      echf2b = int(echf2/0.26)
      echf2n = int(echf3/0.26)
      echf2s = int(echf4/0.26)
      xh = f'%{echf2b}✅ %{echf2n}☑ %{echf2s}❗'      
     # inline.add(rf)
      xccx = f'*TRADING VIEW SIGNALS 5M ⛔\n✅ SIGNAL to buy ☑ Natural SIGNAL ❗SIGNAL to buy \n\n EUR/USD🇪🇺🇺🇸 : SIGNAL {eusd1}   \nSignal strength {eusd2}✅ {eusd3}☑ {eusd4}❗\n {xu}\n\nEUR/AUD🇪🇺🇦🇺 : SIGNAL {eaud1}   \nSignal strength {eaud2}✅ {eaud3}☑ {eaud4}❗ \n {xa}\n\nEUR/CAD🇪🇺🇨🇦 : SIGNAL {ecad1}   \nSignal strength {ecad2}✅ {ecad3}☑ {ecad4}❗\n{xc}\n\nEUR/CHF🇪🇺🇨🇭 : SIGNAL {echf1}   \nSignal strength {echf2}✅ {echf3}☑ {echf4}❗\n{xh}\n\n Done By* [Akil](t.me/Akil828)🇾🇪'
 
      bot.reply_to(call.message,text=xccx,parse_mode='markdown',disable_web_page_preview=True)
      
      print(call.message.reply_to_message.text)
    elif call.data == "1m":    #1m
        eu = TA_Handler(
        symbol="EURUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_1_MINUTE
        )

        ea = TA_Handler(
       symbol="EURAUD",
       screener="forex",
       exchange="FX_IDC",
       interval=Interval.INTERVAL_1_MINUTE)

        ec = TA_Handler(
        symbol="EURCAD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_1_MINUTE
        )

        ech = TA_Handler(
        symbol="EURCHF",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_1_MINUTE
        )
        eusd = eu.get_analysis().summary
        eusd1 = eusd['RECOMMENDATION']
        eusd2 = eusd['BUY']
        eusd3 = eusd['NEUTRAL']
        eusd4 = eusd['SELL']
        eusd2b = int(eusd2/0.26)
        eusd2n = int(eusd3/0.26)
        eusd2s  = int(eusd4/0.26)
        xu = f'%{eusd2b}✅ %{eusd2n}☑ %{eusd2s}❗'
    
    
    
        eaud = ea.get_analysis().summary
        eaud1 = eaud['RECOMMENDATION']
        eaud2 = eaud['BUY']
        eaud3 = eaud['NEUTRAL']
        eaud4 = eaud['SELL']
        eaud2b = int(eaud2/0.26)
        eaud2n = int(eaud3/0.26)
        eaud2s = int(eaud4/0.26)
        xa = f'%{eaud2b}✅ %{eaud2n}☑ %{eaud2s}❗'
      
    
        ecad = ec.get_analysis().summary
        ecad1 = ecad['RECOMMENDATION']
        ecad2 = ecad['BUY']
        ecad3 = ecad['NEUTRAL']
        ecad4 = ecad['SELL']
        ecad2b = int(ecad2/0.26)
        ecad2n = int(ecad3/0.26)
        ecad2s = int(ecad4/0.26)
        xc = f'%{ecad2b}✅ %{ecad2n}☑ %{ecad2s}❗'

        echf = ech.get_analysis().summary
        echf1 = echf['RECOMMENDATION']
        echf2 = echf['BUY']
        echf3 = echf['NEUTRAL']
        echf4 = echf['SELL']
        echf2b = int(echf2/0.26)
        echf2n = int(echf3/0.26)
        echf2s = int(echf4/0.26)
        xh = f'%{echf2b}✅ %{echf2n}☑ %{echf2s}❗'      
     # inline.add(rf)
    
        print(xh)
        bot.send_message(chat_id=(call.message.chat.id),disable_web_page_preview=True,text=f'*TRADING VIEW SIGNALS 1M ⛔\n✅ SIGNAL to buy ☑ Natural SIGNAL ❗SIGNAL to buy \n\n EUR/USD🇪🇺🇺🇸 : SIGNAL {eusd1}   \nSignal strength {eusd2}✅ {eusd3}☑ {eusd4}❗\n {xu}\n\nEUR/AUD🇪🇺🇦🇺 : SIGNAL {eaud1}   \nSignal strength {eaud2}✅ {eaud3}☑ {eaud4}❗ \n {xa}\n\nEUR/CAD🇪🇺🇨🇦 : SIGNAL {ecad1}   \nSignal strength {ecad2}✅ {ecad3}☑ {ecad4}❗\n{xc}\n\nEUR/CHF🇪🇺🇨🇭 : SIGNAL {echf1}   \nSignal strength {echf2}✅ {echf3}☑ {echf4}❗\n{xh}\n\n Done By* [Akil](t.me/Akil828)🇾🇪',parse_mode='markdown')
      
    elif call.data == "15m":    #15m
        eu = TA_Handler(
        symbol="EURUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_15_MINUTES
        )
        ea = TA_Handler(
        symbol="EURAUD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_15_MINUTES)
        
        ec = TA_Handler(
        symbol="EURCAD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_15_MINUTES
        )

        ech = TA_Handler(
        symbol="EURCHF",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_15_MINUTES
        )
        eusd = eu.get_analysis().summary
        eusd1 = eusd['RECOMMENDATION']
        eusd2 = eusd['BUY']
        eusd3 = eusd['NEUTRAL']
        eusd4 = eusd['SELL']
        eusd2b = int(eusd2/0.26)
        eusd2n = int(eusd3/0.26)
        eusd2s  = int(eusd4/0.26)
        xu = f'%{eusd2b}✅ %{eusd2n}☑ %{eusd2s}❗'
    
    
    
        eaud = ea.get_analysis().summary
        eaud1 = eaud['RECOMMENDATION']
        eaud2 = eaud['BUY']
        eaud3 = eaud['NEUTRAL']
        eaud4 = eaud['SELL']
        eaud2b = int(eaud2/0.26)
        eaud2n = int(eaud3/0.26)
        eaud2s = int(eaud4/0.26)
        xa = f'%{eaud2b}✅ %{eaud2n}☑ %{eaud2s}❗'
      
    
        ecad = ec.get_analysis().summary
        ecad1 = ecad['RECOMMENDATION']
        ecad2 = ecad['BUY']
        ecad3 = ecad['NEUTRAL']
        ecad4 = ecad['SELL']
        ecad2b = int(ecad2/0.26)
        ecad2n = int(ecad3/0.26)
        ecad2s = int(ecad4/0.26)
        xc = f'%{ecad2b}✅ %{ecad2n}☑ %{ecad2s}❗'

        echf = ech.get_analysis().summary
        echf1 = echf['RECOMMENDATION']
        echf2 = echf['BUY']
        echf3 = echf['NEUTRAL']
        echf4 = echf['SELL']
        echf2b = int(echf2/0.26)
        echf2n = int(echf3/0.26)
        echf2s = int(echf4/0.26)
        xh = f'%{echf2b}✅ %{echf2n}☑ %{echf2s}❗'      
     # inline.add(rf)
    
 
        bot.send_message(chat_id=(call.message.chat.id),disable_web_page_preview=True,text=f'*TRADING VIEW SIGNALS 15M ⛔\n✅ SIGNAL to buy ☑ Natural SIGNAL ❗SIGNAL to buy \n\n EUR/USD🇪🇺🇺🇸 : SIGNAL {eusd1}   \nSignal strength {eusd2}✅ {eusd3}☑ {eusd4}❗\n {xu}\n\nEUR/AUD🇪🇺🇦🇺 : SIGNAL {eaud1}   \nSignal strength {eaud2}✅ {eaud3}☑ {eaud4}❗ \n {xa}\n\nEUR/CAD🇪🇺🇨🇦 : SIGNAL {ecad1}   \nSignal strength {ecad2}✅ {ecad3}☑ {ecad4}❗\n{xc}\n\nEUR/CHF🇪🇺🇨🇭 : SIGNAL {echf1}   \nSignal strength {echf2}✅ {echf3}☑ {echf4}❗\n{xh}\n\n Done By* [Akil](t.me/Akil828)🇾🇪',parse_mode='markdown')


    elif call.data == "30m":    #30
        eu = TA_Handler(
        symbol="EURUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_30_MINUTES
        )

        ea = TA_Handler(
       symbol="EURAUD",
       screener="forex",
       exchange="FX_IDC",
       interval=Interval.INTERVAL_30_MINUTES)

        ec = TA_Handler(
        symbol="EURCAD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_30_MINUTES
        )

        ech = TA_Handler(
        symbol="EURCHF",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_30_MINUTES
        )
        eusd = eu.get_analysis().summary
        eusd1 = eusd['RECOMMENDATION']
        eusd2 = eusd['BUY']
        eusd3 = eusd['NEUTRAL']
        eusd4 = eusd['SELL']
        eusd2b = int(eusd2/0.26)
        eusd2n = int(eusd3/0.26)
        eusd2s  = int(eusd4/0.26)
        xu = f'%{eusd2b}✅ %{eusd2n}☑ %{eusd2s}❗'
    
        
        eaud = ea.get_analysis().summary
        eaud1 = eaud['RECOMMENDATION']
        eaud2 = eaud['BUY']
        eaud3 = eaud['NEUTRAL']
        eaud4 = eaud['SELL']
        eaud2b = int(eaud2/0.26)
        eaud2n = int(eaud3/0.26)
        eaud2s = int(eaud4/0.26)
        xa = f'%{eaud2b}✅ %{eaud2n}☑ %{eaud2s}❗'
      
    
        ecad = ec.get_analysis().summary
        ecad1 = ecad['RECOMMENDATION']
        ecad2 = ecad['BUY']
        ecad3 = ecad['NEUTRAL']
        ecad4 = ecad['SELL']
        ecad2b = int(ecad2/0.26)
        ecad2n = int(ecad3/0.26)
        ecad2s = int(ecad4/0.26)
        xc = f'%{ecad2b}✅ %{ecad2n}☑ %{ecad2s}❗'

        echf = ech.get_analysis().summary
        echf1 = echf['RECOMMENDATION']
        echf2 = echf['BUY']
        echf3 = echf['NEUTRAL']
        echf4 = echf['SELL']
        echf2b = int(echf2/0.26)
        echf2n = int(echf3/0.26)
        echf2s = int(echf4/0.26)
        xh = f'%{echf2b}✅ %{echf2n}☑ %{echf2s}❗'      
     # inline.add(rf)
    
 
        bot.send_message(chat_id=(call.message.chat.id),disable_web_page_preview=True,text=f'*TRADING VIEW SIGNALS 30M ⛔\n✅ SIGNAL to buy ☑ Natural SIGNAL ❗SIGNAL to buy \n\n EUR/USD🇪🇺🇺🇸 : SIGNAL {eusd1}   \nSignal strength {eusd2}✅ {eusd3}☑ {eusd4}❗\n {xu}\n\nEUR/AUD🇪🇺🇦🇺 : SIGNAL {eaud1}   \nSignal strength {eaud2}✅ {eaud3}☑ {eaud4}❗ \n {xa}\n\nEUR/CAD🇪🇺🇨🇦 : SIGNAL {ecad1}   \nSignal strength {ecad2}✅ {ecad3}☑ {ecad4}❗\n{xc}\n\nEUR/CHF🇪🇺🇨🇭 : SIGNAL {echf1}   \nSignal strength {echf2}✅ {echf3}☑ {echf4}❗\n{xh}\n\n Done By* [Akil](t.me/Akil828)🇾🇪',parse_mode='markdown')

    elif call.data == "1h":  #h1  
        eu = TA_Handler(
        symbol="EURUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_1_HOUR
        )

        ea = TA_Handler(
       symbol="EURAUD",
       screener="forex",
       exchange="FX_IDC",
       interval=Interval.INTERVAL_1_HOUR)

        ec = TA_Handler(
        symbol="EURCAD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_1_HOUR
        )

        ech = TA_Handler(
        symbol="EURCHF",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_1_HOUR
        )
        eusd = eu.get_analysis().summary
        eusd1 = eusd['RECOMMENDATION']
        eusd2 = eusd['BUY']
        eusd3 = eusd['NEUTRAL']
        eusd4 = eusd['SELL']
        eusd2b = int(eusd2/0.26)
        eusd2n = int(eusd3/0.26)
        eusd2s  = int(eusd4/0.26)
        xu = f'%{eusd2b}✅ %{eusd2n}☑ %{eusd2s}❗'
    
    
    
        eaud = ea.get_analysis().summary
        eaud1 = eaud['RECOMMENDATION']
        eaud2 = eaud['BUY']
        eaud3 = eaud['NEUTRAL']
        eaud4 = eaud['SELL']
        eaud2b = int(eaud2/0.26)
        eaud2n = int(eaud3/0.26)
        eaud2s = int(eaud4/0.26)
        xa = f'%{eaud2b}✅ %{eaud2n}☑ %{eaud2s}❗'
      
    
        ecad = ec.get_analysis().summary
        ecad1 = ecad['RECOMMENDATION']
        ecad2 = ecad['BUY']
        ecad3 = ecad['NEUTRAL']
        ecad4 = ecad['SELL']
        ecad2b = int(ecad2/0.26)
        ecad2n = int(ecad3/0.26)
        ecad2s = int(ecad4/0.26)
        xc = f'%{ecad2b}✅ %{ecad2n}☑ %{ecad2s}❗'

        echf = ech.get_analysis().summary
        echf1 = echf['RECOMMENDATION']
        echf2 = echf['BUY']
        echf3 = echf['NEUTRAL']
        echf4 = echf['SELL']
        echf2b = int(echf2/0.26)
        echf2n = int(echf3/0.26)
        echf2s = int(echf4/0.26)
        xh = f'%{echf2b}✅ %{echf2n}☑ %{echf2s}❗'      
     # inline.add(rf)
    
 
        bot.send_message(chat_id=(call.message.chat.id),disable_web_page_preview=True,text=f'*TRADING VIEW SIGNALS 1H ⛔\n✅ SIGNAL to buy ☑ Natural SIGNAL ❗SIGNAL to buy \n\n EUR/USD🇪🇺🇺🇸 : SIGNAL {eusd1}   \nSignal strength {eusd2}✅ {eusd3}☑ {eusd4}❗\n {xu}\n\nEUR/AUD🇪🇺🇦🇺 : SIGNAL {eaud1}   \nSignal strength {eaud2}✅ {eaud3}☑ {eaud4}❗ \n {xa}\n\nEUR/CAD🇪🇺🇨🇦 : SIGNAL {ecad1}   \nSignal strength {ecad2}✅ {ecad3}☑ {ecad4}❗\n{xc}\n\nEUR/CHF🇪🇺🇨🇭 : SIGNAL {echf1}   \nSignal strength {echf2}✅ {echf3}☑ {echf4}❗\n{xh}\n\n Done By* [Akil](t.me/Akil828)🇾🇪',parse_mode='markdown')

    elif call.data == "4h":    
        eu = TA_Handler(
        symbol="EURUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_4_HOURS
        )

        ea = TA_Handler(
       symbol="EURAUD",
       screener="forex",
       exchange="FX_IDC",
       interval=Interval.INTERVAL_4_HOURS)

        ec = TA_Handler(
        symbol="EURCAD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_4_HOURS
        )

        ech = TA_Handler(
        symbol="EURCHF",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_4_HOURS
        )
        eusd = eu.get_analysis().summary
        eusd1 = eusd['RECOMMENDATION']
        eusd2 = eusd['BUY']
        eusd3 = eusd['NEUTRAL']
        eusd4 = eusd['SELL']
        eusd2b = int(eusd2/0.26)
        eusd2n = int(eusd3/0.26)
        eusd2s  = int(eusd4/0.26)
        xu = f'%{eusd2b}✅ %{eusd2n}☑ %{eusd2s}❗'
    
    
    
        eaud = ea.get_analysis().summary
        eaud1 = eaud['RECOMMENDATION']
        eaud2 = eaud['BUY']
        eaud3 = eaud['NEUTRAL']
        eaud4 = eaud['SELL']
        eaud2b = int(eaud2/0.26)
        eaud2n = int(eaud3/0.26)
        eaud2s = int(eaud4/0.26)
        xa = f'%{eaud2b}✅ %{eaud2n}☑ %{eaud2s}❗'
      
    
        ecad = ec.get_analysis().summary
        ecad1 = ecad['RECOMMENDATION']
        ecad2 = ecad['BUY']
        ecad3 = ecad['NEUTRAL']
        ecad4 = ecad['SELL']
        ecad2b = int(ecad2/0.26)
        ecad2n = int(ecad3/0.26)
        ecad2s = int(ecad4/0.26)
        xc = f'%{ecad2b}✅ %{ecad2n}☑ %{ecad2s}❗'

        echf = ech.get_analysis().summary
        echf1 = echf['RECOMMENDATION']
        echf2 = echf['BUY']
        echf3 = echf['NEUTRAL']
        echf4 = echf['SELL']
        echf2b = int(echf2/0.26)
        echf2n = int(echf3/0.26)
        echf2s = int(echf4/0.26)
        xh = f'%{echf2b}✅ %{echf2n}☑ %{echf2s}❗'      
     # inline.add(rf)
    
 
        bot.send_message(chat_id=(call.message.chat.id),disable_web_page_preview=True,text=f'*TRADING VIEW SIGNALS 4H ⛔\n✅ SIGNAL to buy ☑ Natural SIGNAL ❗SIGNAL to buy \n\n EUR/USD🇪🇺🇺🇸 : SIGNAL {eusd1}   \nSignal strength \n {eusd2}✅ {eusd3}☑ {eusd4}❗\n {xu}\n\nEUR/AUD🇪🇺🇦🇺 : SIGNAL {eaud1}   \nSignal strength {eaud2}✅ {eaud3}☑ {eaud4}❗ \n {xa}\n\nEUR/CAD🇪🇺🇨🇦 : SIGNAL {ecad1}   \nSignal strength {ecad2}✅ {ecad3}☑ {ecad4}❗\n{xc}\n\nEUR/CHF🇪🇺🇨🇭 : SIGNAL {echf1}   \nSignal strength {echf2}✅ {echf3}☑ {echf4}❗\n{xh}\n\n Done By* [Akil](t.me/Akil828)🇾🇪',parse_mode='markdown')
    
if __name__ == "__main__":
    bot.polling(none_stop=True)



#PYTHON code 
#FILE NAME : main.py
#DESCRIPTION : Technical analysis bot from TendingView  
#Required libs  : telebot json tradingview_ta
#* : Telegram : [@Akil828 - @ffffffm] , Github : AKILXXX
#* : If you are bitch  change the rights  
#2021/9/19




# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}