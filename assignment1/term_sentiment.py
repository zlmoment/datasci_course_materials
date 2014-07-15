import sys
import json

def hw(afinnfile, tweetfile):
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    output_scores = {}

    for line in tweetfile:
        line_dict = json.loads(line.strip())
        if "delete" not in line_dict and line != "":
            text = line_dict["text"].encode('utf-8')
            word_array = text.split()
            tweet_score = getSentenceScore(word_array, scores)
            for word in word_array:
                if word not in output_scores:
                    output_scores[word] = tweet_score
                else:
                    output_scores[word] = output_scores[word] + tweet_score

    for k, v in output_scores.iteritems():
        print str(k)+" "+str(v)

def getSentenceScore(word_array, scores):
    score = 0
    for word in word_array:
        if word in scores:
            score = score + scores[word]
    return score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()