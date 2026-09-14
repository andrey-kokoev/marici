#!/usr/bin/env python3
"""Falsify literal unsigned-region overlap representation using source kernel signs."""
import json
from pathlib import Path

def main():
 src=json.loads((Path(__file__).parents[1]/'results'/'equal_spacing_toeplitz_rank_ladder.json').read_text());k=src['kernel_values']
 negative_kernel=[{'lag':m,'value':x} for m,x in enumerate(k) if x<0]
 increments=[2*k[m]-k[m-1]-k[m+1] for m in range(1,len(k)-1)]
 negative_increment=[{'lag':m+1,'value':x} for m,x in enumerate(increments) if x<0]
 assert negative_kernel and negative_increment
 result={'schema':'marici.voevodsky.unsigned-mesh-incidence-source-kernel-no-go.v1','sigma':src['sigma'],'spacing':src['spacing'],'negative_kernel_pairings':negative_kernel,'negative_increment_pairings':negative_increment,'unsigned_overlap_rule':'<Phi(D),Phi(E)>=sum_(alpha in D intersection E)c_alpha >=0','literal_unsigned_region_map_possible':False,'conclusion':'The source kernel and its primitive-increment Gram have negative off-diagonal pairings, so they cannot equal unsigned positive region-overlap charges.','surviving_repair':'Use oriented or phase-labelled incidence amplitudes Phi(D)_alpha=s_D(alpha)sqrt(c_alpha); positive cell weights then coexist with signed cross-pairings.'}
 out=Path(__file__).parents[1]/'results'/'unsigned_mesh_incidence_source_kernel_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'negative_kernel_lags':len(negative_kernel),'negative_increment_lags':len(negative_increment)},indent=2))
if __name__=='__main__':main()
