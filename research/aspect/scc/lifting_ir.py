"""Canonical SCC categorical IR: explanations as displayed lifting problems."""
import re
STATES=("not_constructed","empty_fiber","inhabited","multiple_fillers","contractible","selected","coherent_section")
IDENTITIES=("literal_equality","displayed_isomorphism","univalent_identity","observer_equivalence","physical_record_identity")
HEX64=re.compile(r"^[0-9a-f]{64}$")
def fail(gate,reason,**evidence):return {"schema":"marici.scc.lifting-ir.v1","passed":False,"first_failed_gate":gate,"reason":reason,"evidence":evidence}
def compile_lifting_ir(c):
 layers=c.get("layers",[])
 if not isinstance(layers,list) or not layers:return fail("layers","at least one lifting layer is required")
 seen=set();compiled=[];first=None;expected_base=c.get("root_object","root")
 gates={"empty_fiber":"emptiness_witness","inhabited":"inhabitance_witness","multiple_fillers":"multiplicity_witness","contractible":"contractibility_witness","selected":"selector","coherent_section":"section_coherence_witness"}
 for i,x in enumerate(layers):
  if not isinstance(x,dict) or not x.get("id") or x["id"] in seen:return fail("layer_identity","layers need unique ids",index=i)
  seen.add(x["id"]);state=x.get("state")
  if state not in STATES:return fail("lifting_state","unknown lifting state",layer=x["id"],state=state)
  if x.get("base_ref")!=expected_base:return fail("tower_order","layer base must be the preceding total object",layer=x["id"],expected=expected_base)
  kind=x.get("kind","mathematical")
  if kind not in ("mathematical","readout"):return fail("layer_kind","layer kind must be mathematical or readout",layer=x["id"])
  if kind=="readout":
   if i!=len(layers)-1:return fail("readout_order","readout must be final",layer=x["id"])
   missing=[k for k in ("source_locator","detector_map","record_ontology") if not x.get(k)]
   if state!="not_constructed" and missing:return fail("readout_authority","constructed readout lacks source objects",layer=x["id"],missing=missing)
  if state!="not_constructed" and not x.get("projection"):
   return fail("projection","constructed lifting layer requires its forgetful projection",layer=x["id"])
  needed=gates.get(state)
  if needed and not x.get(needed):return fail("state_evidence","lifting state lacks evidence",layer=x["id"],state=state,missing=needed)
  if state in ("inhabited","multiple_fillers","selected","coherent_section") and not x.get("inhabitance_witness"):
   return fail("inhabitance","state requires an inhabitance witness",layer=x["id"],state=state)
  if state in ("selected","coherent_section") and not x.get("selector"):
   return fail("selection","selected state requires a selector",layer=x["id"])
  if state=="coherent_section" and not x.get("selector_invariance_witness"):
   return fail("selector_invariance","coherent section requires selector invariance",layer=x["id"])
  cert=x.get("unimath_certificate")
  if cert:
   if cert.get("status")!="kernel_checked_conditional" or not all(isinstance(cert.get(k),str) and HEX64.fullmatch(cert[k]) for k in ("source_sha256","object_sha256")):
    return fail("unimath_certificate","certificate lacks checked status or digests",layer=x["id"])
  obstruction=None
  if state=="not_constructed":obstruction="missing_displayed_layer"
  elif state=="empty_fiber":obstruction="empty_fiber"
  elif state=="inhabited":obstruction="selector_not_constructed"
  elif state=="multiple_fillers":obstruction="unresolved_multiplicity"
  elif state=="contractible":obstruction="coherent_section_not_exhibited"
  elif state=="selected":obstruction="section_coherence_not_verified"
  prior_blocker=first
  if first is None and obstruction:first={"index":i,"layer":x["id"],"obstruction":obstruction}
  capabilities={"fiber_constructed":state!="not_constructed","inhabited":state in ("inhabited","multiple_fillers","contractible","selected","coherent_section"),"unique_up_to_identity":state=="contractible","selector":state in ("selected","coherent_section"),"coherent_section":state=="coherent_section"}
  if prior_blocker:global_status="blocked_by_prior_layer"
  elif obstruction:global_status="obstructed_here"
  else:global_status="coherent_prefix"
  compiled.append({"id":x["id"],"kind":kind,"base_ref":expected_base,"total_ref":x.get("total_ref",x["id"]+":total"),"state":state,"global_status":global_status,"blocked_by":prior_blocker["layer"] if prior_blocker else None,"projection":x.get("projection"),"capabilities":capabilities,"unimath_certificate":cert or "not_supplied"})
  expected_base=compiled[-1]["total_ref"]
 for claim in c.get("identity_claims",[]):
  kind=claim.get("kind")
  if kind not in IDENTITIES:return fail("identity_kind","unknown identity modality",kind=kind)
  witness={"literal_equality":"equality_witness","displayed_isomorphism":"displayed_iso_witness","univalent_identity":"displayed_univalence_witness","observer_equivalence":"observer_witness","physical_record_identity":"record_identity_witness"}[kind]
  if not claim.get(witness):return fail("identity_witness","identity modality lacks its own witness",kind=kind,missing=witness)
 complete=all(x["state"]=="coherent_section" for x in compiled)
 projections=[{"from":x["total_ref"],"to":x["base_ref"],"projection":x["projection"]} for x in compiled if x["projection"]]
 surviving_prefix=[]
 for x in compiled:
  if x["state"] in ("not_constructed","empty_fiber"):break
  surviving_prefix.append(x["id"])
 return {"schema":"marici.scc.lifting-ir.v1","passed":True,"first_failed_gate":None,"explanation_complete":complete,"layers":compiled,"first_obstruction":first,"forgetful_projections":projections,"surviving_prefix":surviving_prefix,"identity_claims":c.get("identity_claims",[]),"physical_readout_status":next((x["state"] for x in compiled if x["kind"]=="readout"),"not_constructed"),"claim_boundary":"structural lifting certificate; source objects and physical adequacy remain external"}
