"""Generate five-flag halves from endpoints alone and close them by literal reflection. Decode the moving R named by the missing entry fan apex and by the exit BR edge."""
from ramsey_folded_entry_handoff import X,P,T,D,json
from ramsey_row_quotient_constructor import R

def run():
    adj={x:set() for x in range(30)}
    for j,t in enumerate(T,15):
        for d in t:i=P.index(d);adj[i].add(j);adj[j].add(i)
    paths=[[0]]
    for _ in range(5):paths=[w+[x] for w in paths for x in sorted(adj[w[-1]]-set(w))]
    out=[]
    for w in paths:
        if w[-1]!=29 or set(w)&set(map(R.__getitem__,w))!={0,29}:continue
        j,d=w[1],w[-2];fans=[set(X[a])&set(X[b]) for a,b in T[j-15]];missing,=set(range(1,5))-set.union(*fans);br,=[X[k] for k in P[d] if 1 in X[k]];out.append(dict(path=w,entry_missing=missing,exit_R=sum(br)-1,adjacent_to_exit_partner=missing in br))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_boundary_role_table.json').write_text(json.dumps(out)+'\n')
