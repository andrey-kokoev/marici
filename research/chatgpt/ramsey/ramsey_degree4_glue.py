"""Degree-four R(3,8) gluing from maximal independent attachments; no target graph input."""
from pathlib import Path
from itertools import combinations_with_replacement,combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode,independent
D=Path(__file__).parent

def glue(A):
    full=(1<<22)-1;I=[0]
    for v,r in enumerate(A):I += [s|1<<v for s in I if not s&r]
    M=[s for s in I if all(s>>i&1 or A[i]&s for i in range(22))];assert max(s.bit_count() for s in I)==6
    miss=[]
    for s in M:
        miss.append({k:sum(1<<j for j,t in enumerate([x for x in I if x.bit_count()==k]) if not s&t) for k in (4,5,6)})
    nbr=[set() for _ in M];ct=Counter()
    for i,j in combinations_with_replacement(range(len(M)),2):
        if not miss[i][6]&miss[j][6]:nbr[i].add(j);nbr[j].add(i);ct['pairs']+=1
    for i in range(len(M)):
        for j in nbr[i]:
            if j<i:continue
            for k in nbr[i]&nbr[j]:
                if k<j or miss[i][5]&miss[j][5]&miss[k][5]:continue
                ct['triples']+=1
                for l in nbr[i]&nbr[j]&nbr[k]:
                    if l<k:continue
                    ids=[i,j,k,l]
                    if any(miss[a][5]&miss[b][5]&miss[c][5] for a,b,c in combinations(ids,3)):continue
                    ct['pair_triple_quads']+=1
                    if miss[i][4]&miss[j][4]&miss[k][4]&miss[l][4]:continue
                    B=A[:]+[0]*5
                    for u,t in enumerate(ids,22):
                        B[u]=M[t]|1<<26;B[26]|=1<<u
                        for v in range(22):
                            if M[t]>>v&1:B[v]|=1<<u
                    assert all(not B[v]&B[w] for v,w in combinations(range(27),2) if B[v]>>w&1) and not independent(B,(1<<27)-1,8)
                    return [M[t] for t in ids],ct
    return None,ct
if __name__=='__main__':
    lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();stats=Counter();wins=[]
    for idx,line in enumerate(lines,1):
        witness,ct=glue(decode(line));stats.update(ct)
        if witness:wins.append((idx,witness))
    print('cores',len(lines),'successful',len(wins),'first',wins[:1],'search counters',stats)
    (D/'ramsey_degree4_glue.json').write_text(json.dumps({'cores':len(lines),'successful':wins,'search_counters':dict(stats)},indent=2)+'\n')
