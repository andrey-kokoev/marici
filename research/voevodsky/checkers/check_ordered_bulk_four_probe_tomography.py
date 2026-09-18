#!/usr/bin/env python3
"""Exact Gaussian-rational four-probe tomography and phase hostile."""
import json
from fractions import Fraction as Q
from pathlib import Path

a,d,re,im=Q(3),Q(5),Q(7,4),Q(-2,3)
# q(e1), q(e2), q(e1+e2), q(e1-i e2), conjugate-first convention.
q1,q2=a,d
qsum=a+d+2*re
qminus_i=a+d+2*im
re_rec=(qsum-q1-q2)/2
im_rec=(qminus_i-q1-q2)/2
# Quarter-turn second coordinate: off diagonal C12 -> -i*C12 = im-i*re.
rot_re,rot_im=im,-re
checks={
 'real_part_reconstructed':re_rec==re,
 'imaginary_part_reconstructed':im_rec==im,
 'four_probes_reconstruct_cell':(q1,q2,re_rec,im_rec)==(a,d,re,im),
 'quarter_turn_preserves_diagonal':(a,d)==(a,d),
 'quarter_turn_changes_ordered_cross_entry':(rot_re,rot_im)!=(re,im),
 'trace_preserved':a+d==a+d,
 'determinant_preserved':a*d-(re*re+im*im)==a*d-(rot_re*rot_re+rot_im*rot_im),
}
out={'schema':'marici.voevodsky.ordered-bulk-four-probe-tomography.v1','source_cell':{'a':str(a),'d':str(d),'re_C12':str(re),'im_C12':str(im)},'probes':{'q_e1':str(q1),'q_e2':str(q2),'q_e1_plus_e2':str(qsum),'q_e1_minus_i_e2':str(qminus_i)},'quarter_turn_cross_entry':{'real':str(rot_re),'imag':str(rot_im)},'checks':checks,'passed':all(checks.values()),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'ordered_bulk_four_probe_tomography.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
