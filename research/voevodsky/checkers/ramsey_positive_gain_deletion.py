"""One core deletion, two additional ports. The old load-k and load-(k-1) sets give an exact test."""
from collections import Counter
from itertools import combinations_with_replacement
from ramsey_retention_slice import CAT,D,decode,check
import gzip,json


def audit():
    patches=json.loads((D.parent/'ramsey_patch_edge27.json').read_text());ids={r['row'] for r in patches};a_by={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};stats=Counter();examples={};cores=set();all_cases=[]
    for r in patches:
        a=a_by[r['row']];c=r['c'];rows=[a[c[(j+2)%4]]|1<<c[(j+1)%4] for j in range(4)];rows[r['j']]|=r['patch'];I=[0]
        for i,m in enumerate(a):I.extend([q|1<<i for q in I if not q&m]);
        S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];idx={}
        for load in (7,8):
            Q=[q for q in I if q.bit_count()+sum(not q&s for s in rows)==load];col=[sum(1<<j for j,q in enumerate(Q) if q>>i&1) for i in range(27)];mask=(1<<len(Q))-1
            def misses(s):
                m=mask
                while s:
                    b=s&-s;s-=b;m&=~col[b.bit_length()-1]
                return m
            idx[load]=(Q,col,[misses(s) for s in S]);
        _,tight,m8=idx[8];near,c7,m7=idx[7];assert all(m8);zs=[]
        for z in range(27):
            # Every support on the reduced core is contained in an old maximal support restricted to it.
            opts=[i for i,b in enumerate(m8) if not b&~tight[z]];stats['deletions']+=1;stats['one_extra']+=bool(opts);win=False
            for i,j in combinations_with_replacement(opts,2):
                conflict=m7[i]&m7[j]&~c7[z];win=not conflict
                if win:
                    zs.append(z);g=a[:]+[0]*7
                    for k,t in enumerate(rows+[S[i],S[j]],27):
                        g[k]=t|1<<33;g[-1]|=1<<k
                        for v in range(27):g[v]|=int(bool(t>>v&1))<<k
                    assert check(g,((1<<34)-1)^(1<<z),3,9);examples.setdefault('success',dict(record=r['row'],square=c,delete=z,original=rows,new=[S[i]&~(1<<z),S[j]&~(1<<z)]));break
                if i!=j:examples.setdefault('two_separate',dict(record=r['row'],square=c,delete=z,new=[S[i]&~(1<<z),S[j]&~(1<<z)],near_set=near[(conflict&-conflict).bit_length()-1],original=rows))
            stats['two_extra']+=win;stats['two_distinct_singly_available']+=len(set(S[i]&~(1<<z) for i in opts))>=2
        if zs:cores.add(r['row']);all_cases.append(dict(record=r['row'],square=c,deletions=zs))
    out=dict(panels=len(patches),distinct_source_records=len(ids),panels_with_gain=len(all_cases),records_with_gain=len(cores),counts=stats,cases=all_cases,examples=examples);print({k:v for k,v in out.items() if k!='cases'});(D.parent/'ramsey_positive_gain_deletion.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
