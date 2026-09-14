"""Match qg2 endpoint/conductor coordinates to the labelled cyclic Leray edge."""
import json
import sympy as s
xi,k=s.symbols('xi k',nonzero=True);v=2*(xi+1)/(1-k)
edge=s.factor(s.diff(s.log(v/(v-2)),xi));candidate=s.factor(1/(xi+1)-1/(xi+k))
assert s.simplify(edge-candidate)==0
assert s.simplify(v.subs(xi,-1))==0 and s.simplify(v.subs(xi,-k)-2)==0
assert s.simplify(s.residue(edge,xi,-1)-1)==0 and s.simplify(s.residue(edge,xi,-k)+1)==0
out={'schema':'marici.nima.qg2-occurrence-leray-descent.v1','status':'occurrence_labelled_log_edge_identified',
'coordinate_change':'v=2(xi+1)/(1-kappa)','endpoint_map':'xi=-1 -> v=0','conductor_map':'xi=-kappa -> v=2',
'pulled_log_connection':'dlog((xi+1)/(xi+kappa))','residue_vector_endpoint_conductor':[1,-1],
'labelled_edge':'G31_to_G12 cyclic Leray-frame transition','cocycle_provenance':'source frames n12,n23,n31 with transition product one',
'consequence':'the odd endpoint-conductor road class descends with a fixed cyclic occurrence label',
'boundary':'equality with the independently defined raw physical Cech defect remains open'}
open('research/nima/results/qg2-occurrence-leray-descent.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
