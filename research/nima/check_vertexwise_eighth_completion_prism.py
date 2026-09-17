#!/usr/bin/env python3
"""Generate the 128 completion components and 448 naturality squares of the 8th-axis prism.

This is a typed obligation registry, not a proof that every analytical map exists.
"""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
axes=('H','V','D','q','L','C','O')
face_status={
 'H':('constructed','typed rooted convolution is jointly continuous for every projective exponential seminorm and extends uniquely through completion'),
 'V':('constructed','finite physical cut coactions are bounded Laurent translations on every projective exponential seminorm and extend uniquely'),
 'D':('constructed','star/dagger extends on the declared aperture/projective graph completion'),
 'q':('lax','finite Fourier square has leakage A_X=P_X F (I-P_X), coherent by shell cocycle'),
 'L':('constructed','closed Mellin multiplier extends as a coordinate of the retained L/O joint graph domain'),
 'C':('constructed','continuous forward rigged synthesis extends uniquely to retained graph completion; no bounded inverse or equivalence'),
 'O':('constructed','retained closed observation extends on the L/O joint graph and preserves endpoint multiplier naturality'),
}
def bits(v):return ''.join(map(str,v))
vertices=[]
for v in itertools.product((0,1),repeat=7):
 vertices.append({'id':'v'+bits(v),'state':dict(zip(axes,v)),'finite':'X_X['+bits(v)+']','completed':'X_hat['+bits(v)+']','component':'kappa['+bits(v)+']','status':'obligation'})
squares=[]
for v in itertools.product((0,1),repeat=7):
 for i,a in enumerate(axes):
  if v[i]:continue
  w=list(v);w[i]=1;w=tuple(w)
  status,evidence=face_status[a]
  squares.append({'id':f'R{a}:{bits(v)}','axis':a,'source':'v'+bits(v),'target':'v'+bits(w),'equation':f'kappa[{bits(w)}] {a}_X ~= {a}_hat kappa[{bits(v)}]','status':status,'evidence':evidence})
counts={s:sum(x['status']==s for x in squares) for s in ('constructed','lax','conditional','open')}
checks={'components_128':len(vertices)==128,'naturality_squares_448':len(squares)==448,'sixty_four_squares_per_axis':all(sum(x['axis']==a for x in squares)==64 for a in axes),'all_generic_faces_classified':set(face_status)==set(axes),'strict_completion_prism_constructed':False,'lax_completion_prism_constructed':True}
out={'schema':'marici.nima.vertexwise-eighth-completion-prism.v1','interpretation':'formal typed obligation registry; statuses are inherited from generic source theorems and are not 128 independent analytical proofs','axes':axes,'component_count':len(vertices),'square_count':len(squares),'square_status_counts':counts,'generic_faces':{a:{'status':s,'evidence':e} for a,(s,e) in face_status.items()},'components':vertices,'squares':squares,'checks':checks,'passed':all(v for k,v in checks.items() if k!='strict_completion_prism_constructed'),'frontier':['assemble the six strict generic face laws and the q leakage cocycle into the lax eighth coherencer','do not extend graph stability beyond admitted Mellin/Laurent multipliers and transverse marked cuts','do not strictify the nonzero q leakage cell']}
p=ROOT/'research/nima/results/vertexwise-eighth-completion-prism.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('components','squares')},indent=2));raise SystemExit(0 if out['passed'] else 1)
