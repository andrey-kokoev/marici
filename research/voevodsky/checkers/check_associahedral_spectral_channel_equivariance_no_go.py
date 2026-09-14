#!/usr/bin/env python3
"""Exact label-equivariance no-go for ordered spectral channels."""
import json
from pathlib import Path

def main():
 S=[[3,0],[0,1]];swapped=[[1,0],[0,3]]
 eig_S=(3,1);eig_swapped=(3,1)
 required_swap=(1,3)
 assert eig_swapped!=required_swap
 result={'schema':'marici.voevodsky.associahedral-spectral-channel-equivariance-no-go.v1','observation_square':S,'basis_exchanged_square':swapped,'ordered_eigenchannels_before':eig_S,'ordered_eigenchannels_after':eig_swapped,'assoc_channel_covariance_requires':required_swap,'equivariant_labeled_identification_exists_from_ordered_eigenvalues':False,'reason':'Conjugating by the basis swap leaves the ordered eigenvalue pair fixed, while cyclic quadrilateral relabelling exchanges X13 and X24.','surviving_object':'The unordered set {X13,X24} can match the spectrum, but it loses the channel labels and oriented incidence required by the positive geometry.','required_extra_data':'A source-derived eigenline/branch orientation that labels the two roots and transports by exchange; it must remain defined through degeneracies without using positivity.'}
 out=Path(__file__).parents[1]/'results'/'associahedral_spectral_channel_equivariance_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
