"""Reconstruct exact quadratic matrices from conjugate replication-field data."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from sympy.polys.domains import ZZ
from sympy.polys.modulargcd import _integer_rational_reconstruction as rr

P=2305843009213693951

def qlift(x):
    z=rr(int(x)%P,P,ZZ)
    if z is None: raise ValueError(f'no rational reconstruction for {x}')
    return Fraction(int(z.numerator),int(z.denominator))

def pair(xp,xm,zp,zm,kind):
    b=((int(xp)-int(xm))*pow((zp-zm)%P,P-2,P))%P
    a=(int(xp)-b*zp)%P
    aa,bb=qlift(a),qlift(b)
    # Convert a+b*r to basis (1,sqrt(discriminant)).
    if kind=='-3': return [str(aa+bb/2),str(bb/2)]
    return [str(aa-bb/2),str(bb/2)]

def lift_array(ap,am,zp,zm,kind):
    if isinstance(ap,list): return [lift_array(x,y,zp,zm,kind) for x,y in zip(ap,am)]
    return pair(ap,am,zp,zm,kind)

def main():
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    d=json.loads(a.source.read_text()); cs=d['results'];out=[]
    for off,kind,field in [(0,'-3','Q(sqrt(-3))'),(2,'5','Q(sqrt(5))')]:
        plus,minus=cs[off],cs[off+1];zp,zm=int(plus['u0']),int(minus['u0'])
        eps=[]
        for ep,em in zip(plus['charts'][0]['strict_transforms'],minus['charts'][0]['strict_transforms']):
            eps.append({'divisor':ep['divisor'],'orientation':1 if ep['divisor']=='D1' else -1,
              'strict_L1_kernel_basis':lift_array(ep['strict_L1_kernel_basis_mod_p'],em['strict_L1_kernel_basis_mod_p'],zp,zm,kind),
              'corner_residue':lift_array(ep['exceptional_corner_residue_mod_p'],em['exceptional_corner_residue_mod_p'],zp,zm,kind),
              'homogeneous_resonance_map':lift_array(ep['oriented_corner_incidence_mod_p'],em['oriented_corner_incidence_mod_p'],zp,zm,kind),
              'augmented_corner_map':lift_array(ep['oriented_augmented_corner_map_mod_p'],em['oriented_augmented_corner_map_mod_p'],zp,zm,kind),
              'augmented_source_order':['kernel_1','kernel_2','principal']})
        out.append({'field':field,'basis':['1',f'sqrt({kind})'],'minimal_polynomial':('r^2-r+1' if kind=='-3' else 'r^2+r-1'),
          'chart':'u=u0+e, v=u0+e*t','frame_transition':'diag(1,1,t,t)',
          'extension_coordinate_order':['00','01','10','11'],'endpoints':eps})
    a.output.write_text(json.dumps({'schema':'marici.gm.exact_quadratic_corner_maps.v1','fields':out},indent=2))

if __name__=='__main__':main()
