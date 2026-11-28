"""Free completions at and around the known 448077 route: restore at most one old cut, make at most one new cut. Rows, cube labels and degrees within the core are not supplied to the port search."""
from ramsey_three_claim_attack2 import D,CAT,decode,gzip,islice,json,induced,combinations,check
from itertools import permutations
from pathlib import Path
import subprocess,tempfile

def classify(h,rows):
    b=h[:]+[s|1<<34 for s in rows]+[255<<26]
    for j,s in enumerate(rows,26):
        for i in range(26):b[i]|=(s>>i&1)<<j
    assert check(b,(1<<35)-1,3,9);P=list(combinations(range(8),2));over={(i,j):(rows[i]&rows[j]).bit_count() for i,j in P};label=next((p for p in permutations(range(8)) if all(over[i,j]=={1:3,2:1,3:0}[(p[i]^p[j]).bit_count()] for i,j in P)),None);k=[sum(r>>i&1 for r in rows) for i in range(26)];ones=sum(1<<i for i,v in enumerate(k) if v==1);bad=[i for i in range(26) if k[i]>=2 and k[i]*(ones&h[i]).bit_count()!=4];return dict(rows=rows,sizes=list(map(int.bit_count,rows)),cube_label=label,bad_product_sites=bad)

def run():
    T=D.parent;r=json.loads((T/'ramsey_cross_residual_propagation.json').read_text())['survivors'][0];src=r['start'];z=src['z'];vs=[i for i in range(27) if i!=z];removed=list(map(tuple,r['legal'][0]));added=list(map(tuple,src['pair']))
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,448077,None)).strip())
    old=[(i,j) for i,j in combinations(vs,2) if b[i]>>j&1 and (i,j) not in removed];h=b[:];
    for i,j in removed+added:h[i]^=1<<j;h[j]^=1<<i
    jobs=[];meta=[];tried=0
    for restore in [None]+removed:
        for cut in [None]+old:
            tried+=1;g=h[:]
            for e in (restore,cut):
                if e:i,j=e;g[i]^=1<<j;g[j]^=1<<i
            a=induced(g,vs)
            if check(a,(1<<26)-1,3,8):jobs.append(a);meta.append(dict(restore=restore,cut=cut,completions=[]))
    print('tried',tried,'legal cores',len(jobs),flush=True)
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'census.exe';subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_name('ramsey_free_port_census.rs')),'-o',str(exe)],check=True);out=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,g)) for g in jobs),text=True,capture_output=True,check=True).stdout.splitlines()
    done=[]
    for line in out:
        left,right=line.split(' ',1)
        if left=='done':done.append(int(right));continue
        i=int(left);meta[i]['completions'].append(classify(jobs[i],json.loads(right)))
    assert done==list(range(len(jobs))) and meta[0]['completions'];n=sum(len(v['completions']) for v in meta);print('families',n,'on',sum(bool(v['completions']) for v in meta),'cores');(T/'ramsey_port_near_route.json').write_text(json.dumps(dict(record=448077,deleted=z,added=added,core_labels=vs,tested=tried,legal_cores=len(jobs),families=n,cases=meta),indent=1)+'\n')
if __name__=='__main__':run()
