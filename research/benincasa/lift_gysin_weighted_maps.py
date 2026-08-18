"""Lift the rational weighted-crossing matrices and apply the mu_2 trace."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from sympy.polys.domains import ZZ
from sympy.polys.modulargcd import _integer_rational_reconstruction as rr
P=2305843009213693951
def q(x):
 z=rr(int(x)%P,P,ZZ)
 if z is None:raise ValueError(x)
 return str(Fraction(int(z.numerator),int(z.denominator)))
def lift(x):return [lift(z) for z in x] if isinstance(x,list) else q(x)
def twice(x):return [twice(z) for z in x] if isinstance(x,list) else str(2*Fraction(x))
def main():
 p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
 d=json.loads(a.source.read_text());u=next(x for x in d['charts'] if x['chart']=='u_chart');eps=[]
 for z in u['strict_transforms']:
  raw=lift(z['augmented_corner_map_mod_p'])
  eps.append({'divisor':z['divisor'],'orientation':1 if z['divisor']=='D2' else -1,
   'strict_L1_kernel_basis':lift(z['strict_L1_kernel_basis_mod_p']),
   'homogeneous_resonance_map':lift(z['homogeneous_resonance_map_mod_p']),
   'augmented_corner_map_before_trace':raw,'unnormalized_mu2_trace_map':twice(raw),
   'augmented_source_order':['kernel_1','kernel_2','principal']})
 a.output.write_text(json.dumps({'schema':'marici.gm.exact_weighted_corner_maps.v1','field':'Q',
  'mu2_character':'even','frame_transition':'diag(1,1,s^-4,s^-2)',
  'target':'full nonresonant exceptional extension-coordinate object','extension_coordinate_order':['00','01','10','11'],
  'endpoints':eps},indent=2))
if __name__=='__main__':main()
