"""Frozen 42706 contact fingerprint. Predict first; only the scorer runs the exact search."""
import gzip,json,tempfile,subprocess
from pathlib import Path
from itertools import combinations
from ramsey_intact27_joint_five import CAT,D,find,decode

TRAIN=42706
# Frozen using only the training contact. Counts concern all old cliques, not a proposed row.
SIGNATURE=(40,118)
def predict(a):
    I=[0]
    for j,v in enumerate(a):I += [q|1<<j for q in I if not q&v]
    cols={}
    for k in (7,6):
        qs=[q for q in I if q.bit_count()==k];cols[k]=[sum(1<<j for j,q in enumerate(qs) if q>>i&1) for i in range(27)]
    safe=[(i,j) for i,j in combinations(range(27),2) if not a[i]&(a[j]|1<<j)];return safe,[e for e in safe if tuple((c[e[0]]&c[e[1]]).bit_count() for c in cols.values())==SIGNATURE]

def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);pred={};trials=[]
    for i,line in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        b=line.strip()
        if sum(b[1:].translate(w))!=86:continue
        s=b.decode();es,pred[i]=predict(decode(s));trials.append((i,None,s))
        for u,v in es:
            bit=v*(v-1)//2+u;j=1+bit//6;trials.append((i,(u,v),s[:j]+chr(63+((ord(s[j])-63)^(1<<(5-bit%6))))+s[j+1:]))
    assert pred[TRAIN]==[(16,24)]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'pack.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_intact27_seven_pack.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input='\n'.join(f'{k} {s}' for k,(_,_,s) in enumerate(trials)),text=True,capture_output=True,check=True);assert int(p.stderr)==len(trials)
    true=set()
    for k in map(int,p.stdout.split()):
        i,e,s=trials[k];r=find(decode(s));
        if r['example']:true.add((i,e))
    held={i for i in pred if i!=TRAIN and (i,None) not in true};actual={(i,e) for i,e in true if i in held};called={(i,e) for i in held for e in pred[i]};truth={i for i,e in actual};calls={i for i,e in called};out=dict(signature=SIGNATURE,held=len(held),safe_edges=sum(i in held and e is not None for i,e,_ in trials),actual=sorted(actual),predicted=sorted(called),core_tp=len(truth&calls),core_fp=len(calls-truth),core_fn=len(truth-calls),core_tn=len(held-truth-calls),correct_links=sorted(actual&called));print(out);(D.parent/'ramsey_contact_signature_transfer.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
