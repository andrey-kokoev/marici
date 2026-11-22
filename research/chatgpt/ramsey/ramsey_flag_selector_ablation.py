"""Separate information selecting the word from availability of incidence witnesses. Hold rows, endpoints and binding fixed; vary all 36 matchings with the same boundary."""
from collections import Counter
from ramsey_folded_entry_handoff import P,T,X,rho,D,json,permutations

def match(i=0,used=frozenset(),prefix=()):
    if i==15:yield dict(enumerate(prefix));return
    for j,t in enumerate(T,15):
        if j not in used and P[i] in t and (i!=0 or j==16) and (i!=7 or j==29):yield from match(i+1,used|{j},prefix+(j,))

def run():
    E={''.join(e) for e in json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text())['arrows']};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        hist=Counter();examples={}
        for m in match():
            n={rho[d]:rho[j] for d,j in m.items()};results=[];paths=[]
            for row,f,g in [('BRNN',m,n),('BNRN',n,m)]:
                inv={j:d for d,j in g.items()};j=f[0];u=inv[j];k=f[u];v=inv[k];paths.append([0,j,u,k,v]);ds=[0,u,u,v];slots=[{e for e in E if any(set(e)=={p[x-1] for x in X[h]} for h in P[d])} for d in ds];tail=p[row.index('R')];head,={'C','D'}-{tail};word,=[(a,b) for a in E for b in E if a[0]==tail and a[1]==b[0] and b[1]==head];results.append(any(word[0] in slots[i] and word[1] in slots[l] for i,l in [(0,3),(3,2)]))
            key=''.join('1' if b else '0' for b in results);hist[key]+=1;examples.setdefault(key,paths)
        assert sum(hist.values())==36;out.append(dict(binding=''.join(p),pass_by_row=hist,examples=examples))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_flag_selector_ablation.json').write_text(json.dumps(out)+'\n')
