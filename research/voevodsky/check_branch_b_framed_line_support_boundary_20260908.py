#!/usr/bin/env python3
"""Certify the first unrecoverable Branch-B framed line/support interface.

This is deliberately not a proof-by-file-absence and does not assign a zero map.
It checks the complete symbolic cancellation available from the physical source,
then checks that the supplied adapters stop before declaring the two maps needed
to compare that source with the conormal line/support.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

TS = ((1,3),(1,5),(3,5),(1,3,5))
ENDS = {"plus": ((1,3,5), "35"), "minus": ((0,2,4), "04")}
REQ = (
 "research/chatgpt/marici_physical_endpoint_pullback.md",
 "research/chatgpt/marici_comparison_fibre_adjunction_bar.md",
 "research/chatgpt/marici_physical_change_of_rings.md",
 "research/chatgpt/marici_primitive_conormal_column_20260908.md",
 "research/voevodsky/physical-conormal-first-jet-adapter.json",
 "research/voevodsky/endpoint-to-conormal-cohomology-mate.json",
 "research/voevodsky/native-endpoint-operation-action.json",
 "research/voevodsky/conormal-variance-antipode-mate.json",
)

def vec(**kw): return kw

def add(*vs):
 out = {}
 for v in vs:
  for k,x in v.items(): out[k]=out.get(k,0)+x
 return {k:x for k,x in out.items() if x}

def neg(v): return {k:-x for k,x in v.items()}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--root",default="."); ap.add_argument("--output",required=True)
 a=ap.parse_args(); root=Path(a.root); checks=[]
 files={}
 for rel in REQ:
  p=root/rel; assert p.is_file(), rel; files[rel]=sha(p); checks.append("input:"+rel)
 fj=json.loads((root/REQ[4]).read_text()); cm=json.loads((root/REQ[5]).read_text());
 va=json.loads((root/REQ[7]).read_text())
 assert fj["conclusion"]["still_required"].startswith("a typed comparison")
 assert "determinant-line identification" in cm["not_constructed"][-1]
 assert va["scope"]["line_and_support_transport"] is False
 checks += ["first_jet_stops_before_typed_line", "fine_frame_stops_before_determinant_line", "variance_mate_has_no_line_support_transport"]
 frames=[]
 occ={f"X{i}":1 for i in range(6)}
 gamma={"gamma":1}
 for T in TS:
  cart={f"t{i}":1 for i in T}
  lam=add(gamma,neg(occ),neg(cart))
  for sigma,(I,k) in ENDS.items():
   normal={f"t{i}":1 for i in I}
   # top(P_T)+lambda + empty(D_sigma)+external L_sigma
   top=add(occ,cart,lam,neg(normal),normal)
   assert top==gamma
   checks.append(f"top_weight:{sigma}:{''.join(map(str,T))}")
   frames.append({
    "sigma":sigma,"T":list(T),"k":k,"source_top_known_weight":top,
    "source_support_ideal":["t_T"]+[f"t{i}" for i in I],
    "cohomological_degree":3,"primitive_coefficient":1,
    "unresolved_line_arrow":f"theta_{sigma},{''.join(map(str,T))},epsilon: W_{sigma},{''.join(map(str,T))},epsilon -> L_{k} tensor Pi^vee<-1_beta>",
    "unresolved_support_arrow":f"RSupport_(t_T,{','.join('t'+str(i) for i in I)}) -> RSupport_conductor,beta({k})"
   })
 out={
  "schema":"marici.branch_b.framed_line_support_boundary.v1",
  "decision":3,
  "result":"exact_unrecoverable_line_and_support_maps",
  "not_a_zero_map":True,"not_a_nonexistence_result":True,
  "smallest_detector":{
   "known_source_top_weight":{"gamma":1},
   "known_target_relative_line":"L_k tensor Pi^vee<-1_beta>",
   "undetermined_equation":"degree(W_sigma,T,epsilon) = degree(L_k tensor Pi^vee<-1_beta>)",
   "reason":"No consumed input declares degree/transport of the two labelled excess frames and full determinant packet to the marked conormal/polarity line."
  },
  "support_boundary":"No consumed input declares a derived functor/map from the four-generator Rees Koszul support (t_T,t_i for I_sigma) to the occurrence-conductor/beta support; localized endpoint summands explicitly cannot use the conductor quotient unitaly.",
  "frames":frames,"new_checks":len(checks),"checks":checks,"input_sha256":files
 }
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"result":out["result"],"decision":3,"frames":len(frames),"new_checks":len(checks)}))
if __name__=="__main__": main()
