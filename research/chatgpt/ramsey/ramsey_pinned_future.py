"""Exact finite-horizon equivalence of marked traversal histories and explicit size-indistinguishable covers."""
from pathlib import Path
import json
from collections import Counter,deque
D=Path(__file__).parent;load=lambda p:json.loads(p.read_text());tri=load(D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json')['triangles_and_transports'];T={x['outer_arrow']:x['triangle'] for x in tri};E=sorted(T);N=len(E);cuts=[0,3,10,13,20,23,30];seam={'AB','BA'};Q=[(e,last) for e in E for last in 'FS'];start=('AB','F');F={e:next(k for k,t in T.items() if t[0]==T[e][0] and k[0]==e[1]) for e in E};move=lambda e,w:F[e] if w=='F' else e[::-1]
def go(q,w,guard):return None if guard and q[1]==w=='S' else (move(q[0],w),w)
def run(guard,obs):
    sense=lambda q: q[0] if obs=='sector' else q[0] in seam if obs=='seam' else 0
    parts={30:dict.fromkeys(Q,0)}
    for i in reversed(range(30)):
        lookup={};p={}
        for q in Q:
            key=tuple(None if (v:=go(q,w,guard)) is None else (sense(v) if i+1 in cuts else None,parts[i+1][v]) for w in 'FS');p[q]=lookup.setdefault(key,len(lookup))
        parts[i]=p
    histories=Counter({start:1});rows=[]
    for i in range(31):
        if i in cuts:rows.append(dict(tick=i,words=histories.total(),sites=len({q[0] for q in histories}),arrival_states=len(histories),future_classes=len({parts[i][q] for q in histories}),all_state_classes=len(set(parts[i].values()))))
        h=Counter()
        for q,k in histories.items():
            for w in 'FS':
                if (v:=go(q,w,guard)) is not None:h[v]+=k
        histories=h
    return rows
# Lift S on AB by +1 and its reciprocal by -1; other steps preserve sheet. Find admissible walk returning to same arrival state one sheet up; a base word is valid on every sheet.
def shift(e,w):return int(w=='S')*((e=='AB')-(e=='BA'))
def lift_word():
    todo=deque([(start,0,'')]);seen={(start,0)}
    while todo:
        q,h,s=todo.popleft()
        for w in 'FS':
            if (v:=go(q,w,True)) is None:continue
            k=h+shift(q[0],w)
            if v==start and k==1:return s+w
            if -2<=k<=2 and (v,k) not in seen:seen.add((v,k));todo.append((v,k,s+w))
word=lift_word();assert word;out={str((g,o)):run(g,o) for g in (False,True) for o in ('legal','seam','sector')};assert out[str((True,'sector'))][-1]['arrival_states']==24
r=dict(cuts=cuts,unit_sheet_walk=word,runs=out);print(word);print([(o,[r['future_classes'] for r in run(True,o)]) for o in ('legal','seam','sector')]);print(run(True,'seam'));(D/'ramsey_pinned_future.json').write_text(json.dumps(r,indent=2)+'\n')
