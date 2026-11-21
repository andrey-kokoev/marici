"""Near-solutions certify individual rows irredundant: invalidate every old port by one deletion while conserving all but one inequality. Masks avoid graph-solver dependencies."""
from itertools import product
from functools import lru_cache
from ramsey_final_miss_levels import D,json,attach,bits,levels,Counter

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=attach(p['stem_graphs'][-1],p['alternate']['to34']);old=set(json.loads((D/'ramsey_reuse_stress.json').read_text())['35']['old']);Q=[];levels(H,Q.append);I=[0]
    for v,r in enumerate(H):I += [s|1<<v for s in I if not s&r]
    T=[t for t in I if t.bit_count()>=6];F=(1<<len(T))-1;col=[sum(1<<i for i,t in enumerate(T) if not t>>v&1) for v in range(34)];m6,m7,m8=[sum(1<<i for i,t in enumerate(T) if t.bit_count()==j) for j in (6,7,8)]
    @lru_cache(None)
    def miss(s):
        m=F
        for v in bits(s):m&=col[v]
        return m
    seen=set();witness={};toponly={};active={H[v] for v in (2,22,16,9,23,3)};ac=sum(1<<i for i,t in enumerate(T) if t in active);best=None
    local=ac|sum(1<<i for i,t in enumerate(T) if t.bit_count()==8 and any(t&s==s for s in active));pool=[]
    for q in Q:
        for tup in product(*[[s^1<<i for i in bits(s)] if s in old else [s] for s in q]):
            key=tuple(sorted(tup))
            if key in seen:continue
            seen.add(key);a,b,c,d=map(miss,key);ab=a&b;cd=c&d;x=a|b;y=c|d
            M=(ab|cd|(x&y))&m8;N=((ab&y)|(cd&x))&m7;bad=M|N|(ab&cd&m6);assert bad
            if not bad&local and bad.bit_count()<=100:pool.append((bad.bit_count(),key,bad))
            if bad.bit_count()==1:witness.setdefault(T[bad.bit_length()-1],key)
            if not N&ac and M.bit_count()==1:toponly.setdefault(T[M.bit_length()-1],key)
            if not N&ac and (best is None or bad.bit_count()<best[0]):best=(bad.bit_count(),key,[T[i] for i in bits(bad)])
    chosen=[];used=0
    for _,key,bad in sorted(pool):
        if not used&bad:used|=bad;chosen.append({'tuple':key,'failed_rows':[T[i] for i in bits(bad)]})
    print('disjoint global obligations',len(chosen),'sizes',[len(v['failed_rows']) for v in chosen]);return {'disjoint_obligations':chosen,'distinct_tuples':len(seen),'mandatory_all':witness,'mandatory_top_given_six':toponly,'best':best}
if __name__=='__main__':
    r=run();print(r['distinct_tuples'],Counter(t.bit_count() for t in r['mandatory_all']),len(r['mandatory_top_given_six']),r['best']);(D/'ramsey_mandatory_global_rows.json').write_text(json.dumps(r)+'\n')
