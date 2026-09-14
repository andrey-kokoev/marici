#!/usr/bin/env python3
"""Exact rank audit of scalar nullity plus the bulk-polar Green mate."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_scalar_green_mate_joint_kernel_certificate_20260908.json');args=p.parse_args();checks=0
 # Channels are (A,B,C,D). R0 is the completed scalar and M=R2+R3 is
 # the source-derived odd bulk-polar Green mate.
 obs=s.Matrix([[1,1,1,1],[1,-1,1,-1]])
 assert obs.rank()==2;checks+=1
 kernel=obs.nullspace();assert len(kernel)==2;checks+=1
 expected=[s.Matrix([1,0,-1,0]),s.Matrix([0,1,0,-1])]
 assert all(obs*v==s.zeros(2,1) for v in expected);checks+=2
 assert s.Matrix.hstack(*kernel).rank()==2;checks+=1
 # Each survivor cancels a bulk channel against its own polar channel.
 out={'schema':'marici.rh.scalar-green-mate-joint-kernel.v1','status':'two_hidden_channels_remain','checks':checks,'observer_matrix':[[1,1,1,1],[1,-1,1,-1]],'rank':2,'kernel_dimension':2,'kernel_basis':[[1,0,-1,0],[0,1,0,-1]],'claim':'completed scalar nullity together with vanishing of the odd bulk-polar Green mate does not reconstruct or annihilate the four-channel state','residual_interpretation':['direct bulk cancels its direct polar channel','reciprocal bulk cancels its reciprocal polar channel'],'next_requirement':'one additional source relation must couple the direct and reciprocal surviving channels; positivity of the radial form alone does not provide that relation'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'kernel_dimension':2}))
if __name__=='__main__':main()
