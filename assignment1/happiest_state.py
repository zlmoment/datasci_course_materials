import sys
import json
import operator

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def hw(afinnfile, tweetfile):
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    states_score = {}

    for line in tweetfile:
        line_dict = json.loads(line.strip())
        if "delete" not in line_dict and line != "":
            if line_dict["user"]["location"] != "":
                text = line_dict["text"].encode('utf-8')
                word_array = text.split()
                tweet_score = getSentenceScore(word_array, scores)
                state = line_dict["user"]["location"]
                if state in states.values():
                    for k,v in states.iteritems():
                        if v == state:
                            state = k
                    if state not in states_score:
                        states_score[state] = tweet_score
                    else:
                        states_score[state] = states_score[state] + tweet_score
                elif state in states:
                    if state not in states_score:
                        states_score[state] = tweet_score
                    else:
                        states_score[state] = states_score[state] + tweet_score
                else:
                    pass
    sorted_state = sorted(states_score.iteritems(), key=operator.itemgetter(1))
    print sorted_state[len(sorted_state)-1][0]

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