"""Counterbalanced time to first independently verified full attachment with ONE fixed port. Identical prepared CNF/order; fresh solver and no saved rules on each timed invocation."""
from ramsey_time_first_attachment import Solver,perf_counter,D,json,decode,inds,bits,combinations,Random,median,grow,verify

def search(H,a,C,order,learn):
    n=len(H);start=perf_counter();calls=0;cuts=[]
    with Solver(name='g4',bootstrap_with=C) as sat:
        for m,A in order:
            if learn and any(not g&m for g in cuts):continue
            calls+=1
            if sat.solve(assumptions=A):
                model=set(sat.get_model());p=[sum(1<<i for i in range(n) if i+k*n+1 in model) for k in (1,2)];break
            if learn:
                g=sum(1<<(-j-1) for j in sat.get_core());cuts=[h for h in cuts if h&g!=g]+[g]
        else:raise AssertionError('no attachment')
    pre=perf_counter();verify(grow(H,[a,m,*p]),8);return calls,m,(pre-start)*1e6,(perf_counter()-start)*1e6

def run():
    starts=json.loads((D/'ramsey_second_port_core_transfer.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];last=None
    for num,r in enumerate(starts):
        idx=r['record'];a=r['first'];
        if idx!=last:
            H=decode(lines[idx-1]);n=len(H);I=inds(H);base=sorted((s,[-v-1 for v in range(n) if not s>>v&1]) for s in I if all(s>>i&1 or s&h for i,h in enumerate(H)));last=idx
        C=[[-(i+d+1),-(j+d+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for d in (0,n,2*n)]
        for t in I:
            z=7-t.bit_count()-int(not t&a);assert z>=0
            if z<3:
                for ports in combinations(range(3),z+1):C.append([1+i+n*k for k in ports for i in bits(t)])
        for sh in (0,1):
            order=list(base)
            if sh:Random(83219+num).shuffle(order)
            samples=[[],[]];expected=next(m for m,_ in order if m in r['good'])
            for rep in range(4):
                for mode in ((0,1) if (rep+num)%2==0 else (1,0)):
                    calls,s,pre,us=search(H,a,C,order,mode);assert s==expected;samples[mode].append([calls,pre,us])
            out.append(dict(record=idx,first=a,shuffle=sh,second=expected,samples=samples))
    return out
if __name__=='__main__':
    out=run();(D/'ramsey_second_port_first_time.json').write_text(json.dumps(out)+'\n');
    for sh in (0,1):
        z=[r for r in out if r['shuffle']==sh];val=lambda r,i,k:median(s[k] for s in r['samples'][i]);d=[val(r,0,2)-val(r,1,2) for r in z];print(sh,[sum(val(r,i,0) for r in z) for i in (0,1)],[median(val(r,i,2) for r in z) for i in (0,1)],median(d),sum(x>0 for x in d))
