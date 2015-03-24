import operator as op

hashtags={}
sumtweet={}

for h in tweets:
    lowcase = h.lower()
    word = lowcase.split()
    for k in word:
        if k[0] == '#':
            if k not in sumtweet:
                sumtweet[k] = 1
            else:
                sumtweet[k] = sumtweet[k] + 1

                
hashtags = sorted(sumtweet.items(), key = op.itemgetter(0))

hashtags = sorted(hashtags, key = op.itemgetter(1), reverse = True)
