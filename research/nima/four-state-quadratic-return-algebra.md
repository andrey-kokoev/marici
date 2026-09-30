# Four-state quadratic return algebra: identity and recoverable contrast

## Proposal

Let a=I and let m be a positive integer. Suppose the forward operator b satisfies

    b^2 = I/m + (m-1)b/m.

Then

    (b-I)(b+I/m)=0,
    b^-1 = mb-(m-1)I.

The reverse operator belongs to the same algebra as the forward operator. No new algebra generator is needed. This does not by itself prove that the inverse requires no new physical operations or primitive arrows.

Because the polynomial has distinct roots, a finite-dimensional real or complex realization is diagonalizable, with spectrum contained in {1,-1/m}. Either eigenspace may be absent. The generated algebra has dimension at most two, exactly two when both eigenvalues occur.

For every integer k (including negative k),

    b^k = [1+m(-1/m)^k]/(m+1) I
          + m[1-(-1/m)^k]/(m+1) b.

This is compression of operator words, not a reduction of the information dimension of the states on which they act.

## Concrete realization on the existing four-state support

On m+1 labelled states, let J be the all-ones matrix and set

    b=(J-I)/m.

Each state receives the average of the other m states. Since J^2=(m+1)J, this realization satisfies the quadratic relation. It preserves the constant mode and multiplies every sum-zero contrast by -1/m.

For m=3 there are four states and twelve nonzero directed off-diagonal entries, matching the complete directed tetrahedral endpoint support already generated in `twelve-triangle-positive-geometry.md`. Uniform weights 1/3 are specified here; support compatibility alone does not derive this operator from the seed's execution rules. These four scalar state ports are not the previous twelve independent arrow-value ports.

The reverse is

    b^-1=3b-2I=J-3I.

Its off-diagonal entries are +1 and its diagonal entries are -2. It restores the input exactly after one forward step.

## Explicit retained identity and contrast

Define

    P=(I+mb)/(m+1),
    Q=m(I-b)/(m+1).

The quadratic relation gives

    P^2=P, Q^2=Q, PQ=QP=0, P+Q=I,
    b=P-Q/m,
    b^-1=P-mQ,
    b^-1 b=P+Q=I.

For the uniform realization P=J/(m+1) is the orthogonal constant-mode projector and Q is its contrast complement. At m=3 their ranks are one and three. For a general realization satisfying the polynomial, these are algebraic projectors, not necessarily orthogonal projectors.

Thus a two-dimensional operator algebra acts on a full four-dimensional state space: one identity direction and three recoverable contrast directions. Neither the contrasts nor packet information have been collapsed into two scalar state variables.

## Relevance to lossless descent and opposite flow

The earlier scalar-potential and seed-cycle trials established inverse coordinate maps. The seed-cycle trial then supplied an arbitrary cycle-permutation dynamics. This proposal supplies a more directly motivated forward/return candidate on the four-state support:

    x -> bx -> b^-1 bx=x.

A finite averaging operation need not discard information. This particular averaging is invertible, whereas projection onto P is not. For m>1, b^k approaches P as k tends to infinity, but every finite iterate remains invertible. Its inverse amplifies contrast errors by m^k. For m=1 the contrast alternates without decaying.

Reversibility is not the same as unitarity. For m>1 the contrast eigenvalue has modulus below one, so b cannot preserve any positive-definite inner product on a nonzero contrast eigenspace. The forward-and-return composite is nevertheless exactly I. A quartic Euclidean unitarity constraint on b would incorrectly exclude this lossless finite-step candidate.

## Implementation and pair-construction gates

The inverse is an algebraic linear combination involving subtraction and amplification. It is not a nonnegative stochastic transition for m>1. A proposed retained-arrow realization must explain how signed coefficients and gain are implemented. Algebraic closure does not establish a primitive execution cost.

The direct four-port matrices have twelve forward nonzero entries and sixteen inverse nonzero entries when m>1, including four diagonal entries at m=3. Those are matrix-support counts, not a total cycle ledger: identity wires, typed stage ports and composite implementations require an explicit counting convention.

The next constructive test is to compile the forward and inverse operators using the seed-generated support, trace retained information through a complete cycle, and prune arrows while preserving the declared reconstruction objective. Exact preservation of these particular matrices is a different objective from preservation of arbitrary invertibility; the latter alone does not force a dense support.

This is a concrete recovery mechanism, not yet two physical bodies. The identity/contrast split is not a proton/electron assignment. Distinct supports, allowed dynamics, energy readout and a pair-level C(n,3) remain unconstructed. No mass ratio or preferred n follows from algebra closure alone.

## Verification

    python research/nima/checkers/check_four_state_quadratic_return.py

The standard-library checker tests exact rational identities for m=1 through 6: the quadratic relation, inverse, projector decomposition, ranks, positive and negative power formulas, and forward/return recovery. These finite tests supplement the symbolic derivations above; they are not particle-realization certificates.

Related: `lossless-arrow-record-pair-trial.md`, `seed-cycle-retained-pair-trial.md`, and `twelve-triangle-positive-geometry.md`.
