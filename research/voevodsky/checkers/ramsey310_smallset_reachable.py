"""Radius-limited (or exhausted) residual graph search, keeping the six designated supports fixed."""
from ramsey310_smallset_holdout import D,prev,eligible,cut,joint,key,json,Counter
import sys

def run(radius):
    old=json.loads((D/'ramsey310_matching_degree3_types.json').read_text());one=json.loads((D/'ramsey310_smallset_holdout.json').read_text());exclude={bytes.fromhex(c['key']) for c in one['cases']};exclude.update(key(a) for a in old);sources=[]
    for r in json.loads((D/'ramsey310_s3_local_transfer_r10.json').read_text())['uncut']:
        A=old[0].copy()
        for i,j,x,y in r['path']:A[i]^=1<<j;A[j]^=1<<i;A[x]|=1<<y;A[y]|=1<<x
        sources.append(A);exclude.add(key(A))
    reported=set();alltypes=set();out=[];cohorts=[]
    for i,A in enumerate(sources):
        for j,r in enumerate(json.loads((D/f'ramsey310_s3_all_ports_{i}_replay.json').read_text())):
            E=prev.E=tuple(r['E']);q={tuple(A):()};seen=set(q);sizes=[]
            for depth in range(1,radius+1):
                nxt={}
                for parent,path in q.items():
                    for Z,edit in prev.neighbors(list(parent)):
                        if Z in seen:continue
                        seen.add(Z);nxt[Z]=path+(edit,)
                        if depth<2 or (Z,E) in reported:continue
                        z=key(Z)
                        if z in exclude:continue
                        reported.add((Z,E));alltypes.add(z);x=eligible(Z,E)
                        if x:
                            d,C=x;t=cut(d,C);out.append(dict(source=[i,j],path=nxt[Z],type=z.hex(),rows=len(C),cut=t,exact=joint(Z,E)))
                sizes.append(len(nxt));q=nxt
                if not q:break
            cohorts.append(dict(source=[i,j],sizes=sizes,exhausted=not q))
    res=dict(radius=radius,cohorts=cohorts,screened=len(reported),types=len(alltypes),cases=out);(D/f'ramsey310_smallset_radius{radius}.json').write_text(json.dumps(res));print('screened',len(reported),'types',len(alltypes),'passed',len(out),'cut',sum(x['cut'] is not None for x in out),'exhausted',sum(x['exhausted'] for x in cohorts))
if __name__=='__main__':run(int(sys.argv[1]))
