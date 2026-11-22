"""Separation in increasing exchange size. Solve for m maximal missing supports avoiding T. All exchanges on OLD outside vertices included, up to alpha(H); no nonmissing port in separator for five-rows. Use a countermodel to add only actually violated exchanges."""
from ramsey_unique_blue_hall import D,json,decode,inds,bits,Counter,Solver,combinations

def depth(H,t,I,nbr):
    n=len(H);m=8-t.bit_count();C=[]
    for j in range(m):
        lit=lambda x:1+j*n+x
        C.extend([[-lit(x)] for x in bits(t)]);C.extend([[-lit(x),-lit(y)] for x in range(n) for y in bits(H[x]) if x<y]);C.extend([[lit(x)]+[lit(y) for y in bits(H[x])] for x in range(n)])
    Y=[(s,1+s.bit_count()-(nbr[s]&t).bit_count()) for s in I if s and not s&t];Y=[(s,k) for s,k in Y if k>0];trace=[];lower=0
    with Solver(name='g3',bootstrap_with=C) as sat:
        while sat.solve():
            model=set(sat.get_model());M=[sum(1<<x for x in range(n) if j*n+x+1 in model) for j in range(m)];bad=next(((s,k) for s,k in Y if sum(bool(s&a) for a in M)<k),None)
            if not bad:return None,trace,M
            s,k=bad;lower=max(lower,s.bit_count());trace.append(s)
            if k>m:sat.add_clause([])
            else:
                for sub in combinations(range(m),m-k+1):sat.add_clause([1+n*j+x for j in sub for x in bits(s)])
    return lower,trace,None

def run():
    cases=json.loads((D/'ramsey_intrinsic_attachment_basis.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in cases[::8]:
        p=r['parent'];G=decode(lines[p-1]);vs=[i for i in range(22) if i!=r['deleted']];H=[sum(1<<j for j,y in enumerate(vs) if G[x]>>y&1) for x in vs];I=sorted(inds(H),key=lambda x:(x.bit_count(),x));nbr={0:0}
        for s in I[1:]:nbr[s]=nbr[s&(s-1)]|H[(s&-s).bit_length()-1]
        forced=set(r['forced']);h=Counter();examples={}
        for t in I:
            if t.bit_count() not in (4,5):continue
            d,trace,model=depth(H,t,I,nbr);yes=t in forced;assert not yes or d is None;assert t.bit_count()!=4 or (d is None)==yes;key=str((t.bit_count(),d,yes));h[key]+=1;examples.setdefault(key,dict(t=t,trace=trace,model=model))
        out.append(dict(parent=p,counts=h,examples=examples));print(p,h,flush=True);(D/'ramsey_exchange_depth.json').write_text(json.dumps(out)+'\n')
    return out
if __name__=='__main__':print(sum((r['counts'] for r in run()),Counter()))
