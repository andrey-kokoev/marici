"""Forward screen of the entire 86-edge predecessor layer: add one triangle-safe link, then synthesize five rows."""
import tempfile,subprocess,gzip,json
from pathlib import Path
from itertools import combinations
from ramsey_intact27_joint_five import find,check,decode,CAT,D


def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);src={i:l.rstrip().decode() for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')) if sum(l.rstrip()[1:].translate(w))==86}; trials=[]
    for i,s in src.items():
        a=decode(s);trials.append((i,None,s))
        for u,v in combinations(range(27),2):
            if a[u]&a[v] or a[u]>>v&1:continue
            t=v*(v-1)//2+u;pos=1+t//6;word=s[:pos]+chr(63+((ord(s[pos])-63)^(1<<(5-t%6))))+s[pos+1:];trials.append((i,(u,v),word))
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'pack.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_intact27_seven_pack.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input='\n'.join(f'{k} {s}' for k,(_,_,s) in enumerate(trials)),capture_output=True,text=True,check=True);assert int(p.stderr)==len(trials)
    passed={};example=None
    for k in map(int,p.stdout.split()):
        i,e,s=trials[k];r=find(decode(s));
        if r['example']:passed[i,e]=r['example']
    gains=[(i,e) for i,e in passed if e and (i,None) not in passed];
    for i,e in gains:
        a=decode(src[i]);rs=passed[i,e];I=[0]
        for j,n in enumerate(a):I.extend([q|1<<j for q in I if not q&n])
        bad=[q for q in I if q.bit_count()+sum(not q&s for s in rs)>8];assert bad and all(all(q>>j&1 for j in e) for q in bad);old_four=next((j for j in range(5) if all(q.bit_count()+sum(not q&s for h,s in enumerate(rs) if h!=j)<=8 for q in I)),None)
        if old_four is None:continue
        def labels(s):return [j for j in range(27) if s>>j&1]
        example=dict(record=i,new_edge=e,supports=list(map(labels,rs)),added_port=old_four,number_of_blockers=len(bad),common_sites=sorted(set.intersection(*(set(labels(q)) for q in bad))),blockers=list(map(labels,bad)),predicted_edges=[(u,v) for u,v in combinations(labels(__import__('functools').reduce(int.__and__,bad)),2) if not a[u]&a[v] and not any(s>>u&1 and s>>v&1 for s in rs)]);break
    out=dict(input_records=len(src),links_tested=len(trials)-len(src),initial_five=sum(e is None for i,e in passed),gain_repairs=len(gains),gain_records=len({i for i,e in gains}),example=example);print(out);(D.parent/'ramsey_single_contact_gain.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
