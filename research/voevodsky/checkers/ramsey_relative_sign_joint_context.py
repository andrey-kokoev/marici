from ramsey_repair_next_seam import graph,grow,sevens,check,D,sha256,json,combinations
from itertools import product,permutations
from collections import Counter

def build(sites,ss,col):
    n=9+len(sites);tokens=[]
    for k in range(10):
        if k in sites:tokens.append(('new',sites[k]))
        if k<9:tokens.append(('old',k))
    rows=[[j for j,(tag,v) in enumerate(tokens) if (p+1 in v if tag=='new' else v in s)] for p,s in enumerate(ss)];return graph(n,rows,col)

def verdict(g):return check(g,(1<<len(g))-1,3,7)
def run():
    Z=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());ss=grow(tuple(tuple(x-1 for x in s) for s in Z['supports']),Z['gap']);pairs=list(combinations(range(5),2));out=[]
    for edit in Z['wins']:
        col=sum(1<<pairs.index((i-1,j-1)) for i,j in edit);cnt=Counter();examples={};allwins=[]
        singles={(k,p,q):verdict(build({k:(p,q)},ss,col)) for k,p,q in product(range(10),(2,3),(4,5))}
        for k,l in permutations(range(10),2):
            for p,q in product((2,3),repeat=2):
                sites={k:(p,4),l:(q,5)};both=singles[k,p,4] and singles[l,q,5];g=build(sites,ss,col);ok=verdict(g);cnt[f'separate_{int(both)}_joint_{int(ok)}']+=1
                if ok:allwins.append([k,l,p,q])
                if both and not ok and 'lost' not in examples:
                    tri=next((s for s in combinations(range(len(g)),3) if all(g[i]>>j&1 for i,j in combinations(s,2))),None);w=tri or next(sevens(g));examples['lost']=dict(gaps=[k,l],twins=[p,q],color='red' if tri else 'blue',final_sites=[i+1 for i in w if i<11],ports=[i-10 for i in w if i>=11])
        out.append(dict(edits=edit,counts=dict(cnt),legal_single_sites=[m for m,v in singles.items() if v],wins=allwins,examples=examples));print(edit,cnt,allwins[:3],examples)
    dest=D.parent/'ramsey_relative_sign_joint_context_detailed.json';text=json.dumps(dict(protocol_sha=sha256((D.parent/'ramsey_relative_sign_joint_context_protocol.md').read_bytes()).hexdigest(),cases=out),indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
