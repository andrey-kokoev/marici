#!/usr/bin/env python3
"""Materialize the five-axis cube and audit sourced pairwise coherence faces."""
import json,itertools,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
axes=('H_input_arity','V_output_arity','D_polarity','q_chart_successor','L_convolution_degree')
vertices=list(itertools.product((0,1),repeat=5))
edges=[]
for v in vertices:
 for i,a in enumerate(axes):
  if v[i]==0:
   w=list(v);w[i]=1;edges.append({'from':list(v),'to':w,'axis':a})
pair_status={
 ('H_input_arity','V_output_arity'):'constructed_strict_transverse_Beck-Chevalley',
 ('H_input_arity','D_polarity'):'constructed_dagger_naturality_on_minimal_generated_carriers',
 ('V_output_arity','D_polarity'):'constructed_dagger_naturality_on_minimal_generated_carriers',
 ('D_polarity','q_chart_successor'):'constructed_successor-polarity_interchange_on_minimal_generated_carriers',
 ('D_polarity','L_convolution_degree'):'constructed_left-right_successor_dagger_interchange',
 ('q_chart_successor','L_convolution_degree'):'constructed_in_canonical_Pontryagin_chart_model; historical_chart_identification_conditional',
 ('H_input_arity','L_convolution_degree'):'rooted-substitution_compatibility_expected; consolidated_typed_square_missing',
 ('V_output_arity','L_convolution_degree'):'cut/coaction_compatibility_expected; consolidated_typed_square_missing',
 ('H_input_arity','q_chart_successor'):'historical_chart-to-arity_intertwiner_missing',
 ('V_output_arity','q_chart_successor'):'historical_chart-to-arity_intertwiner_missing',
}
squares=[]
for pair in itertools.combinations(axes,2):
 status=pair_status[pair]
 for fixed in itertools.product((0,1),repeat=3):squares.append({'axes':list(pair),'fixed_bits':list(fixed),'status':status})
def gray(i):return i^(i>>1)
gray_cycle=[tuple((gray(i)>>j)&1 for j in reversed(range(5))) for i in range(32)]
def ham(a,b):return sum(x!=y for x,y in zip(a,b))
constructed=lambda s:s.startswith('constructed')
checks={'vertex_count_32':len(vertices)==32,'edge_count_80':len(edges)==80,'square_count_80':len(squares)==80,'maximal_ordered_5_simplices_120':math.factorial(5)==120,'cyclic_gray_code':all(ham(gray_cycle[i],gray_cycle[(i+1)%32])==1 for i in range(32)),'all_ten_pair_types_classified':len(pair_status)==10,'full_historical_five_cell_constructed':False}
out={'schema':'marici.nima.five-axis-successor-coherence-frontier.v1','axes':axes,'counts':{'vertices':32,'edges':80,'squares':80,'three_faces':40,'four_faces':10,'five_cells':1,'maximal_Freudenthal_5_simplices':120},'gray_cycle':[list(x) for x in gray_cycle],'pair_status':{' x '.join(k):v for k,v in pair_status.items()},'constructed_pair_types':sum(constructed(v) for v in pair_status.values()),'conditional_or_missing_pair_types':sum(not constructed(v) for v in pair_status.values()),'checks':checks,'passed':all(v for k,v in checks.items() if k!='full_historical_five_cell_constructed'),'frontier':'The canonical Tate/Pontryagin model has the q-L distributive face. A historical five-cell additionally needs chart-to-arity intertwiners and consolidated H-L/V-L naturality squares.'}
p=ROOT/'research/nima/results/five-axis-successor-coherence-frontier.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'counts':out['counts'],'pair_status':out['pair_status'],'checks':checks,'passed':out['passed'],'frontier':out['frontier']},indent=2));raise SystemExit(0 if out['passed'] else 1)
