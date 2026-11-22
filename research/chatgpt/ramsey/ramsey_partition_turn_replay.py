"""Finite online reader: permit backward use only of the incoming flag of the partition currently being exited, and only after the outgoing flag fires. No arbitrary history or target tour lookup."""
from itertools import permutations
from ramsey_folded_entry_handoff import X,P,D,json

def run():
    seed=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());E={''.join(e) for e in seed['arrows']};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        pair=[]
        for row,path in [('BRNN',(0,16,13,19,7,29)),('BNRN',(0,17,12,27,4,29))]:
            v=start=p[row.index('R')];events=[];prev=None
            for i,(x,y) in enumerate(zip(path,path[1:]),1):
                d=min(x,y);allowed={e for e in E if any(set(e)=={p[z-1] for z in X[k]} for k in P[d])};opts=[e for e in allowed if e[0]==v];assert len(opts)<=1;used=bool(opts)
                if used:
                    e,=opts;events.append((i,i,e));v=e[1]
                    if x>=15 and prev is not None and len(events)==1:
                        older=[e for e in prev if e[0]==v];assert len(older)<=1
                        if older:e,=older;events.append((i,i-1,e));v=e[1]
                prev=allowed if y>=15 and not used else None
                if v in {'C','D'}-{start}:break
            assert len(events)==2 and i==4;pair.append(dict(row=row,events=events,base=events[0][2][1],last_turn=path[2:5]))
        assert sorted([[e[1] for e in q['events']] for q in pair])==[[1,4],[4,3]];out.append(dict(binding=''.join(p),rows=pair))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_partition_turn_replay.json').write_text(json.dumps(out)+'\n')
