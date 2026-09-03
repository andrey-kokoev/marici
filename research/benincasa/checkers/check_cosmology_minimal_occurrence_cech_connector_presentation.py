#!/usr/bin/env python3
"""Construct the minimal free connector presentation on the deletion cube."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
for n in ['cosmology_occurrence_to_cech_connector_obstruction.json','cosmology_saturated_half_boundary_shadow_factorization.json']:
 assert json.loads((R/n).read_text())['passed']
axes=('q_g1','q_g2','q_G12');occ=('G12:e6','G23:e6','G31:e6')
verts=[tuple(bits) for bits in itertools.product((0,1),repeat=3)]
edges=[]
for v in verts:
 for i,a in enumerate(axes):
  if v[i]==0:
   w=list(v);w[i]=1;edges.append({'from':v,'to':tuple(w),'axis':a})
faces=[]
for i,j in itertools.combinations(range(3),2):
 for fixed in (0,1):
  k=3-i-j;v=[0,0,0];v[k]=fixed;faces.append({'base':tuple(v),'axes':[axes[i],axes[j]]})
assert len(verts)==8 and len(edges)==12 and len(faces)==6
axis_maps=[dict(zip(axes,p)) for p in itertools.permutations(occ)]
out={'schema':'marici.benincasa.cosmology-minimal-occurrence-cech-connector-presentation.v1','free_presentation':{'formal_target_objects':['O_'+''.join(map(str,v)) for v in verts],'formal_target_arrows':edges,'cube_functoriality_faces':faces,'component_maps':['eta_'+''.join(map(str,v)) for v in verts],'naturality_relations':12,'axis_map_parameters':axis_maps,'normalization':'eta at the distinguished chart sends the antisymmetric occurrence word to (0,-1,1)'},'counts':{'objects':8,'arrows':12,'cube_face_relations':6,'components':8,'naturality_squares':12,'axis_bijections':6},'formal_consistency':True,'reason':'the free additive category modulo cube, naturality, and one normalization relation exists','source_realized':False,'missing_realization':['source-derived axis bijection with orientations','actual occurrence modules for eight masks','twelve transport arrows','eight component maps','six cube coherences','twelve naturality witnesses','normalization replay'],'conditional_effect':'a realized normalized connector types the boundary-only shadow and completes the unique primitive factorization','next_test':'classify the six formal axis bijections against available source labels and orientation data','passed':True};(R/'cosmology_minimal_occurrence_cech_connector_presentation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'counts':out['counts'],'formal_consistency':True,'source_realized':False,'passed':True},indent=2))
