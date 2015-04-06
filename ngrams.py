import operator, binascii, sys, getopt

def ngrams(tokens, n):
    output = {}
    for i in range(len(tokens)-n+1):
        gram = ''.join(tokens[i:i+n])
        gram = binascii.hexlify(gram)
        output.setdefault(gram, 0)
        output[gram] += 1
    return output

def top_20(ngrams):
    sorted_ngrams = sorted(ngrams.items(), key=lambda g: (g[1], g[0]), reverse=True)
    return sorted_ngrams[0:20]

def tokenize(filename, window):
    tokens = list()
    with open(filename, "rb") as f:
        byte = f.read(window)
        while byte != "":
            tokens.append(byte)
            byte = f.read(window)

    return tokens

if __name__ == '__main__':
    
    inputfile = ''
    outputfile = ''
    ngram_len = ''
    window_len = ''

    if (len(sys.argv) < 5):
        print 'ngram.py inputfile outputfile ngram_len slide_len'
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    ngram_len = int(sys.argv[3])
    window_len = int(sys.argv[4])

    tokens = tokenize(inputfile, window_len)
    n_grams = ngrams(tokens, ngram_len)
    top_20 = top_20(n_grams)

    f = open(outputfile, "w")
    for i in top_20:
        f.write(str(i))
        f.write("\n")
    f.close()
    