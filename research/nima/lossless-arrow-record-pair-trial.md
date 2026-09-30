# Lossless extended/compact pair: first linear trial

## Objective and assumptions

Test whether an extended twelve-arrow presentation and compact retained records can be related by exact descent and reconstruction. This is a new scalar-potential trial, not the existing triangle coefficient protocol or a particle identification. Four labelled states and all twelve ordered nonidentity pairs are assumed; deriving this realization from the six-arrow seed remains open.

Pin p0=0 and retain q=(p1,p2,p3). Define R by (Rq)_ij=pj-pi. Define D by selecting the three arrows 0->1, 0->2, 0->3.

## Exact result

DR=I3. Consequently RD reconstructs every compatible arrow state x in im(R), and (RD)^2=RD. No auxiliary memory is needed for this restricted information class. All three records are necessary: removing any one lowers reconstruction rank to two. Rank three also gives a lower bound of three scalar records for linear lossless encoding. This is record minimality, not primitive interaction-arrow minimality.

The induced metric is H=R^T R=8I-2J, with eigenvalues 2,8,8. Thus q^T H q equals the squared norm of its twelve-arrow presentation. Reconstruction is an isometry between the compact space with this metric and im(R); it is not a square unitary on the ambient twelve-dimensional space.

## Controls and limits

Generic twelve-arrow data have nine further independent directions and are not reconstructed by RD. In particular, this trial assumes endpoint differences, not independent path history or traversal resource. It cannot replace the existing path-cost model without justification.

As a first coexistence trial, give x and q separate ports and impose x=Rq. The agreement matrix B=[I,-R] gives the positive semidefinite operator L=B^T B on fifteen scalar ports. Its kernel has dimension three, consisting exactly of (Rq,q). This creates two coupled presentations of the same three variables; it does not establish independent bodies, a unique phase identity, binding, or a particle pair.

## Next structural gate

Extend the retained information objective to include the seed's cycle/transport information. Determine which cycle data are reconstructible and which require additional records. Then specify separate supports and dynamics for the extended and compact presentations. Only after those choices can primitive arrow pruning and C(n,3) be meaningfully tested. No n, electron unit cost, or mass ratio follows from this trial.

## Verification

`python research/nima/checkers/check_lossless_arrow_record_pair.py`

The standard-library checker uses exact rational elimination and verifies reconstruction, metric, record deletion controls and joint kernel dimension. It passes. An initial SymPy implementation could not run because that optional package was unavailable; the final checker has no third-party dependencies.
