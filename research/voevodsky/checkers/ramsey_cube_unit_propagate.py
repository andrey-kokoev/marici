"""Replay all 90 first-pass survivors. Repeatedly select only unavoidable links. Keep a checkable trace and report any noncontradictory fixed point."""
from ramsey_cube_unlock_free_row import search,induced,G,D,json,Counter

def bits(m):return [i for i in range(m.bit_length()) if m>>i&1]

def probe(cuts,s,base,es,small):
    g=base[:];ds=set(small);steps=[];kind=None
    while True:
        allowed=sum(1<<k for k,(i,j) in enumerate(es) if max(g[i].bit_count(),g[j].bit_count())<7 and not g[i]&(g[j]|1<<j));left={x&allowed for x in ds}
        if 0 in left:
            m=next(x for x in sorted(ds) if not x&allowed);example=[es[i] for i in bits(m)];kind='empty_demand';break
        if not ds:kind='solution';example=[];break
        units=sorted({m.bit_length()-1 for m in left if m.bit_count()==1});
        if not units:kind='needs_branch';example=[es[i] for i in bits(min(left,key=lambda m:(m.bit_count(),m)))];break
        chosen=sum(1<<k for k in units);steps.append([es[k] for k in units]);ds={x for x in ds if not x&chosen}
        for k in units:
            i,j=es[k];g[i]|=1<<j;g[j]|=1<<i
        high=[i for i,v in enumerate(g) if v.bit_count()>7];tri=sorted({tuple(sorted((i,j,n))) for k in units for i,j in [es[k]] for n in bits(g[i]&g[j])})
        if high or tri:kind='degree_and_triangle' if high and tri else 'degree' if high else 'triangle';example=dict(overfull=high,triangles=tri);break
    return dict(cuts=cuts,row=bits(s),steps=steps,status=kind,example=example)

def audit():
    prior=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text());a=induced(G,prior['core_labels']);cases=[]
    def collect(*xs):cases.append(probe(*xs))
    for r in prior['runs']:
        n=r['counts'].get('pass_forced',0)
        if not n:continue
        before=len(cases);st,w=search(a,tuple(map(tuple,r['cuts'])),collect);assert st==r['counts'] and w is None and len(cases)-before==n
    assert len(cases)==90;ct=Counter((c['status'],len(c['steps'])) for c in cases);print(ct,'first',cases[0]);out=dict(outcomes=[dict(status=s,forced_batches=b,count=n) for (s,b),n in sorted(ct.items())],cases=cases);(D.parent/'ramsey_cube_unit_propagate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
