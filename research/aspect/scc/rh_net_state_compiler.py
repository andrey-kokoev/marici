"""Compile the current RH programme as a typed partial interaction-net presentation."""
from rh_net_semantic_views import compile_semantic_views
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
REFINED_RH_TOPOLOGY={
 "prime_diagonal_schur_operator":["projective_exponential_source"],
 "hilbert_schmidt_ideal_membership":["prime_diagonal_schur_operator"],
 "s2_s1_ideal_split":["hilbert_schmidt_ideal_membership"],
 "det2_higher_prime_power_packet":["s2_s1_ideal_split"],
 "finite_det_det2_trace_comparison":["det2_higher_prime_power_packet"],
 "zero_free_diagonal_carrier":["prime_diagonal_schur_operator","det2_higher_prime_power_packet"],
 "passive_wiring_modes":["prime_diagonal_schur_operator"],
 "valuation_fock_passive_dilation":["prime_diagonal_schur_operator","fourier_bohr_discrete_port"],
 "primitive_wall_trace_completion":["finite_det_det2_trace_comparison","arithmetic_analytic_incidence"],
 "reciprocal_adjoint_port_orientation":["valuation_fock_passive_dilation"],
 "archimedean_endpoint_operator_lift":["valuation_fock_passive_dilation"],
 "passive_network_assembly":["valuation_fock_passive_dilation","passive_wiring_modes"],
 "det2_anomaly_identification":["passive_network_assembly","det2_higher_prime_power_packet"],
 "source_cayley_boundary_relation":["primitive_wall_trace_completion","reciprocal_adjoint_port_orientation","archimedean_endpoint_operator_lift","det2_anomaly_identification"],
 "completed_boundary_pencil":["source_cayley_boundary_relation","relative_determinant_line_coherence"],
 "relative_off_seam_five_margin_coercivity":["completed_boundary_pencil","allowed_seam_defect_locus"],
 "xi_boundary_pencil_spectral_identification":["completed_boundary_pencil","relative_determinant_line_coherence"],
 "off_seam_kernel_exclusion":["relative_off_seam_five_margin_coercivity","xi_boundary_pencil_spectral_identification"],
 "riemann_hypothesis_terminal":["off_seam_kernel_exclusion"]}
HOSTILE_IDS=[
 "scalar_sum_breaks_schur_contractivity","det2_dropped_primitive_trace",
 "arbitrary_primitive_continuation_imports_divisor","cascade_drops_det2_anomaly",
 "reciprocal_orientation_without_source_map","global_margin_excludes_seam_zeros",
 "coercivity_promoted_to_identification","identification_promoted_to_coercivity",
 "generic_cocycle_claims_xi_divisor","strict_diagonal_carrier_claims_zeros"]
SOURCE_REALIZATION_OPEN={
 "valuation_fock_passive_dilation","primitive_wall_trace_completion",
 "reciprocal_adjoint_port_orientation","archimedean_endpoint_operator_lift",
 "passive_network_assembly","det2_anomaly_identification",
 "source_cayley_boundary_relation","completed_boundary_pencil",
 "relative_off_seam_five_margin_coercivity",
 "xi_boundary_pencil_spectral_identification","off_seam_kernel_exclusion",
 "riemann_hypothesis_terminal"}
