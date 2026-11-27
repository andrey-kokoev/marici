"""Core-only test of a three-support obstruction. No squares, endpoint or table labels."""
from itertools import combinations
from collections import defaultdict
import json,sys,hashlib
from ramsey_retention_slice import CAT,D,decode,check
O=D.parent;P=O/'ramsey_joint_constraint_transfer_protocol.json'
rule=dict(prediction='In each layer, some core has two panels sharing three supports, with the two alternatives of equal size. Every pair of supports meets the largest-clique demand in both panels. One panel is legal; three supports in the other jointly miss a blue (k-2)-clique.',generation='Use only the supplied predecessor. Candidates are distinct inclusion-maximal blue cliques as red supports. No square, endpoint, or target labeling. Test catalogue records in file order until first matched pair; do not infer frequency. Exhaust all records for a negative.',readout='k=6 then 7. With four ports the union of every pair must meet every blue (k-1)-clique, every triple every blue (k-2)-clique, and all four every blue (k-3)-clique. Name a forbidden triple of supports and its missed clique. Replay both graphs directly.')
def bits(s):return [i for i in range(s.bit_length()) if s>>i&1]
def search(a,k):
    n=len(a);I=[0];F=(1<<n)-1
    for i,v in enumerate(a):I.extend(s|1<<i for s in list(I) if not s&v)
    S=sorted(s for s in I if all(s&(v|1<<i) for i,v in enumerate(a)));Q=[[q for q in I if q.bit_count()==k-z] for z in [1,2,3]];M=[[sum(1<<i for i,q in enumerate(qs) if not s&q) for s in S] for qs in Q];A,B,C=M;neighbors=[{j for j in range(len(S)) if i!=j and not A[i]&A[j]} for i in range(len(S))]
    for i in range(len(S)):
        for j in sorted(t for t in neighbors[i] if t>i):
            ij=neighbors[i]&neighbors[j]
            for h in sorted(t for t in ij if t>j and not B[i]&B[j]&B[t]):
                groups=defaultdict(dict);base=(i,j,h)
                for t in sorted(ij&neighbors[h]):
                    w=next(((p,q,(B[p]&B[q]&B[t])) for p,q in combinations(base,2) if B[p]&B[q]&B[t]),None)
                    if not w and C[i]&C[j]&C[h]&C[t]:continue
                    g=groups[S[t].bit_count()];g.setdefault('bad' if w else 'ok',(t,w))
                    if len(g)!=2:continue
                    good=g['ok'][0];bad,(p,q,miss)=g['bad'];cl=Q[1][(miss&-miss).bit_length()-1];out=dict(shared=[bits(S[v]) for v in base],legal=bits(S[good]),illegal=bits(S[bad]),missed_clique=bits(cl),missing_shared=[base.index(p),base.index(q)])
                    for last,correct in [(good,True),(bad,False)]:
                        G=a.copy()+[0]*5
                        for r,v in enumerate((*base,last),n):
                            G[r]=S[v]|1<<(n+4);G[-1]|=1<<r
                            for x in bits(S[v]):G[x]|=1<<r
                        assert check(G,(1<<len(G))-1,3,k+1)==correct
                    return out

def run(k):
    assert json.loads(P.read_text())==rule;f=CAT/f'r3{k}_{17 if k==6 else 22}.g6';rows=f.read_text().splitlines();w=None
    for idx,line in enumerate(rows,1):
        w=search(decode(line),k)
        if w:break
    out=dict(protocol_sha=hashlib.sha256(P.read_bytes()).hexdigest(),k=k,records_tested=idx,records_available=len(rows),core_graph6=line if w else None,witness=w);print(out);dest=O/f'ramsey_joint_constraint_transfer_k{k}.json';text=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':
    if sys.argv[1]=='freeze':
        text=json.dumps(rule,indent=2)+'\n';assert not P.exists() or P.read_text()==text;P.write_text(text)
    else:run(int(sys.argv[1]))
