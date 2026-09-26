"""Generic rational 2x2 companion-matrix trace for one FULL sourced psi component."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
source=json.loads((OUT/'nine-point-complete-four-mass-psi-component-trace.json').read_text());assert source['passed']
fixture=json.loads((ROOT/'research/voevodsky/fixtures/n2mhv-yangian-invariant-constructor-coverage.v1.json').read_text())
assert next(v for v in fixture['cyclic_classes'] if v['id']==9)['formula']=='psi [A,1,2,3,4] [B,5,6,7,8]'
def complete_component(br):
 e0,e1=br(8,5,6,3),br(8,5,6,4)
 f0,f1=br(5,6,3,7),br(5,6,4,7)
 n0,n1=br(1,2,7,3),br(1,2,8,3)
 d0,d1=br(4,1,2,7),br(4,1,2,8)
 A=e0*d1+e1*n1;B=e0*d0+e1*n0-f0*d1-f1*n1;C=-f0*d0-f1*n0
 assert A!=0 and B*B-4*A*C!=0
 # Multiplication by alpha in Q[alpha]/(A*alpha^2+B*alpha+C).
 T=s.Matrix([[0,-C/A],[1,-B/A]]);I=s.eye(2)
 assert all(s.cancel(entry)==0 for entry in A*T*T+B*T+C*I)
 beta=(n0*I+n1*T)*(d0*I+d1*T).inv()
 def aux(seq,name):
  label='A' if name=='A' else 'B';lo,hi=(7,8) if name=='A' else (3,4)
  variable=T if name=='A' else beta
  assert seq.count(label)==1
  return br(*(lo if j==label else j for j in seq))*I+br(*(hi if j==label else j for j in seq))*variable
 na=aux((2,3,4,'A'),'A');nb=aux((6,7,8,'B'),'B')
 da=[aux(seq,'A') for seq in (('A',1,2,3),(2,3,4,'A'),(3,4,'A',1),(4,'A',1,2))]
 da.insert(1,br(1,2,3,4)*I)
 db=[aux(seq,'B') for seq in (('B',5,6,7),(6,7,8,'B'),(7,8,'B',5),(8,'B',5,6))]
 db.insert(1,br(5,6,7,8)*I)
 assert da[2]==na and db[2]==nb
 psi_num=aux(('A',4,1,2),'A')*aux(('B',8,5,6),'B')
 psi_den=psi_num-aux(('A',4,5,6),'A')*aux(('B',8,1,2),'B')
 assert psi_den.det()!=0
 result=psi_num*psi_den.inv()*na**4*nb**4
 for index,factor in enumerate(da+db):
  assert factor.det()!=0, ('cyclic_five_bracket_factor',index)
  result=result*factor.inv()
 assert s.simplify(T*result-result*T)==s.zeros(2)
 return s.factor(s.trace(result)),s.factor(s.trace(result*psi_den*psi_num.inv()))
# Test the frozen nine-point rational target's quotient four-brackets.
import check_nine_point_four_mass_auxiliary_match as previous
traced,_=complete_component(previous.bracket)
assert traced==s.Rational(source['two_branch_component_trace'])
# Independent positive four-dimensional moment-curve datum, no Y from the
# frozen n=9 target. This tests the SAME root-free expression on new inputs.
z=s.Matrix([[j**p for p in range(4)] for j in range(1,9)])
def moment_br(i,j,k,l):return s.Matrix.vstack(z[i-1,:],z[j-1,:],z[k-1,:],z[l-1,:]).det(method='domain-ge')
other,without_prefactor=complete_component(moment_br)
assert other!=0 and other!=traced and without_prefactor!=other
packet={'schema':'marici.nima.four-mass-complete-component-companion-trace.v1','passed':True,
 'generic_rational_formula':'Let Q(alpha)=A alpha^2+B alpha+C from sourced auxiliary brackets, T=[[0,-C/A],[1,-B/A]], beta=(n0 I+n1 T)(d0 I+d1 T)^-1. Substitute alpha=T and beta into sourced psi*[A1234]*[B5678]; trace the complete chi1^4 chi5^4 coefficient as a 2x2 rational-matrix product. This is a root-free rational expression in external four-brackets on the nondegenerate open set.',
 'first_target_trace_matches_prior_exact_packet':True,
 'second_external_four_dimensional_moment_curve_trace':str(other),
 'second_sample_psi_prefactor_is_essential':without_prefactor!=other,
 'claim_boundary':'An explicit global RATIONAL formula for one complete SOURCED four-mass superfunction component as a compact 2x2 companion-matrix trace; NOT a global bosonic target eight-form coefficient or proof of its nilpotent regularity. Source orientation ratio -1 must be applied when comparing to the previously declared cyclic source residue.'}
(OUT/'four-mass-complete-component-companion-trace.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'passed':True,'root_free_global_source_component':True,
 'independent_four_dimensional_sample_nonzero':True,'bosonic_target_form_equated':False},indent=2))
