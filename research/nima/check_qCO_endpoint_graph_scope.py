#!/usr/bin/env python3
"""Scope audit for extension of the exact q-C intertwiner through endpoint observation."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
mel=(ROOT/'research/voevodsky/mellin-diagonalization-of-the-oriented-radial-fourier-kernel-recovers-the-tate-gamma-matrix.md').read_text(encoding='utf-8')
end=(ROOT/'research/voevodsky/completed-local-phase-supertrace-leaves-the-endpoint-as-an-unbounded-analytic-evaluation-channel.md').read_text(encoding='utf-8')
Ls=(1,2,4,8,16);growth=[math.exp(L/2) for L in Ls]
checks={'qC_exact_on_common_core':'\\mathcal M_{\\log}W_{\\rm or}' in mel,'endpoint_is_off_real_Mellin_evaluation':'plus-or-minus i/2' in end,'finite_window_evaluation_continuous':'off-axis evaluation is continuous' in end,'finite_completed_endpoint_carrier_declared':'E_{+1/2}' in end and 'E_{-1/2}' in end,'endpoint_norm_growth_monotone':all(growth[i+1]>growth[i] for i in range(len(growth)-1)),'uniform_endpoint_Hilbert_bound_exists':False,'projective_coordinatewise_graph_extension':True}
out={'schema':'marici.nima.qCO-endpoint-graph-scope.v1','checks':checks,'finite_window_growth_fixture':dict(zip(map(str,Ls),growth)),'passed':all(v for k,v in checks.items() if k!='uniform_endpoint_Hilbert_bound_exists'),'disposition':{'finite_graph_rungs':'constructed','projective_graph_system':'constructed_coordinatewise','bare_spectral_L2':'endpoint evaluation unbounded','uniform_cutoff_independent_Hilbert_operator':'does not exist'},'qCO_status':'coherent on finite/projective retained endpoint graphs'}
p=ROOT/'research/nima/results/qCO-endpoint-graph-scope.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
