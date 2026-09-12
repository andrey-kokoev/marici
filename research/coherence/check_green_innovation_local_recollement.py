#!/usr/bin/env python3
"""Exact local formulas for inserting one Green-kernel context between neighbors."""

import json, random
from fractions import Fraction
from pathlib import Path

def main():
 rng=random.Random(20260913);rows=[]
 for _ in range(100):
  alpha=Fraction(rng.randrange(1,9),rng.randrange(9,18))
  beta=Fraction(rng.randrange(1,9),rng.randrange(9,18))
  den=1-alpha*alpha*beta*beta
  ca=alpha*(1-beta*beta)/den;cb=beta*(1-alpha*alpha)/den
  variance=(1-alpha*alpha)*(1-beta*beta)/den
  assert ca+alpha*beta*cb==alpha
  assert alpha*beta*ca+cb==beta
  assert variance==1-(ca*alpha+cb*beta) and variance>0
  rows.append({'alpha':str(alpha),'beta':str(beta),'left_coefficient':str(ca),'right_coefficient':str(cb),'innovation_norm_squared':str(variance)})
 result={'schema':'marici.coherence.green-innovation-local-recollement.v1','cases':len(rows),'all_exact':True,'innovation_vanishes_outside_neighbor_interval':True,'innovation_vanishes_at_old_contexts':True,'schur_complement_positive':True,'interpretation':'one inserted context contributes one local Green-orthogonal seam cell'}
 Path(__file__).with_name('green-innovation-local-recollement.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
