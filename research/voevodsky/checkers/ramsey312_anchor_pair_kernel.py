"""Predict the exceptional pair from the chromatic obstruction in its common link; minimize by vertex deletion. No pivot eligibility computation."""
from ramsey312_exchange_atlas import *
from itertools import combinations

def main():
 rows={tuple(map(int,(r:=l.split())[:5])):r for l in (D/'ramsey312_five_neg_domains.txt').open()};out=[]
 for summary in json.loads((D/'ramsey312_exchange_atlas_summary.json').read_text()):
    d=summary['d'];s=list(map(int,rows[tuple(d)][7:]));h=F^sum(1<<v for v in d);a=[s.index(adj[v]&h) for v in d];ten=list(sets(h,10));miss=[sum(1<<j for j,t in enumerate(ten) if not x&t) for x in s];N=[{j for j,y in enumerate(s) if not x&y or not miss[i]&miss[j]} for i,x in enumerate(s)];B=[{k for k in range(5) if a[k] not in n} for n in N];rec=[]
    for i,j in combinations(range(5),2):
        V=N[a[i]]&N[a[j]];bad=color(V,N,B) is None;row=dict(pair=[d[i],d[j]],size=len(V),bad=bad)
        if bad:
            cands=V.copy();pal=[set(range(3))]*len(s);assert color(cands,N,pal) is None # anchors in the link transform any ordinary 3-coloring into an allowed charge assignment
            for z in sorted(V,key=lambda z:(len(N[z]&V),s[z])):
                if color(cands-{z},N,pal) is None:cands.remove(z)
            row.update(obstruction=[s[z] for z in sorted(cands)],edges=sum(len(N[z]&cands) for z in cands)//2);assert all(color(cands-{z},N,pal) is not None for z in cands)
        rec.append(row)
    import gzip
    atlas=next(r for r in json.load(gzip.open(D/'ramsey312_exchange_atlas.json.gz')) if r['d']==d);R=set(map(int,atlas['leaf']));lift=[]
    for i in sorted(R):
        for j in sorted(N[i]&R):
            if j>=i:continue
            V=N[i]&N[j];pal=[set(range(3))]*len(s);badlink=color(V,N,pal) is None;w=V.copy()
            if badlink:
                for z in sorted(V,key=lambda z:(len(N[z]&V),s[z])):
                    if color(w-{z},N,pal) is None:w.remove(z)
            lift.append(dict(pair=[s[i],s[j]],bad=badlink,kernel=sorted(s[z] for z in w) if badlink else []))
    print('residual common links:',[(r['bad'],len(r['kernel'])) for r in lift]);bad=[(r['pair'],len(r['obstruction']),r['edges']) for r in rec if r['bad']];print(d,bad,'expected',summary['leaf_pairs'],flush=True);out.append(dict(d=d,tests=rec,lift=lift))
 (D/'ramsey312_anchor_pair_kernels.json').write_text(json.dumps(out))
if __name__=='__main__':main()
