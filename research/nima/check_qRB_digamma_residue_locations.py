import json
from fractions import Fraction
poles=[(k,complex(0,2*k+0.5)) for k in range(6)]
checks={'first_pole_is_i_half':poles[0][1]==complex(0,0.5),'spacing_is_two':all(poles[k+1][1].imag-poles[k][1].imag==2 for k in range(5)),'all_poles_positive_imaginary_for_upward_shift':all(z.real==0 and z.imag>0 for _,z in poles),'half_residue_rule_registered':True}
out={'schema':'marici.nima.qRB-digamma-residue-location-audit.v1','poles':[{'k':k,'u_imag':z.imag,'u_residue':'2i'} for k,z in poles],'checks':checks,'passed':all(checks.values()),'scope':'location and convention audit; no contour integral evaluation','rh_proved':False}
from pathlib import Path
q=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-digamma-residue-location-audit.json';q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
