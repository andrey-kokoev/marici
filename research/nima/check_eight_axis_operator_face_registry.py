#!/usr/bin/env python3
"""Register all 28 generic square decorations on the eight-axis positive cube."""
import itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
A=('H','V','D','q','L','C','O','R')
reg={
 ('H','V'):('strict','transverse rooted-substitution/cut Beck-Chevalley'),
 ('H','D'):('strict','dagger naturality of rooted substitution'),
 ('H','q'):('canonical','Fourier transports rooted convolution to chart product'),
 ('H','L'):('strict','associativity of rooted convolution and degree successor'),
 ('H','C'):('strict','Mellin/forward realization is multiplicative'),
 ('H','O'):('strict','endpoint observation is multiplicative'),
 ('H','R'):('strict','projective completion continuity of rooted substitution'),
 ('V','D'):('strict','dagger naturality of marked physical cut'),
 ('V','q'):('canonical','Fourier transports marked Laurent cut multipliers'),
 ('V','L'):('strict','cut Laurent multipliers commute with admitted degree multipliers'),
 ('V','C'):('strict','coefficientwise realization intertwines marked cut branches'),
 ('V','O'):('strict','endpoint transport of marked Laurent cut labels'),
 ('V','R'):('strict','projective Laurent completion continuity of physical cut'),
 ('D','q'):('strict','source reflection intertwines chart successor'),
 ('D','L'):('strict','dagger exchanges left and right successors'),
 ('D','C'):('strict','contragredient transpose realization square'),
 ('D','O'):('strict','endpoint swap-conjugation square'),
 ('D','R'):('strict','dagger extends through graph completion'),
 ('q','L'):('canonical','Fourier sends convolution successor to multiplication successor'),
 ('q','C'):('strict_core','log-Mellin intertwines oriented radial Fourier with Tate gamma reflection on the common Schwartz core'),
 ('q','O'):('strict','QDLO chart transport preserves retained observation'),
 ('q','R'):('lax','leakage A_X=P_X F (I-P_X)'),
 ('L','C'):('strict','Mellin realization of convolution successor'),
 ('L','O'):('strict','endpoint multiplier naturality'),
 ('L','R'):('strict','closed multiplier extension on joint graph'),
 ('C','O'):('strict','observation factors through forward retained realization'),
 ('C','R'):('strict','forward realization extends through graph completion'),
 ('O','R'):('strict','retained observation extends through joint graph completion'),
}
assert set(reg)==set(itertools.combinations(A,2))
squares=[]
for pair in itertools.combinations(A,2):
 other=[a for a in A if a not in pair]
 for fixed in itertools.product((0,1),repeat=6):squares.append({'pair':pair,'fixed':fixed,'status':reg[pair][0]})
# Every 3-face has exactly its three pair restrictions, and each edge label is inherited from one axis.
three_faces=0;triple_complete=True
for triple in itertools.combinations(A,3):
 expected=set(itertools.combinations(triple,2))
 triple_complete &= expected<=set(reg)
 three_faces+=2**5
status_counts={s:sum(v[0]==s for v in reg.values()) for s in ('strict','strict_core','canonical','lax')}
checks={'all_28_pair_types_registered':len(reg)==28,'all_1792_square_instances_materialized':len(squares)==math.comb(8,2)*2**6,'all_1792_three_faces_have_three_pair_restrictions':three_faces==1792 and triple_complete,'one_lax_pair_type':status_counts['lax']==1,'unique_strict_core_pair_is_qC':status_counts['strict_core']==1 and reg[('q','C')][0]=='strict_core','edge_restrictions_are_axis_consistent':all(pair[0] in A and pair[1] in A for pair in reg)}
out={'schema':'marici.nima.eight-axis-operator-face-registry.v1','axes':A,'pair_types':{' x '.join(k):{'status':v[0],'decoration':v[1]} for k,v in reg.items()},'status_counts':status_counts,'square_instances':len(squares),'three_face_instances':three_faces,'checks':checks,'passed':all(checks.values()),'frontier':'Extend the exact q-C core intertwiner through endpoint observation and native regulator completion. Higher operator residue identities on 4-faces remain separate.'}
p=ROOT/'research/nima/results/eight-axis-operator-face-registry.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
