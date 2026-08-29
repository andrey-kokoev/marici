#!/usr/bin/env python3
"""Freeze hardware calibration thresholds and emit a controller-binding template."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"comparison-loop-hardware-binding.v1.json"
MESH=ASPECT/"results"/"comparison_loop_optical_mesh_program.json"
CONNECTED=ASPECT/"results"/"connected_route_coherent_control.json"
RESULT=ASPECT/"results"/"comparison_loop_hardware_binding.json"
TEMPLATE=ASPECT/"results"/"comparison_loop_hardware_binding_template.json"
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); mesh=json.loads(MESH.read_text(encoding="utf-8")); connected=json.loads(CONNECTED.read_text(encoding="utf-8"))
 rotations=[op for route in mesh["routes"].values() for op in route["rotations"]]; n=len(rotations)
 eps=c["error_budget"]["rotation_systematic"]/n
 records=[]
 for op in rotations:
  records.append({"hardware_id":None,"mesh_id":op["mesh_id"],"rotation_index":op["rotation_index"],"control_channel":None,"mode_a":op["mode_a"],"mode_b":op["mode_b"],"target_angle":math.atan2(op["sine"],op["cosine"]),"measured_angle":None,"angle_standard_error":None,"insertion_loss":None,"timestamp":None,"calibration_authority":None})
 phase_records=[]
 for arm,route in mesh["routes"].items():
  for mode,target in enumerate(route["terminal_phases"]):
   phase_records.append({"hardware_id":None,"mesh_id":f"route-{arm}-mesh-v1","mode":mode,"target_phase":target,"measured_phase":None,"phase_standard_error":None,"calibration_authority":None})
 spread=connected["fringe_range"][1]-connected["fringe_range"][0]; total=c["error_budget"]["total_fringe"]
 checks={"rotation_count":n==c["derivation"]["total_rotations"],"uniform_angle_bound":abs(eps-0.01/108)<1e-15,"budget_sums":abs(sum(c["error_budget"][k] for k in ("rotation_systematic","terminal_phase","differential_loss","statistical_quadrature"))-total)<1e-15,"probe_dependence_resolved":spread>2*total,"all_rotation_records":len(records)==108,"all_phase_records":len(phase_records)==40,"unbound_fields_null":all(r["hardware_id"] is None and r["control_channel"] is None and r["measured_angle"] is None for r in records),"claim_boundary":not any(c["claim_boundary"].values())}
 template={"schema":"marici.aspect.comparison-loop-hardware-binding-packet.v1","status":"template","per_rotation_angle_bound_radians":eps,"rotation_records":records,"phase_records":phase_records,"physical_acquisition":None}
 out={"schema":"marici.aspect.comparison-loop-hardware-binding-result.v1","passed":all(checks.values()),"checks":checks,"per_rotation_angle_bound_radians":eps,"reference_fringe_spread":spread,"two_sided_total_error":2*total,"remaining_margin":spread-2*total,"binding_template":str(TEMPLATE.relative_to(ROOT)).replace("\\","/"),"physical_status":"awaiting_hardware_binding"}
 TEMPLATE.write_text(json.dumps(template,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()
