"""All further red removals on the three alternative starts that passed the old blue-seven screen. No cube degree filter. A red removal cannot repair a blue eight."""
from ramsey_three_claim_attack2 import D,CAT,decode,gzip,islice,json,induced,combinations,check
from ramsey_retention_slice import has
from ramsey_port_near_route import classify
from pathlib import Path
import subprocess,tempfile

def descendants(a,added):
    N=len(a);F=(1<<N)-1;res=[]
    def safe(g,e):
        i,j=e;return not has([~v for v in g],F&~(g[i]|g[j]),6)
    def rec(g,es,rm):
        res.append((g,rm));todo=[e for e in es if safe(g,e)]
        for n,e in enumerate(todo):
            i,j=e;h=g[:];h[i]^=1<<j;h[j]^=1<<i;rec(h,todo[n+1:],rm+[e])
    assert check(a,F,3,8);rec(a,[e for e in combinations(range(N),2) if e not in added and a[e[0]]>>e[1]&1],[]);return res

def run():
    T=D.parent;idx=448077;starts=json.loads((T/'ramsey_double_cross_blind_veto.json').read_text())['candidates'];ids=json.loads((T/'ramsey_three_claim_attack.json').read_text())['passed_port_indices'];
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,idx,None)).strip())
    # Freeze only the pair. Reconstruct all path-cut prefixes, including previously excluded site degrees.
    from itertools import product
    pair=starts[ids[0]]['pair'];assert all(starts[n]['pair']==pair for n in ids);eligible=[];prefixes=[]
    for z,v in enumerate(b):
        if not all(z not in e and sum(v>>i&1 for i in e)==1 for e in pair):continue
        eligible.append(z);a=b[:];vs=[j for j in range(27) if j!=z];opts=[]
        for i,j in pair:
            a[i]|=1<<j;a[j]|=1<<i
            for m in vs:
                if b[i]&b[j]&(1<<m):opts.append((tuple(sorted((i,m))),tuple(sorted((m,j)))))
        covers={frozenset(p) for p in product(*opts)}
        for p in sorted((p for p in covers if not any(q<p for q in covers)),key=sorted):
            h=a[:]
            for i,j in p:h[i]^=1<<j;h[j]^=1<<i
            if not check(induced(h,vs),(1<<26)-1,3,8):continue
            s=dict(z=z,pair=pair,forced=list(map(list,sorted(p))));n=next((n for n in ids if all(starts[n][k]==v for k,v in s.items())),None)
            if n is None:n=len(starts);starts.append(s)
            prefixes.append(n)
    assert set(ids)<=set(prefixes);meta=[];jobs=[];cases=[]
    for n in prefixes:
        s=starts[n];vs=[j for j in range(27) if j!=s['z']];a=b[:]
        for i,j in s['pair']+s['forced']:a[i]^=1<<j;a[j]^=1<<i
        d=descendants(induced(a,vs),{tuple(vs.index(v) for v in e) for e in s['pair']});cases.append(dict(start=n,proposal=s,descendants=len(d),passing_sevens=0,completions=0));print(n,len(d),flush=True)
        for h,rm in d:meta.append((len(cases)-1,[(vs[i],vs[j]) for i,j in rm]));jobs.append(h)
    with tempfile.TemporaryDirectory() as td:
        def execute(stem,graphs):
            exe=Path(td)/(stem+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_name(stem+'.rs')),'-o',str(exe)],check=True);return subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,h)) for h in graphs),text=True,capture_output=True,check=True).stdout.splitlines()
        # Also screen and complete the known positive, in the same run.
        r=json.loads((T/'ramsey_cross_residual_propagation.json').read_text())['survivors'][0];g=b[:];z=r['start']['z'];
        for i,j in r['start']['pair']+r['legal'][0]:g[i]^=1<<j;g[j]^=1<<i
        jobs.append(induced(g,[j for j in range(27) if j!=z]));tags=[int(v) for v in execute('ramsey_port_seven_screen',jobs)];assert len(tags)==len(jobs) and tags[-1]==1;passing=[i for i,v in enumerate(tags) if v];print('passing',len(passing)-1,flush=True);done=[];survivors=[]
        for i in passing[:-1]:cases[meta[i][0]]['passing_sevens']+=1
        control=0
        for line in execute('ramsey_free_port_census',[jobs[i] for i in passing]):
            k,v=line.split(' ',1)
            if k=='done':done.append(int(v));continue
            i=passing[int(k)];record=classify(jobs[i],json.loads(v));
            if i==len(jobs)-1:control+=1;continue
            j,rm=meta[i];cases[j]['completions']+=1;survivors.append(dict(start=cases[j]['start'],extra_removals=rm,output=record))
        assert done==list(range(len(passing))) and control==1
    out=dict(record=idx,eligible_sites=eligible,cases=cases,control_families=control,survivors=survivors);print(cases);(T/'ramsey_port_descendants.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
