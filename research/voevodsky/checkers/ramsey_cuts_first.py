"""Preloaded single-worker ordering benchmark. Resume between complete pairs. audit runs outside the timed experiment, never filtered by row coverage."""
from ramsey_row_cut_tests import D,CAT,gzip,islice,decode,json,combinations,sets,subprocess,tempfile,Path,check
from time import perf_counter
from statistics import median
from collections import Counter
from hashlib import sha256
import sys,os

def bytes_in(gs):return '\n'.join(' '.join(map(str,g)) for g in gs)
def read(idx):
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:return decode(next(islice(f,idx,None)).strip())

def arm(exe,ports,data,order,audit):
    t=perf_counter();ls=subprocess.run([str(exe),order,'audit' if audit else 'quiet'],input=data,text=True,capture_output=True,check=True).stdout.splitlines();stats=[];cores=set();slack=Counter()
    for l in ls:
        tag,z,v=l.split(' ',2)
        if tag=='core':cores.add((int(z),tuple(json.loads(v))))
        elif tag=='done':stats.append(list(map(int,v.split())))
        else:
            es,options,emitted=map(int,v.split());d=es-76
            if d>=0:slack['live' if emitted else 'dead']+=1;slack['shortfall']+=options<d;assert not(options<d and emitted)
    assert len(stats)==27;cores=sorted(cores);start=perf_counter();ls=subprocess.run([str(ports)],input=bytes_in([g for _,g in cores]),text=True,capture_output=True,check=True).stdout.splitlines() if cores else [];wins=[];done=[]
    for l in ls:
        i,v=l.split(' ',1)
        if i=='done':done.append(int(v));continue
        z,g=cores[int(i)];wins.append([z,list(g),sorted(json.loads(v))])
    assert done==list(range(len(cores)));wins.sort();end=perf_counter();n,nodes,emitted,row_ns,opt_ns=map(sum,zip(*stats));return dict(seconds=end-t,early_rows=row_ns/1e9,optional_cuts=opt_ns/1e9,final_ports=end-start,prefixes=n,optional_nodes=nodes,distinct_cores=len(cores),slack=slack),wins,cores

def seven(g):
    rows=sets(g,7);m=[sum(1<<j for j,q in enumerate(rows) if not q&s) for s in rows];adj=[sum(1<<j for j in range(i+1,len(rows)) if not a&m[j]) for i,a in enumerate(m)]
    def search(opts,k):
        if not k:return []
        while opts.bit_count()>=k:
            bit=opts&-opts;opts-=bit;i=bit.bit_length()-1;w=search(opts&adj[i],k-1)
            if w is not None:return [rows[i]]+w
    w=search((1<<len(rows))-1,8);assert w is None or len(set(w))==8 and all(sum(not s&q for s in w)<=1 for q in rows);return w

def run(mode):
    T=D.parent;here=Path(__file__);names=['ramsey_cuts_first','ramsey_free_port_census'];pins={f.name:sha256(f.read_bytes()).hexdigest() for f in [here,*[here.with_name(n+'.rs') for n in names+['ramsey_six_hit_search']]]};tmp=T/'ramsey_cuts_first_timing.json';env=os.environ.copy()
    with tempfile.TemporaryDirectory() as td:
        exes=[]
        for n in names:
            f=Path(td)/(n+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(here.with_name(n+'.rs')),'-o',str(f)],check=True);exes.append(f)
        if mode=='audit':
            results=[]
            for idx in (99148,374184):
                st,wins,cores=arm(*exes,bytes_in([read(idx)]),'cuts',True);assert wins;winning={(z,tuple(g)) for z,g,_ in wins};details=[]
                for z,g in cores:
                    assert check(g,(1<<26)-1,3,8);w=seven(g);ok=(z,g) in winning;assert not ok or w;details.append(dict(z=z,core=g,seven_witness=w,completes=ok))
                results.append(dict(record=idx,cuts_first=st,details=details,outputs=wins));print(idx,st,'seven pass',sum(bool(d['seven_witness']) for d in details),'legal cores',len(winning),flush=True)
            (T/'ramsey_cuts_first_audit.json').write_text(json.dumps(dict(pins=pins,runs=results),indent=1)+'\n');return
        assert mode=='timing';data=bytes_in([read(99148)]);out=json.loads(tmp.read_text()) if tmp.exists() else dict(record=99148,pins=pins,pairs=[],outputs=None);assert out['pins']==pins
        for j in range(len(out['pairs']),5):
            pair={}
            for name in (('cuts','rows') if j%2==0 else ('rows','cuts')):
                st,wins,_=arm(*exes,data,name,False);assert wins
                if out['outputs'] is None:out['outputs']=wins
                assert wins==out['outputs'];pair[name]=st;print(j,name,st,flush=True)
            out['pairs'].append(pair);out['median_ratio']=median(p['cuts']['seconds']/p['rows']['seconds'] for p in out['pairs']);out['complete']=len(out['pairs'])==5;p=tmp.with_suffix('.tmp');p.write_text(json.dumps(out,indent=1)+'\n');p.replace(tmp)
if __name__=='__main__':run(sys.argv[1])
