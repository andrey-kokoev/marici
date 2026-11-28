"""Keep record 262402's restored row fixed, re-solve all reverse additions in each of the four cut conditions. Catalogue labels throughout."""
import gzip,json
from itertools import combinations,islice
from ramsey_retention_slice import CAT,D,decode,check

def audit():
    replay=json.loads((D.parent/'ramsey_cube_two_cut_forward.json').read_text());idx=replay['record_zero_based'];z=replay['deleted'];
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:parent=decode(next(islice(f,idx,None)).strip())
    row=parent[z];core=parent[:];core[z]=0
    for i in range(27):core[i]&=~(1<<z)
    cuts=[tuple(sorted(e)) for e in replay['add']];
    for i,j in replay['remove']+replay['add']:core[i]^=1<<j;core[j]^=1<<i
    vs=[i for i in range(27) if i!=z];results=[];states=[]
    for cut in [(),(cuts[0],),(cuts[1],),tuple(cuts)]:
        b=core[:]
        for i,j in cut:b[i]^=1<<j;b[j]^=1<<i
        I=[0]
        for i in vs:I.extend([q|1<<i for q in I if not b[i]&q]);
        qs=sorted(q for q in I if q.bit_count()==8 or q.bit_count()==7 and not q&row);b[z]=row
        for i in vs:b[i]|=((row>>i)&1)<<z
        es=[(i,j) for i,j in combinations(vs,2) if (i,j) not in cut and not b[i]&((1<<j)|b[j]) and max(b[i].bit_count(),b[j].bit_count())<7];M={q:frozenset((i,j) for i,j in es if q>>i&q>>j&1) for q in qs}
        def solve(sub):
            ds=[]
            for d in sorted({M[q] for q in sub},key=lambda d:(len(d),sorted(d))):
                if not any(x<=d for x in ds):ds.append(d)
            def rec(g,ds,chosen):
                if not ds:return chosen
                opts=min(([e for e in d if not g[e[0]]&g[e[1]] and max(g[i].bit_count() for i in e)<7] for d in ds),key=len)
                for i,j in sorted(opts,key=lambda e:(-sum(e in d for d in ds),e)):
                    h=g[:];h[i]|=1<<j;h[j]|=1<<i;res=rec(h,[d for d in ds if (i,j) not in d],chosen+[(i,j)])
                    if res is not None:return res
            return rec(b,ds,[])
        triangles=[(z,i,j) for i,j in combinations(vs,2) if row>>i&row>>j&b[i]>>j&1];assert all(b[i].bit_count()<=8 for i in vs);over=[i for i in range(27) if b[i].bit_count()>7];w=None if triangles or over else solve(qs);empty=[q for q in qs if not M[q]];cert=[]
        if triangles or over:pass # Red additions cannot remove an existing triangle or reduce degree.
        elif w is None:
            if empty:cert=[empty[0]]
            else:
                cert=qs[:]
                for q in qs:
                    if solve([x for x in cert if x!=q]) is None:cert.remove(q)
        else:
            g=b[:]
            for i,j in w:g[i]|=1<<j;g[j]|=1<<i
            assert check(g,(1<<27)-1,3,8)
        results.append(dict(cuts=cut,restored_triangles=triangles,overfull=over,demands=len(qs),individually_impossible=len(empty),additions=w,certificate=[dict(clique=[i for i in vs if q>>i&1],options=sorted(M[q])) for q in cert]));states.append((M,empty,cert));
    both=states[-1][0];w=results[-1]['additions'];assert w is not None
    for rec,(m,empty,cert) in zip(results,states):
        for c,q in zip(rec['certificate'],cert):c.update(options_with_both=sorted(both[q]),used_with_both=[e for e in w if e in both[q]])
    out=dict(record=idx,restored=z,row=[i for i in vs if row>>i&1],conditions=results);print(out);(D.parent/'ramsey_cube_witness_cut_ablation.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
