# No scalar-weighted reduced exclusion energy is both finite and gapped

## Bounded question

After removing the common vacuum contribution, can the all-prime positive
exclusion curvatures be aggregated into one finite, faithful, completion-stable
energy?

## Canonical vacuum reduction

Let

\[
P_0=|e_1\rangle\langle e_1|.
\]

Since \(P_0\leq P_{p\nmid n}\) for every prime, define the reduced positive
projection

\[
E_p=P_{p\nmid n}-P_0.
\]

It projects onto labels \(n>1\) not divisible by \(p\). For positive weights
\(w_p\), consider

\[
H_w=\sum_pw_pE_p.
\]

On a nonvacuum basis label,

\[
H_we_n=\lambda_ne_n,
\qquad
\lambda_n=\sum_{p\nmid n}w_p.
\]

## Nonsummable weights destroy the domain

Every integer \(n>1\) is divisible by only finitely many primes. If

\[
\sum_pw_p=+\infty,
\]

then

\[
\lambda_n=+\infty
\]

for every \(n>1\). The quadratic form is finite only on the vacuum line among
finite-support packets, so it does not define the required dense coefficient
domain.

## Summable weights lose the gap

Suppose instead

\[
W=\sum_pw_p<\infty
\]

with every \(w_p>0\). Enumerate the primes as \(p_1,p_2,\ldots\) and take the
primorial labels

\[
n_N=\prod_{j=1}^Np_j.
\]

Then

\[
\lambda_{n_N}
=\sum_{j>N}w_{p_j}
\longrightarrow0.
\]

Thus \(H_w\) is pointwise faithful on the vacuum-orthogonal basis but has no
positive lower bound there. Its range is not closed, and normalized primorial
packets escape through increasingly composite labels.

## Finite support loses faithfulness

If only finitely many \(w_p\) are nonzero, any label divisible by every prime
in the support lies in the kernel of \(H_w\). Hence finite aggregation is not
jointly faithful.

## Exact trichotomy

Every positive scalar weighting falls into one of three regimes:

1. nonsummable weights: nonvacuum basis states have infinite energy;
2. summable infinite support: finite and pointwise faithful, but ungapped;
3. finite support: finite and gapped on part of the module, but unfaithful.

No scalar weighted sum is simultaneously finite on the source module,
jointly faithful, and bounded below modulo the vacuum.

## Result

Vacuum subtraction is canonical, but scalar aggregation destroys one of the
properties needed for completion-stable zero confinement. The primitive
exclusion family must remain a product-valued family of ports, or be coupled to
an additional source-derived label energy that penalizes primorial escape.

The logarithmic degree does not automatically repair the problem: its growth
on primorials is large, but adding it changes the proposed boundary identity.
Such a term must arise from the same Green current rather than be inserted as
a convenient graph norm.

## Sharp next gate

Retain the exclusion profile

\[
c\longmapsto(E_pc)_p
\]

before scalar summation and determine whether the completed zero-state
boundary law is componentwise, product-topological, or paired with logarithmic
degree by an exact source identity. A scalar weighted norm cannot decide this
without losing source information or completion stability.
