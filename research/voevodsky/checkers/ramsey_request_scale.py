"""A/B exact continuation-key cost, with a deterministic cap on saturation. Times local, not solver lower bounds."""
import sys,json,itertools,time,statistics
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';K=D.parents[1]/'chatgpt/ramsey';sys.path.insert(0,str(K))
from ramsey_fork_audit_uniform import grow,inds
from ramsey_rooted_size_crossover import decode

def prepare(A):
 I=sorted(inds(A));return I

def sat(C,A,limit=100000):
 # Incrementally keep just the inclusion-minimal rows. Process in deterministic rounds.
 def slim(V):
    acc=[]
    for x in sorted(set(V),key=lambda x:(x.bit_count(),x)):
        if not any(y&x==y for y in acc):acc.append(x)
    return tuple(acc)
 C=slim(C);initial=len(C);pairs=0;gen=0;peak=len(C);rounds=0
 while True:
    N=set(C);rounds+=1
    for a,b in itertools.combinations(C,2):
        pairs+=1
        if pairs>limit:return None,dict(initial=initial,peak=peak,pairs=pairs-1,generated=gen,rounds=rounds)
        # Only unique-to-clause endpoints can yield a nonsubsumed consequence.
        l=a&~b;r=b&~a
        while l:
            x=l&-l;l^=x;m=A[x.bit_length()-1]&r
            while m:
                y=m&-m;m^=y;new=(a|b)^(x|y)
                if new not in N:N.add(new);gen+=1
        peak=max(peak,len(N))
        if len(N)>=4000:return None,dict(initial=initial,peak=peak,pairs=pairs,generated=gen,rounds=rounds)
    nxt=slim(N)
    if nxt==C:return C,dict(initial=initial,peak=peak,pairs=pairs,generated=gen,rounds=rounds)
    C=nxt

def run(A,make):
 t=time.perf_counter();I=prepare(A);prep=time.perf_counter()-t;results=[];t=time.perf_counter();M=[sum(1<<j for j,s in enumerate(I) if s>>v&1) for v in range(len(A))];full=(1<<len(I))-1;index_time=time.perf_counter()-t
 for tag,C in make(I):
    # Direct legal domain bitsets, identical signature iff continuation sets equal.
    def key(rows):
        live=full
        for c in rows:
            h=0
            while c:x=c&-c;c^=x;h|=M[x.bit_length()-1]
            live&=h
        return live
    start=time.perf_counter();live=key(C);kt=time.perf_counter()-start;start=time.perf_counter();closure,stats=sat(C,A);st=time.perf_counter()-start
    if closure is not None:assert key(closure)==live
    results.append(dict(tag=tag,raw=len(C),survivors=live.bit_count(),key_ms=kt*1000,sat_ms=st*1000,closed=None if closure is None else len(closure),**stats))
 return dict(vertices=len(A),domain=len(I),enumerate_ms=1000*prep,index_ms=1000*index_time,rows=results)
if __name__=='__main__':
 A=decode((K/'pauli-realization-catalogues/r35_13.g6').read_text().splitlines()[0]);sm=run(A,lambda I:((s,[t for t in I if t.bit_count()==4 and not s&t]) for s in I if s.bit_count()==4));p=json.loads((K/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);q=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];lg=run(H,lambda I:((i,[s for s in I if 6<=s.bit_count()<=8 and s.bit_count()+sum(not s&a for a in r['triple'])==9]) for i,r in enumerate(q)));out=[sm,lg];(D/'ramsey_request_scale.json').write_text(json.dumps(out));
 for r in out:
    rows=r['rows'];print({k:v for k,v in r.items() if k!='rows'},'cases',len(rows),'closed',sum(x['closed'] is not None for x in rows));print({k:(min(y[k] for y in rows),statistics.median(y[k] for y in rows),max(y[k] for y in rows)) for k in ('raw','peak','survivors','key_ms','sat_ms')})
