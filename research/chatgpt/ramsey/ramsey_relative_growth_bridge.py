"""Append a star of pair readings to the saved relative record; remove its bridge."""
import json
from collections import defaultdict
from itertools import pairwise
from pathlib import Path
from ramsey_common_witness_chain_20 import chain
from ramsey_37_pair_rotation_rule import build


def decode(links, seeds):
    graph = defaultdict(list)
    for a,b,d in links:
        assert len(set(a)&set(b)) == 1
        graph[a].append((b,d)); graph[b].append((a,d))
    known = dict(seeds); todo = list(known)
    while todo:
        a = todo.pop()
        for b,d in graph[a]:
            v = known[a]^d
            if b not in known:
                known[b] = v; todo.append(b)
            else: assert known[b] == v
    return known


def main():
    data=json.loads(Path(__file__).with_name('ramsey_common_witness_chain_20.json').read_text()); labels=data['address_order']; n=len(labels)
    old=[tuple(sorted((labels[i],labels[j]))) for i,j in chain(n)]
    links=[(a,b,int(d)) for (a,b),d in zip(pairwise(old),data['different_from_next'],strict=True)]
    star=[(i,n) for i in labels]; g=build(); truth={p:(g[p[0]]>>p[1])&1 for p in old+star}
    def record(a,b):return a,b,truth[a]^truth[b]
    separate=links+[record(a,b) for a,b in pairwise(star)]
    bridge=record((0,1),(0,n)); joined=separate+[bridge]
    for p in old+star:assert decode(joined,{p:truth[p]})==truth
    seed={(0,1):truth[0,1]}; assert set(decode(separate,seed))==set(old)
    for bit in [0,1]:
        result=decode(separate,{**seed,star[0]:bit});flip=bit^truth[star[0]]
        assert result=={**{p:truth[p] for p in old},**{p:truth[p]^flip for p in star}}
    print('old comparisons',len(links),'new internal',len(star)-1,'bridge',bridge,'anchors verified',len(truth),'without bridge: 2 completions for one old anchor')

if __name__=='__main__':main()
