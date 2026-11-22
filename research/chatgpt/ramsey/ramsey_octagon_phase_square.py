"""Vary only the two octagon phases. Recompute literal mate, shared/open paths and the action of the independently constructed decagon polarity on each phase choice."""
from itertools import product
from ramsey_antipode_extension import run as polarity
from ramsey_row_quotient_constructor import R,move,final,flags
from ramsey_folded_entry_handoff import D,json

def run():
    data=json.loads((D/'ramsey_polefree_component_exchange.json').read_text())['marked_counterexamples'];a,b=[frozenset(map(tuple,r['matching'])) for r in data];cs=data[0]['components'];octs=[frozenset(tuple(sorted((x,w[(i+1)%8]))) for i,x in enumerate(w)) for w in cs if len(w)==8];assert a^b==octs[0]|octs[1];p=polarity()[0]['map'];out=[]
    for bits in product(range(2),repeat=2):
        m=a
        for k,s in zip(bits,octs):
            if k:m=m^s
        assert len(dict(m))==len({j for _,j in m})==15;n=move(m,R);neither=flags-(m|n);paths=[];adj={x:set() for x in range(30)}
        for x,y in neither:adj[x].add(y);adj[y].add(x)
        seen=set()
        for x in adj:
            if len(adj[x])!=1 or x in seen:continue
            w=[x];prev=None
            while adj[w[-1]]-{prev}:prev,y=w[-1],next(iter(adj[w[-1]]-{prev}));w.append(y)
            seen.update(w);paths.append(len(w)-1)
        out.append(dict(flip=bits,shared=len(m&n),active=len(m^n),selected=m in final,polarity_gives_mate=move(m,p)==n,thread_lengths=sorted(paths),owner_1_18=(1,18) in m,owner_2_21=(2,21) in m))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_octagon_phase_square.json').write_text(json.dumps(out)+'\n')
