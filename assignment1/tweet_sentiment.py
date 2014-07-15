import sys
import json

def hw(afinnfile, tweetfile):
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in tweetfile:
        score = 0
        line_dict = json.loads(line.strip())
        if "delete" not in line_dict and line != "":
            text = line_dict["text"]
            word_array = text.split()
            for word in word_array:
                if word in scores:
                    score = score + scores[word]
            print score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()