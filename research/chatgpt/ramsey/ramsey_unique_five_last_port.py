"""For EVERY old-only feasible missing triple for a candidate unique five-row T, project partial independent seven-sets to old vertices. Test independent transversal for the last port, and whether tight obligations shared across ALL triples already refute T."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits
from collections import Counter

def run():
    cases=json.loads((D/'ramsey_intrinsic_attachment_basis.json').read_text())[::8];lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in cases:
        p=r['parent'];G=decode(lines[p-1]);V=[i for i in range(22) if i!=r['deleted']];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];I=sorted(inds(H));M=[s for s in I if all(s>>i&1 or s&h for i,h in enumerate(H))];T=sorted(t for t in I if t.bit_count() in (4,5,6));m=[sum(1<<i for i,t in enumerate(T) if not s&t) for s in M];u,v,w=[sum(1<<i for i,t in enumerate(T) if t.bit_count()==k) for k in (4,5,6)];N=[sum(1<<j for j in range(i,len(M)) if not b&m[j]&w) for i,b in enumerate(m)];records={};truth=set(r['forced']);F=(1<<len(M))-1;options=[sum(1<<j for j,s in enumerate(M) if s&t) for t in T];
        def legal(req):
            live=F
            for i in bits(req):
                live&=options[i]
                if not live:break
            return live
        for i,P in enumerate(N):
            a=m[i]
            for j in bits(P):
                b=m[j];ab=a&b
                for k in bits(P&N[j]):
                    c=m[k];tr=ab&c;viol=tr&v
                    if viol.bit_count()!=1:continue
                    t=T[viol.bit_length()-1];req=(tr&u)|((ab|((a|b)&c))&v)|((a|b|c)&w);rec=records.setdefault(t,[0,0,req,0,None]);rec[0]+=1;rec[2]&=req;rec[3]|=req;live=legal(req)
                    if live:
                        rec[1]+=1
                        if rec[4] is None:rec[4]=[M[i],M[j],M[k],M[next(bits(live))]]
        for t,(n,g,inter,union,example) in records.items():
            assert bool(g)==(t in truth);shared=legal(inter);out.append(dict(parent=p,t=t,triples=n,extendible=g,shared_rows=inter.bit_count(),shared_candidates=shared.bit_count(),universal_fourths=legal(union).bit_count(),example=example))
    return out
if __name__=='__main__':
    z=run();print(len(z),sum(r['triples'] for r in z),sum(r['extendible'] for r in z));print(Counter('dead shared' if not r['shared_candidates'] else 'dead distributed' if not r['extendible'] else 'all triples' if r['extendible']==r['triples'] else 'mixed' for r in z));print(sum(bool(r['universal_fourths']) for r in z));print(max((r for r in z if not r['extendible']),key=lambda r:r['triples']));(D/'ramsey_unique_five_last_port.json').write_text(json.dumps(z)+'\n')
