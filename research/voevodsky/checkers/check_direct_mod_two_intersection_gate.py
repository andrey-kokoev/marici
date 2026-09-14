#!/usr/bin/env python3
"""Verify that available split coordinates are localized de Rham data, not integral mod-two thimble pairings."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/rational_split_coordinates_do_not_supply_the_two_mod_two_thimble_intersections.md'
FRAME=ROOT/'research/benincasa/marked-extension-algebraic-line-support.md'
LOCAL=ROOT/'research/voevodsky/local_integral_legendre_thimble_does_not_select_the_ambient_two_bit_lift.md'
RESULT=ROOT/'research/voevodsky/results/direct_mod_two_intersection_gate.json'
u,v,y,P6=s.symbols('u v y P6');c0,c1=s.symbols('c0 c1')
alpha=(1-y**2)*(y**2-u**4);beta=2*(u**2+y**2);gamma=-2*y**2*(u**2+1);h=u*(u+v)*(u+v-4)*P6/s.Integer(4)
k0=s.Matrix([1,0,0,0]);k1=s.Matrix([0,alpha,beta,gamma]);b=k0*(c0+h*c1)+k1*c1
recovered_c1=s.factor(b[1]/alpha);recovered_c0=s.factor(b[0]-h*recovered_c1)
mod2=lambda p:s.Poly(s.expand(p),u,v,y,P6,modulus=2).as_expr()
frame=FRAME.read_text(encoding='utf-8');local=LOCAL.read_text(encoding='utf-8');text=PACKET.read_text(encoding='utf-8')
checks={
 'frame_formulas_sourced':'c_1=\\frac{b_1}{\\alpha}' in frame and 'c_0=b_0-hc_1' in frame,
 'coordinate_recovery':recovered_c1==c1 and recovered_c0==c0,
 'beta_mod2_zero':mod2(beta)==0,
 'gamma_mod2_zero':mod2(gamma)==0,
 'alpha_mod2_nonzero':mod2(alpha)!=0,
 'alpha_nonunit':s.Poly(alpha,u,y,domain=s.ZZ).total_degree()>0,
 'h_denominator_four':s.denom(h)==4,
 'integral_pairings_missing':'No existing artifact supplies this chain-level embedding' in local,
 'thimble_column_missing':'No current artifact supplies such a thimble column' in text,
 'betti_derham_gate':'silently replace an integral Betti comparison by a localized de Rham splitting' in text,
}
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.direct-mod-two-intersection-gate.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'frame_sha256':sha256(FRAME.read_bytes()).hexdigest(),'local_thimble_sha256':sha256(LOCAL.read_bytes()).hexdigest(),'frame':{'k0':['1','0','0','0'],'k1':['0',str(alpha),str(beta),str(gamma)],'c1':'b1/alpha','c0':'b0-h*c1','h':str(h)},'mod2_frame':{'beta':'0','gamma':'0','alpha':str(mod2(alpha))},'checks':checks,'passed':all(checks.values()),'disposition':{'two_integral_intersections':'not computable from current frame','available_duals':'localized rational de Rham coordinates','first_missing_objects':['globally embedded thimble column','integral Betti dual cocycles','Betti-de Rham comparison preserving normalization']}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
