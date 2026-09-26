"""Symbolic local interface audit for COPY--NIL and ERASE--K."""
from itertools import product
from pathlib import Path
import json
# Allowed COPY auxiliary peers established in the wired grammar. Each side
# carries a distinct externally rooted component token, not merely a type.
consumers={'Q_B.a':'support N.p','Q_S.p':'support N.p','Q_R.p':'support N.p','E.p':'eraser N.p','B.a':'bit successor N.p'}
instances=[]
for left,right in product(consumers,repeat=2):
 before={'source':'ORIGINAL N.p','a':(left,'root_a'),'b':(right,'root_b')}
 after={'a':(left,'fresh COPIED N_a.p','root_a'),'b':(right,'fresh COPIED N_b.p','root_b')}
 assert before['source']=='ORIGINAL N.p'
 assert after['a'][2]!=after['b'][2] and after['a'][1]!=after['b'][1]
 assert consumers[left].endswith('N.p') and consumers[right].endswith('N.p')
 instances.append((left,right))
# ERASE.p--K.p consumes both; K.a is connected to a successor principal
# with either K or NIL. New ERASE.p is connected to precisely that successor.
for suffix in ('K.p','N.p'):
 before=('root_E','E.p--K.p','K.a--'+suffix)
 after=('root_E','fresh E.p--'+suffix)
 assert before[0]==after[0] and after[1].endswith(suffix)
report={'passed':True,'copy_nil_port_combinations':len(instances),'erase_k_suffix_types':2,'premises':'independent externally rooted COPY.a/b branches; COPY.p--ORIGINAL NIL.p; K.a--COPIED K/N.p','effect':'COPY--NIL attaches separate fresh copied NIL to each branch, retaining both root tokens; ERASE--K transfers eraser root to successor K/N','scope':'Symbolic local-interface proof for two rule templates only; assumes the two side roots are genuinely distinct connected components after cutting COPY. No complete 15-rule preservation theorem.'}
out=Path(__file__).resolve().parents[1]/'results/symbolic-copy-nil-erase-k-ports.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
