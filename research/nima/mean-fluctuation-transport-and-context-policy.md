# Coherent transport of the full mean/fluctuation packet

## Obligation and source operation

The active SCC obligation is **route/coherencer compatibility**, before
mean-only readout descent. This is a finite algebraic construction, not a new
physical observation law or a realization of the complete rung diagram.

Fix the retained137 comparison slots, positive weights w_i summing to1, and an
invertible reference d:A->B with return r=d^-1:B->A. Residuals R_i:A->B are
retained with their slot identities. First declare **same-slot composition**:

    (B diamond A)_i = A_i+B_i+B_i r A_i.

It is the residual of (d+B_i)r(d+A_i) relative to d. Thus its type and order come
from reference composition, not from a desired scalar response. It is associative
and has the zero residual as unit. Same-slot incidence is an input policy;
this construction does not identify slot multiplication with pointwise
multiplication on the marked S4 probe carrier.

## The complete packet and its derived law

Write every retained array exactly as

    mu_A = sum_i w_i A_i,
    a_i = A_i-mu_A,
    sum_i w_i a_i = 0.

The packet (mu_A,{a_i}) retains all records. It is an invertible coordinate
change, not a quotient. For B use mean mu_B and centered records b_i. Define

    K(B,A) = sum_i w_i b_i r a_i.

Direct expansion of the source operation gives the packet transport:

    mu_new = mu_A+mu_B+mu_B r mu_A+K(B,A),
    delta_new_i = a_i+b_i+mu_B r a_i+b_i r mu_A
                  +b_i r a_i-K(B,A).

The second line is centered. Restoring mu_new+delta_new_i gives precisely
(B diamond A)_i. Consequently packet composition is associative and unital:
it is the original associative operation in invertible coordinates.

**The correction is derived from the retained records.** No independent
coupling or higher witness is assigned to it. It is generally a matrix, with
ordered arguments, rather than a scalar variance or a positive norm.

## Coherence through the indexed presentations

Group slots by their source index or their target index, keeping arrow and state
families distinct. Give each family its total mass W_F and normalized conditional
weights. Local packets reconstruct every original member. The correction obeys

    K_global(B,A)
      = sum_F W_F K_F(B,A)
        + sum_F W_F (mu_B,F-mu_B) r (mu_A,F-mu_A).

This is the matrix-valued total-covariance identity. The within-family and
between-family terms together make composition commute with either retained
presentation. Dropping the conditional records generally loses the first term.
The checker verifies reconstruction and these commuting mean routes for both
source- and target-indexed families, with uniform and nonuniform weights.

These are presentation transports on the stated137 records. They are not yet
an identification of the intended horizontal maps9,8,7 with this construction.

## What the multiplicativity defect satisfies

For the bridge-only operation B star A = B r A and linear mean J, let
D(B,A)=J(B star A)-J(B)rJ(A). This is K(B,A). Associativity gives

    D(C star B,A)+D(C,B)rJ(A)
      = D(C,B star A)+J(C)rD(B,A).

Both sides expand to J(C r B r A)-J(C)rJ(B)rJ(A). Constant-reference inputs
have zero defect. This is an exact compatibility identity; it does not assert
that a nonzero response is null-homotopic in the earlier graded model. Nor is
J assumed to supply an algebra action for an ordinary Hochschild complex.
The full packet gives strict transport; mean-only transport requires these
nonzero correction terms and the data from which to compute them.

## Two finite obstructions to discarding the packet

### A normalized mean cannot be a nontrivial same-context character

Let e_i*d be the field equal to d at one slot and zero elsewhere. It is
idempotent under the bridge product. Its mean is w_i*d. Multiplicativity would
require w_i=w_i^2 for every i. Normalization then selects a single slot.
Thus a genuine average over several slots cannot preserve all same-context
products. Rescaling while preserving the unit does not remove this obstruction.
This concerns the declared slot algebra; it does not contradict identity
*evaluation* being multiplicative in a different probe-function algebra.

### Mean plus second-order data is not generally closed

A valid shared-leg fixture puts scalar residuals (1,1,-2) on three arrow rows,
repeated over their eleven outgoing legs, and zero residual elsewhere. Its
sign reversal has the same mean and the same second moment/correction. Both
therefore give the same mean after two self-compositions. After three, their
means differ:

    165/274 * I versus 231/274 * I.

The difference is a retained third-order contribution. A binary correction alone
is not a general replacement for the full packet. This is not proof that every
restricted physical sector needs all moments; such a sector would require its
own closure theorem.

## Why coherence alone does not select independent contexts

A different source operation pairs independent retained contexts (j,i) and
uses product weights w_j*w_i. Its mean composes without a covariance correction.
Flattening context triples gives associative iteration. Same-slot composition
with the full packet is also associative, but generally gives a different mean.

More generally, for a joint incidence/weight law pi_ji with the prescribed
marginals, the mixed contribution is

    mu_B r mu_A + sum_(j,i) pi_ji b_j r a_i.

Diagonal incidence and independent incidence are two distinct policies. Product
incidence removes the correction for every coefficient array. Demanding that
property for arbitrary arrays determines the product weights by coefficient
matching; it does not derive independence from source physics. A single coherent
joint-context construction, rather than unrelated choices of pairwise moments,
is needed for iteration.

A two-context exact example has inputs (+H,-H) and (+K,-K). Both input means
vanish. Shared contexts give K r H; independent contexts give zero. Both policies
have coherent source composition. Requiring coherence alone therefore cannot
choose the physical policy.

## Result and next constructor

We now have a complete, associative **conditional transport law** that retains
fluctuations and generates its readout corrections from them. It commutes with
the tested retained family presentations. There is no need to invent independent
correction coefficients to repair its mean response.

The missing source input is narrower: **which joint context incidence does the
intended comparison generator produce?** Supply that incidence, its weights and
its transport with the records. The covariance correction then follows; it is
not a normalization to tune. A marked-probe multiplication adapter, the intended
horizontal rung maps, a weak-return extension and the physical rung4 metric
remain outside this result.

## Verification

    python research/nima/checkers/check_mean_fluctuation_transport.py
    python research/aspect/scc/scc.py check nima-mean-fluctuation-transport

The checker writes `research/nima/results/mean-fluctuation-transport.json`.
All matrix calculations use exact rational arithmetic. The symbolic expansions
above explain the general identities; finite checks exercise noncommutative
fixtures, two weight laws, both indexed presentations, units and associativity,
second-moment closure failure and the two distinct context policies. No continuum
completion, physical state count or coupling constant is asserted.
