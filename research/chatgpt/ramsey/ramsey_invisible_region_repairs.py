"""Ablation of frozen square assumptions: add colours on invisible vertices, recolour or drop private incidences, allow extra overlap. Exact full attachment CNF, fixed seed incidence in every model; verify graph witnesses."""
from ramsey_orientation_veto import D,json,graph,inds,bits,prove,gzip,Counter
from ramsey_capacity_transfer_78 import verify,grow,combinations
from pysat.solvers import Solver
from pysat.card import CardEnc

def audit(H,T,W,tab,analyze=None):
    n=len(H);a=next(bits(W));b=next(bits(H[a]&W));c,d=bits(W^(1<<a|1<<b));V=(a,b,c,d);ends=[1<<i|1<<j for i in (a,b) for j in (c,d)];Z=[];C=[];dom={};single=[];force=[];fixed=[[],[]];used=[];zsingle=[];privsingle=[];blockz=[]
    for u in range(n):
        if W>>u&1:continue
        m=sum(1<<j for j,v in enumerate(V) if H[u]>>v&1);hs=[h for h,e in enumerate(ends) if not H[u]&e];dom[u]=hs;A=[1+4*u+h for h in hs];pairs=[[-x,-y] for x,y in combinations(A,2)]
        if not m:
            Z.append(u);y=4*n+u+1;used.append(y);C.extend([[-x,y] for x in A]);zsingle+=pairs;blockz.extend(-x for x in A)
        else:
            force.append(A);privsingle+=pairs
            for j,ta in enumerate(tab):fixed[j].append(4*u+ta[m].bit_length())
    for u,hs in dom.items():
        for v in bits(H[u]):
            if v>u and v in dom:C.extend([[-(1+4*u+h),-(1+4*v+h)] for h in set(hs)&set(dom[v])])
    for t in T:
        for ps in combinations(range(4),9-t.bit_count()):
            if not any(ends[h]&t for h in ps):C.append([1+4*u+h for u in bits(t) if u in dom for h in ps if h in dom[u]])
    if analyze:return analyze(C,dom,ends,Z)
    def solve(extra,assume=(),minz=False):
        with Solver(name='g4',bootstrap_with=C+extra) as sat:
            if not sat.solve(assumptions=assume):return None
            m=set(sat.get_model())
        if minz:
            for k in range(sum(y in m for y in used)):
                cn=CardEnc.atmost(used,k,top_id=5*n)
                with Solver(name='g4',bootstrap_with=C+extra+cn.clauses) as sat:
                    if sat.solve(assumptions=assume):m=set(sat.get_model());break
        S=[e|sum(1<<u for u,hs in dom.items() if h in hs and 1+4*u+h in m) for h,e in enumerate(ends)];verify(grow(H,S),9);return dict(ports=S,used=[v for v in Z if any(s>>v&1 for s in S)])
    one=privsingle+zsingle;raw=[solve(one,f,True) for f in fixed];ret=dict(raw=next((x for x in sorted((x for x in raw if x),key=lambda x:len(x['used']))),None),invisible=Z)
    for name,ex,ass in [('switch',one+force,()),('thin',one,()),('multi_z',privsingle,()),('full_no_z',[],blockz),('full',[],())]:ret[name]=solve(ex,ass,name=='switch')
    return ret

def run():
    src=json.loads((D/'ramsey_orientation_veto.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();tab=[dict(r['table']) for r in prove()];out=[]
    for rec in src:
        H=graph(ls[rec['record']-1]);T=[s for s in inds(H) if s.bit_count()>=5]
        for r in rec['rows']:out.append(dict(record=rec['record'],seed=r['seed'],tag=r['tag'],**audit(H,T,r['seed'],tab)))
    return out
if __name__=='__main__':
    z=run();print({k:sum(bool(r[k]) for r in z) for k in ('raw','switch','thin','multi_z','full_no_z','full')});print(Counter((r['tag'],bool(r['switch']),bool(r['full'])) for r in z));(D/'ramsey_invisible_region_repairs.json').write_text(json.dumps(z)+'\n')