def fail(gate,reason,**evidence):return {"passed":False,"first_failed_gate":gate,"reason":reason,"evidence":evidence}
def output_type(cell):
    rules=(("prime_diagonal","schur_operator"),("ideal_split","operator_ideal_filtration"),("ideal_membership","operator_ideal_witness"),("det2_higher","regularized_determinant_packet"),("det_det2_trace","determinant_comparison"),("zero_free_diagonal","zero_free_carrier_witness"),("passive_wiring","wiring_mode_sum_type"),("passive_dilation","passive_colligation"),("primitive_wall","primitive_trace_completion"),("adjoint_port","oriented_reciprocal_port"),("archimedean_endpoint","archimedean_operator_port"),("passive_network","passive_network"),("det2_anomaly","determinant_anomaly"),("cayley_boundary","boundary_relation"),("boundary_pencil","completed_boundary_pencil"),("allowed_seam","defect_locus"),("off_seam_five","relative_coercivity_witness"),("xi_boundary","xi_identification_witness"),("off_seam_kernel","kernel_exclusion_witness"),("overlap_","pairwise_comparison"),("associator","associator"),("unitor","unitor"),("pentagon","pentagon_witness"),("triangle","triangle_witness"),("completion_stable_frontier","completed_coherence"),("nine_operation","operation_domain"),("naturality","naturality_witness"),("sewing","sewing_witness"),("fourier_transport","completed_transport"),("determinant_line","determinant_line_witness"),("five_margin","coercivity_margin_packet"),("spectral_identification","spectral_identification"),("critical_line","critical_line_exclusion"),("riemann_hypothesis","proposition"),("type_fiber_adams","adams_cell"),("endpoint_operator","endpoint_cell"),("archimedean_determinant","archimedean_cell"))
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
G4_TOPOLOGY={
 "three_port_source_separation":[],
 "theta_koszul_divisor_complex":["three_port_source_separation"],
 "bare_euler_det3_with_two_anomaly_lines":["three_port_source_separation"],
 "relative_reciprocal_det2_return":["bare_euler_det3_with_two_anomaly_lines"],
 "centered_trace_class_seam_return":["relative_reciprocal_det2_return"],
 "centered_incidence_range_closure_typing":["three_port_source_separation"],
 "zero_free_arithmetic_complement":["three_port_source_separation"],
 "two_sided_evans_matching_lift":["theta_koszul_divisor_complex","centered_trace_class_seam_return"],
 "conservative_green_complex":["centered_trace_class_seam_return","three_port_source_separation"],
 "exact_evans_history_domain":["conservative_green_complex"],
 "three_port_block_domain_membership":["exact_evans_history_domain","three_port_source_separation"],
 "five_port_arithmetic_summability":["exact_evans_history_domain","centered_incidence_range_closure_typing"],
 "maximal_isotropic_evans_domain":["two_sided_evans_matching_lift","exact_evans_history_domain"],
 "prime_shell_adjoint_residual_family":["five_port_arithmetic_summability","conservative_green_complex"],
 "global_fourier_poisson_response_intertwining":["three_port_block_domain_membership","five_port_arithmetic_summability","maximal_isotropic_evans_domain"],
 "evans_to_conservative_green_chain_map":["theta_koszul_divisor_complex","two_sided_evans_matching_lift","conservative_green_complex","prime_shell_adjoint_residual_family","global_fourier_poisson_response_intertwining"],
 "holomorphic_mapping_cone_complement":["evans_to_conservative_green_chain_map","zero_free_arithmetic_complement"],
 "local_module_length_preservation":["evans_to_conservative_green_chain_map"],
 "critical_seam_green_confinement":["evans_to_conservative_green_chain_map","centered_incidence_range_closure_typing","local_module_length_preservation"],
 "riemann_hypothesis_terminal":["evans_to_conservative_green_chain_map","critical_seam_green_confinement"]}
G4_HOSTILE_IDS=[
 "bare_euler_det3_replaced_by_relative_det2",
 "relative_det2_double_counted_as_bare_euler",
 "theta_koszul_claimed_as_independent_green_realization",
 "same_sign_passive_feedback_claims_seam_zero",
 "range_closure_promoted_to_exact_range",
 "gram_compression_promoted_to_primitive_dynamics",
 "scalar_evans_mismatch_claims_vector_adjoint_cancellation",
 "adjoint_cancellation_without_all_prime_shell_residuals",
 "seam_scalar_substitutes_for_maximal_isotropic_state",
 "pointwise_kernel_inclusion_substitutes_for_module_length"]
G4_OPEN={
 "prime_shell_adjoint_residual_family","global_fourier_poisson_response_intertwining",
 "evans_to_conservative_green_chain_map",
 "holomorphic_mapping_cone_complement","local_module_length_preservation",
 "critical_seam_green_confinement","riemann_hypothesis_terminal"}
G4_SEMANTIC_INVARIANTS={
 "pass_does_not_imply_proved":True,
 "simulation_does_not_imply_physical_realization":True,
 "readout_does_not_imply_faithfulness":True,
 "local_confluence_does_not_imply_global_coherence":True,
 "source_formula_does_not_imply_source_realization":True}
