"""Labelled proof candidates compose relationally, unlike sparse selection."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
X={'x0':(Q(1),Q(2),Q(0),Q(0)),'x1':(Q(0),Q(1),Q(1),Q(1))}
Y={'y0':(Q(0),Q(0),Q(1),Q(2)),'y1':(Q(1),Q(1),Q(0),Q(1))}
z=(Q(0),Q(1),Q(0),Q(0))
add=lambda *ps:tuple(sum((p[i] for p in ps),Q(0)) for i in range(4))
labelled={(i,j):add(x,y) for i,x in X.items() for j,y in Y.items()}
assert len(labelled)==4 and len(set(labelled.values()))==3
assert labelled['x0','y0']==labelled['x1','y1']
sparse=min(labelled.items(),key=lambda kv:(sum(v>0 for v in kv[1]),kv[1]))
assert sparse[0]==('x1','y0')
# Keeping all four candidates is closed under postcomposition (Minkowski
# sum). Collapsing equal packet values loses distinct provider/path labels.
left={((i,j),'z'):add(p,z) for (i,j),p in labelled.items()}
right={(i,(j,'z')):add(X[i],Y[j],z) for i,j in product(X,Y)}
assert len(left)==len(right)==4 and set(left.values())==set(right.values())
assert set(left)!=set(right)
# Explicit associator on LABEL TREES preserves root names and packet tips;
# it is a bijection, not an identity of actual execution histories.
assoc={((i,j),'z'):(i,(j,'z')) for i,j in product(X,Y)}
assert len(set(assoc.values()))==4 and all(left[k]==right[v] for k,v in assoc.items())
# A literal set of proof vectors keeps only 3 elements and is too coarse for
# the fine replay that distinguishes the two routes to (1,2,1,2).
report={'passed':True,'labelled_pair_candidates':len(labelled),'distinct_packet_candidates':len(set(labelled.values())),'sparse_global_label':list(sparse[0]),'three_input_left_right_candidate_count':4,'packet_sets_associative':True,'label_tree_associator_bijective':True,'fine_replay_not_preserved_by_packet_set':True,'scope':'Finite frozen candidate sets on same irredundant source, coefficient-one addition and tagged primitive row labels. Formal associator not real history equivalence or analytic authority.'}
out=Path(__file__).resolve().parents[1]/'results/set-valued-farkas-composition.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
