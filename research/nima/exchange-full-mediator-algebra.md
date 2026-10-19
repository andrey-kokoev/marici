# Adding occupation does not close the fixed-contact mediator binding

## Result

**95 exact checks pass.** The existing occupation and contact-flip operations
are noncommuting, but their fixed-contact representation still cannot retain
the complete exchange mismatch through one global linear intertwiner.

The reason is stronger than the preceding commutation obstruction:

- the six exchange updates generate the entire matrix algebra M6 on mismatch;
- occupation and fixed contact flip generate a six-dimensional operator algebra
  on the eight-dimensional logical-pair/mediator carrier;
- that target decomposes into one two-dimensional singlet/mediator channel and
  six one-dimensional triplet/occupation channels.

Every target invariant channel is too small to carry the irreducible
six-dimensional source response. Mere noncommutativity is insufficient.

## Source certificate

For the existing reduced updates T_i, let D_i=I-T_i. With the existing invertible
K=I+F^T H F,

    D_i = K[:,i] e_i^T,
    D_i D_j = K_ij K[:,i] e_j^T.

All K_ij are nonzero. These 36 products span every six-by-six matrix, verified
by exact rank. Thus the source module has no proper nonzero subspace invariant
under all six updates, over either real or complex scalars.

This is about all port operators on a common carrier, not an assertion that
all products are admissible sequential seed paths.

## Existing richer target tested

On logical pair times one mediator, retain the same singlet projector P and use

    N = I_4 tensor n,
    V = P tensor X.

The checker verifies NV != VN and exactly constructs their unital algebra:

    I, N, P tensor I, P tensor n, P tensor X, P tensor nX.

These six matrices are independent, closed under multiplication, and generated
by N and V. They include the previous signed gates and arbitrary combinations
of the fixed-contact occupation/flip Hamiltonian terms. In finite dimension,
exponentials of such terms also stay in this algebra.

A rational change of pair basis separates the singlet and three triplets.
Every target algebra element preserves the resulting channels. The singlet
supports a full two-dimensional mediator block; each triplet retains only its
two separate occupation lines. The channel projections are jointly faithful.

## Global intertwiner obstruction

Suppose L T_i = V_i L for all source ports, with arbitrary V_i in the target
algebra. Compose L with any target channel projection. Its kernel is invariant
under every T_i, hence is either zero or the entire source by irreducibility.
It cannot be zero: a six-dimensional space cannot inject into a channel of
dimension at most two. Therefore every projected map vanishes. Since the
projections jointly recover the target, L itself vanishes.

This establishes the obstruction without choosing or fitting a port-to-target
assignment. On the original full exchange space, a compatible map can still
retain inactive anchor information; it cannot retain the active mismatch.

## Scope and remaining alternatives

This test is **not** the complete spatial contact model. Relative-coordinate
kinetics, independent spin rotations, moving contact projectors and additional
controls are not in the algebra tested here. Nor does the argument cover a
family of endpoint-dependent intertwiners, history-dependent maps or nonlinear
encodings. Those require their actual operation contracts.

In particular, the newly bound species spin actions may mix singlet and triplet
channels and therefore change this algebra. They must not be assumed to do so
through a physically selected joint schedule merely because candidate matrices
are available.

The result closes the specific proposed repair: adding the existing occupation
operator to a fixed contact flip is not enough. A subsequent adapter must change
the invariant-channel structure, not merely add another noncommuting symbol.
No physical interaction or admission policy is selected by this calculation.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_exchange_full_mediator_algebra.py

Receipt: `results/exchange-full-mediator-algebra.json`.
The exact source exchange comparison is freshly rebuilt. The target logical
algebra is reconstructed from the existing operator equations; the full spatial
contact producer is not rerun. No owner source or contact receipt is modified.
