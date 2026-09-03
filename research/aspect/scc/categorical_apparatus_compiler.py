"""Voevodsky-compatible categorical intermediate representation for SCC."""
LAYERS=("base_computad","cells_and_laws","partial_completion","filler_and_selection",
        "certificate_transfer","sector_overlap","typed_horn_tower","bounded_completeness")
PROFILE=("base_incidence","declared_cells","completion","relative_filler","strict_selection",
         "certificate_backend","sector_vertex","sector_edge","horn_coverage","physical_backend")


def fail(gate, reason, **evidence):
    return {"schema":"marici.scc.categorical-apparatus.v1","passed":False,
            "first_failed_gate":gate,"reason":reason,"evidence":evidence}


def compile_categorical_apparatus(c):
    layers=c.get("layers",{})
    unknown=set(layers)-set(LAYERS)
    if unknown:return fail("layer_manifest","unknown layers",unknown=sorted(unknown))
    normalized={name:layers.get(name,{"status":"not_constructed"}) for name in LAYERS}
    for name,spec in normalized.items():
        if spec.get("status") not in ("constructed","not_constructed"):
            return fail("layer_manifest","layer status must be constructed or not_constructed",layer=name)
        if spec["status"]=="constructed" and not spec.get("artifact_locator"):
            return fail("artifact_locator","constructed layer lacks artifact locator",layer=name)
        for dep in spec.get("depends_on",[]):
            if dep not in LAYERS or LAYERS.index(dep)>=LAYERS.index(name):
                return fail("dependency_dag","dependency is unknown or non-prior",layer=name,dependency=dep)
            if normalized[dep].get("status")!="constructed":
                return fail("dependency_dag","constructed layer depends on unconstructed layer",layer=name,dependency=dep)
    ports=c.get("ports",{})
    loc=ports.get("localization")
    if loc and not (loc.get("weak_equivalence_class_locator") and loc.get("universal_inversion_verified")):
        return fail("localization","localization needs source weak equivalences and universal inversion")
    completion=ports.get("univalent_completion")
    if completion and not loc:return fail("univalent_completion","completion requires a typed localization port")
    if completion and not (completion.get("presentation") and completion.get("equivalences_as_identity_paths_verified")):
        return fail("univalent_completion","completion needs presentation and identity-path verification")
    observation=ports.get("observational_quotient")
    if observation:
        req=("record_ontology","detector_map","physical_interface","descent_authority")
        missing=[x for x in req if not observation.get(x)]
        if missing:return fail("observational_quotient","physical quotient lacks source objects",missing=missing)
    filler=c.get("filler")
    if filler and filler.get("exists") and filler.get("selected"):
        if not (filler.get("selection_map") and filler.get("selection_invariance_verified")):
            return fail("strict_selection","filler existence does not define invariant selection")
    horns=c.get("horn_coverage",[])
    for horn in horns:
        if not all(k in horn for k in ("dimension","boundary_locator","filler_type","coverage_bound")):
            return fail("horn_coverage","horn lacks dimension, boundary, filler type, or bound")
        if int(horn["dimension"])<1 or int(horn["coverage_bound"])<int(horn["dimension"]):
            return fail("horn_coverage","invalid bounded horn declaration",horn=horn)
    if normalized["bounded_completeness"]["status"]=="constructed" and not c.get("bounded_completeness_predicate"):
        return fail("bounded_completeness","completeness requires an explicit bounded predicate")
    p=c.get("conformance",{})
    profile={key:p.get(key,"not_constructed") for key in PROFILE}
    if any(v not in (True,False,"not_constructed") for v in profile.values()):
        return fail("conformance_profile","profile coordinates are independent booleans or not_constructed")
    if profile["physical_backend"] is True and not observation:
        return fail("physical_backend","physical backend requires observational quotient port")
    return {"schema":"marici.scc.categorical-apparatus.v1","passed":True,"first_failed_gate":None,
            "layer_order":list(LAYERS),"layers":normalized,"conformance":profile,
            "ports":{"localization":loc or "not_constructed",
                     "univalent_completion":completion or "not_constructed",
                     "observational_quotient":observation or "not_constructed"},
            "filler_selection":filler or "not_constructed","horn_coverage":horns,
            "claim_boundary":"bounded profile; no scalar completeness or physical promotion"}
