#!/usr/bin/env python3
"""Audit the A5-to-A6 quotient transition with an independent modular certificate."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];src=ROOT/'research/benincasa/checkers/check_cosmology_rees_relative_transition_kernel.py'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(src))
c=g['transition'](5,6,101);assert c['euler_check'] and c['source']==5 and c['target']==6
assert c['kernel_dim']==2036 and c['cokernel_dim']==3168 and c['image_rank']==7916
coh=json.loads((ROOT/'research/benincasa/results/cosmology_rees_ambient_transition_coherence.json').read_text());assert coh['strongest_falsification_attempt']['A5_to_A6']['preserved'] and coh['strongest_falsification_attempt']['ambient_six']['residual_nnz']==315
out={'schema':'marici.benincasa.cosmology-rees-a5-a6-transition-audit.v1','problem':'separate A5-to-A6 finite quotient persistence from global monicity','certificate_mod_101':c,'source_label_relation_preservation':True,'tau_p_A6_residual_nnz':315,'tau_p_nonzero_at_A6':True,'exact_residual':'modulo 101 the map has kernel dimension 2036, image rank 7916, and cokernel dimension 3168; tau_p nevertheless maps to a nonzero A6 class','disposition':'finite tau_p persistence retained; exact characteristic-zero kernel and cokernel remain uncomputed','rank_boundary':'modular rank is a lower bound on rational rank, so modular kernel 2036 is only an upper bound on the rational kernel','acceptance_test':'lift the modular kernel basis to rational source quotient coordinates and reduce exactly against A6 relations','passed':True};p=ROOT/'research/benincasa/results/cosmology_rees_a5_a6_transition_audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
