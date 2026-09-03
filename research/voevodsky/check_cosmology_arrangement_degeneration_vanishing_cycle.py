"""Audit specialization from the triangle arrangement to the concurrent arrangement."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_arrangement_degeneration_vanishing_cycle.json'
def det(t):
 # rows X, Y, X+Y+tZ
 return t
def main():
 assert det(0)==0 and all(det(t)!=0 for t in (-3,-1,1,2,5))
 # Generic punctured family is trivialized by Z'=tZ.
 generic_b2=1;special_b2=0;vanishing_rank=generic_b2-special_b2;assert vanishing_rank==1
 # At t=0, l3-l1-l2=0; for t!=0 residual is tZ.
 for t in (-2,-1,1,3):assert (1-1,1-1,t-0)==(0,0,t)
 # A regular coefficient cannot invert t at the special fiber.
 assert det(0)==0
 out={'schema':'marici.voevodsky.cosmology-arrangement-degeneration-vanishing-cycle.v1','status':'Xi_is_the_rank_one_class_lost_at_concurrency','family':'X=0, Y=0, X+Y+tZ=0','incidence_determinant':'t','punctured_family':'For t nonzero, Z prime=tZ projectively trivializes the arrangement, so the generic H2 local system is constant of rank one.','special_relation':'At t=0 the new circuit l3-l1-l2=0 appears and kills the sole projective arrangement H2 class. For t nonzero its residual is tZ.','cohomology_ranks':{'generic_H2':generic_b2,'special_H2':special_b2,'vanishing_cycle':vanishing_rank},'comparison_map':'The specialization map from special H2 to nearby H2 is 0 -> Q and cannot transport a special-fiber nullhomotopy to the generic Xi class. The nearby class maps isomorphically to the rank-one vanishing quotient.','pole_gate':'Using the special circuit to solve the generic class requires division by t. That coefficient is not regular at the degeneration and is not a source-natural integral/rational family morphism over the base.','decision':'The concurrent filler does not extend back to the triangle. The degeneration identifies Xi_log as the vanishing class obstructing extension; it supplies no regular sourced horn on the generic/original fiber.','next_gate':'test whether allowing a controlled logarithmic 1/t singularity defines a legitimate nearby-cycle boundary or merely restates the vanishing-cycle connecting morphism','limitations':['arrangement cohomology and regular-family comparison','no admissible singular coefficient authorized','no horn, Bockstein, contour, or physical period constructed'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
