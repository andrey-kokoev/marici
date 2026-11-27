"""Enumerate permutations of added cells, with fixed edit order and checkpoint times."""
from ramsey38_three_route_novelty import P as novelty,R as novel_r,sig
from ramsey38_three_matched_holdout import P as first,R as first_r
from ramsey38_sphere_link_holdout import P as sphere,R as sphere_r
from ramsey38_early_interior_holdout import P as early,R as early_r
from ramsey38_three_releases import graph,setup,add,prev,json,attaches,boundary,Counter,permutations

def run():
    out=[];tot=Counter();classes=set()
    for path,result in [(first,first_r),(novelty,novel_r),(sphere,sphere_r),(early,early_r)]:
        chk=json.loads(result.read_text());assert chk['prediction_sha']==prev.sha(path.read_bytes());
        for e,z in zip(json.loads(path.read_text())['cases'],chk['cases'],strict=True):
            g=graph(e['word']);L=sorted(g[e['u']]);dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1)
            for p in e['plans']:
                if p['goal'] not in z['verified']:continue
                goal=p['goal'];st=p['stages'];h=g;rs=[];buried=[];old=[]
                for m in p['moves']:
                    _,r,_=setup(h,e['u']);old.append(dec(r[m[0]]));h=add(h,m);_,r,_=setup(h,e['u']);rs.append({j:dec(x) for j,x in r.items()});buried.append(old.copy())
                initial=set(map(frozenset,st[0]['cells']));middle=set(map(frozenset,st[1]['cells']));end=set(map(frozenset,st[2]['cells']));adds=[frozenset(t) for s in st[1:] for t in s['append']];cut=len(st[1]['append']);assert len(set(adds))==len(adds) and initial|set(adds)==end
                def meets(M,k):
                    bd=boundary(M);return all(any(s<=t for t in M) for s in rs[k].values()) and not set(buried[k])&bd and {j for j,s in rs[k].items() if len(s)<4 and not any(s<=f for f in bd)}==set(goal[:k+1])
                orders={};n=len(adds)
                for perm in permutations(range(n)):
                    M=initial.copy();ok=True;checkpoint=None
                    for i,k in enumerate(perm,1):
                        if not attaches(M,adds[k]):ok=False;break
                        M.add(adds[k]);
                        if i==cut:checkpoint=M.copy()
                    orders[perm]=('geometric_failure' if not ok else 'goal_failure' if not meets(checkpoint,1) or not meets(M,2) else 'same_middle' if checkpoint==middle else 'other_middle')
                seq=tuple(range(n));assert orders[seq]=='same_middle';good={s for s,v in orders.items() if v in ('same_middle','other_middle')};cc=[];unseen=good.copy()
                while unseen:
                    todo=[unseen.pop()];c=[]
                    while todo:
                        s=todo.pop();c.append(s)
                        for i in range(n-1):
                            t=s[:i]+(s[i+1],s[i])+s[i+2:]
                            if t in unseen:unseen.remove(t);todo.append(t)
                    cc.append(sorted(c))
                swaps=[orders[seq[:i]+(seq[i+1],seq[i])+seq[i+2:]] for i in range(n-1)];tot.update(orders.values());classes.add(sig(L,p)[0]);out.append(dict(record=e['record'],goal=goal,moves=p['moves'],attachments=list(map(sorted,adds)),checkpoint=cut,orders=[dict(perm=s,status=v) for s,v in orders.items()],components=cc,swaps_from_certificate=swaps));print(e['record'],goal,cut,Counter(orders.values()),swaps)
    print('total',tot,'routes',len(out),'classes',len(classes));prev.save(prev.out/'ramsey38_attachment_commutation.json',dict(scope='Permute only the post-initial attachments; preserve edit order, cell counts at checkpoints, exact releases and buried triangles. Compare fixed vs variable middle mesh. No permutation of the initial shelling.',counts=dict(tot),route_classes=len(classes),cases=out))
if __name__=='__main__':run()
