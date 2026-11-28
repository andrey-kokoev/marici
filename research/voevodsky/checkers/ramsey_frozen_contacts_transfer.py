"""Transfer the frozen degree/contact test to a second known-positive and random same-layer controls. Isomorphism is used only on the final outputs."""
from ramsey_forward_rigid_seven import CAT,D,decode,budgets,check,json,gzip,combinations
from ramsey_retention_slice import check
from pathlib import Path
import random,subprocess,tempfile
from collections import Counter

def bits(s):return [i for i in range(27) if s>>i&1]
def build(exe,a):
    zs=[i for i,v in enumerate(a) if v.bit_count()==7];lines=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,[z]+a)) for z in zs),text=True,capture_output=True,check=True).stdout.splitlines();st=Counter(sites=len(zs),interfaces=len(lines));rows=[]
    for line in lines:
        z,e,f,H=map(int,line.split());b=[n&~(1<<z) for n in a];b[z]=0;pair=[bits(e),bits(f)]
        for i,j in pair:b[i]|=1<<j;b[j]|=1<<i
        out=[j for j in range(27) if j!=z and H>>j&1==0];lists=budgets(b,out,H);st['removal_lists']+=len(lists)
        for rm in lists:
            g=b[:]
            for i,j in rm:g[i]^=1<<j;g[j]^=1<<i
            if check(g,((1<<27)-1)^(1<<z),3,8):rows.append(dict(z=z,add=pair,remove=rm,h=H,graph=g));st['legal']+=1
    return st,rows

def audit():
    w=bytes([(j-63).bit_count() if 63<=j<=126 else 0 for j in range(256)]);known=236272;G={};layer=[]
    for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        s=l.strip();e=sum(s[1:].translate(w));
        if e==91:layer.append(i);G[i]=s
        if i==262402:G[i]=s
    sample=sorted(random.Random(4355).sample([i for i in layer if i!=known],48));raw={}
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'frozen.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_frozen_contacts.rs')),'-o',str(exe)],check=True)
        for i in [262402,known]+sample:raw[i]=build(exe,decode(G[i].decode()))
    from ramsey_cube_retention_floor import G as endpoint,induced,iso
    target=induced(endpoint,[i for i in range(34) if not endpoint[34]>>i&1]);reports=[]
    for i,(st,rows) in raw.items():
        for r in rows:r['cube']=iso(induced(r.pop('graph'),[j for j in range(27) if j!=r['z']]),target) is not None;st['cube']+=r['cube']
        reports.append(dict(record=i,counts=st,witnesses=rows))
    assert raw[262402][0]['removal_lists']==105 and raw[262402][0]['cube']==1 and raw[known][0]['cube']>0;control=sum((raw[i][0] for i in sample),Counter());print('known',raw[known][0],[(r['z'],r['add'],r['cube']) for r in raw[known][1]],'controls',control,'nonempty',sum(bool(raw[i][1]) for i in sample));(D.parent/'ramsey_frozen_contacts_transfer.json').write_text(json.dumps(dict(seed=4355,layer_size=len(layer),sample=sample,control_totals=control,records=reports),indent=2)+'\n')
if __name__=='__main__':audit()
