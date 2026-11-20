"""Filter potential mixed eligibility collisions by depth-four invariants. A residual collision is NOT a counterexample."""
from ramsey_36_try_deck import data,unpack,Path,TemporaryDirectory,run,os
from collections import defaultdict

def audit():
    hosts=list(map(unpack,data(17).splitlines()))
    with TemporaryDirectory() as tmp:
        def compile(src):
            exe=Path(tmp)/(src+('.exe' if os.name=='nt' else ''));run(['rustc','-O',str(Path(__file__).with_name(src+'.rs')),'-o',str(exe)],check=True);return exe
        pair=compile('ramsey_36_three_filter');four=compile('ramsey_36_four_profile')
        # Orders 11..13 already separate at depth 3; orders >=13 need <=4 additions.
        for n in range(1,11):
            d=data(n);raw=d.splitlines();keys=run([str(pair)],input=d,capture_output=True,check=True).stdout.splitlines();assert len(keys)==len(raw)
            groups=defaultdict(list)
            for s,h in zip(raw,keys):groups[h].append(s)
            records=[];labels=[]
            for group in groups.values():
                if len(group)<2:continue
                tags=[any(h.subisomorphic_lad(unpack(s),induced=True) for h in hosts) for s in group]
                if any(tags) and not all(tags):records.extend(group);labels.extend(tags)
            keys=run([str(four)],input=b'\n'.join(records),capture_output=True,check=True).stdout.splitlines();assert len(keys)==len(records)
            residual=defaultdict(list)
            for key,s,t in zip(keys,records,labels):residual[key].append((s,t))
            mixed=[g for g in residual.values() if len(set(t for _,t in g))>1];print(n,len(raw),'mixed groups remaining',len(mixed),flush=True)
            if mixed:print('example candidates',mixed[0][:8],flush=True)
if __name__=='__main__':audit()
