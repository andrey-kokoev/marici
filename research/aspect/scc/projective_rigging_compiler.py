"""SCC compiler for source-selected projective exponential Fock riggings."""
REQUIRED_GRADES={"primitive":"dual_boundary_current","square":"tempered_or_hilbert_counterterm","connected":"smooth_uniform_bohr","seam":"dual_evaluation","endpoint":"dual_evaluation","archimedean":"determinant_line_tensor_extension"}
def fail(gate,reason,**evidence):return {"passed":False,"first_failed_gate":gate,"reason":reason,"evidence":evidence}
def compile_projective_rigging(c):
    if c.get("topology_authority")!="source_selected":return fail("topology_authority","projective branch lacks source authority")
    scales=c.get("seminorm_scales",[])
    if not scales or any(not isinstance(x,(int,float)) or x<=0 for x in scales) or c.get("all_positive_scales") is not True:return fail("projective_scale","need a positive sample and declared projective family over every positive scale")
    for law in c.get("convolution_laws",[]):
        if law.get("scale") not in scales or law.get("weight_multiplicative") is not True or law.get("bounded_same_seminorm") is not True:return fail("projective_convolution","convolution fails on a declared seminorm",scale=law.get("scale"))
    adams=[]
    for a in c.get("adams_transport",[]):
        r=a.get("r")
        if not isinstance(r,int) or r<1 or a.get("law")!="q_delta(psi^r c)=q_(r delta)(c)" or a.get("fiberwise_coherent") is not True or a.get("fixed_rung_bounded_claim") is not False:return fail("seminorm_transport","Adams action is mistyped",adams=a.get("id"))
        adams.append({"id":a.get("id"),"index_map":"delta -> "+str(r)+" delta"})
    grades=c.get("grade_roles",{})
    if grades!=REQUIRED_GRADES:return fail("grade_asymmetry","theta grades were collapsed or mistyped",expected=REQUIRED_GRADES,actual=grades)
    for row in c.get("dual_rows",[]):
        if row.get("finite_exponential_order") is not True or not row.get("formula") or not row.get("source_locator") or row.get("promoted_to_hilbert_state") is not False:return fail("strong_dual","dual row is underived or overpromoted",row=row.get("id"))
    bohr=c.get("fourier_bohr",{})
    if not(bohr.get("invariant_mean_authorized") and bohr.get("typed_fibers_retained") and bohr.get("hilbert_isometry")):return fail("fourier_bohr","Hilbert presentation is incomplete")
    lift=c.get("archimedean_operator_lift",{})
    if lift.get("status")!="constructed" or not lift.get("source_locator") or lift.get("maps_determinant_line_to_graph_operator") is not True:return fail("archimedean_operator_lift","determinant-line tensor extension has no authorized lift into the Green graph domain")
    domain=c.get("common_graph_domain",{});required={"doubled_green","seam_trace","endpoint_trace","primitive_current","square_current","connected_tail","lifted_archimedean_operator","reciprocal_sewing","determinant_pairing"}
    if domain.get("status")!="constructed" or set(domain.get("operators",[]))!=required or not domain.get("source_locator") or domain.get("mixed_continuity_verified") is not True:return fail("common_graph_domain","common mixed graph domain remains unconstructed",missing=sorted(required-set(domain.get("operators",[]))))
    return {"schema":"marici.scc.projective-rigging-compilation.v1","rigging":c.get("id"),"passed":True,"first_failed_gate":None,"adams":adams,"grades":grades}
