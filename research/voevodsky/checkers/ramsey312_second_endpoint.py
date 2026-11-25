"""For matched 7-cycle cases characterize the full second-endpoint deficit, recording shared-red and missed-ten witnesses for every nearest failed exterior pair."""
from ramsey312_google_two_step import *
from itertools import combinations
from collections import Counter

def main():
 rows={int(z[0]):list(map(int,z[1:])) for l in open(sys.argv[1]) if (z:=l.split())};sing=json.loads((D/'ramsey312_single20_link_summary.json').read_text())['bad'];T=list(sets(F,10));out=[]
 for v in (13,30,34):
    d=sum(1<<i for i in (37,39,41,46,v));h=F^d;c=adj[37]&adj[39]&adj[41]&h;w=next(z['kernel'] for z in sing if z['d']==d);
    if v==13:w=next(z['cert'][0]['cycle'] for z in json.loads((D/'ramsey312_conditioned_packing.json').read_text()) if set(z['d'])=={37,39,41,46,v} and z['cert'])
    assert len(w)==7;ts=[t for t in T if not t&d];s=rows[d];m={x:sum(1<<j for j,t in enumerate(ts) if not t&x) for x in s};ext=[x for x in s if x&c!=c];ok=lambda x,y:not x&y or not m[x]&m[y];blocked=lambda x:[y for y in w if not ok(x,y)];P=[x for x in ext if not blocked(x)];print(v,'outside',len(ext),'eligible',len(P),'endpoint sizes',[x.bit_count() for x in P], 'pair counts',Counter(bool(ok(x,y)) for x,y in combinations(P,2)));print('cycle degree',sorted(sum(bool(ok(x,y)) for y in w if x!=y) for x in w));
    allpairs=[];near=[]
    for x,y in combinations(P,2):
        b=m[x]&m[y];allpairs.append(dict(x=x,y=y,red_shared=x&y,miss_count=b.bit_count(),ten=ts[(b&-b).bit_length()-1] if b else None))
    for x in P:
        options=[y for y in ext if y!=x and ok(x,y)];k=min((len(blocked(y)) for y in options),default=None);best=[y for y in options if len(blocked(y))==k];print('e',x,'best',k,'n',len(best));near.append(dict(x=x,best=k,candidates=[dict(y=y,blocks=[dict(s=z,shared=y&z,miss_count=(a:=m[y]&m[z]).bit_count(),ten=ts[(a&-a).bit_length()-1]) for z in blocked(y)]) for y in best]))
    repairs=[]
    for n in near:
        for choice in n['candidates']:
            y=choice['y'];bz=blocked(y)
            if not bz:continue
            sets_by_edge=[[ts[j] for j in bits(m[y]&m[z])] for z in bz];red=[list(bits(y&z)) for z in bz];blue=[sorted(set.intersection(*(set(bits(t)) for t in tt))) for tt in sets_by_edge];fix=sorted(set.intersection(*(set(b)|(set(r) if len(r)==1 else set()) for b,r in zip(blue,red))));entry=dict(y=y,bz=bz,red=red,blue=blue,fix=fix,tens=sets_by_edge)
            if entry not in repairs:repairs.append(entry);print('repair',v,red,blue,fix)
    out.append(dict(v=v,repairs=repairs,cycle=w,ext_count=len(ext),eligible=P,pairs=allpairs,near=near))
 (D/'ramsey312_second_endpoint.json').write_text(json.dumps(out))
if __name__=='__main__':main()
