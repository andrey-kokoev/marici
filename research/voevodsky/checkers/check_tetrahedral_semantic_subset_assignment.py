#!/usr/bin/env python3
"""Check the role-level Boolean-subset assignment to the tower-cotower tetrahedron."""
import hashlib,json,platform
from itertools import permutations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/tetrahedral_semantic_subset_assignment.v1.json';OUT=ROOT/'research/voevodsky/results/tetrahedral_semantic_subset_assignment.json';D=json.loads(FIX.read_text())
atoms={x['id']:x for x in D['atoms']};edges=D['edges'];faces=D['faces'];bulk=D['bulk']
all_subsets=set(atoms)|set(edges)|set(faces)|{bulk['subset']}
expected={''.join(c for c in '1234' if mask&(1<<(int(c)-1))) for mask in range(1,16)}
schedules=[];flags=set()
for p in permutations('1234'):
 flag=tuple(''.join(sorted(p[:k])) for k in range(1,5));schedules.append(p);flags.add(flag)
face_coeff={faces[k]['cell']:faces[k]['coefficient'] for k in faces}
checks={'all_15_nonempty_subsets_assigned':all_subsets==expected,'four_distinct_endpoint_atoms':len(atoms)==4 and len({x['semantic'] for x in atoms.values()})==4,'variance_split_two_plus_two':sum(x['variance']=='positive' for x in atoms.values())==2 and sum(x['variance']=='negative' for x in atoms.values())==2,'six_edges_assigned':len(edges)==6,'four_faces_assigned':len(faces)==4,'opposite_principal_edges':edges['12']['cell']=='E12' and edges['34']['cell']=='E43' and edges['34']['orientation']=='4->3','oriented_boundary':face_coeff=={'F1':1,'F2':-1,'F3':1,'F4':-1} and bulk['boundary']=='F1-F2+F3-F4','all_24_schedules_give_distinct_maximal_flags':len(schedules)==len(flags)==24,'schedule_atoms_not_mistyped_as_mixed_dimension_roles':'not four freely commuting Marici operations' in D['schedule_semantics']}
out={'schema':'marici.voevodsky.tetrahedral-semantic-subset-assignment-check.v1','passed':all(checks.values()),'checks':checks,'observed':{'assigned_cells_by_dimension':[len(atoms),len(edges),len(faces),1],'complete_flags':len(flags),'first_flag':[''.join(sorted(schedules[0][:k])) for k in range(1,5)]},'disposition':'The subset-to-cell assignment is dimensionally coherent and corrects the prior mixed-dimension schedule labeling. Exact semantic maps remain absent.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_tetrahedral_semantic_subset_assignment.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
