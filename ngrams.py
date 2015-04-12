import operator, binascii, sys, getopt, collections

def window_slide(ngrams, window_len):
    idx = 0
    ngram_list = ngrams.items()
    result = list()
    if (window_len == 1):
        return ngrams
    else:
        while (idx < len(ngram_list)):
            result.append(ngram_list[idx])
            idx += window_len
        return result


def ngrams(tokens, n):
    output = collections.OrderedDict()
    for i in range(len(tokens)-n+1):
        gram = ''.join(tokens[i:i+n])
        gram = binascii.hexlify(gram)
        output.setdefault(gram, 0)
        output[gram] += 1
    return output

def top_20(ngrams):
    sorted_ngrams = sorted(ngrams, key=lambda g: (g[1], g[0]), reverse=True)
    return sorted_ngrams[0:20]

def tokenize(filename, n):
    tokens = list()
    with open(filename, "rb") as f:
        byte = f.read(n)
        while byte != "":
            tokens.append(byte)
            byte = f.read(n)

    return tokens

if __name__ == '__main__':
    
    inputfile = ''
    outputfile = ''
    ngram_len = ''
    window_len = ''

    if (len(sys.argv) < 5):
        print 'ngram.py inputfile outputfile ngram_len window_len'
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    ngram_len = int(sys.argv[3])
    window_len = int(sys.argv[4])

    if window_len > ngram_len:
        print 'window_len must be <= ngram_len'
        sys.exit(1)

    tokens = tokenize(inputfile, ngram_len)
    n_grams = ngrams(tokens, ngram_len)
    window_grams = window_slide(n_grams, window_len)
    top_20 = top_20(window_grams)

    f = open(outputfile, "w")
    for i in top_20:
        f.write(str(i))
        f.write("\n")
    f.close()
    