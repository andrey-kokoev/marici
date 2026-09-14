#!/usr/bin/env python3
"""Exact Hermitian derivation of the forced two-sheet boundary-work identity."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_two_sheet_forced_boundary_work_certificate_20260908.json');args=p.parse_args();checks=0
 # Real and imaginary components of u,v,F,z.
 ur,ui,vr,vi,fr,fi,zr,zi=s.symbols('ur ui vr vi fr fi zr zi',real=True)
 # u'=-zu-F, v'=zv-F.
 upr=-(zr*ur-zi*ui)-fr;upi=-(zr*ui+zi*ur)-fi
 vpr=(zr*vr-zi*vi)-fr;vpi=(zr*vi+zi*vr)-fi
 Jprime=s.expand(2*(ur*upr+ui*upi)-2*(vr*vpr+vi*vpi))
 bulk=ur**2+ui**2+vr**2+vi**2
 # Re(F(conj(u)-conj(v))).
 work=s.expand(fr*(ur-vr)+fi*(ui-vi))
 expected=s.expand(-2*zr*bulk-2*work)
 assert s.expand(Jprime-expected)==0;checks+=1
 # Adding twice the integrated work leaves only transverse drift times bulk.
 dbw_density=s.expand(Jprime+2*work)
 assert s.expand(dbw_density+2*zr*bulk)==0;checks+=1
 # Imaginary spectral drift cancels from the Hermitian current exactly.
 assert zi not in dbw_density.free_symbols;checks+=1
 out={'schema':'marici.rh.two-sheet-forced-boundary-work.v1','status':'forced_green_identity_exact','checks':checks,'equations':'u_prime=-z u-F; v_prime=z v-F','current':'J=|u|^2-|v|^2','work':'Re(F(conj(u)-conj(v)))','identity':'J_prime=-2 Re(z)(|u|^2+|v|^2)-2 Work','combined_defect':'J_prime+2 Work=-2 Re(z) Bulk','claim':'the forcing term and endpoint-current orientation reproduce the declared D_bw convention exactly','consequence':'after integration, D_bw=J(q1)-J(q0)+2R=-2 Re(z) B','boundary':'the missing theorem is still that a completed theta-section zero enforces the integrated boundary-work sewing D_bw=0 on its selected two-sheet response'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'imaginary_drift_cancels':True}))
if __name__=='__main__':main()
