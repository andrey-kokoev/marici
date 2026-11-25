"""Charge both approaches for identical request formation; output full labeled next supports, not just feasibility. No saved outcomes as inputs."""
from ramsey_blind_forcing import *
from functools import cache
from time import perf_counter as now

def main():
 p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);qs=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];n=len(A);F=(1<<n)-1;t=now();lib=[]
 def gen(m,s):
    k=s.bit_count()
    if k>=6:lib.append(s)
    if k==8:return
    while m and k+m.bit_count()>=6:
        b=m&-m;m-=b;gen(m&~A[b.bit_length()-1],s|b)
 gen(F,0);lib.sort(key=lambda s:(s.bit_count(),s));prepared=[]
 for q in qs:
    a,b,c=q['triple'];prepared.append([s for s in lib if s.bit_count()+(not s&a)+(not s&b)+(not s&c)==9])
 prep=now()-t;t=now();I=prepare(A);cols=[sum(1<<j for j,s in enumerate(I) if s>>v&1) for v in range(n)];full=(1<<len(I))-1;setup=now()-t
 @cache
 def hit(s):
    b=s&-s;return cols[b.bit_length()-1]|hit(s^b) if s else 0
 def indexed(rows):
    m=full
    for s in rows:
        m&=hit(s)
        if not m:break
    out=[]
    while m:b=m&-m;m-=b;out.append(I[b.bit_length()-1]);
    return out
 def finish(core,rows):
    rem=F^core
    for i in range(n):
        if core>>i&1:rem&=~A[i]
    need=[r for r in rows if not r&core];out=[];num=0
    def visit(m,s):
        nonlocal num;num+=1
        if all(s&r for r in need):out.append(s)
        while m:b=m&-m;m-=b;visit(m&~A[b.bit_length()-1],s|b)
    visit(rem,core);return out,num
 times=Counter();work=Counter();cases=[]
 for i,rows in enumerate(prepared):
    t=now();expected=indexed(rows);times['indexed']+=now()-t;t=now();r=search(A,rows);live=r['core'] is not None;times['search_live' if live else 'search_dead']+=now()-t;t=now();actual,num=finish(r['core'],rows) if live else ([],0);times['finish']+=now()-t;assert sorted(actual)==sorted(expected);work['live']+=live;work['post_core_candidates']+=num;work['legal']+=len(actual);cases.append([i,r['core'],r['nodes'],num,len(actual)])
 result=dict(prep_s=prep,index_setup_s=setup,times=times,work=work,full_domain=len(I),cached_masks=hit.cache_info().currsize,cases=cases);print(prep,setup,times,work,hit.cache_info());(D/'ramsey_all_branch_forcing.json').write_text(json.dumps(result))
if __name__=='__main__':main()
