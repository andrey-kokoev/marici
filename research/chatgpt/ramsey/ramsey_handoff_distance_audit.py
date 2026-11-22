"""Color-free control: ordered apex visits vs shortest forward separation. Enumerate cyclic native tours from the retained source arrows only; no strip matcher, selected-tour table or graph score imported."""
from pathlib import Path
from itertools import permutations
import json
D=Path(__file__).resolve().parent

def run():
    seed=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());edges=list(map(tuple,seed['arrows']));faces=[set(zip(f,f[1:])) for f in seed['retained_face_cycles']];out=[]
    for w in permutations(edges):
        if w[0]!=min(edges) or any(a[1]!=b[0] for a,b in zip(w,w[1:]+w[:1])):continue
        verts=[e[0] for e in w];v=[verts[i] for i in range(6) if set((w+w)[i:i+3])==faces[0] and set((w+w)[i+3:i+6])==faces[1]];base,=v
        distances={(a+b):(verts.index(b)-verts.index(a))%6 for a,b in [('C','D'),('D','C')]};out.append(dict(word=[''.join(e) for e in w],seam=base,forward_distance=distances))
    assert len(out)==2 and {row['seam']:row['forward_distance'] for row in out}=={'A':{'CD':2,'DC':4},'B':{'CD':4,'DC':2}}
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_handoff_distance_audit.json').write_text(json.dumps(out)+'\n')
