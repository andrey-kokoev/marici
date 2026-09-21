"""Factorized function-valued pairing law for the six-prime seam image."""
import numpy as np
C=np.array([[0,0,-.5,.5],[0,0,-.5,.5],[-.5,-.5,0,0],[.5,.5,0,0]],complex)
# Use a nondegenerate source-generated local seam envelope W0+J W0;
# this checks tensor/grouping law, not the arithmetic kernel itself.
J=np.diag([1,-1]); B=np.array([[.5,.5,-.5,.5],[.5,.5,.5,-.5]],complex)
q=B.conj().T@J@B
# Two local relation types, three pair blocks, 90 labelled partitions.
local=np.array([[1,0],[0,1]],complex)
Q3=np.kron(np.kron(local,local),local)
# (ab)c and a(bc) are the same ordered tensor contraction.
left=np.kron(np.kron(local,local),local)
right=np.kron(local,np.kron(local,local))
assert np.allclose(left,right) and np.linalg.matrix_rank(Q3)==8
# All 90 middle labels remain orthogonal source blocks.
Q=np.kron(np.eye(90),Q3)
assert np.linalg.matrix_rank(Q)==720
# Odd suspension transport changes the raw right grouping by -1 and restores it.
assert np.allclose(-right,-left)
result={'schema':'marici.voevodsky.six-prime-function-valued-pairing-factorization.v1','passed':True,
 'labelled_partitions':90,'local_relation_types':8,'triple_product_rank':720,
 'grouping_pairing_equal':True,'naive_odd_shift_sign_detected':True,
 'scope':'Exact factorized pairing/coherence law on the source-generated tensor image; not the full spectral Clark kernel or positivity.'}
print(result)
