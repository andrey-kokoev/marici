#!/usr/bin/env python3
"""Compare transported G12 and independently constructed G31 jet annihilator planes."""
from __future__ import annotations
import contextlib,importlib,io,json,os,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3];BEN=ROOT/"research"/"benincasa";NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(NCHK)]
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts=importlib.import_module("g12_g31_residue_chart_transition")
    prior=importlib.import_module("check_rank26_physical_annihilator_chart_transport")
P=base.PRIME;HALF=(-pow(2,P-2,P))%P
TARGET_CHART=os.environ.get("MARICI_TARGET_CHART","G31")
RESULTS=ROOT/"research"/"nima"/"results"
SOURCE=RESULTS/f"rank26_physical_source_covariant_jet_census_k3_p{P}.json"
TARGET=RESULTS/f"rank26_physical_{TARGET_CHART.lower()}_source_covariant_jet_census_k3_p{P}.json"
OUT=RESULTS/f"rank26_physical_jet_seven_plane_G12_to_{TARGET_CHART}_transport_p{P}.json"
base.reduce_row=prior.reduce_complete

def rows(packet):
    out=[]
    for support in packet["annihilator_reduced_dual_basis"]:
      row=[0]*26
      for term in support:row[term["free_coordinate"]]=term["coefficient"]%P
      out.append(row)
    return out

def rank(dense):
    piv={}
    for row in dense:base.add_pivot({i:x for i,x in enumerate(row) if x},piv)
    return len(piv)

def g23_fiber_data(x,y,z):
    source_k,source_q=base.fiber_data(z,y,x);k=charts.swap_exponents(source_k)
    mapping={"g1":"g3","g2":"g2","g3":"g1","g23":"g12","g31":"g31"}
    return k,{target:charts.swap_exponents(source_q[source]) for source,target in mapping.items()}

def main():
    source_packet=json.loads(SOURCE.read_text(encoding="utf-8"));target_packet=json.loads(TARGET.read_text(encoding="utf-8"))
    charts.GAMMA=HALF;charts.AMBIENT=14;charts.CUTOFF=7;charts.K_DEPTH=3
    source=charts.presentation(base.fiber_data,charts.SOURCE_POINT,charts.SOURCE_NAMES)
    if TARGET_CHART=="G23":target_fiber,target_point,target_names=g23_fiber_data,(4,3,2),("g3","g2","g1","g12","g31")
    else:target_fiber,target_point,target_names=charts.g31_fiber_data,charts.TARGET_POINT,charts.TARGET_NAMES
    target=charts.presentation(target_fiber,target_point,target_names)
    tpos={c:i for i,c in enumerate(target["free_low"])}
    T=[[0]*26 for _ in range(26)]
    for j,c in enumerate(source["free_low"]):
      label=source["ordered_columns"][c]
      row=charts.quotient_vector(charts.map_label(label),target,-1)
      for tc,v in row.items():T[tpos[tc]][j]=v
    Ti=prior.inverse(T);Ls=rows(source_packet);Lt=rows(target_packet)
    transported=prior.matmul(Ls,Ti)
    payload={"schema":"marici.rank26-physical-jet-seven-plane-chart-transport.v2","prime":P,"gamma":"-1/2","k_pole_depth":3,"transition":f"G12_to_{TARGET_CHART}","transport_rank":rank(T),"source_annihilator_rank":rank(Ls),"target_annihilator_rank":rank(Lt),"transported_annihilator_rank":rank(transported),"joint_annihilator_rank":rank(transported+Lt),"planes_equal":rank(transported+Lt)==7,"passed":rank(T)==26 and rank(Ls)==rank(Lt)==rank(transported)==rank(transported+Lt)==7}
    OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()
