# Four independent signed shifts force unbounded context rank

## Context family

Admit four independent shift directions and endpoint observation. A word of length at most \(k\) produces a signed displacement vector

\[
\nu\in\mathbb Z^4,
\qquad \|\nu\|_1\le k.
\]

For prime logarithmic lengths, distinct vectors give distinct real displacements:

\[
\sum_i\nu_i\log p_i=0
\Longrightarrow
\prod_i p_i^{\nu_i}=1
\Longrightarrow
\nu=0.
\]

After restricting to the half-line, opposite nonzero vectors contribute one nonnegative evaluation position. The number of distinct endpoint contexts is therefore

\[
N_4(k)
=
\frac{1}{2}
\left(
1+
\sum_{j=0}^4 2^j\binom4j\binom kj
\right).
\]

The first values are

\[
1,5,21,65,161,341,645,1121,1825.
\]

## Realization consequence

Point evaluations at distinct locations are linearly independent on the finite broken graph test space. Hence the context observation space has dimension at least \(N_4(k)\).

Since

\[
N_4(k)\sim\frac{k^4}{3},
\]

the endpoint context tower does not stabilize at any finite state dimension when all four independent signed shifts remain admitted.

This contrasts with the translation/reversal protocol, whose Hankel rank stabilizes at two. The difference is not a contradiction:

```text
one common translation generator + reversal -> rank 2
four independently executable labelled shifts -> unbounded rank
```

## Interpretation

The stationary hyperbolic double compresses the common continuous symmetry action. It does not compress the complete labelled word history exposed by independent endpoint evaluations.

Therefore a finite next primitive exists only after one of the following is justified:

- restrict the constructor alphabet;
- quotient labelled shifts through a common displacement action;
- weaken the observation family;
- retain a graded depth-indexed type rather than a stationary finite type;
- prove additional relations that collapse distinct signed words.

Without such a step, the correct realization is an infinite or pro-object.

## Rank audit

For four prime directions:

```text
constructor rank             = 4
continuous orbit rank        = 1
finite-depth observation rank = N_4(k)
unbounded realization rank   = infinite
```

Thus orbit rank alone does not determine behavioral realization rank. Labels and continuation authority matter.

## Verification

```text
python research/coherence/check_signed_shift_context_rank_growth.py
```

Artifacts:

- `check_signed_shift_context_rank_growth.py`
- `signed-shift-context-rank-growth.v1.json`
