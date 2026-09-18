#!/usr/bin/env python3
"""Fresh headless closure run for all top-level amplitude replication suites."""
import json,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
checkers=['check_abhy_four_point_foundational_benchmark.py','check_abhy_biadjoint_replication_suite.py','check_abhy_associahedron_replication_suite.py','check_abhy_scattering_form_projectivity_suite.py','check_exhaustive_double_partial_biadjoint_factorization.py','check_four_point_one_loop_mhv_integrand.py','check_four_point_one_loop_mhv_dlog_identity.py','check_arbitrary_n_one_loop_mhv_kermit_covariance.py','check_one_loop_mhv_kermit_pole_census.py','check_one_loop_mhv_kermit_cyclic_invariance.py','check_one_loop_mhv_kermit_reflection_invariance.py','check_one_loop_mhv_replication_suite.py','check_momentum_twistor_nmhv_replication_suite.py','check_momentum_twistor_covariance_suite.py','check_nmhv_generic_kinematics_suite.py','check_nmhv_dihedral_replication_suite.py','check_nmhv_spurious_boundary_replication_suite.py','check_nmhv_physical_boundary_replication_suite.py','check_nmhv_bcfw_boundary_count_formula.py','check_nmhv_bcfw_oriented_boundary_cancellation.py','check_irl_amplitudes_replication_manifest.py','check_irl_amplitudes_replication_provenance.py']
rows=[];passed=True
for name in checkers:
 start=time.monotonic();p=subprocess.run([sys.executable,str(ROOT/'research/nima'/name)],cwd=ROOT,text=True,capture_output=True,timeout=120);elapsed=time.monotonic()-start;ok=p.returncode==0;passed &= ok
 rows.append({'checker':f'research/nima/{name}','returncode':p.returncode,'elapsed_seconds':round(elapsed,3),'passed':ok,'stdout_tail':p.stdout[-500:]})
out={'schema':'marici.nima.irl-amplitudes-replication-closure.v1','checker_count':len(rows),'per_checker_timeout_seconds':120,'checks':rows,'all_checkers_passed':passed,'passed':passed}
p=ROOT/'research/nima/results/irl-amplitudes-replication-closure.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':passed,'checker_count':len(rows),'total_elapsed_seconds':round(sum(r['elapsed_seconds'] for r in rows),3),'failures':[r['checker'] for r in rows if not r['passed']]},indent=2));raise SystemExit(0 if passed else 1)