G4_NEGATIVE_GATES={
 "finite_moment_subtraction_closes_primitive_pv_lane":False,
 "scalar_seam_data_separates_reciprocal_off_seam_pairs":False,
 "range_closure_equals_exact_range":False,
 "local_coercivity_implies_global_confinement":False}
G4_INTERFACE_FIELDS=("coefficient_object","completion","topology","quotient","authority")
def _g4_cut_sets(by, terminal):
    """Return the unresolved frontier and singleton minimal blockers for an AND dependency net."""
    memo={}
    def frontier(cell):
        if cell in memo:return memo[cell]
        node=by[cell]
        if node["status"]=="open" and all(by[d]["status"]=="constructed" for d in node.get("depends_on",[])):
            memo[cell]={cell};return memo[cell]
        out=set()
        for dep in node.get("depends_on",[]):
            if by[dep]["status"]=="open":out.update(frontier(dep))
        memo[cell]=out;return out
    roots=sorted(frontier(terminal))
    return {"completion_frontier":roots,"minimal_blocking_sets":[[x] for x in roots],"dependency_semantics":"all listed dependencies are conjunctive"}
def compile_g4_rh_net_state(c):
    if c.get("claim")!="current_g4_rh_programme_not_rh_proof":return fail("claim_boundary","G4 RH state model must not claim RH")
    versioning=c.get("versioning",{})
    if versioning.get("predecessor")!="theta-rh-interaction-net-state.v1" or versioning.get("relation")!="refines_without_rewriting" or not versioning.get("nontransportable_conclusions"):
        return fail("version_migration","v2 must refine frozen v1 and declare nontransportable conclusions")
    nodes=c.get("constructors",[]);by={n.get("id"):n for n in nodes}
    if len(by)!=len(nodes) or None in by:return fail("constructor_identity","constructor ids must be unique")
    interface=c.get("interface_descriptors",{}).get("g4_common")
    if not isinstance(interface,dict) or any(not interface.get(x) for x in G4_INTERFACE_FIELDS):return fail("interface_descriptor","shared G4 interface is incomplete")
    for cell,deps in G4_TOPOLOGY.items():
        if cell not in by:return fail("g4_topology","required corrected-G4 cell is absent",constructor=cell)
        n=by[cell]
        if n.get("depends_on")!=deps:return fail("g4_topology","corrected-G4 dependency was omitted or shortcut",constructor=cell,expected=deps,actual=n.get("depends_on"))
        if n.get("interface_ref")!="g4_common":return fail("interface_pullback","constructor is outside the admitted shared interface",constructor=cell)
        if n.get("interface_overrides"):return fail("interface_pullback","interface override requires a separately authorized comparison map",constructor=cell)
    for n in nodes:
        expected_open=n.get("id") in G4_OPEN
        if expected_open and (n.get("status")!="open" or n.get("authority_class")!="formal_slot"):return fail("g4_premature_promotion","RH-bearing G4 cell must remain open",constructor=n.get("id"))
        if not expected_open and n.get("id") in G4_TOPOLOGY:
            witness=(c.get("evidence_objects",{}).get(n.get("witness_ref")) if n.get("witness_ref") else n.get("witness")) or {}
            required=("source_locator","checker","source_digest","assumptions","assessment_regime","proof_strength")
            if n.get("status")!="constructed" or n.get("authority_class")!="source_derived" or any(not witness.get(x) for x in required):
                return fail("g4_construction_authority","constructed G4 cell lacks witness-bearing source authority",constructor=n.get("id"),required=required)
        for dep in n.get("depends_on",[]):
            if dep not in by:return fail("dependency_closure","unknown dependency",constructor=n.get("id"),dependency=dep)
            if n.get("status")=="constructed" and by[dep].get("status")!="constructed":return fail("premature_promotion","constructed cell depends on an open cell",constructor=n.get("id"),dependency=dep)
    if c.get("semantic_invariants")!=G4_SEMANTIC_INVARIANTS:return fail("semantic_invariants","universal SCC nonpromotion invariants changed")
    if c.get("negative_knowledge_gates")!=G4_NEGATIVE_GATES:return fail("negative_knowledge","known no-go results must remain executable false gates")
    range_contract=c.get("centered_incidence_contract",{})
    if range_contract!={"kernel":"zero","forcing_vector_membership":"range_closure_not_exact_range","exact_lift_authorized":False}:return fail("range_closure_typing","closure membership must not be promoted to an exact forcing lift")
    ports=c.get("three_port_contract",{})
    if ports!={"carrier":["history","theta","arithmetic"],"theta_generator":0,"primitive_theta_arithmetic_dynamic_arrow":False,"gram_compression_is_dynamics":False}:return fail("three_port_typing","theta, arithmetic, and history ports must remain separated")
    determinant=c.get("determinant_ideal_contract",{})
    if determinant!={"bare_euler":"det3","relative_reciprocal_return":"det2","centered_seam_return":"trace_class_fredholm"}:return fail("determinant_ideal_typing","det3, det2, and trace-class returns must remain distinct")
    residual=c.get("rh_bearing_residual",{})
    if residual.get("identity")!="B_Sigma^dagger u_z = 0" or residual.get("locus")!="Xi_divisor" or residual.get("prime_shell_family_complete") is not False:return fail("rh_bearing_residual","the unresolved Xi-divisor vector residual must remain explicit")
    hostiles=c.get("hostile_fixtures",[])
    if [x.get("id") for x in hostiles]!=G4_HOSTILE_IDS or any(not x.get("must_reject") for x in hostiles):return fail("g4_hostile_fixture_basis","all ten ordered corrected-G4 hostiles are required")
    terminal=c.get("terminal_constructor")
    if terminal!="riemann_hypothesis_terminal" or by.get(terminal,{}).get("status")!="open":return fail("rh_overpromotion","RH terminal must remain open")
    open_ids={n["id"] for n in nodes if n["status"]=="open"}
    cut_sets=_g4_cut_sets(by,terminal);frontier=cut_sets["completion_frontier"]
    visualization=compile_semantic_views(c)
    if not visualization.get("passed"):return fail("visualization_contract",visualization)
    return {"schema":"marici.scc.rh-interaction-net-state.v2","passed":True,"proved":False,"physical_realization":False,"first_failed_gate":None,"model_generation":"corrected_G4","versioning":versioning,"visualization":visualization,"interface_pullback":{"descriptor":"g4_common","fields":list(G4_INTERFACE_FIELDS),"all_edges_checked":True},"semantic_invariants":G4_SEMANTIC_INVARIANTS,"negative_knowledge_gates":G4_NEGATIVE_GATES,"terminal_cut_sets":cut_sets,"frontier_antichain":frontier,"downstream_open":sorted(open_ids-set(frontier)),"interaction_net":interaction_net(nodes),"determinant_ideal_contract":determinant,"three_port_contract":ports,"centered_incidence_contract":range_contract,"rh_bearing_residual":residual,"hostile_fixtures":hostiles,"terminal":{"id":terminal,"status":"open","rh_proved":False},"explanation":"The corrected G4 topology is typed conservatively. RH remains blocked by the prime-shell adjoint residual family, seam-state/domain gates, and the Evans-to-conservative-Green chain map."}
