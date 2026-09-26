from copy import deepcopy
from sequenced_set import SequencedSet
from pipeline_canonical import key
from forest_canonical import canonical
from pathlib import Path
import json
net=SequencedSet((1,0),[('member',0),('member',1)]);net.execute()
assert tuple(net.answer(o) for o in net.outputs)==(True,False)
before=deepcopy(net.__dict__);key(net);assert before==net.__dict__
swap=deepcopy(net);a,b=[o+'.p' for o in net.outputs];x,y=swap.wires[a],swap.wires[b]
swap.wires[a]=y;swap.wires[y]=a;swap.wires[b]=x;swap.wires[x]=b
assert canonical(net)==canonical(swap)
assert key(net,False)!=key(swap,False) and key(net)!=key(swap)
renamed=deepcopy(net)
mapping={n:(n if n=='RET' else net.kind(n)+'_'+str(9000+i)) for i,n in enumerate(reversed(list(net.types)))}
def port(p):
 n,q=p.split('.');return mapping[n]+'.'+q
renamed.types={mapping[n]:ps for n,ps in net.types.items()}
renamed.wires={port(p):port(q) for p,q in net.wires.items()}
renamed.stage={mapping[n]:t for n,t in net.stage.items()}
renamed.outputs=[mapping[n] for n in net.outputs]
assert key(net)==key(renamed) and key(net,False)==key(renamed,False)
report={'passed':True,'controls':['old key merges swapped unequal answers','new key distinguishes ordered answers','alpha renaming preserves both modes','key leaves graph metadata unchanged'],'scope':'Forest encoding with output identity; proof key includes stage declarations, observation key deliberately forgets stages.'}
out=Path(__file__).resolve().parents[1]/'results/pipeline-canonical.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
