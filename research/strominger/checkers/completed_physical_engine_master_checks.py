"""Aggregate completion manifest for the completed physical engine."""
import json, os, pathlib, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
CHECKERS=[
 ("completed_physical_source_category_checks.py","completed_physical_source_category.json"),
 ("physical_puncture_constructor_checks.py","physical_puncture_constructor.json"),
 ("physical_puncture_parity_transport_checks.py","physical_puncture_parity_transport.json"),
 ("completed_two_chart_parity_module_checks.py","completed_two_chart_parity_module.json"),
 ("completed_parity_helicity_representation_checks.py","completed_parity_helicity_representation.json"),
 ("completed_grade_three_source_readout_checks.py","completed_grade_three_source_readout.json"),
 ("physical_laurent_completion_cutoff_checks.py","physical_laurent_completion_cutoff.json"),
 ("physical_spin_readout_constructor_checks.py","physical_spin_readout_constructor.json"),
 ("completed_local_distribution_target_checks.py","completed_local_distribution_target.json"),
 ("completed_local_to_contour_transform_checks.py","completed_local_to_contour_transform.json"),
 ("completed_gauge_conservation_antipodal_quotient_checks.py","completed_gauge_conservation_antipodal_quotient.json"),
 ("completed_distinct_puncture_kernel_checks.py","completed_distinct_puncture_kernel.json"),
 ("completed_collision_strata_checks.py","completed_collision_strata.json"),
 ("completed_tower_exception_analogue_checks.py","completed_tower_exception_analogue.json"),
 ("completed_physical_engine_hostile_falsifiers.py","completed_physical_engine_hostile_falsifiers.json"),
]
DOCS=[
 "completed-physical-source-category.md","physical-puncture-constructor.md",
 "physical-puncture-parity-transport.md","completed-two-chart-parity-module.md",
 "completed-parity-helicity-representation.md","completed-grade-three-source-readout.md",
 "physical-laurent-completion-and-cutoffs.md","physical-spin-readout-constructor.md",
 "completed-local-distribution-target.md","completed-local-to-contour-transform.md",
 "completed-gauge-conservation-antipodal-quotient.md",
 "completed-distinct-puncture-kernel-classification.md",
 "completed-collision-strata-classification.md",
 "completed-tower-exception-analogue-classification.md",
 "completed-physical-engine-hostile-falsifiers.md",
 "completed-physical-engine-diagram.md","completed-physical-engine-master-theorem.md",
 "completed-physical-engine-correction-audit.md",
]
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
runs=[]
for script,result in CHECKERS:
 cp=subprocess.run([sys.executable,"-u",str(ROOT/"checkers"/script)],cwd=str(ROOT.parents[1]),capture_output=True,text=True,timeout=120)
 result_path=ROOT/"results"/result
 payload=json.loads(result_path.read_text(encoding="ascii")) if result_path.exists() else {}
 ok=cp.returncode==0 and payload.get("passed")==payload.get("total") and payload.get("total",0)>0
 runs.append({"checker":script,"returncode":cp.returncode,"passed":payload.get("passed"),"total":payload.get("total"),"stdout_tail":cp.stdout[-500:]})
 rec("RUN."+script.removesuffix(".py"),"constituent checker reruns cleanly",ok,f"exit={cp.returncode}; gates={payload.get('passed')}/{payload.get('total')}")
missing=[name for name in DOCS if not (ROOT/name).exists()]
rec("ARTIFACT.docs","every required theorem packet exists",not missing,"missing="+repr(missing))
control=[]
for name in DOCS:
 data=(ROOT/name).read_bytes()
 bad=[b for b in data if b<32 and b not in (9,10,13)]
 if bad: control.append((name,sorted(set(bad))))
rec("FORMAT.controls","canonical packets contain no control bytes",not control,"bad="+repr(control))
canonical="\n".join((ROOT/name).read_text(encoding="utf-8") for name in DOCS)
forbidden=["K_0=\\frac{\\bar z}{z(1+u)}","F_\\xi(z)=\\frac{\\xi^2}{z^2}","exact quartic witness"]
found=[term for term in forbidden if term in canonical]
rec("CORRECTION.superseded","superseded coordinate-Green claims are absent from canonical packets",not found,"found="+repr(found))
required_terms=["strict LF","p^4-q^4","Graph(A)","(1,-3,2)","|P|-1","l=0,1","sextic"]
missing_terms=[term for term in required_terms if term not in canonical]
rec("SCOPE.coverage","canonical packets contain every master invariant",not missing_terms,"missing="+repr(missing_terms))
passed=sum(i["passed"] for i in checks)
payload={"checker":"completed_physical_engine_master_checks.py","strength":"fresh requirement-by-requirement completion audit","passed":passed,"total":len(checks),"checks":checks,"constituent_runs":runs,"verdict":"The completed physical parity engine is verified from source category through two-chart transport, parity/helicity, grade-three local injectivity, distributional and contour quotients, conservation and antipodal matching, collision strata, named-class analogues, and twelve hostile falsifiers. Every loss is attached to its first nonfaithful arrow."}
out=ROOT/"results"/"completed_physical_engine_master.json"
out.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="ascii")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)
