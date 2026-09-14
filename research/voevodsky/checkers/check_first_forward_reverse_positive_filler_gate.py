#!/usr/bin/env python3
"""Exact 2-to-3 forward/reverse incidence and positive-filler gate."""
import json
from fractions import Fraction
from pathlib import Path

def det3(a,b):return 1-2*a*a+2*a*a*b-b*b
def main():
 # Normalized reversal-invariant Toeplitz packet [[1,a,b],[a,1,a],[b,a,1]].
 fixtures=[]
 for name,a,b in [('admitted',Fraction(1,2),Fraction(0)),('hostile',Fraction(9,10),Fraction(-9,10))]:
  lower=2*a*a-1;odd=1-b;even_det=1+b-2*a*a;det=det3(a,b)
  rank2=abs(a)<=1 and abs(b)<=1
  psd=rank2 and odd>=0 and even_det>=0
  fixtures.append({'name':name,'a':str(a),'b':str(b),'all_rank_two_faces_psd':rank2,'reversal_incidence_exact':True,'allowed_b_interval':[str(lower),'1'],'odd_channel_margin':str(odd),'even_channel_margin':str(even_det),'determinant':str(det),'rank_three_positive_filler_exists':psd})
 assert fixtures[0]['rank_three_positive_filler_exists']
 assert fixtures[1]['all_rank_two_faces_psd'] and not fixtures[1]['rank_three_positive_filler_exists']
 result={'schema':'marici.voevodsky.first-forward-reverse-positive-filler-gate.v1','normalized_packet':'[[1,a,b],[a,1,a],[b,a,1]]','reversal_split':{'odd_condition':'1-b >= 0','even_condition':'1+b-2a^2 >= 0'},'positive_filler_interval':'2a^2-1 <= b <= 1','kernel_form':['K(0)-K(2h) >= 0','K(0)(K(0)+K(2h))-2K(h)^2 >= 0'],'fixtures':fixtures,'conclusion':'Forward/reverse incidence sharpens the next reading to an interval, but incidence and positive lower faces alone do not force that interval to contain the source-prescribed reading. The coupled kernel inequality is the first substantive extension gate.'}
 out=Path(__file__).parents[1]/'results'/'first_forward_reverse_positive_filler_gate.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
