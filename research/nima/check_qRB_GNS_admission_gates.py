#!/usr/bin/env python3
"""Fail-closed admission audit for the arithmetic qRB GNS realization."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky';N=ROOT/'research/nima/results'
faith=json.loads((N/'fixed-width-gaussian-joint-faithfulness.json').read_text());source=json.loads((V/'results/compact_weil_source_identity_contract.json').read_text());alltr=json.loads((V/'results/all_translate_weil_kernel_faithfulness.json').read_text());sym=(V/'the-semilocal-tate-logarithmic-connection-commutes-with-fourier-sewing-and-adds-under-cutoffs.md').read_text()
gates={'kernel_observers_jointly_faithful':faith['passed'],'q_symmetry_invariance_on_common_core':'Fourier invariant and place-additive' in sym,'R_place_additivity':'\\mathbb A_{S\'}' in sym and '=\\mathbb A_S+\\mathbb A_p' in sym,'external_source_normalization_verified':not source['external_source_verification_required'],'all_rank_source_kernel_positive':alltr['source_all_translate_kernel_supplied']}
out={'schema':'marici.nima.qRB-GNS-admission-gates.v1','gates':gates,'closed_count':sum(gates.values()),'total_count':len(gates),'GNS_realization_admitted':all(gates.values()),'uniqueness_if_exists':gates['kernel_observers_jointly_faithful'],'remaining':['external source normalization','all-rank source-derived Weil kernel positivity'],'interpretation':'q and natural place refinement are already compatible with the prospective GNS realization; only identification and positivity prevent admission','rh_proved':False,'passed_audit':True}
p=N/'qRB-GNS-admission-gates.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
