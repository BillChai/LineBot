from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#YOUR_CHANNEL_ACCESS_TOKEN
line_bot_api = LineBotApi('vV1Hn9941SFk+l05YXDNqa50r9nNw0psHvb4mAnTDd9hVvs36w+dd4YyUiNEZy22P+n+RpUBdgtH/EucryF3m/u8OyNW4LB5J34x1rmm4BcqW1ArH7NiEVT8U020upayI7Puypy03Gfjb+DwoqrDCQdB04t89/1O/w1cDnyilFU=')

#YOUR_CHANNEL_SECRET
handler = WebhookHandler('2ce97115e6b47f8b21ebc16b4ce9cfb2')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(debug=True)