#!/usr/bin/env python3
"""Distinguish the homogeneous radial identity from the full affine system."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(src))
g=h['g'];X,s,K,Q=g['X'],g['s'],h['K'],h['Q'];mul,sc,add=h['mul'],h['sc'],h['add'];L=h['L'];fx=sc(mul(X,K),F(-3,5));fy=sc(mul(s,K),F(-3,5));actual=add(L(fx,0,1),L(fy,1,1));target=sc(mul(mul(K,K),Q),3);res=add(actual,sc(target,-1));out={'schema':'marici.benincasa.cosmology-rees-affine-radial-falsifier.v1','candidate':'f1=-(3/5)K(X,s)','full_affine_exact_match':not res,'nonzero_residual_term_count':len(res),'first_residual_terms':[[list(k),str(v)] for k,v in sorted(res.items())[:12]],'homogeneous_leading_symbol_match':True};R=HERE.parents[1]/'results';(R/'cosmology_rees_affine_radial_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
