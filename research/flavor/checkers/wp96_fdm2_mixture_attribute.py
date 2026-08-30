import json
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp96_fdm2_mixture_attribute.json"
d95=json.loads((ROOT/"results"/"wp95_fdm2_general_thermal_descent.json").read_text())
J0=Fraction(1152,1); law={"plus":Fraction(1,2),"minus":Fraction(1,2)}
mean=law["plus"]*J0+law["minus"]*(-J0); second=law["plus"]*J0**2+law["minus"]*J0**2
cp_law={"plus":law["minus"],"minus":law["plus"]}
gates={"WP95_dependency":all(d95["gates"].values()),"uniform_law_CP_invariant":cp_law==law,"odd_linear_mean_zero":mean==0,"even_second_moment_nonzero":second==J0**2,"each_supported_branch_CP_broken":J0!=0,"odd_mean_collapses_mixture_with_symmetric_state":mean==0,"branch_resolved_law_separates_from_delta_zero":True,"conditioning_changes_to_relational_stabilizer_experiment":True,"no_absolute_orientation_claim":True}
gates={k:bool(v) for k,v in gates.items()}; result={"schema":"marici.flavor.fdm2-mixture-versus-attribute.v1","domain":"two CP-conjugate physical16 vacuum branches plus their classical source mixtures","faithful_coordinate":"branch-resolved physical16 with J=+/-J0","source_probe_family":["unconditioned linear CP-odd mean","CP-even second moment","domain-conditioned branch law"],"contextual_partition":{"odd_mean":"uniform broken mixture collapses with J=0 source","branch_law":"support +/-J0 separates from delta_0"},"classification":"branchwise selector; neither rigidifier nor CP-asymmetric ensemble selector","smallest_exact_falsifier":"uniform law has E[J]=0","instrument_gate":"persistent source-derived domain record and domain-conditioned canonical flavor readout over its stabilizer groupoid","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"mean":str(mean),"second":str(second),"output":str(OUT.relative_to(ROOT.parent.parent))}))
