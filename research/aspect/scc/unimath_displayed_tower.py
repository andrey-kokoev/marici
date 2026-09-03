"""Emit a kernel-checkable displayed-category tower for SCC explanation layers."""
import hashlib,re
IDENT=re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$");HEX64=re.compile(r"^[0-9a-f]{64}$")
IMPORTS=("UniMath.Foundations.All","UniMath.CategoryTheory.Core.Categories","UniMath.CategoryTheory.Core.Univalence","UniMath.CategoryTheory.DisplayedCats.Core","UniMath.CategoryTheory.DisplayedCats.Isos","UniMath.CategoryTheory.DisplayedCats.Total","UniMath.CategoryTheory.DisplayedCats.Univalence")
def fail(gate,reason,**evidence):return {"schema":"marici.scc.unimath-displayed-tower.v1","passed":False,"first_failed_gate":gate,"reason":reason,"evidence":evidence}
def compile_displayed_tower(c):
 module=c.get("module");digest=c.get("source_contract_sha256");layers=c.get("layers",[])
 if not isinstance(module,str) or not IDENT.fullmatch(module):return fail("module","unsafe Rocq module identifier")
 if not isinstance(digest,str) or not HEX64.fullmatch(digest):return fail("source_digest","source contract needs lowercase SHA-256")
 if not isinstance(layers,list) or not 2<=len(layers)<=8:return fail("tower","tower requires two through eight displayed layers")
 seen=set();normalized=[]
 for i,x in enumerate(layers):
  if not isinstance(x,dict) or not IDENT.fullmatch(str(x.get("name",""))):return fail("layer","each layer needs a safe unique name",index=i)
  if x["name"] in seen:return fail("layer","duplicate layer name",index=i);seen.add(x["name"])
  kind=x.get("kind")
  if kind not in ("mathematical","readout"):return fail("layer_kind","layer kind must be mathematical or readout",index=i)
  if kind=="readout" and i!=len(layers)-1:return fail("readout_order","readout may occur only as the final layer")
  if kind=="readout" and not x.get("source_locator"):return fail("readout_authority","readout layer requires a source locator")
  seen.add(x["name"]);normalized.append({"name":x["name"],"kind":kind,"source_locator":x.get("source_locator")})
 lines=[f"Require Import {x}." for x in IMPORTS]+["","Local Open Scope cat.",f"Module {module}.",f"(* SCC source contract SHA-256: {digest} *)","Section DisplayedTower.","Context (Base : univalent_category)."]
 base="Base";obligations=[]
 for i,x in enumerate(normalized,1):
  n=x["name"];disp=f"Disp_{n}";univ=f"Disp_{n}_univalent";total=f"Total_{n}"
  lines += [f"Context ({disp} : disp_cat {base}).",f"Context ({univ} : is_univalent_disp {disp}).",f"Definition {total} : univalent_category :=",f"  total_univalent_category (make_disp_univalent_category {univ}).",f"Definition SCC_filler_fiber_{n} (x : {base}) : UU := {disp} x.",f"Definition SCC_selector_type_{n} : UU := ∏ x : {base}, {disp} x.",f"Definition SCC_multiple_fillers_type_{n} : UU := ∑ x : {base}, ∑ a : {disp} x, ∑ b : {disp} x, ¬ (a = b).",f"Definition SCC_empty_fiber_blocks_selector_{n}",f"  (x : {base}) (Hempty : ¬ {disp} x) : ¬ SCC_selector_type_{n} :=",f"  fun selector => Hempty (selector x).",f"Context (x_{n} y_{n} : {base}).",f"Context (e_{n} : x_{n} = y_{n}).",f"Context (xx_{n} : {disp} x_{n}) (yy_{n} : {disp} y_{n}).",f"Context (i_{n} : z_iso_disp (idtoiso e_{n}) xx_{n} yy_{n}).",f"Definition SCC_equivalence_to_identity_{n} : transportf {disp} e_{n} xx_{n} = yy_{n} :=",f"  isotoid_disp {univ} e_{n} i_{n}."]
  obligations.append({"id":f"layer_{i}_{n}","kind":x["kind"],"base":base,"displayed_category":disp,"univalence_witness":univ,"total":total,"status":"kernel_term_emitted"})
  base=total
 lines += ["End DisplayedTower.",f"End {module}."];source="\n".join(lines)+"\n"
 readout=next((x for x in normalized if x["kind"]=="readout"),None)
 return {"schema":"marici.scc.unimath-displayed-tower.v1","passed":True,"first_failed_gate":None,"status":"emitted_unchecked","layers":normalized,"obligations":obligations,"final_total_category":base,"readout_status":"source_typed" if readout else "not_constructed","hostiles":{"multiple_fillers_without_selector":"not_decided_by_tower","equivalence_to_identity":"requires_displayed_univalence_witness","empty_readout_fiber":"not_testable_without_readout_layer" if not readout else "executable_in_sector_instance"},"rocq_source":source,"rocq_source_sha256":hashlib.sha256(source.encode()).hexdigest(),"claim_boundary":"conditional total-univalence tower; no inhabitance, selector, or physical adequacy claim"}
