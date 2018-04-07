from textblob import TextBlob
from myapp.util.FetchTweets import FetchData
from myapp.models import Tweet
import re


class Analyzer():
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyzeData(self, tag):

        fetcher = FetchData()
        public_tweets = fetcher.getTwitterData(tag)

        final_list = []
        pos = 0
        neg = 0
        net = 0
        pie_data = []

        if len(public_tweets) > 0:
            for tweet in public_tweets:
                tweet_dict = {}
                text = tweet.full_text
                analysis = TextBlob(tweet.full_text)

                pol = float("{0:.2f}".format(analysis.sentiment.polarity))

                if pol < 0:
                    neg += 1
                elif pol > 0:
                    pos += 1
                else:
                    net += 1

                tweet_dict['tweet'] = tweet.full_text
                tweet_dict['user'] = tweet.user.screen_name
                tweet_dict['id'] = tweet.id
                tweet_dict['polarity'] = pol
                tweet_dict['desc'] = tweet.user.description
                tweet_dict['proimg'] = tweet.user.profile_image_url
                tweet_dict['created_at'] = tweet.created_at

                if Tweet.objects.filter(tw_id = tweet.id).exists() == False:
                    t = Tweet(tw_text=tweet.full_text,tw_user=tweet.user.name,tw_cat=pol,tw_img_src=tweet.user.profile_image_url,tw_id=tweet.id,tw_desc=tweet.user.description,created_at= tweet.created_at)
                    t.save()
                

                final_list.append(tweet_dict)

        total = pos + neg + net
        if total == 0:
            net = 1
            total = 1

        pos = float("{0:.2f}".format((pos / total) * 100))
        neg = float("{0:.2f}".format((neg / total) * 100))
        net = float("{0:.2f}".format((net / total) * 100))

        pie_data.append(net)
        pie_data.append(pos)
        pie_data.append(neg)


        return {'tweet_list': final_list, 'pie_list': pie_data, 'count': total}
