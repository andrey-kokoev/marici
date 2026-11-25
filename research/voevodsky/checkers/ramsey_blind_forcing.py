"""Blind failed-literal search. Given only core graph and original requests, certify every forced vertex by exhaustion; return checkable small UNsat subfamilies."""
from ramsey_request_scale import *
from collections import Counter
from functools import reduce
from operator import or_

def search(A,rows,feasibility_only=False):
 n=len(A);F=(1<<n)-1;allrows=(1<<len(rows))-1;hits=[sum(1<<i for i,r in enumerate(rows) if r>>v&1) for v in range(n)];nodes=0
 def solve(av,un):
    nonlocal nodes;nodes+=1
    if not un:return 0,set()
    sample=un;best=n+1
    for _ in range(24):
        b=sample&-sample;j=b.bit_length()-1;opts=rows[j]&av;k=opts.bit_count()
        if k<best:best=k;idx=j;m=opts
        if k<=1:break
        sample^=b
        if not sample:break
    proof={idx}
    while m:
        x=m&-m;m^=x;v=x.bit_length()-1;s,why=solve(av&~(x|A[v]),un&~hits[v]);
        if s is not None:return x|s,set()
        proof.update(why)
    return None,proof
 initial,why=solve(F,allrows)
 if initial is None:return dict(core=None,proofs={},witnesses=[],nodes=nodes,dead_certificate=[rows[i] for i in sorted(why)])
 if feasibility_only:return dict(core=None,witnesses=[initial],nodes=nodes)
 core=0;proofs={};wits=[initial];todo=initial
 while todo:
    x=todo&-todo;todo^=x;s,why=solve(F^x,allrows)
    if s is None:core|=x;proofs[x.bit_length()-1]=[rows[i] for i in sorted(why)]
    else:todo&=s;wits.append(s)
 assert all(all(s&r for r in rows) and all(not(A[i]&s) for i in range(n) if s>>i&1) for s in wits);assert reduce(lambda a,b:a&b,wits)==core
 return dict(core=core,proofs=proofs,witnesses=wits,nodes=nodes)

def main():
 p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);q=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];audit=json.loads((D/'ramsey_live_product_audit.json').read_text());# enumerate independent six-to-eight sets only for the original constraint library, NOT for support solutions
 lib=[]
 def gen(s,m):
    if s.bit_count()>=6:lib.append(s)
    if s.bit_count()==8:return
    while m and s.bit_count()+m.bit_count()>=6:
        b=m&-m;m^=b;gen(s|b,m&~A[b.bit_length()-1])
 gen(0,(1<<len(A))-1);out=[]
 for a in audit:
    i=a['cases'][0];t=q[i]['triple'];rows=sorted((s for s in lib if s.bit_count()+sum(not s&x for x in t)==9),key=lambda x:(x.bit_count(),x));start=time.perf_counter();res=search(A,rows);ms=1000*(time.perf_counter()-start);assert res['core']==a['core'];out.append(dict(case=i,ms=ms,**res))
 (D/'ramsey_blind_forcing.json').write_text(json.dumps(out));lens=[len(p) for x in out for p in x['proofs'].values()];print(len(out),len(lens),'proof lengths',min(lens),statistics.median(lens),max(lens),'times',statistics.median(x['ms'] for x in out),'nodes',statistics.median(x['nodes'] for x in out));a=next(a for a in out if a['case']==51);print('51',a['ms'],a['nodes'],[(v,len(p)) for v,p in a['proofs'].items()]);
if __name__=='__main__':main()
