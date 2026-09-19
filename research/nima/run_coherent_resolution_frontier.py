#!/usr/bin/env python3
"""Rebuild the admitted Coherent Resolution frontier in dependency order."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
R=Path(__file__).resolve().parents[2]
checks=[
'research/nima/checkers/check_n8_boundary_programme_manifest.py',
'research/nima/checkers/check_a3_weighted_local_system_code.py',
'research/figueiredo/checkers/check_coherent_resolution_maximal_free_flavor_presentation.py',
'research/nima/checkers/check_a3_flavor_weighted_integration.py',
'research/kitaev/checkers/check_coherent_resolution_twisted_css.py',
'research/nima/checkers/check_a3_mod2_transport_obstruction.py',
'research/nima/checkers/check_a3_weighted_formal_alignment.py',
'research/sontag/checkers/coherent_resolution_control_audit.py',
'research/nima/checkers/check_arbitrary_m_characteristic_inverse.py',
'research/nima/checkers/check_six_point_nmhv_bcj_chain_relation.py',
'research/nima/checkers/check_six_point_minimal_bcj_chain_repair.py',
'research/strominger/checkers/six_point_cr_bcj_enrichment_attempt.py',
'research/nima/checkers/check_six_point_cr_bcj_no_go_certificate.py',
'research/aspect/checkers/build_independent_g4_bordered_response_interface.py',
'research/nima/checkers/check_independent_g4_interface_population.py',
'research/nima/checkers/check_n8_exceptional_boundary_transition_refined_scc.py',
'research/voevodsky/checkers/check_first_zero_evans_complete_certificate.py',
'research/nima/checkers/check_rh_programme_frontier.py',
'research/nima/checkers/check_lean_polygon_diagonal_alignment.py',
'research/nima/checkers/check_arbitrary_m_facet_cochain_carrier.py',
'research/nima/checkers/check_arbitrary_n_history_to_facet_compiler.py',
'research/nima/checkers/check_arbitrary_m_codim2_facet_incidence.py',
'research/nima/checkers/check_coherent_resolution_programme_frontier.py']
rows=[];start=time.time()
for rel in checks:
 p=R/rel;t=time.time();q=subprocess.run([sys.executable,str(p)],cwd=R,capture_output=True,text=True)
 rows.append({'checker':rel,'returncode':q.returncode,'elapsed_seconds':round(time.time()-t,3),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'stderr_tail':q.stderr[-500:]})
 if q.returncode:
  print(q.stdout[-2000:]);print(q.stderr[-2000:],file=sys.stderr);break
out={'schema':'marici.nima.coherent-resolution-frontier-rebuild.v1','checker_count':len(rows),'expected_checker_count':len(checks),'all_pass':len(rows)==len(checks) and all(x['returncode']==0 for x in rows),'elapsed_seconds':round(time.time()-start,3),'checks':rows,'claim_boundary':'This rebuild proves reproducibility of the listed finite artifacts only; it does not strengthen their scientific claim boundaries.'}
p=R/'research/nima/results/coherent-resolution-frontier-rebuild.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checker_count':out['checker_count'],'all_pass':out['all_pass'],'elapsed_seconds':out['elapsed_seconds']},indent=2));raise SystemExit(0 if out['all_pass'] else 1)
