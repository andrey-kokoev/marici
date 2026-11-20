"""Compare residue accumulation with successive folded-square shortcuts. A shortcut removes two visits and flips the literal exit row."""
from ramsey_strip_matching_restart import tracks
from ramsey_strip_prism_proof import labels,rep,E
from ramsey_strip_shortcut_row_exit import paths,phase,rows
from collections import deque
fold=lambda p:tuple(labels[rep(v)] for v in p[1:-1])
target=fold((0,16,13,19,7,29));print('target',target,'exists in length census',target in paths)
for i in (2,3,5):
 start=fold(tracks[i-1]);Q=deque([(start,[])]);seen={start};hits=[];term=[]
 while Q:
    w,h=Q.popleft()
    if len(w)==len(target):
        term.append((w,h));
        if w==target:hits.append(h)
        continue
    for k in range(len(w)-3):
        if tuple(sorted((w[k],w[k+3]))) not in E:continue
        nxt=w[:k+1]+w[k+3:];assert nxt in paths and phase(paths[nxt]['path'],rows)!=phase(paths[w]['path'],rows)
        if nxt not in seen:seen.add(nxt);Q.append((nxt,h+[k]))
 print('track',i,'target shortcut chains',hits,'four-visit reductions',[(w,h,phase(paths[w]['path'],rows)) for w,h in term]);assert not hits
assert phase(paths[target]['path'],rows)==1
