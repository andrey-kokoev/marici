"""Joint half-phase compatibility on six retained directed occurrences.
Reuses existing triangle operations; exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from check_triangle_half_phase import mm, mv, transpose, add, sub, scale
from check_four_packet_record_feedback import rank


def eye(n):
    return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))


def power(a,n):
    result=eye(len(a))
    for _ in range(n):
        result=mm(a,result)
    return result


S=scale(((2,2,-1),(-1,2,2),(2,-1,2)),F(1,3))
I=eye(6)
# ABC=(AB,BC,CA), ADB in shared-edge-first order=(BA,AD,DB).
first=(0,1,2); second=(5,3,4)
local1=tuple(I[i] for i in first)
local2=tuple(I[i] for i in second)
rows=[None]*6
for indexes in (first,second):
    for i,slot in enumerate(indexes):
        rows[slot]=tuple(sum(S[i][k]*I[indexes[k]][j] for k in range(3)) for j in range(6))
U=tuple(rows)
cycles=((F(1),F(1),F(1),F(0),F(0),F(0)),
        (F(0),F(0),F(0),F(1),F(1),F(1)),
        (F(1),F(0),F(0),F(0),F(0),F(1)))
assert mm(local1,U)==mm(S,local1)
assert mm(local2,U)==mm(S,local2)
assert power(U,6)==I
assert mm(transpose(U),U)==I
assert mm(cycles[:2],U)==cycles[:2]
# Require the two-cycle record unchanged at EVERY step, not just the endpoint.
h=(cycles[2],)
constraints=tuple(sub(mm(h,power(U,k)),h)[0] for k in range(1,7))
assert rank(constraints)==2
# One future seam check is weaker than cycle-wide preservation; two suffice.
assert rank(constraints[:1])==1
assert rank(constraints[:2])==2
assert rank(constraints[:2]+constraints)==2
one_step_hostile=next(tuple(map(F,x)) for x in product(range(-1,2),repeat=6)
                      if mv(constraints[:1],tuple(map(F,x)))==(F(0),)
                      and any(mv(constraints[:2],tuple(map(F,x)))))
assert mv(h,mv(U,one_step_hostile))==mv(h,one_step_hostile)
assert mv(h,mv(power(U,2),one_step_hostile))!=mv(h,one_step_hostile)
print('One-step-only hostile:',one_step_hostile)
print('Shared readings at phases 0,1,2:',[mv(h,mv(power(U,k),one_step_hostile))[0] for k in range(3)])
# x=(a,b,c,h-b,h-c,h-a); four independent retained coordinates.
K=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,-1,0,1),(0,0,-1,1),(-1,0,0,1))
assert rank(K)==4
assert mm(constraints,K)==tuple((F(0),)*4 for _ in constraints)
T=tuple(tuple(S[i][j] if i<3 and j<3 else F(i==j) for j in range(4)) for i in range(4))
assert mm(U,K)==mm(K,T)
# Closure under the actual continuation U and its inverse, not only present agreement.
assert mm(power(U,5),K)==mm(K,power(T,5))
assert mm(cycles,mm(U,K))==mm(cycles,K)
assert rank(mm(cycles,K))==2
# Exact relation among cycle records on the compatible subspace.
assert tuple(sum(cycles[i][j]*c for i,c in enumerate((1,1,-3))) for j in range(6))!= (0,)*6
assert mm((tuple(cycles[0][j]+cycles[1][j]-3*cycles[2][j] for j in range(6)),),K)==((0,0,0,0),)
# Decode all admitted states without erasing their nonzero h record.
D=(I[0],I[1],I[2],cycles[2])
assert mm(D,K)==eye(4)
for k in range(6):
    assert mm(D,mm(power(U,k),K))==power(T,k)
metric=mm(transpose(K),K)
assert mm(mm(transpose(T),metric),T)==metric
# h=0 recovers the previously studied oriented-cochain synchronization.
assert tuple(row[:3] for row in K)==((1,0,0),(0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(-1,0,0))
# Full retained interface: local triple, mean seam value, two seam defects.
# Unlike restricting to K, this is an invertible coordinate change on ALL inputs.
record_map=(I[0],I[1],I[2],tuple(F(1,3) for _ in range(6)),
            tuple(local1[1][j]+local2[1][j]-h[0][j] for j in range(6)),
            tuple(local1[2][j]+local2[2][j]-h[0][j] for j in range(6)))
restore=((1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),
         (0,-1,0,1,F(2,3),F(-1,3)),
         (0,0,-1,1,F(-1,3),F(2,3)),
         (-1,0,0,1,F(-1,3),F(-1,3)))
assert mm(record_map,restore)==I==mm(restore,record_map)
record_update=mm(mm(record_map,U),restore)
assert tuple(tuple(row[j] for j in range(4)) for row in record_update[:4])==T
assert all(record_update[i][j]==0 for i in range(4) for j in (4,5))
assert all(record_update[i][j]==0 for i in (4,5) for j in range(4))
defect_update=tuple(tuple(record_update[i][j] for j in (4,5)) for i in (4,5))
assert power(defect_update,6)==eye(2)
defect_metric=((F(1),F(-1,2)),(F(-1,2),F(1)))
assert mm(mm(transpose(defect_update),defect_metric),defect_update)==defect_metric
assert power(defect_update,3)==scale(eye(2),F(-1))
# Exact identification of the two defect coordinates with triangle contrast.
# z=l+t; subtract its common component, reconstructing from (z1-z0,z2-z0).
J=((F(-1,3),F(-1,3)),(F(2,3),F(-1,3)),(F(-1,3),F(2,3)))
Qdiff=((-1,1,0),(-1,0,1))
assert mm(Qdiff,J)==eye(2)
assert mm(S,J)==mm(J,defect_update)
assert mm(transpose(J),J)==scale(defect_metric,F(2,3))
plane_projector=sub(eye(3),tuple((F(1,3),)*3 for _ in range(3)))
assert mm(J,Qdiff)==plane_projector
# The defect is contrast of the SUM of the two triangles, not a new third field.
pair_sum=add(local1,local2)
assert mm(J,record_map[4:])==mm(plane_projector,pair_sum)
# A symmetric decomposition exhibits both independent source factors.
# z=l+t, w=l-t each evolve by the same S; inverse uses halves.
pair_difference=sub(local1,local2)
symmetric=pair_sum+pair_difference
assert rank(symmetric)==6
assert mm(pair_sum,U)==mm(S,pair_sum)
assert mm(pair_difference,U)==mm(S,pair_difference)
assert add(scale(pair_sum,F(1,2)),scale(pair_difference,F(1,2)))==local1
assert sub(scale(pair_sum,F(1,2)),scale(pair_difference,F(1,2)))==local2
# Full operator splits into two common lines plus two identical contrast planes.
assert 6-rank(sub(U,I))==2
assert rank(sub(U,I))==4
print('PASS: exact defect/triangle-contrast intertwiner; induced metrics agree up to 2/3.')
print('PASS: sum and difference triples evolve independently; two common lines plus two contrast planes.')
assert all(power(defect_update,k)!=eye(2) for k in range(1,6))
# Actual seam reading is recovered from the mean and current defects.
assert mm(h,restore)==((0,0,0,1,F(-1,3),F(-1,3)),)
assert tuple(tuple(row[j] for j in range(4)) for row in restore)==K
print('Retained seam-defect update:',defect_update)
print('PASS: full 6 = compatible coordinates 4 + evolving defect records 2; exact reconstruction.')
# A generic input is not admissible and is NOT silently projected.
bad=(F(1),F(0),F(0),F(0),F(0),F(0))
assert any(mv(constraints,bad))
# Extend each individual local update by the prior exact-endpoint policy.
edges=((0,1),(1,2),(2,0),(0,3),(3,1),(1,0))
incidence=tuple(tuple(F(j==v)-F(j==w) for j in range(4)) for w,v in edges)
def lift(indexes,vertices):
    local=tuple(I[i] for i in indexes)
    delta=sub(mm(S,local),local)
    a=tuple(-(2*delta[0][j]+delta[1][j])/3 for j in range(6))
    b=tuple(a[j]+delta[0][j] for j in range(6))
    c=tuple(b[j]+delta[1][j] for j in range(6))
    shifts=[(F(0),)*6 for _ in range(4)]
    for v,row in zip(vertices,(a,b,c)): shifts[v]=row
    result=add(I,mm(incidence,tuple(shifts)))
    assert mm(cycles,result)==cycles
    assert mm(local,result)==mm(S,local)
    assert power(result,6)==I
    return result
F1=lift(first,(0,1,2))
F2=lift(second,(1,0,3))
serial=mm(F2,F1)
assert serial!=mm(F1,F2)
assert mm(cycles,serial)==cycles
assert mm(serial,K)!=mm(U,K)
trace=sum(serial[i][i] for i in range(6))
assert trace.denominator!=1 # Rational finite-order matrix would have integer trace.
assert mm(mm(power(F1,5),power(F2,5)),serial)==I
print('PASS: simultaneous six-step half-phase; maximal cycle-preserving subspace dimension 4.')
print('PASS: all admissible records reconstruct; cycle sums satisfy cABC+cADB=3h.')
print('PASS: previous cochain synchronization recovered at h=0; generic input rejected.')
print('PASS: ordered full-space updates preserve all 3 cycles and have explicit inverse.')
print('Serial trace:',trace,'=> infinite order; serial and simultaneous operations differ.')
