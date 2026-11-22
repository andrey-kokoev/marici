"""Try to certify nonexistence of four-row refutations by an elementary counting bound. For each fixed triple enumerate all and only tight rows, and sum the four largest numbers of maximal supports individually excluded. No heuristic support sampling."""
from ramsey_fork_audit_uniform import D,json,grow,inds
from ramsey_final_miss_levels import bits

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=inds(H);M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(H))];n=len(M);cols=[sum(1<<j for j,s in enumerate(M) if s>>v&1) for v in range(len(H))];T={}
    for t in I:
        if not 6<=t.bit_count()<=8:continue
        h=0
        for v in bits(t):h|=cols[v]
        T[t]=(n-h.bit_count(),((1<<n)-1)^h)
    src=json.loads((D/'ramsey_compulsory_kernel_test.json').read_text());out=[]
    for r in src['triples']:
        if r['maximal_count']:continue
        a,b,c=r['triple'];rows=[t for t in T if t.bit_count()+int(not t&a)+int(not t&b)+int(not t&c)==9];rows.sort(key=lambda t:-T[t][0]);covered=0
        for t in rows:covered|=T[t][1]
        assert covered.bit_count()==n
        # Prune sorted candidates when remaining rows cannot cover the residual supports.
        peak=sum(T[t][0] for t in rows[:4]);survive=0;checks=0;witness=None
        def cover(i,m,k):
            nonlocal checks,survive
            if k==0:return [] if m==covered else None
            for j in range(i,len(rows)-k+1):
                t=rows[j];b=T[t][0];gap=n-m.bit_count()
                if k*b<gap:break
                u=m|T[t][1];checks+=1
                if u.bit_count()+(k-1)*b<n:continue
                v=cover(j+1,u,k-1)
                if v is not None:return [t]+v
            return None
        if peak>=n:witness=cover(0,0,4)
        out.append(dict(fixed=[a,b,c],tight=len(rows),top_four=[T[t][0] for t in rows[:4]],checks=checks,four=witness))
    q=min(out,key=lambda r:sum(r['top_four']));rows=[t for t in T if t.bit_count()+sum(not t&s for s in q['fixed'])==9];left=(1<<n)-1;greedy=[]
    while left:
        t=max(rows,key=lambda t:(left&T[t][1]).bit_count());assert left&T[t][1];greedy.append(t);left&=~T[t][1]
    return dict(supports=n,records=out,example=dict(fixed=q['fixed'],cover=greedy))
if __name__=='__main__':
    out=run();r=out['records'];print(len(r),sum(q['four'] is not None for q in r),sum(sum(q['top_four'])<out['supports'] for q in r),min(r,key=lambda q:sum(q['top_four'])));(D/'ramsey_four_row_bound.json').write_text(json.dumps(out)+'\n')
