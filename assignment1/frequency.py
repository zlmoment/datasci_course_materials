import sys
import json

def hw(tweetfile):
    word_dict = {}
    total = 0
    for line in tweetfile:
        line_dict = json.loads(line.strip())
        if "delete" not in line_dict and line != "":
            text = line_dict["text"].encode('utf-8')
            word_array = text.split()
            for word in word_array:
                total = total + 1
                if word in word_dict:
                    word_dict[word] = word_dict[word] + 1
                else:
                    word_dict[word] = 1
    for k, v in word_dict.iteritems():
        print str(k) + " " + str(float(v/total))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()