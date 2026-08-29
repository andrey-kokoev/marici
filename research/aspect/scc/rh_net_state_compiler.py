"""Compile the current RH programme as a typed partial interaction-net presentation."""
LENS_REQ={
 "additive":["common_fiber","bounded_residual"],
 "determinant":["operator_ideal","normalization_authority","counterterm_authority"],
 "ordered":["generator_domain","pathwise_integrability","composition","cocycle_residuals"],
}
HIGHER_COHERENCE={
 "typed_three_way_associator":[
  "overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean"],
 "left_unitor":[
  "overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean"],
 "right_unitor":[
  "overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean"],
 "four_input_pentagon_cocycle_coherence":["typed_three_way_associator"],
 "triangle_unit_associator_coherence":["typed_three_way_associator","left_unitor","right_unitor"],
 "completion_stable_frontier_coherence":[
  "four_input_pentagon_cocycle_coherence","triangle_unit_associator_coherence"],
 "common_nine_operation_graph_domain":[
  "completion_stable_frontier_coherence","tail_seam_hilbert_schmidt_coupling"],
}
COMPLETION_EVIDENCE=[
 "associator_continuity","left_unitor_continuity","right_unitor_continuity",
 "inverse_continuity","uniform_composite_path_control","pentagon_residual_zero",
 "triangle_residual_zero"]
COMPOSITE_CONTROL={
 "accepted_modes":["isometric_unitary","uniform_composite_path_bound"],
 "quantifies_over":["admitted_canonical_coherence_paths","cutoffs","constructor_depths"],
 "controls":["forward_composite_norm","inverse_composite_norm"],
 "generator_only_bound_admissible":False,
 "isometric_unitary_norm":1}
def fail(gate,reason,**evidence):return {"passed":False,"first_failed_gate":gate,"reason":reason,"evidence":evidence}
def output_type(cell):
    rules=(("overlap_","pairwise_comparison"),("associator","associator"),("unitor","unitor"),("pentagon","pentagon_witness"),("triangle","triangle_witness"),("completion_stable_frontier","completed_coherence"),("nine_operation","operation_domain"),("naturality","naturality_witness"),("sewing","sewing_witness"),("fourier_transport","completed_transport"),("determinant_line","determinant_line_witness"),("five_margin","coercivity_margin_packet"),("spectral_identification","spectral_identification"),("critical_line","critical_line_exclusion"),("riemann_hypothesis","proposition"),("type_fiber_adams","adams_cell"),("endpoint_operator","endpoint_cell"),("archimedean_determinant","archimedean_cell"))
    return next((kind for token,kind in rules if token in cell),"source_inhabitant")
def interaction_net(nodes):
    agents=[];wires=[]
    for n in nodes:
        principal={"id":n["id"]+".out","role":"principal","direction":"out","type":output_type(n["id"])}
        auxiliaries=[]
        for i,dep in enumerate(n.get("depends_on",[])):
            port={"id":n["id"]+".in."+str(i),"role":"auxiliary","direction":"in","type":output_type(dep),"label":dep}
            auxiliaries.append(port);wires.append({"id":dep+"->"+n["id"],"source_port":dep+".out","target_port":port["id"],"wire_type":port["type"],"source_agent":dep,"target_agent":n["id"]})
        agents.append({"id":n["id"],"principal":principal,"auxiliaries":auxiliaries})
    return {"typing_authority":"compiler_derived_visualization_schema","agents":agents,"wires":wires}
