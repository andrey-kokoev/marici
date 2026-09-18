#!/usr/bin/env python3
"""Exact real celestial momentum-conserving family at every finite multiplicity."""
from fractions import Fraction
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
def family(n):
 z=[Fraction(i,1) for i in range(1,n+1)];w=[]
 for i in range(n):
  den=Fraction(1)
  for j in range(n):
   if i!=j:den*=z[i]-z[j]
  w.append(1/den)
 moments=[sum(w[i]*z[i]**k for i in range(n)) for k in range(3)]
 # p_i = eta_i E_i [[1,z],[z,z^2]], eta=sign(w), E=abs(w)
 return {'n':n,'z':[str(x) for x in z],'signed_omega':[str(x) for x in w],'incoming_legs':sum(x<0 for x in w),'outgoing_legs':sum(x>0 for x in w),'all_energies_positive_after_orientation':all(abs(x)>0 for x in w),'real_slice':True,'momentum_moments':[str(x) for x in moments],'momentum_conserved':moments==[0,0,0]}
rows=[family(n) for n in range(4,16)]
checks={'every_family_exactly_momentum_conserving':all(r['momentum_conserved'] for r in rows),'real_celestial_slice':all(r['real_slice'] for r in rows),'positive_oriented_energies':all(r['all_energies_positive_after_orientation'] for r in rows),'both_incoming_and_outgoing':all(r['incoming_legs']>0 and r['outgoing_legs']>0 for r in rows)}
out={'schema':'marici.nima.arbitrary-n-real-celestial-kinematics.v1','construction':'Choose distinct real z_i and signed omega_i=1/product_(j!=i)(z_i-z_j). Set p_i=omega_i [[1,z_i],[z_i,z_i^2]].','identity':'sum_i omega_i z_i^k=0 for k=0,...,n-2 by barycentric interpolation; k=0,1,2 gives momentum conservation for n>=4.','orientation':'eta_i=sign(omega_i), E_i=abs(omega_i)>0 separates incoming and outgoing null generators.','rows':rows,'checks':checks,'passed':all(checks.values()),'conclusion':'Exact real celestial external-leg generators with positive oriented energies and momentum conservation exist at every finite multiplicity.','claim_boundary':'This constructs kinematics only. It supplies neither helicity/shear normalization nor a cluster-dependent Coherent-Resolution chain map.'};p=ROOT/'research/nima/results/arbitrary-n-real-celestial-kinematics.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'construction':out['construction'],'identity':out['identity'],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
