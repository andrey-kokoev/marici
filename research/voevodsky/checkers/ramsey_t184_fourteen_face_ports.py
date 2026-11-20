"""Freeze: T184 -> root, its four facet neighbors -> four plus ports, proper central faces -> four-bit face-containment rows. Assign plus to containment (also test its global complement). All four remaining roles may be reserved arbitrarily: test a necessary condition without fitting them."""
from pathlib import Path
from collections import Counter
import json,hashlib
H=Path(__file__).resolve().parents[1];D=H/'results';d=json.loads((D/'esd7_explicit_analytical_census.json').read_text());ts=d['tetrahedra'];C=next(t for t in ts if t['id']=='T184')['vertices'];u=set(C);nb=[]
for v in C:
    q=[t for t in ts if t['id']!='T184' and u-{v}<=set(t['vertices'])];assert len(q)==1;nb.append(set(q[0]['vertices']))
def sig(face):return sum(1<<j for j,s in enumerate(nb) if face<=s)
faces={m:sig({v for j,v in enumerate(C) if m>>j&1}) for m in range(1,15)};assert all(s==15^m for m,s in faces.items());target=set(faces.values());assert len(target)==14
outer=[{v['id']} for v in d['vertices'] if 7 in v['barycentric']];assert len(outer)==4 and all(sig(s)==0 for s in [u]+outer);assert all(len(s&t)==2 for j,s in enumerate(nb) for t in nb[j+1:])
def case(E,r):
    P=sorted(j if i==r else i for i,j in E if r in (i,j));assert len(P)==4
    h=Counter(sum(1<<j for j,p in enumerate(P) if tuple(sorted((p,v))) in E) for v in range(22) if v!=r and v not in P);return dict(ports=P,mask_histogram=h,proper_types=len(target&h.keys()),missing=sorted(target-h.keys()))
w=json.loads((D/'ramsey_37_root_glue.json').read_text())['witness'];example=case(set(map(tuple,w['plus_edges'])),0);hist=Counter();records=0
cat=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6'
for g in cat.read_text().splitlines():
    assert ord(g[0])-63==22;bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);E={(i,j) for j in range(22) for i in range(j) if bits[j*(j-1)//2+i]=='1'};records+=1
    for r in range(22):
        if sum(r in e for e in E)==4:hist[case(E,r)['proper_types']]+=1
# 13 of the 14 rows cost >=25 port incidences; each port has at most five + edges beyond the root.
required=min(sum(m.bit_count() for m in target-{omitted}) for omitted in target);assert required==25>4*(6-1);assert max(hist)<13
out=dict(face_masks=faces,marked_role_control='four parent vertices and T184 all have signature zero; distinguished labels needed',rooted_example=example,catalogue_graphs=records,degree_four_roots=sum(hist.values()),root_hist=dict(sorted(hist.items())),min_required_plus=required,available_plus_max=20,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(out);(D/'ramsey_t184_fourteen_face_ports.json').write_text(json.dumps(out,indent=2)+'\n')
