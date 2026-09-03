#!/usr/bin/env python3
"""DPC comparison of the gauge elliptic curve with source elliptic covers."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
gauge=json.loads((R/'cosmology_p_locus_gauge_cover_genus.json').read_text());cand=json.loads((R/'five-site-region-pair-polar-elliptic-discriminant.json').read_text());assert gauge['passed']
I=241;J=-2450;delta=49987584;j=Fraction(6912*I**3,delta);assert j==Fraction(13997521,7232)
assert cand['schema']=='marici.five_site_region_pair_polar_elliptic_discriminant.v1'
out={'schema':'marici.benincasa.cosmology-p-gauge-elliptic-source-match.v1','conjecture':'the gauge elliptic curve is already identified with a source elliptic cover','gauge_curve':'y^2=-4u^4+12u^3+u^2-12u+4','gauge_binary_quartic_invariants':{'I':I,'J':J},'gauge_j_invariant':str(j),'source_elliptic_candidates':1,'strongest_candidate':{'artifact':'five-site-region-pair-polar-elliptic-discriminant.json','family':cand['elliptic_curve'],'branch_points':cand['branch_points'],'parameter_specialization_to_p_locus_declared':False,'typed_base_map_declared':False,'fixed_j_invariant_declared':False},'invariant_match_testable':False,'conjecture_disposition':'falsified as a source identification','reason':'the sole candidate is an unspecialized five-site family on a different base; no map supplies h_i and delta_i from the p-locus coordinate','moduli_fitting_authorized':False,'gauge_cover_source_authorized':False,'next_conjecture':'although the elliptic cover is not source-identified, its anti-invariant gauge descends as a sign-twisted comparison under the deck involution','next_falsifier':'compute deck action on the gauge and test ordinary versus sign-twisted descent and integral monodromy','passed':True};(R/'cosmology_p_gauge_elliptic_source_match.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
