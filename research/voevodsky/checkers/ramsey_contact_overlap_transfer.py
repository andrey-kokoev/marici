"""Fresh 87-edge test. Compare full distributions of overlap between pairs of blue sevens containing a proposed link. Restrict to endpoints of the frozen 40/118 mark."""
from ramsey_contact_signature_transfer import predict,D,CAT,find,decode
from itertools import combinations
from pathlib import Path
import gzip,json,tempfile,subprocess
from concurrent.futures import ThreadPoolExecutor

def profile(a,e):
    p=sum(1<<u for u in e);I=[p]
    for i,v in enumerate(a):
        if p&(v|1<<i):continue
        I.extend([q|1<<i for q in I if not q&v])
    seven=[q for q in I if q.bit_count()==7];h=[0]*5
    for q,r in combinations(seven,2):h[(q&r).bit_count()-2]+=1
    return tuple(h)

def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);train={42706:(16,24),92172:(8,9),237883:(13,15)};ref=[];graphs={}
    for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        s=l.rstrip();
        if i in train:ref.append(profile(decode(s.decode()),train[i]))
        if sum(s[1:].translate(w))==87:graphs[i]=s.decode()
    # Rule fixed before scoring: keep all nearest ties by raw L1 histogram distance, per marked core.
    candidates={};pred={};trials=[]
    for i,s in graphs.items():
        a=decode(s);es,marks=predict(a);end={v for e in marks for v in e};opts=[e for e in es if end.intersection(e)];candidates[i]=opts
        if opts:
            ds={e:min(sum(abs(x-y) for x,y in zip(profile(a,e),r)) for r in ref) for e in opts};pred[i]=[e for e,d in ds.items() if d==min(ds.values())]
        trials.append((i,None,s))
        for u,v in es:
            t=v*(v-1)//2+u;j=1+t//6;trials.append((i,(u,v),s[:j]+chr(63+((ord(s[j])-63)^(1<<(5-t%6))))+s[j+1:]))
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'pack.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_intact27_seven_pack.rs')),'-o',str(exe)],check=True)
        def test(ks):
            p=subprocess.run([str(exe)],input='\n'.join(f'{k} {trials[k][2]}' for k in ks),text=True,capture_output=True,check=True);assert int(p.stderr)==len(ks);return [int(k) for k in p.stdout.split() if find(decode(trials[int(k)][2]))['example']]
        with ThreadPoolExecutor(8) as pool:positive={trials[k][:2] for ks in pool.map(test,[range(j,min(j+500,len(trials))) for j in range(0,len(trials),500)]) for k in ks}
    eligible={i for i in graphs if (i,None) not in positive};truth={(i,e) for i,e in positive if i in eligible};near={(i,e) for i in eligible for e in candidates[i]};calls={(i,e) for i in eligible for e in pred.get(i,[])};tcore={i for i,e in truth};ccore={i for i,e in calls};out=dict(layer=len(graphs),training_profiles=ref,eligible=len(eligible),safe=sum(i in eligible and e is not None for i,e,_ in trials),actual_links=len(truth),actual_cores=len(tcore),marked_cores=len(ccore),true_marked_cores=len(ccore&tcore),endpoint_links=len(near),true_endpoint_links=len(near&truth),predicted_links=len(calls),true_predicted_links=len(calls&truth),hits=sorted(calls&truth),actual=sorted(truth),predictions=sorted(calls));print({k:v for k,v in out.items() if k not in ('actual','predictions','hits')},flush=True);(D.parent/'ramsey_contact_overlap_transfer.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
