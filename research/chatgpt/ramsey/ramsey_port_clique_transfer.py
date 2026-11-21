"""Cross-k constructor: enumerate maximal independent supports and compatible multisets of ports.
Calibration nonneighbor cores only: port incidences are not passed to the constructor."""
from pathlib import Path
from itertools import combinations
import csv,json,sys
from ramsey_hall_center_conjecture import independent,decode
from ramsey_39_cyclic_constructor import graph
D=Path(__file__).parent

def induce(A,V):return [sum(1<<j for j,w in enumerate(V) if A[v]>>w&1) for v in V]
def solve(H,k,d):
    n=len(H);F=(1<<n)-1;inds=[0]
    for v,row in enumerate(H):inds += [s|1<<v for s in inds if not s&row]
    assert max(x.bit_count() for x in inds)<=k-2
    maximal=[s for s in inds if all(s>>v&1 or s&row for v,row in enumerate(H))];top=[s for s in inds if s.bit_count()==k-2];miss=[sum(1<<i for i,t in enumerate(top) if not s&t) for s in maximal];adj=[sum(1<<j for j,b in enumerate(miss) if not a&b) for a in miss];visits=0
    def dfs(ids,opts,B):
        nonlocal visits
        if len(ids)==d:return ids,B
        while opts:
            bit=opts&-opts;i=bit.bit_length()-1;opts-=bit;s=maximal[i];visits+=1
            # Check only new independent k-sets: must contain the incoming port.
            if independent(B,((1<<len(B))-1)^s,k-1):continue
            C=[row|(1<<len(B) if s>>v&1 else 0) for v,row in enumerate(B)]+[s]
            ans=dfs(ids+[i],(opts|bit)&adj[i],C)
            if ans:return ans
        return None
    ans=dfs([], (1<<len(maximal))-1,H);res={'k':k,'core_order':n,'ports':d,'maximal_supports':len(maximal),'top_sets':len(top),'partial_trials':visits}
    if ans:
        ids,B=ans;B=[row|(1<<len(B) if v>=n else 0) for v,row in enumerate(B)]+[((1<<d)-1)<<n];assert not independent(B,(1<<len(B))-1,k) and all(not B[i]&B[j] for i,j in combinations(range(len(B)),2) if B[i]>>j&1);res.update(supports=[maximal[i] for i in ids],graph=B)
    return res

def inputs(k):
    if k in (7,8):
        lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();A=decode(lines[190 if k==7 else 17]);return (induce(A,[v for v in range(1,22) if not A[0]>>v&1]),6) if k==7 else (A,4)
    if k==9:
        A=graph((1,7,11,16));return induce(A,[v for v in range(1,35) if not A[0]>>v&1]),8
    A=[sum(int(x)<<i for i,x in enumerate(row)) for row in csv.reader((D/'ramsey_3_10_witness_39.csv').read_text().splitlines()) if row];return induce(A,[v for v in range(39) if v not in (35,29,36,37,38)]),4
if __name__=='__main__':
    for k in map(int,sys.argv[1:]):
        res=solve(inputs(k)[0],k,inputs(k)[1]);print({x:y for x,y in res.items() if x not in ('graph','supports')},'success',bool(res.get('graph')),flush=True);(D/f'ramsey_port_clique_k{k}.json').write_text(json.dumps(res)+'\n')
