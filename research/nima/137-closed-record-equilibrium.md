# Closed record equilibrium and equal exchange response

## Closed operation

Whiten the16-dimensional tensor metric and normalize each comparison feature
u_i. Add137 scalar records w_i. Each comparison swaps u_i^T q and w_i,
leaving orthogonal carrier directions and other records unchanged. Its normal
in the153-dimensional joint state is d_i=(u_i-e_i)/sqrt(2), and its matrix is
H_i=I-2 d_i d_i^T. Here e_i denotes the ith record axis.

The joint isotropic covariance C=a I is preserved by every exchange. Each
slot has outgoing and returning budget a, with zero net external input.
The carrier stores16a and records137a. This supplies a passive alternative to
the independent external refresh trial. It requires the specified joint initial
ensemble; closed reversible evolution does not attract arbitrary initial states
to it. The153-dimensional bookkeeping is16+137, not the earlier mass-slot count.

## Fixed information

Common fixed states satisfy w_i=u_i^T q. Stack the rows u_i into U and define
W=(I;U). Its columns span a16-dimensional common fixed space. The orthogonal
projector is F=W(W^T W)^-1 W^T. Every comparison fixes that space pointwise.

The covariance I+F is another stationary ensemble. Its carrier trace is
19.7693654561, compared with16 for I. Mean outgoing arrow/state slot budgets
are1.06523204243 and1.27109733809, compared with1 and1 for I. Both ensembles
have equal outgoing and returning budget for every individual slot.

However, the exchange-difference observable w_i-u_i^T q ignores the common
fixed component. Its variance equals2 for BOTH ensembles and every slot.
Thus marginal stored budget and actual exchange response are different readouts.

## Equal response from strong stationarity

Suppose a real symmetric positive semidefinite covariance C is invariant under
every individual comparison, H_i C H_i^T=C. This is stronger than stationarity
at the end of one fixed sweep.

Since H_i is an orthogonal reflection, invariance implies C commutes with H_i,
so every d_i is an eigenvector of C. If d_i and d_j are not orthogonal, symmetry
of C forces their eigenvalues to agree. The137 normals are independent because
each has its own record component. Their nonorthogonality graph is connected
in the tested four-state construction. Therefore C=a I on the137-dimensional
span of the d_i, while its restriction to the common fixed16-space is arbitrary
positive semidefinite. Cross terms vanish by symmetry.

It follows that

    Var(w_i-u_i^T q) = 2 d_i^T C d_i = 2a

for all137 slots. For a>0, normalizing these exchange variances by their sum
gives exactly1/137. This is a conditional derivation of equal response from a
specific observable and strong stationarity, rather than assumed equal slot
weights. At a=0 there is no exchange fluctuation and that ratio is undefined.

## What this selects and what it leaves open

The model now offers a candidate observable: fluctuation of the mismatch
between the carrier and its retained comparison record. In equilibrium invariant
under every comparison, all normalized responses agree even when marginal
carrier/record budgets differ. The common fixed information can change those
marginals without changing the exchange response.

The physical carrier must still select this comparison operation, the strong
stationarity condition, and this observable as electromagnetic response.
Order-specific periodic covariance is not enough to invoke the argument.
No physical clock, absolute source scale, or observed decimal correction is
derived here. Actual attraction requires a mixing, coarse-graining, or open
system mechanism, beyond these individual reversible exchanges.

## Verification

    uv run research/nima/checkers/check_137_closed_record_stationarity.py

Checks both stationary covariances under all137 exchanges, their budgets and
exchange responses, the16-dimensional fixed projector, independence of the
reflection normals, and connectivity of their nonorthogonality graph, using
NumPy with explicit tolerances. The general covariance implication is the
linear algebra argument above; the numerical graph check is for this fixture.
