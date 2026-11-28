"""Audit the held-out marginal denominator and the stronger 'two sixes are necessary' reading of the source result. Independently enumerate the small losing family sets with Python bitsets."""
from ramsey_joint_six_demands import D,CAT,decode,gzip,islice,json,combinations,sets
from itertools import product

def read(idx):
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:return decode(next(islice(f,idx,None)).strip())

def run():
    T=D.parent;t=json.loads((T/'ramsey_six_hit_timing_resume.json').read_text());assert t['complete'];a=read(99148);wins=set()
    for z,g,_ in t['outputs']:
        vs=[v for v in range(27) if v!=z];add=[];rm=[]
        for i,j in combinations(range(26),2):
            u,v=vs[i],vs[j];e=a[u]>>v&1;f=g[i]>>j&1
            if e!=f:(rm if e else add).append((u,v))
        assert len(add)==2;b=a[:]
        for i,j in add:b[i]|=1<<j;b[j]|=1<<i
        tri=[sorted(set(combinations((i,j,k),2))&set(rm)) for i,j,k in combinations(vs,3) if (b[i]>>j)&(b[i]>>k)&(b[j]>>k)&1];covers={frozenset(p) for p in product(*tri)};wins.update((z,tuple(add),tuple(sorted(p))) for p in covers if not any(q<p for q in covers))
    screen=json.loads((T/'ramsey_six_hit_screen.json').read_text());known=json.loads((T/'ramsey_joint_six_demands.json').read_text());a=read(448077);source=sets(a,7);bad=[];shared=None
    for p in screen['baseline_prefixes']:
        if p['failed_probe']:continue
        z=p['z'];vs=[v for v in range(27) if v!=z];adds=p['additions'];orig=[[vs[i],vs[j]] for i,j in adds];prev=next(c for c in known if c['z']==z and c['additions']==orig)
        if prev['all_pairs_witnessed']:continue
        g=p['core'];six=sets(g,6);ss=set(six);q7=sets(g,7);qs=[q for s in source if s>>z&1 and (q:=sum((s>>v&1)<<j for j,v in enumerate(vs))) in ss];fixed=g[:]
        for i,j in combinations(range(26),2):
            if g[i]>>j&1 and [i,j] not in adds and not any(not s&(g[i]|g[j]) for s in six):fixed[i]^=1<<j;fixed[j]^=1<<i
        rows=sets(fixed,7);ms=[sum(1<<j for j,q in enumerate(q7) if not r&q) for r in rows];adj=[sum(1<<j for j in range(i+1,len(ms)) if not m&ms[j]) for i,m in enumerate(ms)];packs=[]
        def dfs(opts,chosen):
            if len(chosen)==8:packs.append(chosen);return
            while opts.bit_count()+len(chosen)>=8:
                bit=opts&-opts;opts-=bit;j=bit.bit_length()-1;dfs(opts&adj[j],chosen+[rows[j]])
        dfs((1<<len(ms))-1,[]);assert len(packs)==prev['packs_visited'];fails=[q for q in qs if all(sum(bool(s&q) for s in rr)<6 for rr in packs)];assert len(fails)==len(qs)-prev['individually_feasible'];labels=lambda q:tuple(v for j,v in enumerate(vs) if q>>j&1);lf={labels(q) for q in fails};shared=lf if shared is None else shared&lf;bad.append(dict(z=z,additions=orig,single_full_family_vetoes=sorted(lf),families=len(packs)))
    c=t['pairs'][0]['on']['counts'];out=dict(holdout_winning_prefixes=sorted(wins),holdout_losing=c[2]-len(wins),holdout_rejected=c[3],single_vetoes=bad,shared_across_all_four=sorted(shared));print('holdout',len(wins),c[3],c[2]-len(wins),'single veto counts',[len(r['single_full_family_vetoes']) for r in bad],'shared',shared);(T/'ramsey_six_hit_holdout_audit.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
