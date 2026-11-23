"""Fixed support-preserving orientation. Score against the P step already specified by the ordered source window, not a step selected after seeing the wiring. Transport BOTH address and wiring for the advance control."""
from pathlib import Path
from collections import Counter
import json
D=Path(__file__).resolve().parents[1];r=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());W=r['wirings'];S=r['address_masks'];E=list(map(tuple,r['edge_order']));Q=60;c=(0,1,4,5,2,3,6);cm=lambda s:sum(1<<c[i] for i in range(7) if s>>i&1);idx=[S.index(cm(s)) for s in S];perm=[E.index(tuple(sorted((idx[i],idx[j])))) for i,j in E];C=lambda w:sum(((w>>i)&1)<<j for i,j in enumerate(perm));bind={3:'C0',5:'C1',2:'M0',4:'M1'}
def selected(i,w):
 a=S.index((1<<6)|(1<<i));z,=[S[b] for k,(u,v) in enumerate(E) if w>>k&1 and a in (u,v) for b in [v if u==a else u] if S[b].bit_count()==2 and not S[b]&~Q];return z
rows=[]
for w in W:
 s=selected(3,w);t=selected(5,C(w));assert t==cm(s);pair=lambda x:sorted(bind[i] for i in bind if x>>i&1);before=pair(s);after=pair(t);match=before==['C1','M0'];assert match==(after==['C0','M1']);rows.append(dict(wiring=w,before=before,after_in_original_names=after,matches_P_step=match))
print(Counter(tuple(x['before']) for x in rows));(D/'results/ramsey_red_p_face_pair.json').write_text(json.dumps(rows,indent=2)+'\n')
