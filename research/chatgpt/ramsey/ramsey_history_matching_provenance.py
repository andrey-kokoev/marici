"""Can the proposed discriminating history actually be observed by a stationary Hall matching successor? Fit prefixes to arbitrary fixed matching pairs and to pairs related by the literal row involution. Also count minimum latent frame changes, preserving traversal phase."""
from ramsey_folded_entry_handoff import P,T,rho,D,json

def enum(i=0,taken=frozenset(),w=()):
    if i==15:yield frozenset(enumerate(w));return
    for j,t in enumerate(T,15):
        if P[i] in t and j not in taken:yield from enum(i+1,taken|{j},w+(j,))

def run():
    ms=list(enum());assert len(ms)==288;h=json.loads((D/'ramsey_return_address_memory.json').read_text())['either']['last_collision'][0];out=[]
    for nxt in (4,7):
        path=h+[nxt];cost=[0]*len(ms);a=set(range(len(ms)));b=set(a);same=a.copy();log=[]
        for k,(x,y) in enumerate(zip(path,path[1:])):
            flag=tuple(sorted((x,y)));ref=tuple(rho[v] for v in flag) if k%2 else flag;accept={i for i,m in enumerate(ms) if ref in m};best=min(cost);cost=[min(c,best+1) if i in accept else 1000 for i,c in enumerate(cost)];same&=accept
            if k%2:b&={i for i,m in enumerate(ms) if flag in m}
            else:a&=accept
            log.append(dict(visit=y,row_related=len(same),arbitrary=len(a)*len(b),min_changes=min(cost)))
        out.append(dict(departure=nxt,checks=log))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_history_matching_provenance.json').write_text(json.dumps(out)+'\n')
