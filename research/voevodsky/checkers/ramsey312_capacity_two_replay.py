"""Replay one capacity-two certificate against the 384 seven-cliques from the sample and its one-swap ring."""
from ramsey312_google_two_step import *
from collections import Counter
from itertools import combinations

def main():
 T=sum(1<<i for i in [1,9,12,31,33,45,49,50,51]);assert all(not adj[i]&T for i in bits(T));r=json.loads((D/'ramsey312_sample6_triples.json').read_text());uniform=F;hist=Counter();cores=set()
 for z in r:
    assert not z['d']&T;s=[x for x in z['s'] if x&T==0];u=0
    for x,y,w in combinations(s,3):u|=x&y&w
    uniform&=u;cores.add(z['d']);hist[sum(x>>14&1 for x in s)]+=1
 assert min(hist)>=3;print('cores',len(cores),'cliques',len(r),'anchors',list(bits(uniform)),'occupancy',hist)
if __name__=='__main__':main()
