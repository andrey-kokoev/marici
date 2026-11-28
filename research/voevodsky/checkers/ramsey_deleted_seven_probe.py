"""Before looking at eight-row families: remove z from each seven in the untouched 448077 that contains z. For each surviving blue six, test necessary conditions using at most six chosen optimistic rows. Compare before/after the trial cut. Reattack all three original rules on the less restricted prefixes."""
from ramsey_row_cut_tests import sets,D,CAT,gzip,islice,decode,json,induced,combinations,subprocess,tempfile,Path,analyse

def run():
    T=D.parent;prior=json.loads((T/'ramsey_row_cut_tests.json').read_text());out=[]
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,448077,None)).strip());source=sets(b,7)
    with tempfile.TemporaryDirectory() as td:
        def build(name):
            exe=Path(td)/(name+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_name(name+'.rs')),'-o',str(exe)],check=True);return exe
        probe=build('ramsey_deleted_seven_probe');tri=build('ramsey_row_cut_tests')
        for c in prior:
            s=c['start'];z=s['z'];vs=[i for i in range(27) if i!=z];adds={tuple(vs.index(v) for v in e) for e in s['pair']};base=b[:]
            for i,j in s['pair']+s['forced']:base[i]^=1<<j;base[j]^=1<<i
            for cut in [None,c['extra']]:
                h=base[:]
                if cut:i,j=cut;h[i]^=1<<j;h[j]^=1<<i
                g=induced(h,vs);six=sets(g,6);fixed=g[:];qs=sets(g,7)
                for i,j in combinations(range(26),2):
                    if g[i]>>j&1 and (i,j) not in adds and not any(not q&(g[i]|g[j]) for q in six):fixed[i]^=1<<j;fixed[j]^=1<<i
                rows=sets(fixed,7);sixes=set(six);probes=[(sum((S>>v&1)<<i for i,v in enumerate(vs)),S) for S in source if S>>z&1];src={q:S for q,S in probes if q in sixes};ls=subprocess.run([str(probe)],input='\n'.join(' '.join(map(str,v)) for v in (rows,qs,src)),text=True,capture_output=True,check=True).stdout.splitlines();assert len(ls)==len(src);fail=[]
                for l in ls:
                    q,alone,two=map(int,l.split());assert two<=alone
                    if not two:fail.append(dict(source_seven=[i for i in range(27) if src[q]>>i&1],six_hits_possible=bool(alone)))
                verdict=analyse(g,vs,adds,tri) if cut is None else c['result'];r=dict(z=z,trial_cut=cut,source_sevens=len(probes),surviving_sixes=len(src),failed_probes=fail,distinct_witness=verdict['distinct_packing'],pair_witness=verdict['joint_packing'],third_row_interference=verdict['triple_counterexample']);out.append(r);print(z,cut,len(fail),sum(not f['six_hits_possible'] for f in fail),bool(r['distinct_witness']),bool(r['pair_witness']),bool(r['third_row_interference']),flush=True)
    assert all(not r['failed_probes'] for r in out if r['z']==5)
    shared=sorted(set.intersection(*[{tuple(p['source_seven']) for p in r['failed_probes'] if not p['six_hits_possible']} for r in out if r['z']!=5 and r['trial_cut'] is None]));assert shared;S=shared[0];capacity={}
    for c in prior[:-1]:
        s=c['start'];z=s['z'];vs=[i for i in range(27) if i!=z];h=b[:];
        for u,v in s['pair']+s['forced']:h[u]^=1<<v;h[v]^=1<<u
        g=induced(h,vs);fixed=g[:];six=sets(g,6);q=sum(1<<vs.index(v) for v in S if v!=z)
        for i,j in combinations(range(26),2):
            if g[i]>>j&1 and [vs[i],vs[j]] not in s['pair'] and not any(not d&(g[i]|g[j]) for d in six):fixed[i]^=1<<j;fixed[j]^=1<<i
        rows=[v for v in sets(fixed,7) if v&q];ds=sets(g,7);miss=[sum(1<<j for j,d in enumerate(ds) if not v&d) for v in rows];adj=[sum(1<<j for j in range(i+1,len(rows)) if not miss[i]&miss[j]) for i in range(len(rows))]
        def pack(m,k):
            if k==0:return []
            while m.bit_count()>=k:
                bit=m&-m;m-=bit;i=bit.bit_length()-1;w=pack(m&adj[i],k-1)
                if w is not None:return [i]+w
        for k in range(6,-1,-1):
            w=pack((1<<len(rows))-1,k)
            if w is not None:break
        assert k<6;capacity[z]=dict(maximum=k,witness=[[v for j,v in enumerate(vs) if rows[i]>>j&1] for i in w]);print('common certificate',S,z,k)
    (T/'ramsey_deleted_seven_probe.json').write_text(json.dumps(dict(trials=out,shared_source_sevens=shared,first_shared_capacity=capacity),indent=1)+'\n')
if __name__=='__main__':run()
