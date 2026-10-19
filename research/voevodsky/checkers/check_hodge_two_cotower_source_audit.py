"""Exact source-interface controls; no construction of Hodge cotowers."""
import json
from fractions import Fraction as Q
from pathlib import Path


def eye(n): return tuple(tuple(Q(i==j) for j in range(n)) for i in range(n))
def scale(a,s): return tuple(tuple(x*s for x in row) for row in a)
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def mul(a,b): return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def transpose(a): return tuple(zip(*a))
def polynomial(a, coeffs):
    result=scale(eye(len(a)),0)
    for c in reversed(coeffs): result=add(mul(result,a),scale(eye(len(a)),Q(c)))
    return result


def main():
    f=((Q(125),Q(0),Q(0)),(Q(0),Q(-117),Q(44)),(Q(0),Q(-44),Q(-117)))
    q=mul(mul(polynomial(f,[15625,70,1]),polynomial(f,[15625,-150,1])),polynomial(f,[-125,1]))
    p=scale(mul(polynomial(f,[10391779,68381]),q),-Q(1,930187500000000000))
    assert p==((0,0,0),(0,1,0),(0,0,1))
    assert mul(p,p)==p and mul(p,f)==mul(f,p)
    x=((0,1),(1,0));z=((1,0),(0,-1));i=eye(2)
    xz,zx=mul(x,z),mul(z,x)
    assert xz==scale(zx,-1) and xz!=zx
    assert mul(transpose(xz),xz)==mul(transpose(zx),zx)==i
    raw=mul(transpose(zx),xz)
    assert raw==scale(i,-1)
    assert scale(raw,-1)==i and raw!=i  # odd-odd vs even interchange
    assert (-1)**(6*6)==1  # cohomological class parity, not codimension parity
    vertices=[(a,b,c,7-a-b-c) for a in range(8) for b in range(8-a) for c in range(8-a-b)]
    assert len(vertices)==120 and (Q(7,4),)*4 not in vertices
    result={'passed':True,'classification':'bounded_source_audit_inconclusive_not_binding',
        'audit_disposition':'inconclusive','fixed_Hodge_projector_matrix_checked':True,
        'quadratic_route_phase_loss_checked':True,'routes_have_nonzero_kernel':False,
        'Koszul_parity_control_checked':True,'lattice_vertex_count':120,
        'mixed_Hodge_lattice_square_constructed':False,
        'first_missing_object':'Indexed Hodge source objects and elementary transfers with typed degrees',
        'Hodge_proved':False,'Hodge_refuted':False}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-two-cotower-source-audit-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
