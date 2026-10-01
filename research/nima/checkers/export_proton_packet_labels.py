"""Export actual endpoint-label pairs of the existing construction, without weights."""
from fractions import Fraction
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import mm,transpose

root=Path(__file__).resolve().parents[1]
source=root/'results/twelve-triangle-positive-geometry.json'
data=json.loads(source.read_text())
rows=sorted(data['triangles_and_transports'],key=lambda r:r['outer_arrow'])
rotations={r['outer_arrow']:tuple(tuple(Fraction(x) for x in row) for row in r['rotation']) for r in rows}
axes='xyz'
pairs=[]
for g in rotations:
    for a in axes:
        for b in axes:
            pairs.append((f'input-{g}-{a}',f'selected-{g}-{b}'))
assert len(pairs)==108
for g,R in rotations.items():
    for h,S in rotations.items():
        transport=mm(S,transpose(R))
        for a in range(3):
            for b in range(3):
                if transport[b][a]:
                    pairs.append((f'selected-{g}-{axes[a]}',f'aligned-{h}-{axes[b]}'))
assert len(pairs)==540
for g in rotations:
    for h in rotations:
        for a in axes:
            for b in axes:
                pairs.append((f'aligned-{g}-{a}',f'input-{h}-{b}'))
assert len(pairs)==len(set(pairs))==1836
assert len({p for pair in pairs for p in pair})==108

def save(name,pairs):
    (root/'results'/name).write_text('[\n'+',\n'.join(f'  ({a}, {b})' for a,b in pairs)+'\n]\n',encoding='utf-8')
save('proton-like-1836-label-pairs.txt',pairs)
surface=[]
for face,cycle in [('ABC','ABC'),('ABD','ADB'),('ACD','ACD'),('BCD','BDC')]:
    for a,b in zip(cycle,cycle[1:]+cycle[:1]):
        f='F_'+face
        surface.extend(((f,a),(a,b),(b,f)))
assert len(surface)==len(set(surface))==36
save('proton-like-36-surface-label-pairs.txt',surface)
print('Exported 1836 stage-labelled pairs and 36 surface-labelled pairs; exact counts and uniqueness checked.')
