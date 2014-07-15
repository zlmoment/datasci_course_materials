import sys
import json
import operator

def hw(tweetfile):
    hashtags_count = {}
    for line in tweetfile:
        score = 0
        line_dict = json.loads(line.strip())
        if "delete" not in line_dict and line != "":
            hashtags = line_dict["entities"]["hashtags"]
            if len(hashtags) != 0:
                for hashtag in hashtags:
                    hashtag = hashtag["text"].encode('utf-8')
                    if hashtag in hashtags_count:
                        hashtags_count[hashtag] = hashtags_count[hashtag] + 1
                    else:
                        hashtags_count[hashtag] = 1
    sorted_hashtag = sorted(hashtags_count.iteritems(), key=operator.itemgetter(1))
    if len(sorted_hashtag) > 10:
        loop = 11
    else:
        loop = len(sorted_hashtag) + 1

    for i in range(1,loop):
        print str(sorted_hashtag[len(sorted_hashtag)-i][0])+" "+str(sorted_hashtag[len(sorted_hashtag)-i][1])



def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()