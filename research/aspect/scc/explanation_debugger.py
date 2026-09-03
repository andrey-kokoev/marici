"""First-missing-arrow, minimal-obstruction, and comparison-budget tooling."""
from fractions import Fraction

CHAINS={
 "identity_from_equivalence":["weak_equivalence_class","localization","univalent_completion"],
 "observational_equivalence":["weak_equivalence_class","localization","univalent_completion","record_ontology","detector_map","physical_interface","descent_authority","observational_quotient"],
 "strict_selected_filler":["filler_family","selection_map","selection_invariance","strict_selection"],
 "cross_sector_composition":["sector_vertices","overlap_incidence","sector_edge"],
 "bounded_completeness":["horn_boundaries","horn_fillers","coverage_bound","bounded_completeness_predicate"],
}

DOWNSTREAM={
 "weak_equivalence_class":["localization","univalent_completion","observational_quotient"],
 "localization":["univalent_completion","observational_quotient"],
 "univalent_completion":["identity_from_equivalence"],
 "record_ontology":["observational_quotient","physical_backend"],
 "detector_map":["observational_quotient","physical_backend"],
 "physical_interface":["observational_quotient","physical_backend"],
 "descent_authority":["observational_quotient","physical_backend"],
 "selection_map":["strict_selection"],"selection_invariance":["strict_selection"],
 "overlap_incidence":["sector_edge","cross_sector_composition"],
 "horn_fillers":["bounded_completeness"],"coverage_bound":["bounded_completeness"],
}


def debug_explanation(contract):
    claim=contract.get("target_claim")
    if claim not in CHAINS:return {"schema":"marici.scc.explanation-debug.v1","passed":False,"reason":"unknown target claim"}
    supplied=contract.get("supplied",{})
    missing=[item for item in CHAINS[claim] if not supplied.get(item)]
    first=missing[0] if missing else None
    retracted=[]
    if first:
        queue=[first];seen=set()
        while queue:
            x=queue.pop(0)
            for y in DOWNSTREAM.get(x,[]):
                if y not in seen:seen.add(y);queue.append(y)
        retracted=sorted(seen)
    return {"schema":"marici.scc.explanation-debug.v1","passed":not missing,
            "target_claim":claim,"first_missing_arrow":first,
            "minimal_obstruction":[first] if first else [],"all_missing":missing,
            "retract_downstream":retracted,
            "acceptance_test":None if not first else f"supply and verify {first}",
            "claim_boundary":"dependency diagnosis; does not synthesize missing authority"}


def propagate_comparison_budget(contract):
    try:margin=Fraction(str(contract["initial_margin"]))
    except (KeyError,ValueError,ZeroDivisionError):
        return {"schema":"marici.scc.comparison-budget.v1","passed":False,"first_failed_gate":"initial_margin"}
    if margin<=0:return {"schema":"marici.scc.comparison-budget.v1","passed":False,"first_failed_gate":"initial_margin"}
    trace=[];remaining=margin
    for i,square in enumerate(contract.get("squares",[])):
        if not square.get("type") in ("completion_observation","coherence_positivity","localization"):
            return {"schema":"marici.scc.comparison-budget.v1","passed":False,"first_failed_gate":"square_type","index":i}
        if square.get("direction") not in ("exact","upper"):
            return {"schema":"marici.scc.comparison-budget.v1","passed":False,"first_failed_gate":"bound_direction","index":i}
        try:cost=Fraction(str(square["cost"]))
        except (KeyError,ValueError,ZeroDivisionError):
            return {"schema":"marici.scc.comparison-budget.v1","passed":False,"first_failed_gate":"square_cost","index":i}
        if cost<0:return {"schema":"marici.scc.comparison-budget.v1","passed":False,"first_failed_gate":"square_cost","index":i}
        before=remaining;remaining-=cost
        trace.append({"index":i,"type":square["type"],"direction":square["direction"],
                      "before":str(before),"cost":str(cost),"after":str(remaining)})
        if remaining<=0:
            return {"schema":"marici.scc.comparison-budget.v1","passed":False,"first_failed_gate":"margin",
                    "first_exhausted_square":i,"trace":trace,"residual_margin":str(remaining)}
    return {"schema":"marici.scc.comparison-budget.v1","passed":True,"first_failed_gate":None,
            "trace":trace,"residual_margin":str(remaining),"strict_margin_survives":True}
