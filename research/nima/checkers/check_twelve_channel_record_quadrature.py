"""Conditional isometric twelve-arrow quadrature adapter for record feedback.

Graph incidence fixes the relative port. A common-mode port and external i
quadrature convention are explicit choices. No masses or fitted amplitudes.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json
from check_four_packet_cycle import rotate, tensor, norm2, UNIT
from check_four_packet_record_feedback import (
    BASIS, ZERO4, lift, left_rotate, readout, cycle, budget,
    RetainedState, add, scale, basis, transpose, mm,
)

ARROWS=tuple((i,j) for i in range(4) for j in range(4) if i!=j)
# Tetrahedral contrast frame: H^T H=I_3 and H^T 1=0.
H=tuple(tuple(F(v,2) for v in row) for row in
        ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)))
D=tuple(tuple(H[j][k]-H[i][k] for k in range(3)) for i,j in ARROWS)

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def mv(a,v): return tuple(dot(row,v) for row in a)

def ports(x):
    # eta_ij = common/sqrt(12) + difference_ij/sqrt(8).
    # Keep both radical coefficients exact; no floating-point approximation.
    return tuple((x[0],dot(row,x[1:])) for row in D)

def port_budget(x):
    p=ports(x)
    rational=sum((s*s/F(12)+d*d/F(8) for s,d in p),F(0))
    cross=sum((2*s*d for s,d in p),F(0)) # coefficient of 1/sqrt(96)
    assert cross==0
    return rational

def summary(x,t):
    s=x[0]
    # Sum eta= sqrt(12)*s = sqrt(3)*(2s).
    return {'carrier':[str(v) for v in x],
            'eta_sqrt3_coefficient':str(2*s),
            'outer_real':12,'outer_modulus_squared':str(144+12*s*s),
            'times_153_modulus_squared':str(153**2*(144+12*s*s)),
            'sum_channel_modulus_squared':str(12+port_budget(x)),
            'record_budget':str(norm2(t)),
            'baseline_plus_total_budget':str(12+budget(x,t)),
            'conjugate_reciprocity':s==0}

def main():
    assert mm(transpose(H),H)==basis(3)
    assert all(sum(row[k] for row in H)==0 for k in range(3))
    assert mm(transpose(D),D)==tuple(tuple(F(8*(i==j)) for j in range(3)) for i in range(3))
    assert all(sum(row[k] for row in D)==0 for k in range(3))
    reverse={index:ARROWS.index((j,i)) for index,(i,j) in enumerate(ARROWS)}
    samples=[tuple(x) for x in product((F(-1),F(0),F(1,8),F(1)),repeat=4)]
    for x in samples:
        p=ports(x)
        assert port_budget(x)==norm2(x)
        assert sum(d for s,d in p)==0
        assert sum(s for s,d in p)==12*x[0]
        for i,j in reverse.items():
            assert p[j]==(p[i][0],-p[i][1])
            # a_ji=conjugate(a_ij) iff the common imaginary component vanishes.
            assert (p[j]==tuple(-v for v in p[i]))==(x[0]==0)
        total=12+port_budget(x);coherent=144+12*x[0]*x[0]
        assert 12*total-coherent==12*norm2(x[1:])
        # One-time squared preparation has an explicit first-return scalar.
        t=tensor(rotate(x),x)
        y,u=cycle(x,t)
        expected=(x[0]**2+x[1]**2+x[2]**2-x[3]**2)/2
        assert y[0]==expected
        assert 12+port_budget(y)+norm2(u)==12+budget(x,t)
    # Verify graph-readout covariance for all 24 vertex relabellings.
    # This does not assert full S4 covariance of the previously chosen cycle R.
    for perm in permutations(range(4)):
        for x in BASIS:
            potentials=mv(H,x[1:]);new_potentials=tuple(potentials[perm[i]] for i in range(4))
            rotated_contrast=mv(transpose(H),new_potentials)
            xp=(x[0],)+rotated_contrast
            p=ports(x);pp=ports(xp)
            for n,(i,j) in enumerate(ARROWS):
                assert pp[n]==p[ARROWS.index((perm[i],perm[j]))]
    # Exact hidden-scalar return creates the proposed additive imaginary port.
    scalar_hidden=left_rotate(lift(UNIT))
    assert readout(scalar_hidden)==ZERO4
    assert cycle(ZERO4,scalar_hidden)[0]==UNIT
    # Hidden contrast also returns, but cancels in the aggregate of twelve arrows.
    contrast_hidden=left_rotate(lift(BASIS[1]))
    contrast_return,_=cycle(ZERO4,contrast_hidden)
    assert contrast_return==BASIS[1] and sum(d for s,d in ports(contrast_return))==0
    # There is no selected amplitude: scaling a hidden scalar scales eta freely.
    for alpha in (F(0),F(1,10),F(1),F(2)):
        y,t=cycle(ZERO4,scale(scalar_hidden,alpha))
        assert y[0]==alpha and port_budget(y)==alpha*alpha
    small=(F(1,4),F(1,8),F(1,8),F(1,8))
    seeds={'hidden_scalar':(ZERO4,scalar_hidden),
           'hidden_contrast':(ZERO4,contrast_hidden),
           'unit_square':(UNIT,tensor(UNIT,UNIT)),
           'previous_small_square':(small,tensor(rotate(small),small)),
           'balanced_fixed':(UNIT,add(lift(UNIT),left_rotate(lift(UNIT))))}
    histories={}
    for name,(x,t) in seeds.items():
        state=RetainedState(x,t);rows=[];B=12+budget(x,t)
        for n in range(4):
            rows.append(summary(state.carrier,state.record))
            assert 12+port_budget(state.carrier)+norm2(state.record)==B
            if n<3: state=state.advance()
        try: state.advance()
        except ValueError: pass
        else: raise AssertionError('Depth limit must still apply')
        histories[name]=rows
    report={'status':'passed','classification':'conditional isometric common-plus-gradient quadrature adapter; no proton prediction',
            'arrow_count':len(ARROWS),'sample_count':len(samples),'vertex_relabellings':24,
            'channel':'a_ij=1+i*(s/sqrt(12)+(H v)_j/sqrt(8)-(H v)_i/sqrt(8))',
            'outer':'sum a_ij=12+i*sqrt(12)*s',
            'record_return':'s_next=(C L t)_0',
            'square_preparation_eta':'eta_next=sqrt(3)*(s²+q²+p²-z²)',
            'conserved_readout_budget':'sum |a_ij|²+||t||²=12+||x||²+||t||²',
            'reciprocity_gate':'a_ji=conjugate(a_ij) forces s=eta=0 for this adapter',
            'histories':histories,
            'not_derived':['physical quadrature reference and common-mode admission',
                           'seed amplitude selection','physical mass/energy readout',
                           'source typing from Clifford coefficients to endpoint packets']}
    dest=Path(__file__).resolve().parents[1]/'results'/'twelve-channel-record-quadrature.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: exact 12-channel isometry, 256 samples, 24 relabellings, record-to-quadrature return, conserved budget, reciprocity and depth gates. Eta is seed-dependent.')

if __name__=='__main__': main()
