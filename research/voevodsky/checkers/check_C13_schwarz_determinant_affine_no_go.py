#!/usr/bin/env python3
"""Exact degree obstruction to identifying affine C13 with a Schwarz determinant."""
import json
from pathlib import Path

def main():
 # On real Hermitian data (a,b,c), det=ac-b^2 has nonzero quadratic coefficients.
 determinant_coefficients={'a*c':1,'b^2':-1}
 affine_C13_coefficients={'1':'delta','a':'alpha','b':'beta','c':'gamma'}
 # Restricting b=0 still leaves ac, non-affine on a two-dimensional source.
 samples=[{'a':1,'b':0,'c':1,'det':1},{'a':2,'b':0,'c':1,'det':2},{'a':1,'b':0,'c':2,'det':2},{'a':2,'b':0,'c':2,'det':4}]
 # Mixed second difference is 1, but every affine function has zero mixed second difference.
 mixed=samples[3]['det']-samples[1]['det']-samples[2]['det']+samples[0]['det'];assert mixed==1
 result={'schema':'marici.voevodsky.C13-schwarz-determinant-affine-no-go.v1','schwarz_determinant':'a*c-|b|^2','schwarz_degree':2,'C13_positive_geometry_role':'affine source/support coordinate in X13+X24=C13','direct_affine_identification_exists':False,'mixed_second_difference_fixture':samples,'mixed_second_difference':mixed,'conclusion':'C13 cannot equal the universal Schwarz determinant through an affine source-coordinate identification on an open Gram-data domain.','surviving_options':['a nonlinear determinant-line lift','a source slice imposing relations that reduce the determinant to an affine coordinate','identify X13 and X24 with spectral/Schur pivots, which itself requires a separately sourced nonlinear map'],'warning':'Defining the new coordinate to be the determinant merely renames the positivity gate.'}
 out=Path(__file__).parents[1]/'results'/'C13_schwarz_determinant_affine_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
