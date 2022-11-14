from asyncio.log import logger
import tweepy
import yaml
import schedule

class TwitterBot:
    def __init__(self) -> None:
        """
        Constructor of the bot
        """
        self._secrets = self._getSecrets()
        self._api = self._authenticate()

    def _getSecrets(self):
        with open(r'twitterKeys.yaml') as file:
            _secrets = yaml.load(file, Loader=yaml.FullLoader)
        return _secrets

    def _authenticate(self):
        self._getSecrets()

        auth = tweepy.OAuthHandler(self._secrets.get(
            'CONSUMER_KEY'), self._secrets.get('CONSUMER_SECRET'))
        auth.set_access_token(self._secrets.get(
            'ACCESS_TOKEN'), self._secrets.get('ACCESS_TOKEN_SECRET'))
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            logger.info("Successful Authentication")
        except Exception as e:
            raise Exception("Authentication Failed:", e)
        return api

    def getMajorHeadlines(self):
        result = self._api.search_tweets(
            q='bbc news world', count=2, lang='en', result_type='recent')
        resultArray = []
        for i in result:
            resultArray.append(i.text)
        status = '\n'.join(resultArray)
        return status

    def updateStatus(self):
        result = self.getMajorHeadlines()[:270]
        flag = False
        try:
            self._api.update_status(status=result)
            logger.info("Successful Updation of the Tweet")
            flag = True
        except Exception as e:
            raise Exception('Could NOT Update the status:', e)
        return flag

def main():
    bot1 = TwitterBot()
    bot1.updateStatus()

if __name__ == "__main__":
    main()

"""schedule.every(1440).seconds.do(main)
while True:
    schedule.run_pending()"""