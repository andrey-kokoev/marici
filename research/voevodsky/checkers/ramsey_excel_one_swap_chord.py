from itertools import combinations
from pathlib import Path
import json
from hashlib import sha256

D=Path(__file__).resolve().parents[1]/'results';V=range(1,12)
rows=[s for s in combinations(V,3) if all(j-i>=2 for i,j in zip(s,s[1:]))];seeds={(1,5,10),(1,5,11),(1,6,9),(3,6,9)};chords=[e for e in combinations(V,2) if e[1]-e[0]>1];base={(i,i+1) for i in range(1,11)}

def run():
    front=seeds;records=[];chosen=[(2,5),(7,10)]
    for radius in range(3):
        graph_ok=[];probes={};row_ok=[]
        for ch in [None,*chords]:
            core=base|({ch} if ch else set());triangle=any(all(e in core for e in combinations(q,2)) for q in combinations(V,3));sixes=[set(q) for q in combinations(V,6) if all(e not in core for e in combinations(q,2))];hit=[s for s in sorted(front) if ch and set(ch)<=set(s)];bad=[s for s in sorted(front) if any(not set(s)&q for q in sixes)]
            if not hit:row_ok.append(ch)
            if not triangle and not hit and not bad:graph_ok.append(ch)
            if ch in chosen:probes[str(ch)]=dict(red_triangle_rows=hit,blue_seven_rows=bad)
        records.append(dict(radius=radius,rows=len(front),geometric_candidates=[e for e in row_ok if e],legal_chords=[e for e in graph_ok if e],path_admitted=None in graph_ok,probes=probes));front=front|{s for s in rows if any(sum(abs(a-b) for a,b in zip(s,t))==1 for t in front)}
    for z in records:print(z['radius'],z['rows'],len(z['legal_chords']),z['path_admitted'],z['probes']);
    # Post-selection diagnostic only: evaluate the actual third corner after the selector.
    ss=[(1,5,10),(1,5,11),(1,4,10),(1,6,9),(3,6,9)];wins=[]
    for ch in records[1]['legal_chords']:
        edges=base|{ch,(12,16),(13,16)}|{(x,12+i) for i,s in enumerate(ss) for x in s}
        if not any(all((e in edges)==color for e in combinations(q,2)) for n,color in [(3,True),(7,False)] for q in combinations(range(1,17),n)):wins.append(ch)
    records[1]['postcheck_chords_accepting_third_corner']=wins
    proto=D/'ramsey_excel_one_swap_chord_protocol.md';(D/'ramsey_excel_one_swap_chord.json').write_text(json.dumps(dict(protocol_sha=sha256(proto.read_bytes()).hexdigest(),seeds=sorted(seeds),results=records),indent=2)+'\n')
if __name__=='__main__':run()
