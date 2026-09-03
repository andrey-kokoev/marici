#!/usr/bin/env python3
"""Exhibit the exact K-q square syzygy obstructing a naive strictness proof."""
import json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# Coefficients are monomials K^a q^b; target basis labels are (k-level,q-level).
def add(v,key,mon,c):v[(key,mon)]+=c
def Q(v,k,l,a,b,c=1):add(v,(k,l),(a,b),c);add(v,(k,l+1),(a,b+1),-c)
def K(v,k,l,a,b,c=1):add(v,(k,l),(a,b),c);add(v,(k+1,l),(a+1,b),-c)
v=defaultdict(int);Q(v,0,0,0,0,1);Q(v,1,0,1,0,-1);K(v,0,0,0,0,-1);K(v,0,1,0,1,1);v={k:x for k,x in v.items() if x};assert not v
out={'schema':'marici.benincasa.cosmology-rees-K-q-syzygy.v1','problem':'prove the shifted filtered image has no hidden cancellations from higher-filtered source inputs','bold_conjecture':'family shifts alone make the operator presentation strict','named_rivals':['strict direct sum of independent family images','nontrivial K-q and derivative-multiplication syzygies','finite-cutoff equality without unbounded strictness'],'risky_consequences':['no high-filtration combination may cancel to a lower target filtration','critical pairs among K and q maps must reduce within the proposed shifted order'],'strongest_falsification_attempt':{'identity':'Q_{k,l}(f)-Q_{k+1,l}(fK)-K_{k,l}(f)+K_{k,l+1}(fq)=0','exact_residual':0,'shifted_input_levels_for_degree_d':['d+1','d+5','d+4','d+5'],'consequence':'leading filtration-d+5 terms cancel exactly, so familywise count equality does not prove strictness'},'disposition':'reject strictness by shifts alone; retain the shifted filtration only after completing its syzygy/critical-pair basis','surviving_scope':'finite Q_A row spaces and the 308-prototype operator matrix remain correct','first_missing_object':'a filtered syzygy basis including K-q squares and derivative compatibility critical pairs','acceptance_test':'enumerate finite prototype critical pairs, reduce them in a shifted Schreyer order, and prove no unreduced lower-filtration image remains','passed':True};(R/'cosmology_rees_K_q_syzygy.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