def compile_rh_net_state(c):
    if c.get("claim")!="current_rh_programme_not_rh_proof":return fail("claim_boundary","RH state model must not claim RH")
    nodes=c.get("constructors",[]);by={n.get("id"):n for n in nodes}
    if len(by)!=len(nodes) or None in by:return fail("constructor_identity","constructor ids must be unique")
    for cell,deps in HIGHER_COHERENCE.items():
        if cell not in by:return fail("higher_coherence_topology","required higher-coherence cell is absent",constructor=cell)
        if by[cell].get("depends_on")!=deps:return fail("higher_coherence_topology","higher-coherence dependency was omitted or shortcut",constructor=cell,expected=deps,actual=by[cell].get("depends_on"))
    if c.get("completion_evidence_requirements")!=COMPLETION_EVIDENCE:return fail("completion_evidence_schema","completion stability must require continuity, inverse control, uniform bounds, and commuting diagrams")
    if c.get("completion_control_contract")!=COMPOSITE_CONTROL:return fail("composite_path_control","uniform control must cover forward and inverse composites over every canonical path, cutoff, and constructor depth")
    conditional={x.get("structure"):x for x in c.get("conditional_coherences",[])}
    for structure,witness in (("braiding","hexagon_coherence"),("dagger","dagger_compatibility")):
        item=conditional.get(structure,{})
        if item.get("required_witness")!=witness or item.get("applicability")!="when_declared":return fail("conditional_coherence","optional structure lacks its conditional coherence obligation",structure=structure)
    for n in nodes:
        if n.get("status") not in ("constructed","open"):return fail("constructor_status","invalid status",constructor=n.get("id"))
        if n.get("status")=="constructed":
            if n.get("authority_class")!="source_derived" or not n.get("source_locator"):return fail("source_authority","constructed cell lacks a source-derived inhabitant",constructor=n.get("id"))
            if n.get("id")=="completion_stable_frontier_coherence":
                evidence=n.get("completion_evidence") or {}
                missing=[x for x in COMPLETION_EVIDENCE if evidence.get(x) is None]
                if missing:return fail("completion_analytic_control","completed coherence lacks analytic control evidence",missing=missing)
        elif n.get("authority_class")!="formal_slot":return fail("slot_typing","open constructor must remain a formal slot",constructor=n.get("id"))
        for dep in n.get("depends_on",[]):
            if dep not in by:return fail("dependency_closure","unknown dependency",constructor=n.get("id"),dependency=dep)
            if n.get("status")=="constructed" and by[dep].get("status")!="constructed":return fail("premature_promotion","constructed cell depends on an open cell",constructor=n.get("id"),dependency=dep)
    for lens in c.get("lenses",[]):
        kind=lens.get("kind")
        if kind not in LENS_REQ:return fail("lens_typing","unknown lens",lens=kind)
        if lens.get("status")=="constructed":
            missing=[x for x in LENS_REQ[kind] if not lens.get(x)]
            if missing:return fail("lens_typing","constructed lens lacks required evidence",lens=kind,missing=missing)
        elif lens.get("status")!="open":return fail("lens_typing","lens status must be constructed or open",lens=kind)
    open_ids={n["id"] for n in nodes if n["status"]=="open"}
    frontier=sorted(n["id"] for n in nodes if n["status"]=="open" and all(d not in open_ids for d in n.get("depends_on",[])))
    downstream=sorted(open_ids-set(frontier))
    terminal=c.get("terminal_constructor")
    if terminal not in by:return fail("terminal","terminal constructor is absent")
    if by[terminal]["status"]!="open":return fail("rh_overpromotion","terminal RH constructor cannot currently be constructed")
    constructed=sorted(n["id"] for n in nodes if n["status"]=="constructed")
    formal_slots=sorted(n["id"] for n in nodes if n["status"]=="open")
    return {
      "schema":"marici.scc.rh-interaction-net-state.v1","passed":True,"first_failed_gate":None,
      "domain_algebra":{"source_derived_inhabitants":constructed,"formal_constructor_slots":formal_slots,"open_holes":sorted(open_ids),"closed_schema":False,"universal_core_eligible":False},
      "frontier_antichain":frontier,"downstream_open":downstream,
      "higher_coherence_witness_chain":list(HIGHER_COHERENCE),
      "completion_evidence_requirements":COMPLETION_EVIDENCE,
      "completion_control_contract":COMPOSITE_CONTROL,
      "conditional_coherences":c.get("conditional_coherences",[]),
      "interaction_net":interaction_net(nodes),
      "lenses":{x["kind"]:x["status"] for x in c.get("lenses",[])},
      "terminal":{"id":terminal,"status":"open","rh_proved":False},
      "next_parallel_constructors":frontier,
      "explanation":"The programme has a typed partial net with source-authorized arithmetic-to-analytic crossings and transport, but no closed reduction class reaching the RH terminal evaluator."
    }
