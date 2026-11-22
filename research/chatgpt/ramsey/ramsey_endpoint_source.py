"""See frozen protocol. Evaluate candidate colors, rather than reading target colors, against transported root incidences."""
from pathlib import Path
from itertools import combinations
import json
D=Path(__file__).parent;load=lambda s:json.loads((D/(s+'.json')).read_text());L={v%35 for t in (1,7,11,16) for v in (t,-t)};predict=lambda a,b:(b-a)%35 in L;U=sorted(set(range(1,35))-L);sig={v:{t for t in L if predict(v,t)} for v in U};E=[e for e in combinations(U,2) if sig[e[0]].isdisjoint(sig[e[1]])];idx={e:i for i,e in enumerate(E)};read=load('ramsey_nine_frame_readout');Q=read['readout'];word=sum(predict(a,b)<<i for i,(a,b) in enumerate(Q));cal=load('ramsey_sector_handed_bridge')['corner_by_probe_word'];corner=cal[str(word)];anti=next(int(k) for k,v in cal.items() if all(x!=y for x,y in zip(v,corner)));W=read['coordinate_ordered_wirings'];assert W[word]==sum(predict(a,b)<<i for i,(a,b) in enumerate(E));arc=[]
for turn in (1,-1):
    alive=list(range(8));changes=[]
    for k in range(1,35):
        b=k*turn%35
        for j in range(k):
            a=j*turn%35;e=tuple(sorted((a,b)));new=[s for s in alive if e not in idx or bool(W[s]>>idx[e]&1)==predict(a,b)];
            if new!=alive:changes.append(dict(k=k,pair=e,root_displacement=(b-a)%35,red=predict(a,b),survivors=new))
            alive=new
        if len(alive)==1:break
    assert alive==[word];arc.append(dict(direction=turn,changes=changes))
hist=load('ramsey_basepoint_identifiability')['compatible_binding_histories'];seam=load('ramsey_seam_replay_basepoint');assert len({r['mapped_stationary_endpoint'][-1] for r in hist})==2;out=dict(cyclic_word=word,corner=corner,antipodal_word=anti,arc=arc,history_controls=hist,recut_readings=seam['recut_control']['readings'],different_links=(W[word]^W[anti]).bit_count());print(out);(D/'ramsey_endpoint_source.json').write_text(json.dumps(out,indent=2)+'\n')
