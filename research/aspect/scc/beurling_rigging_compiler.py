"""Finite exact compiler for typed Beurling rigging candidates."""
from fractions import Fraction

REQUIRED_CHANNELS={"primitive","square","connected","seam","endpoint","archimedean"}
def F(x):return Fraction(str(x))
def fail(gate,reason,**evidence):return {"passed":False,"first_failed_gate":gate,"reason":reason,"evidence":evidence}
def compile_beurling_rigging(c):
    s=c.get("weight_exponent")
    if not isinstance(s,int) or s<0:return fail("weight","weight exponent must be a nonnegative integer")
    elements={x.get("id"):x for x in c.get("monoid_elements",[])}
    if None in elements or not elements:return fail("valuation_monoid","finite valuation packet is missing")
    weight=lambda x:(1+elements[x]["degree"])**s
    products=[]
    for p in c.get("products",[]):
        if any(p.get(k) not in elements for k in ("left","right","product")):return fail("valuation_monoid","product names absent element",product=p)
        degree_ok=elements[p["product"]]["degree"]==elements[p["left"]]["degree"]+elements[p["right"]]["degree"]
        sub=weight(p["product"])<=weight(p["left"])*weight(p["right"])
        products.append({"id":p.get("id"),"degree_additive":degree_ok,"weight_submultiplicative":sub})
        if not degree_ok or not sub:return fail("bounded_convolution","weight or valuation product is not multiplicative",product=p.get("id"))
    channels=set(c.get("type_fibers",{}).get("channels",[]))
    if not REQUIRED_CHANNELS.issubset(channels) or c.get("type_fibers",{}).get("scalar_collapse_forbidden") is not True:return fail("type_fibers","channel fibers are incomplete or scalar collapse is admitted",missing=sorted(REQUIRED_CHANNELS-channels))
    adams=[]
    for a in c.get("adams_maps",[]):
        r=a.get("r");bound=r**s if isinstance(r,int) and r>=1 else None
        if bound is None or a.get("fiberwise_coherent") is not True or a.get("multiplicative") is not True:return fail("adams_coherence","Adams map lacks a coherent multiplicative fiber action",adams=a.get("id"))
        ratios=[]
        for source,target in a.get("element_map",{}).items():
            if source not in elements or target not in elements:return fail("adams_coherence","Adams map names absent element",adams=a.get("id"))
            ratios.append(F(weight(target))/F(weight(source)))
        if ratios and max(ratios)>bound:return fail("adams_bound","Adams weight ratio exceeds r^s",adams=a.get("id"),ratio=str(max(ratios)),bound=bound)
        adams.append({"id":a.get("id"),"bound":bound,"max_ratio":str(max(ratios)) if ratios else "0"})
    rows=[];minimal=0
    for row in c.get("boundary_rows",[]):
        degree=row.get("growth_degree")
        if not isinstance(degree,int) or degree<0:return fail("boundary_growth","boundary growth degree is invalid",row=row.get("id"))
        minimal=max(minimal,degree)
        if degree>s:return fail("boundary_growth","boundary row grows faster than the selected weight",row=row.get("id"),degree=degree,s=s)
        if row.get("claimed_hilbert_bounded") is True and row.get("cutoff_norm_growth") not in ("bounded",0):return fail("hilbert_port","divergent boundary row was promoted to a bounded Hilbert port",row=row.get("id"))
        rows.append({"id":row.get("id"),"growth_degree":degree,"dual_continuous":True,"hilbert_bounded":row.get("claimed_hilbert_bounded") is True})
    if c.get("minimal_exponent_claim")!=minimal or s!=minimal:return fail("minimal_weight","selected exponent is not the least exponent controlling declared rows",derived=minimal,selected=s,claimed=c.get("minimal_exponent_claim"))
    green=c.get("doubled_green",{})
    if not green.get("test_to_dual_continuous") or not green.get("fiber_signature_complete") or green.get("claimed_hilbert_bounded") is True:return fail("doubled_green_continuity","doubled Green pairing is missing, mistyped, or overpromoted")
    common=c.get("common_operations",[])
    for op in common:
        if not all(op.get(k) for k in ("test_algebra_action","hilbert_action","dual_pairing_action","mixed_coherence")):return fail("three_rung_coherence","common operation lacks a coherent action on all three rungs",operation=op.get("id"))
    return {"schema":"marici.scc.beurling-rigging-compilation.v1","rigging":c.get("id"),"passed":True,"first_failed_gate":None,"weight_exponent":s,"derived_minimal_exponent":minimal,"products":products,"adams":adams,"boundary_rows":rows,"rungs":["typed_test_algebra","fourier_bohr_hilbert_module","boundary_dual"],"claim":"finite carrier-class coherence only; source-specific coefficient laws remain separate"}

def audit_beurling_source_gate(c):
    """Audit source derivation without promoting a viable carrier candidate."""
    if c.get("topology_authority")!="source_selected":return fail("topology_branch","polynomial Beurling packet is a hostile/control branch, not the active theta topology",authority=c.get("topology_authority"))
    required=["primitive","square","connected","seam","endpoint","archimedean"]
    rows={x.get("id"):x for x in c.get("coefficient_laws",[])}
    evidence=[]
    for rid in required:
        row=rows.get(rid)
        if not row:return fail("coefficient_law","required source coefficient is absent",coefficient=rid)
        if row.get("status")!="source_derived" or not row.get("formula") or not row.get("locator") or not isinstance(row.get("growth_degree"),int):return fail("coefficient_law","source coefficient law remains open",coefficient=rid,status=row.get("status") if row else None)
        evidence.append({"id":rid,"growth_degree":row["growth_degree"],"locator":row["locator"]})
    derived_s=max(x["growth_degree"] for x in evidence)
    if c.get("selected_weight_exponent")!=derived_s:return fail("source_selected_weight","weight exponent does not equal the maximum derived growth degree",derived=derived_s,selected=c.get("selected_weight_exponent"))
    fibers=c.get("type_fiber_derivation",{})
    if fibers.get("status")!="source_derived" or not REQUIRED_CHANNELS.issubset(set(fibers.get("channels",[]))) or not fibers.get("locator"):return fail("source_type_fibers","complete typed fibers are not source-derived")
    for a in c.get("required_adams",[]):
        if a.get("status")!="source_derived" or not a.get("formula") or not a.get("locator") or a.get("fiberwise_coherent") is not True:return fail("source_adams","required Adams map remains underived or incoherent",adams=a.get("id"))
    green=c.get("doubled_green_source_law",{})
    if green.get("status")!="source_derived" or not green.get("formula") or not green.get("locator") or green.get("test_to_dual_continuous") is not True:return fail("source_doubled_green","doubled-Green source law remains open")
    return {"schema":"marici.scc.beurling-source-gate.v1","source_packet":c.get("id"),"passed":True,"first_failed_gate":None,"selected_weight_exponent":derived_s,"coefficient_laws":evidence,"claim":"source-selected typed Beurling rigging"}
