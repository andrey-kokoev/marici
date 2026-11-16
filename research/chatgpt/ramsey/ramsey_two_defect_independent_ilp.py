"""Independent MILP check of the matching-two-defect/two-filler obstruction.
17+1 hypothetical R(3,6) case. See accompanying 14-case certificate for
finite hand-checkable reduction.
"""
from itertools import combinations
from scipy.optimize import milp
import ramsey_two_filler_ilp as p
# Exactly two cross-B defects, at (u0,v0), (u1,v1).
for i in p.U:
 for j in p.V:
  p.fix[tuple(sorted((i,j)))]=int((i,j) not in ((0,3),(1,4)))
for w,iu,iv in [(16,0,3),(17,1,4)]:
 for i in p.U:p.fix[tuple(sorted((w,i)))]=int(i==iu)
 for j in p.V:p.fix[tuple(sorted((w,j)))]=int(j==iv)
del p.fix[(16,17)]
M,b,c=p.build(True)
print('Constraints:',M.shape,'fixed edges',len(p.fix),flush=True)
r=milp([0]*153,integrality=[1]*153,bounds=b,constraints=c,options={'time_limit':12})
print('MILP:',r.status,r.message,flush=True)
assert r.status==2,'Should be proven infeasible'
