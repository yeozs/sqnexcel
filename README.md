# sqnexcel
Creating a Telegram Bot to House Daily Work Programme Details

Reason for Creating Bot:
Imagine a workplace with daily programme details stored in an excel file. Everyday, individuals will manually grab particular details from the excel file, and type them into telegram to send to the main telegram group chat. This app aims to kick start a telegram bot that automates the process of grabbing certain details from the daily programme excel file and uploading them to telegram.

What folders are present:
- sqnexcel.xlsx => the prove of concept copy of real daily programme excel folder. It extracts details from a 'daily programme' called 'sheet 2' to form the foundations for a telegram message.

- 126sqnexcel.csv, flyingprogramme.csv, sarprogramme.csv, sqnexcel.csv => csv files exported from excel are an acceptable format to upload to telegram

- main.py => python folder containing source code to upload csv files to telegram bot

- requirements.txt, procfile => Used for webhook to Heroku Cloud (to allow python code to run 24/7)
-------------------------------------
How to use the application:

1. Download all the files in git repository
2. Set up telegram bot via BotFather in telegram. Insert token from BotFather into main.py at TOKEN =
3. Open Terminal
4. Create local git repository file and place all the files in this repository there. ("cd" to file and type "git init" in terminal)
5. Set up Heroku account at https://signup.heroku.com/
6. Create a new Heroku app
7. Download the Heroku Command Line Interface(CLI) at https://devcenter.heroku.com/articles/heroku-cli#download-and-install
9. "pip install pyTelegramBotAPI && pip install flask"
10. "heroku login" => follow pop up, login to your Heroku Account
11. In Heroku, go to settings, find your app web URL https://{your app}.herokuapp.com/. Insert this to main.py at "def webhook()"

Deploying to Heroku:
1. "pip install pipreqs" => "pipreqs ./" => requirements.txt file created
2. In procfile, type "web: python {type name of python doc here}.py"
3. In terminal, type "git add .", "git commit -am "first deploy"", "git push heroku master"

Setting up webhook to Telegram:
1. [Go to Heroku => Settings => heroku git URL]
2. Open a web browser, type https://api.telegram.org/bot{type bot token here}/setWebhook?url={type heroku git URL here}
3. Check webhook creation status at https://api.telegram.org/bot{type bot token here}/getWebhookInfo
4. Got new Heroku folder to link to? To delete webhook, type https://api.telegram.org/{type bot token here}/deleteWebhook?url={type heroku git URL here}
  
Controlling Heroku from Terminal:
1. To check free dyno quota remaining, type "heroku ps"
2. To assign dyno to Telegram bot, type "heroku ps:scale web=1"
3. To remove dyno assigned to Telegram bot, type "heroku ps:scale web=0"
--------------------------------------------  


Drawbacks of this Telegram Bot:
- Lack of security features. Do write to me on how to improve on security features! :)
