"""Independent obstruction: same fine update, incompatible exact admission answers.
No candidate constructor or retirement service import.
"""
from fractions import Fraction as Q
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_scalar_envelope_band import domain,envelopes,cross,value
if not __debug__:raise RuntimeError('Assertions required')
def verify(expected,packet):
 assert packet['expected']==expected
 assert expected['family']=='owning-m4-moment-curve-two-history-v1'
 assert expected['continuation']=='append-fine-upper-then-exact-point-admission'
 n=expected['n'];cut=Q(expected['h_upper']);p=tuple(map(Q,packet['public_point']))
 assert len(p)==2;poly=domain(n)
 assert all(cross(a,b,p)>=0 for a,b in zip(poly,poly[1:]+poly[:1]))
 lo,up=envelopes(n);plane=tuple(map(Q,packet['A_lower_plane']));assert plane in lo
 lower=value(plane,p);assert lower>cut
 # Farkas weights one: -h<=-lower plus h<=cut gives 0<=cut-lower<0.
 assert packet['A_farkas_weights']==['1','1']
 assert Q(packet['A_combined_upper'])==cut-lower<0
 d=Q(1,128**4);r=[Q(1,128**j) for j in range(4)]
 t=tuple(map(Q,packet['B_source_witness']));assert len(t)==4
 assert all(0<=v<=100+2*j for j,v in enumerate(t))
 assert sum(t)==206+d*p[0]
 assert sum(a*b for a,b in zip(t,r))==sum(a*b for a,b in zip((50,51,52,53),r))+d*p[1]
 h=(t[0]-50)/d;assert t[1]==51 and 0<=h<=1 and h<=cut
 assert all(h<=value(a,p) for a in up)
 return {'A_admits_point':False,'B_admits_point':True,
 'conclusion':'Identical retained semantic state cannot answer both exact continuation requests correctly without history-dependent side information.'}
