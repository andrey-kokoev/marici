"""All reverse triples at budget ten; free port rows one removal short of the recovered core; another transfer record."""
from ramsey_three_claim_attack2 import *
from pathlib import Path
import subprocess,tempfile

def run():
    T=D.parent;labels=json.loads((T/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,labels);r=json.loads((T/'ramsey_cross_residual_propagation.json').read_text())['survivors'][0];start=r['start'];z=start['z'];vs=[i for i in range(27) if i!=z];
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,448077,None)).strip())
    jobs=[];olds=[None]+r['forced_rounds'][0];
    for keep in olds:
        h=b[:]
        for i,j in start['pair']+[e for e in r['legal'][0] if e!=keep]:h[i]^=1<<j;h[j]^=1<<i
        h=induced(h,vs);assert check(h,(1<<26)-1,3,8);jobs.append(h)
    def execute(td,name,graphs):
        exe=Path(td)/(name+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_name(name+'.rs')),'-o',str(exe)],check=True);return subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,g)) for g in graphs),text=True,capture_output=True,check=True).stdout.splitlines()
    with tempfile.TemporaryDirectory() as td:
        cost=execute(td,'ramsey_bounded_reverse_triples',[a]);print('cost',cost[:3],cost[-1],flush=True);ports=[json.loads(s) for s in execute(td,'ramsey_free_ports',jobs)];assert len(ports)==len(jobs) and len(ports[0])==8
        for ss,h in zip(ports,jobs):
            if not ss:continue
            g=h[:]+[s|1<<34 for s in ss]+[255<<26];
            for j,s in enumerate(ss,26):
                for i in range(26):g[i]|=(s>>i&1)<<j
            assert check(g,(1<<35)-1,3,9)
    print('port counts',list(map(len,ports)),flush=True);idx=374184;src=generate(idx=idx,score_cube=False,site_degrees=(6,7));res=finish(src);(T/'ramsey_three_claim_attack3.json').write_text(json.dumps(dict(triples=cost,ports=list(zip(olds,ports)),transfer=dict(record=idx,starts=res['start_count'],cases=res['case_counts'],survivors=res['survivors'])),indent=1)+'\n')
if __name__=='__main__':run()
