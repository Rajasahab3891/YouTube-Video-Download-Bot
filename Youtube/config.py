import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7308230673:AAHmYqfO1Y0CnTOwTg1X-HHRUiBFM11qrTI")
    API_ID = int(os.environ.get("API_ID", 28196711))
    API_HASH = os.environ.get("API_HASH", "a8a23bffb12aae7a4c72fa2b4cd538a1")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002044871468")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = '182.74.243.47:3128'
