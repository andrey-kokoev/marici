"""Extend a verified four-port prefix on an intact 27-core by hitting its tight cliques. No cube labels."""
import json,gzip
from collections import Counter
from ramsey_retention_slice import CAT,D,decode,check


def audit():
    patches=json.loads((D.parent/'ramsey_patch_edge27.json').read_text());ids={r['row'] for r in patches};graphs={i:decode(s.strip()) for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];hist=Counter()
    for r in patches:
        a=graphs[r['row']];c=r['c'];rows=[a[c[(j+2)%4]]|(1<<c[(j+1)%4]) for j in range(4)];rows[r['j']]|=r['patch'];I=[0]
        for i,m in enumerate(a):I.extend([q|1<<i for q in I if not q&m]);
        def tight(q):return q.bit_count()+sum(not q&s for s in rows)
        assert max(map(tight,I))==8;T=sorted((q for q in I if tight(q)==8),key=lambda q:(q.bit_count(),q));maximal=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];options=[s for s in maximal if all(s&q for q in T)];rec=dict(record=r['row'],square=c,tight_sizes=Counter(q.bit_count() for q in T),maximal_supports=len(maximal),fifth_options=len(options))
        if options:
            s=options[0];G=a[:]+[0]*6
            for j,t in enumerate(rows+[s],27):
                G[j]=t|(1<<32);G[32]|=1<<j
                for i in range(27):G[i]|=int(bool(t>>i&1))<<j
            assert check(G,(1<<33)-1,3,9);rec['example_fifth']=s
        else:
            # Deletion-minimize the demands via bit sets of maximal supports missing each one.
            full=(1<<len(maximal))-1;hits=[sum(1<<j for j,s in enumerate(maximal) if q&s) for q in T];keep=list(range(len(T)));prefix=[full]
            for h in hits:prefix.append(prefix[-1]&h)
            tail=full;core=[]
            for j in reversed(keep):
                if prefix[j]&tail:core.append(j);tail&=hits[j]
            rec['obstruction']=[T[j] for j in core];assert all(any(all(s&T[k] for k in core if k!=j) for s in maximal) for j in core)
        hist[bool(options)]+=1;out.append(rec)
    print(hist);print(out[0]);print('min negative certificate',min((len(r['obstruction']) for r in out if 'obstruction'in r),default=None));(D.parent/'ramsey_square_fifth_from_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