def compile_rh_net_state(c):
    if c.get("schema")=="marici.scc.rh-interaction-net-state-contract.v2":return compile_g4_rh_net_state(c)
    if c.get("claim")!="current_rh_programme_not_rh_proof":return fail("claim_boundary","RH state model must not claim RH")
    nodes=c.get("constructors",[]);by={n.get("id"):n for n in nodes}
    if len(by)!=len(nodes) or None in by:return fail("constructor_identity","constructor ids must be unique")
    for cell,deps in HIGHER_COHERENCE.items():
        if cell not in by:return fail("higher_coherence_topology","required higher-coherence cell is absent",constructor=cell)
        if by[cell].get("depends_on")!=deps:return fail("higher_coherence_topology","higher-coherence dependency was omitted or shortcut",constructor=cell,expected=deps,actual=by[cell].get("depends_on"))
    for cell,deps in REFINED_RH_TOPOLOGY.items():
        if cell not in by:return fail("refined_rh_topology","required audit-3 cell is absent",constructor=cell)
        if by[cell].get("depends_on")!=deps:return fail("refined_rh_topology","audit-3 dependency was omitted or shortcut",constructor=cell,expected=deps,actual=by[cell].get("depends_on"))
    locus=by.get("allowed_seam_defect_locus",{})
    if locus.get("locus")!="critical_seam" or locus.get("off_locus_requirement")!="compact_uniform_positive_separation":return fail("relative_defect_locus","coercivity must be relative to the allowed critical seam")
    wiring=c.get("passive_wiring_contract",{})
    if wiring.get("unconditional_modes")!=["typed_direct_sum"] or "ordinary_scalar_sum" not in wiring.get("forbidden_modes",[]):return fail("passive_wiring_typing","only typed direct sum is unconditionally passive; scalar sum must be forbidden")
    hostiles=c.get("hostile_fixtures",[])
    if [x.get("id") for x in hostiles]!=HOSTILE_IDS or any(not x.get("must_reject") for x in hostiles):return fail("audit3_hostile_fixture_basis","all ten ordered hostile fixtures are required")
    promoted=sorted(x for x in SOURCE_REALIZATION_OPEN if by.get(x,{}).get("status")!="open" or by.get(x,{}).get("authority_class")!="formal_slot")
    if promoted:return fail("source_realization_boundary","algebraic formulas cannot construct source-realization cells",constructors=promoted)
    if c.get("completion_evidence_requirements")!=COMPLETION_EVIDENCE:return fail("completion_evidence_schema","completion stability must require continuity, inverse control, uniform bounds, and commuting diagrams")
    if c.get("completion_control_contract")!=COMPOSITE_CONTROL:return fail("composite_path_control","uniform control must cover forward and inverse composites over every canonical path, cutoff, and constructor depth")
    conditional={x.get("structure"):x for x in c.get("conditional_coherences",[])}
    for structure,witness in (("braiding","hexagon_coherence"),("dagger","dagger_compatibility")):
        item=conditional.get(structure,{})
        if item.get("required_witness")!=witness or item.get("applicability")!="when_declared":return fail("conditional_coherence","optional structure lacks its conditional coherence obligation",structure=structure)
    for n in nodes:
        if n.get("status") not in ("constructed","open"):return fail("constructor_status","invalid status",constructor=n.get("id"))
        if n.get("status")=="constructed":
            if n.get("authority_class") not in ("source_derived","algebraic_derived_nonrealization") or not n.get("source_locator"):return fail("construction_authority","constructed cell lacks typed derivation authority",constructor=n.get("id"))
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
    source_constructed=sorted(n["id"] for n in nodes if n["status"]=="constructed" and n["authority_class"]=="source_derived")
    algebraic_nonrealizations=sorted(n["id"] for n in nodes if n["status"]=="constructed" and n["authority_class"]=="algebraic_derived_nonrealization")
    formal_slots=sorted(n["id"] for n in nodes if n["status"]=="open")
    return {
      "schema":"marici.scc.rh-interaction-net-state.v1","passed":True,"first_failed_gate":None,
      "domain_algebra":{"source_derived_inhabitants":source_constructed,"algebraic_nonrealization_cells":algebraic_nonrealizations,"formal_constructor_slots":formal_slots,"open_holes":sorted(open_ids),"closed_schema":False,"universal_core_eligible":False},
      "frontier_antichain":frontier,"downstream_open":downstream,
      "higher_coherence_witness_chain":list(HIGHER_COHERENCE),
      "completion_evidence_requirements":COMPLETION_EVIDENCE,
      "completion_control_contract":COMPOSITE_CONTROL,
      "conditional_coherences":c.get("conditional_coherences",[]),
      "interaction_net":interaction_net(nodes),
      "passive_wiring_contract":wiring,"hostile_fixtures":hostiles,
      "lenses":{x["kind"]:x["status"] for x in c.get("lenses",[])},
      "terminal":{"id":terminal,"status":"open","rh_proved":False},
      "next_parallel_constructors":frontier,
      "explanation":"The programme has a typed partial net with source-authorized arithmetic-to-analytic crossings and transport, but no closed reduction class reaching the RH terminal evaluator."
    }

