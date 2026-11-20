"""Exact optimum by triple inclusion-exclusion plus lazy fourfold resolution. Compare labelled triple bounds alone vs additionally using the number (not internal colors) of common blue extension sites. Count exact fourfold queries, not candidate generation or total operation cost. The reference optimal cost is accessed only for post-checks."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,sys
from ramsey_37_shared_pockets import solve as shared_solve
shared=[]
H=Path(__file__).resolve().parents[1];D=H/'results';cat=(H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6').read_text().splitlines();ref=json.loads((D/'ramsey_37_switch_extension_catalogue.json').read_text())['report'];out=[];V=(1<<22)-1
for rec,g in zip(ref,cat):
    bits=''.join(f'{ord(ch)-63:06b}' for ch in g[1:]);N=[0]*22
    for j in range(22):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1':N[i]|=1<<j;N[j]|=1<<i
    A=[0]
    for i in range(22):A += [s|1<<i for s in A if not s&N[i]]
    six=[s for s in A if s.bit_count()==6]
    for d in rec['deletions']:
        u,v=d['edge'];P=1<<u|1<<v;W=V&~(P|N[u]|N[v]);F=[s for s in six if not s&P];mom={};B=[{},{}];data={}
        for s in A:
            if s&~W:continue
            ids=[i for i in range(22) if s>>i&1];block=s
            for i in ids:block|=N[i]
            if W&~block:continue
            terms={}
            for k in range(min(3,len(ids))+1):
                for T in combinations(ids,k):
                    t=sum(1<<i for i in T)
                    if t not in mom:mom[t]=sum((h&t)==t for h in F)
                    terms[t]=mom[t]
            z=sum((-1)**t.bit_count()*c for t,c in terms.items());lo=hi=pl=ph=0
            if len(ids)==4:
                lo=0;hi=len(F)
                for t in terms:
                    val=sum((-1)**((y^t).bit_count())*c for y,c in terms.items() if y&t==t)
                    if t.bit_count()%2:hi=min(hi,val)
                    else:lo=max(lo,-val)
                pocket=V&~(block|P);k=pocket.bit_count();pl=max(lo,[0,0,0,1,2,5][k]);ph=min(hi,[0,0,1,2,4,5][k]);assert lo<=pl<=ph<=hi;data[s]=(z,pocket)
            B[0][s]=(z+lo,z+hi);B[1][s]=(z+pl,z+ph)
        # Retain pre-query intervals for a retrospective certificate audit. The search below
        # does not see the optimum or the audit choices.
        initial=dict(B[1]);traces=[]
        if any(flag in sys.argv for flag in ('--shared','--global','--threshold')):
            result=shared_solve(initial,data,lambda p:sum(not(N[i]>>j&1) for i,j in combinations([i for i in range(22) if p>>i&1],2)),global_support=('--global' in sys.argv or '--threshold' in sys.argv),threshold='--threshold' in sys.argv)
            assert result['cost']==d['freshMin']==sum(not(s&result['witness']) for s in F)
            shared.append(dict(record=rec['record'],edge=d['edge'],**result))
        for bounds in B:
            queries=[]
            while True:
                best=min(bounds,key=lambda t:bounds[t][1]);probe=min(bounds,key=lambda t:(bounds[t][0],bounds[t][1]));
                if bounds[probe][0]==bounds[best][1]:break
                if bounds[probe][0]==bounds[probe][1]:raise AssertionError
                z,pocket=data[probe];t4=sum(not(N[i]>>j&1) for i,j in combinations([i for i in range(22) if pocket>>i&1],2));val=z+t4;assert bounds[probe][0]<=val<=bounds[probe][1];bounds[probe]=(val,val);queries.append(probe)
            exact=bounds[best][1];assert exact==d['freshMin']==sum(not(s&best) for s in F);traces.append(dict(queries=queries,best=best,cost=exact))
        # Independent interval oracle, certify BOTH exact optimum and an attaining set.
        # Every lower endpoint < exact must be queried. Once those costs are known,
        # one extra query is necessary and sufficient iff no upper endpoint proves
        # attainment. This is instance-optimal evidence, not an online algorithm.
        mandatory=[s for s,(l,h) in initial.items() if l<exact]
        audited=dict(initial)
        for s in mandatory:
            cost=sum(not(s&h) for h in F);audited[s]=(cost,cost)
        extra=int(min(h for l,h in audited.values())>exact)
        certificate=mandatory+([traces[1]['best']] if extra else [])
        for s in certificate:
            cost=sum(not(s&h) for h in F);audited[s]=(cost,cost)
        assert min(l for l,h in audited.values())==min(h for l,h in audited.values())==exact
        assert set(mandatory)<=set(traces[1]['queries']) and len(certificate)<=len(traces[1]['queries'])
        out.append(dict(record=rec['record'],edge=d['edge'],quartets=len(data),traces=traces,interval_audit=dict(mandatory=mandatory,extra_attainment=extra,minimum_certificate=certificate)))
if shared:
    (D/('ramsey_37_joint_threshold.json' if '--threshold' in sys.argv else 'ramsey_37_global_pockets.json' if '--global' in sys.argv else 'ramsey_37_shared_pockets.json')).write_text(json.dumps(shared,indent=2)+'\n');print('shared queries',sum(len(r['queries']) for r in shared))
print([dict(Counter(len(r['traces'][i]['queries']) for r in out)) for i in (0,1)]);print(next(r for r in out if r['record']==3 and r['edge']==[16,20]));(D/'ramsey_37_lazy_fourfold.json').write_text(json.dumps(out,indent=2)+'\n')
