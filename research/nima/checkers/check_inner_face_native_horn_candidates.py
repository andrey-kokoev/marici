"""Exhaust all incidence-level horns using existing cone vertices/faces.
Geometric horn incidence is not an extracted native path-coherence request.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from check_inner_face_tetrahedron_candidate import faces,vol
from check_twelve_triangle_positive_geometry import POINTS,mean,LABELS
ROOT=Path(__file__).resolve().parents[1]

def main():
    src=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())
    points=dict(POINTS);points['O']=(F(0),)*3
    for f in combinations(LABELS,3):points['F_'+''.join(f)]=mean([POINTS[k] for k in f])
    cells={frozenset(('O',*r['triangle'])) for r in src['triangles_and_transports']}
    available=set(faces(cells));target=frozenset(('O','A','B'))
    # Ordered source arrow selects its internal triangle by a declared incidence
    # adapter. Orientation reversal selects the same un-oriented shared face.
    assert {frozenset(('O',*r['outer_arrow'])) for r in src['triangles_and_transports']}=={
        frozenset(('O',a,b)) for a,b in combinations(LABELS,2)}
    rows=[]
    for tup in combinations(sorted(points),4):
        c=frozenset(tup);boundary={frozenset(f) for f in combinations(tup,3)}
        known=boundary&available
        if len(known)<3:continue
        volume=vol(c,points)
        kind='existing_cell' if c in cells else ('degenerate' if volume==0 else 'coarse_union')
        constituent_count=0
        if kind=='coarse_union':
            corners=c-{'O'};assert len(corners)==3 and corners<=set(LABELS)
            centre='F_'+''.join(sorted(corners))
            constituents={frozenset(('O',centre,a,b)) for a,b in combinations(sorted(corners),2)}
            assert constituents<=cells
            assert sum(vol(t,points) for t in constituents)==volume==F(2,3)
            constituent_count=len(constituents)
            # Outer apex face is exactly partitioned by its centroid; common O
            # cones have disjoint interiors, so the volume equality is a union,
            # not evidence for an added independent cell.
        rows.append(dict(vertices=list(tup),known_faces=len(known),volume=str(volume),
                         classification=kind,contains_selected_face=target<=c,
                         constituent_count=constituent_count))
    counts=Counter(r['classification'] for r in rows)
    assert counts=={'existing_cell':12,'coarse_union':4,'degenerate':4}
    selected=[r for r in rows if r['contains_selected_face']]
    assert Counter(r['classification'] for r in selected)=={'existing_cell':2,'coarse_union':2}
    assert {tuple(r['vertices']) for r in selected if r['classification']=='coarse_union'}=={('A','B','C','O'),('A','B','D','O')}
    assert not any(0<F(r['volume'])<F(2,9) for r in rows)
    result=dict(schema='marici.nima.inner-face-native-horn-candidates.v1',status='pass',
        source_vertices=len(points),candidate_four_vertex_sets=126,
        at_least_three_faces_available=dict(counts),selected_face=sorted(target),
        selected_face_candidates=selected,strictly_smaller_positive_candidate=False,
        interpretation='No fresh vertex or face was supplied. Horn-shaped candidates recover old cells, coarsen three old cells, or are spatially degenerate.',
        native_boundary='Cells.build completes a supplied path-coherence horn; the geometric source has not provided an interpretation of these incidence faces as that horn. Successful geometric enumeration is not a native admission proof.',
        candidates=rows)
    (ROOT/'results/inner-face-native-horn-candidates.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='candidates'},indent=2))

if __name__=='__main__':main()
