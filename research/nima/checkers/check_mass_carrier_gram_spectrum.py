"""Exact source-Gram spectrum audit: comparison labels versus physical features."""
from pathlib import Path
from contextlib import redirect_stdout
from fractions import Fraction as F
from collections import Counter
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    source=runpy.run_path(str(HERE/'check_proton_electron_comparison_slots.py'))
    runpy.run_path(str(HERE/'check_proton_electron_gram_energy.py'))
slots=source['expanded']; N=len(slots)
G=[[12 if i==j else 1 for j in range(4)] for i in range(4)]
def state(i): return tuple(int(j==i) for j in range(4))
def arrow(e): return tuple(int(j==e[1])-int(j==e[0]) for j in range(4))
def mul(A,v): return tuple(sum(a*x for a,x in zip(row,v)) for row in A)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(v): return dot(v,mul(G,v))
def feature(s,tagged):
    outer,(kind,a,b)=s
    vs=(arrow(outer),arrow(a),arrow(b)) if kind=='arrow' else (arrow(outer),state(a),state(b))
    offset=64 if tagged and kind=='state' else 0
    return {offset+16*i+4*j+k:F(x*y*z) for i,x in enumerate(vs[0]) for j,y in enumerate(vs[1]) for k,z in enumerate(vs[2]) if x*y*z}

def rank(rows):
    pivots={}
    for row in rows:
        row=dict(row)
        while row:
            p=min(row); c=row[p]
            if p not in pivots:
                pivots[p]={k:v/c for k,v in row.items()}; break
            for k,v in pivots[p].items():
                new=row.get(k,F(0))-c*v
                if new: row[k]=new
                else: row.pop(k,None)
    return len(pivots)
tagged_rank=rank(feature(s,True) for s in slots)
untagged_rank=rank(feature(s,False) for s in slots)
assert (tagged_rank,untagged_rank)==(54,42)
# Full directed-arrow frame S=sum_e v_e v_e^T=8I-2*ones.
S=[[sum(arrow(e)[i]*arrow(e)[j] for e in source['E']) for j in range(4)] for i in range(4)]
assert S==[[6 if i==j else -2 for j in range(4)] for i in range(4)]
standard=[arrow((0,i)) for i in (1,2,3)]
for v in standard: assert mul(S,mul(G,v))==tuple(88*x for x in v)
# State frame R=diag(0,1,1,1). R G has nonzero eigenvalues14,11,11.
state_basis=[(0,1,1,1),(0,1,-1,0),(0,1,0,-1)]
state_eigen=[14,11,11]
for v,lam in zip(state_basis,state_eigen):
    gv=mul(G,v); rgv=(0,)+gv[1:]
    assert rgv==tuple(lam*x for x in v)
# Nonzero spectra of F^dagger M F and F F^dagger M agree. Block tags are
# retained and M=G tensor G tensor G on each block. No1836-square matrix needed.
spectrum=Counter({88**3:27})
for _ in standard:
    for a in state_eigen:
        for b in state_eigen: spectrum[88*a*b]+=1
assert spectrum==Counter({681472:27,17248:3,13552:12,10648:12})
assert sum(spectrum.values())==tagged_rank
trace=sum(lam*m for lam,m in spectrum.items())
slot_trace=0
for outer,(kind,a,b) in slots:
    va,vb=(arrow(a),arrow(b)) if kind=='arrow' else (state(a),state(b))
    slot_trace+=norm(arrow(outer))*norm(va)*norm(vb)
assert trace==slot_trace==18741888
smallest=min(spectrum)
ratios={str(F(lam,smallest)):m for lam,m in sorted(spectrum.items())}
assert F(1836) not in [F(lam,smallest) for lam in spectrum]
assert F(trace,smallest)==F(212976,121)
# An explicit coherent dark direction: opposite outer arrows, same inner slot.
s=((0,1),('state',1,1)); t=((1,0),('state',1,1))
a,b=feature(s,True),feature(t,True)
assert all(a.get(k,0)+b.get(k,0)==0 for k in a.keys()|b.keys())
# Independent label energies require a different Hamiltonian/readout, not F.
assert N-tagged_rank==1782
result={
 'status':'passed','classification':'carrier_gram_energy_does_not_select_1836_particle_gap',
 'slot_count':N,'tagged_feature_rank':tagged_rank,'untagged_feature_rank':untagged_rank,
 'gram_hamiltonian_nullity':N-tagged_rank,
 'nonzero_spectrum':{str(k):v for k,v in sorted(spectrum.items())},
 'ratios_to_smallest_nonzero_eigenvalue':ratios,
 'trace_to_smallest_gap':str(F(trace,smallest)),
 'checks':{'source_count_and_gram_checks_fresh':True,'exact_feature_ranks':True,
           'exact_tensor_frame_spectrum':True,'trace_matches_slot_energy_sum':True,
           'coherent_dark_direction':True,'1836_not_a_nonzero_gap_ratio':True},
 'conclusion':'The admitted Gram features yield a conditional positive Hamiltonian with54 nonzero modes and1782 dark label directions, not an1836-unit particle gap. Its nonzero ratios are1,14/11,196/121 and64. Retaining labelled resource costs instead is a different physical realization, requiring its own energy law.',
 'next_falsifier':'Supply a source operation or action beyond the static Gram feature map that makes comparison records physical, fixes their energy metric and selects a conserved particle sector. Static counts and Gram geometry alone do not determine these.'}
out=HERE.parent/'results/mass-carrier-gram-spectrum.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
