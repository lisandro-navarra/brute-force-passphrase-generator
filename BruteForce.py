#!/usr/bin/python/

import string
import argparse
import multiprocessing
from itertools import product,permutations


def p_worker(string_list):

    p_done = 0

    for s in permutations(string_list):

        result = "".join(s)

        p_done += 1

    return p_done


def c_worker(prefix,suffix_len,length):

    c_done = 0

    if length <= suffix_len:

        for t in product(CHARSET, repeat=length):

            result = "".join(t)

            c_done += 1

    else:

        for t in product(CHARSET, repeat=suffix_len):

            result = prefix + "".join(t)

            c_done += 1

    return c_done


def combos_done(c_num):

    global c_done

    if isinstance(c_num,list):

        c_done += (sum(n for n in c_num))

    else:

        c_done += c_num

    print c_done, "combinations created"



def perms_done(p_num):

    global p_done

    if isinstance(p_num,list):

        p_done += (sum(n for n in p_num))

    else:

        p_done += p_num

    print p_done, "permutations created"



def brute_enforcer(myPool):

    if PASSPHRASE is not None:

        words = [PASSPHRASE]

        pass_len = len(PASSPHRASE)

        for l in range(1,pass_len):

            x = pass_len-l

            w1,w2 = PASSPHRASE[0:x],PASSPHRASE[-x:]

            if len(w1) > 1:

                words.append(w1)

            if len(w2) > 1:

                words.append(w2)

        myPool.map_async(p_worker,words,callback=perms_done)

    suffix_len = 0

    while len(CHARSET)**suffix_len <= CALC_LIMIT:

        suffix_len += 1

    suffix_len -= 1

    short_string_thresh = min(suffix_len,MAX_LENGTH)+1

    for length in xrange(1, short_string_thresh):

        myPool.apply_async(c_worker,args=("",suffix_len,length),callback=combos_done)

    for length in xrange(short_string_thresh,MAX_LENGTH + 1):

        for t in product(CHARSET, repeat=length-suffix_len):

            prefix = "".join(t)

            myPool.apply_async(c_worker,args=(prefix,suffix_len,length),callback=combos_done)

    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This program should evaluate a passphrase and generate all possible phrases.')

    parser.add_argument('-p','--passphrase', help='Provide test passphrase for permutation calculation',required=False)

    parser.add_argument('-l','--maxlength',help='Provide max length of passphrase to generate', required=True)

    args = parser.parse_args()

    PASSPHRASE=args.passphrase

    MAX_LENGTH=int(args.maxlength)

    CHARSET = string.ascii_letters + string.digits + string.punctuation

    CALC_LIMIT = 1000000

    myPool = multiprocessing.Pool(None)

    p_done,c_done = 0,0

    brute_enforcer(myPool)

    myPool.close()

    myPool.join()