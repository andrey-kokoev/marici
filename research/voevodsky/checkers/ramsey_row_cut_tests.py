"""Five frozen prefixes: distinguish repeated-row, pair-cut and three-row mixed failures. Independently replay positive witnesses and verify a negative eight-clique result with Python integer bitsets."""
from ramsey_port_descendants import D,CAT,decode,gzip,islice,json,induced,combinations,check,has,subprocess,tempfile,Path
F=(1<<26)-1

def sets(a,k):
    I=[0]
    for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v and q.bit_count()<k]);
    return [q for q in I if q.bit_count()==k]

def analyse(g,vs,adds,exe):
    fixed=g[:];six=sets(g,6);qs=sets(g,7);old=[e for e in combinations(range(26),2) if g[e[0]]>>e[1]&1];
    for i,j in old:
        if (i,j) not in adds and not any(not s&(g[i]|g[j]) for s in six):fixed[i]^=1<<j;fixed[j]^=1<<i
    rows=sets(fixed,7);edges=[frozenset((i,j) for i,j in old if r>>i&r>>j&1) for r in rows];miss=[sum(1<<j for j,q in enumerate(qs) if not r&q) for r in rows];cache={}
    def after(ids):
        b=g[:]
        for i,j in frozenset.union(*(edges[t] for t in ids)):b[i]^=1<<j;b[j]^=1<<i
        return b
    def pair(i,j):
        if miss[i]&miss[j]:return False
        m=edges[i]|edges[j]
        if m not in cache:cache[m]=check(after([i,j]),F,3,8)
        return cache[m]
    ls=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,v)) for v in (g,rows)),text=True,capture_output=True,check=True).stdout.splitlines();s,p,cts=map(json.loads,ls[:3]);
    def replay(ids,joint):
        if ids:assert len(set(ids))==8 and all(pair(i,j) if joint else not (miss[i]&miss[j]) for i,j in combinations(ids,2));return
        adj=[0]*len(rows)
        for i,j in combinations(range(len(rows)),2):
            if pair(i,j) if joint else not (miss[i]&miss[j]):adj[i]|=1<<j
        def pack(m,k):
            if k==0:return True
            while m.bit_count()>=k:
                b=m&-m;m-=b
                if pack(m&adj[b.bit_length()-1],k-1):return True
            return False
        assert not pack((1<<len(rows))-1,8)
    replay(s,False);replay(p,True);tri=None;labels=lambda q:[i for j,i in enumerate(vs) if q>>j&1]
    if not ls[3].startswith('none'):
        i,j,k,q,_=map(int,ls[3].split());ids=[i,j,k];assert len(set(ids))==3 and all(pair(u,v) for u,v in combinations(ids,2));b=after(ids);assert check(b,F,3,8) and q.bit_count()==7 and not q&(rows[i]|rows[j]);red=[(u,v) for u,v in old if q>>u&q>>v&1];assert red and all(e in edges[k] and e not in edges[i]|edges[j] and not b[e[0]]>>e[1]&1 for e in red);tri=dict(rows=[labels(rows[t]) for t in ids],new_blue_seven=labels(q),old_red_edges=[[vs[u],vs[v]] for u,v in red]);
    return dict(candidate_rows=len(rows),coverage_pairs=cts[0],joint_pairs=cts[1],distinct_packing=[labels(rows[t]) for t in s],joint_packing=[labels(rows[t]) for t in p],triple_counterexample=tri)

def run():
    T=D.parent;cases=[(c['proposal'],[17,20]) for c in json.loads((T/'ramsey_port_descendants.json').read_text())['cases']];cases.append((json.loads((T/'ramsey_cross_residual_propagation.json').read_text())['survivors'][0]['start'],[0,17]));out=[]
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,448077,None)).strip())
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'tests.exe';subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        for start,extra in cases:
            g=a[:];vs=[v for v in range(27) if v!=start['z']];adds={tuple(vs.index(v) for v in e) for e in start['pair']}
            for i,j in start['pair']+start['forced']+[extra]:g[i]^=1<<j;g[j]^=1<<i
            res=analyse(induced(g,vs),vs,adds,exe);out.append(dict(start=start,extra=extra,result=res));print(start['z'],res['candidate_rows'],len(res['distinct_packing']),len(res['joint_packing']),res['triple_counterexample'],flush=True)
    assert out[-1]['result']['joint_packing'];(T/'ramsey_row_cut_tests.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
