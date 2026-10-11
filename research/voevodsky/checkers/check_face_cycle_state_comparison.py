"""Exact comparison of local character cycles and spatial face transport.
Run: uv run --with sympy python THIS_FILE
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

BASE=Path(__file__).resolve().parents[1]


def clean(m):return m.applyfunc(s.simplify)


def main():
    paths={n:BASE/'results'/f for n,f in [('proton','proton_merkle_store.json'),('electron','electron_tetrahedral_spinor_store.json')]}
    raw={n:p.read_bytes() for n,p in paths.items()};data={n:json.loads(r) for n,r in raw.items()}
    obj=data['proton']['objects'];geo=obj[obj[data['proton']['root']]['geometry']]['payload']
    owners={r['outer_arrow']:r['triangle'][0][2:] for r in geo['triangles_and_transports']}
    vertices={k:s.Matrix(v) for k,v in zip('ABCD',[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)])}
    omega=(-1+s.I*s.sqrt(3))/2;chi=(1+s.I*s.sqrt(3))/2
    coeff=s.Matrix([1,omega,s.expand(omega**2)])
    cycle=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
    def real(pair):return s.Rational(pair[0])+s.sqrt(3)*s.Rational(pair[1])
    def complex_value(pair):return real(pair[0])+s.I*real(pair[1])
    sources=[(s.Matrix(list(map(real,n))),s.Matrix([[complex_value(z) for z in row] for row in p]))
             for n,p in zip(data['electron']['normals'],data['electron']['face_projectors'])]
    rows=[]
    for word in ('ABC','ADB','ACD','BDC'):
        a,b,c=[vertices[x] for x in word];f=(a+b+c)/3
        normal=(b-a).cross(c-a);normal=clean(normal/s.sqrt(normal.dot(normal)))
        assert s.simplify(normal.dot(f))>0
        nx,ny,nz=normal
        cross=s.Matrix([[0,-nz,ny],[nz,0,-nx],[-ny,nx,0]])
        rotation=clean(s.eye(3)+s.sqrt(3)*cross/2+s.Rational(3,2)*cross**2)
        assert rotation*a==b and rotation*b==c and rotation*c==a
        assert rotation**3==s.eye(3)
        vectors=[]
        for left,right in zip(word,word[1:]+word[:1]):
            assert owners[left+right]==''.join(sorted(word))
            x=s.Matrix.hstack(f,vertices[left],vertices[right])
            v=clean(x*coeff);local=clean(x*cycle*x.inv())
            assert clean(local*v-omega*v)==s.zeros(3,1)
            assert local!=rotation
            vectors.append(v)
        assert all(clean(rotation*vectors[i]-vectors[(i+1)%3])==s.zeros(3,1) for i in range(3))
        assert clean(sum(vectors,s.zeros(3,1)))==s.zeros(3,1)
        v=vectors[0];norm=s.simplify((v.H*v)[0]);polar=s.I*cross
        positive=(polar**2+polar)/2;negative=(polar**2-polar)/2
        wp=s.simplify((v.H*positive*v)[0]/norm)
        wm=s.simplify((v.H*negative*v)[0]/norm)
        assert wp==s.Rational(4,5) and wm==s.Rational(1,5)
        assert clean(rotation*(positive*v)-s.conjugate(omega)*(positive*v))==s.zeros(3,1)
        assert clean(rotation*(negative*v)-omega*(negative*v))==s.zeros(3,1)
        assert clean(rotation*v-omega*v)!=s.zeros(3,1)
        assert clean(rotation*v-s.conjugate(omega)*v)!=s.zeros(3,1)
        h=s.Matrix([[nz,nx-s.I*ny],[nx+s.I*ny,-nz]])
        p=clean((s.eye(2)-h)/2)
        assert any(clean(normal-n)==s.zeros(3,1) and clean(p-sp)==s.zeros(2) for n,sp in sources)
        spin=clean(s.eye(2)/2-s.I*s.sqrt(3)*h/2)
        assert clean(spin*p-chi*p)==s.zeros(2)
        assert clean(spin**3)==-s.eye(2)
        assert s.simplify(chi**2-omega)==0
        rows.append({'face':''.join(sorted(word)),'oriented_cycle':word,
                     'proton_positive_polarization_weight':str(wp),'proton_negative_polarization_weight':str(wm),
                     'proton_spatial_full_turn':'+I','electron_face_line_step_phase':str(chi),
                     'electron_spatial_full_turn':'-I'})
    report={'verification_passed':True,'source_sha256':{n:sha256(r).hexdigest() for n,r in raw.items()},
            'faces':rows,
            'distinct_operations':'The small-triangle character operator X C X^-1 differs from the spatial face stabilizer rotation.',
            'proton_transport':'AB->BC->CA permutes three triangle records and rotates their ambient vectors; coefficients are equal in co-transported local frames.',
            'proton_ambient_face_sum':'Zero for the three actual selected vectors, despite nonzero individual states.',
            'electron_transport':'The spatial 120-degree lift preserves one face line with phase exp(i*pi/3); three steps give -1.',
            'comparison':'The square of the electron line character equals omega, but omega is only the negative-polarization component character of the original proton vector under spatial rotation, not its whole state.',
            'next_gate':'Compare an explicitly polarization-selected vector sector with the spinor square, retaining discarded components and inter-face transport; do not silently replace the original proton.'}
    (BASE/'results/face_cycle_state_comparison.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
