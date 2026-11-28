"""All 2850 red edge pairs on the common rooted cube type, free row and no cap on red additions. Positive controls inject two cuts into a known legal predecessor, using the same kernel."""
from ramsey_cube_retention_floor import G,D,induced,CAT,decode,combinations,json,Counter
from ramsey_retention_slice import check
from concurrent.futures import ThreadPoolExecutor
import tempfile,subprocess,gzip
from pathlib import Path
from itertools import islice

def audit():
    prev=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text());a=induced(G,prev['core_labels']);edges=[(i,j) for i,j in combinations(range(26),2) if a[i]>>j&1];jobs=[(c,a) for c in combinations(edges,2)];n=len(jobs);assert n==2850
    # Extra red links in an otherwise legal control graph will be removed by the kernel. Choose safe links so even the control input is triangle-free.
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:g=decode(next(f).strip());b=induced(g,list(range(26)));es=[(i,j) for i,j in combinations(range(26),2) if not b[i]&(1<<j|b[j])];c=next((e,f) for e,f in combinations(es,2) if not set(e)&set(f));base=b[:]
    for u,v in c:base[u]|=1<<v;base[v]|=1<<u
    jobs.append((c,base));data=[]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'joint.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        def run(chunk):
            p=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,[*e,*f,*g])) for (e,f),g in chunk),text=True,capture_output=True,check=True);ls=p.stdout.splitlines();assert len(ls)==len(chunk);return [l.split(' ',6) for l in ls]
        with ThreadPoolExecutor(8) as pool:
            for chunk in pool.map(run,[jobs[i:i+20] for i in range(0,len(jobs),20)]):data.extend(chunk)
    assert len(data)==n+1;res=[];st=Counter();old={tuple(map(tuple,r['cuts'])):r['counts'].get('each_breakable',0) for r in prev['runs']};old_seen=0
    for j,((cuts,a),ls) in enumerate(zip(jobs,data)):
        unlock,rows,wins,necessary,branches,no_branch=map(int,ls[:6]);ex=json.loads(ls[-1]);
        if ex:
            s,adds,needed=ex;b=a[:]+[s]
            for u,v in cuts:b[u]^=1<<v;b[v]^=1<<u
            for u,v in adds:b[u]|=1<<v;b[v]|=1<<u
            for i in range(26):b[i]|=(s>>i&1)<<26
            assert check(b,(1<<27)-1,3,8)
        if j==n:assert wins and ex;break
        if cuts in old:assert rows==old[cuts] and not wins;old_seen+=1
        st.update(dict(pairs=1,unlock_pairs=bool(unlock),eligible_rows=rows,feasible_rows=wins,feasible_pairs=bool(wins),necessary_rows=necessary,necessary_pairs=bool(necessary),failed_without_branch=no_branch,branch_nodes=branches));res.append(dict(cuts=cuts,unlocks=unlock,rows=rows,wins=wins,necessary=necessary,witness=ex))
    assert old_seen==96;out=dict(counts=st,control_rows=int(data[-1][2]),control_witness=json.loads(data[-1][-1]),cases=res);print(st,'control',out['control_rows'],'first',next((r for r in res if r['wins']),None));(D.parent/'ramsey_cube_two_cut_joint.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':audit()
