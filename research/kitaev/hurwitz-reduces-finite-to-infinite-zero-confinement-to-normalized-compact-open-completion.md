# Hurwitz reduces finite-to-infinite zero confinement to normalized compact-open completion

## Question

Every finite Euler-stage transition may be invertible and zero-free while its
inverse margin deteriorates.  What is the weakest exact scalar completion law
that prevents an isolated off-seam zero from appearing in the limit?

The answer is substantially weaker than a uniform pointwise inverse bound:
normalized compact-open convergence is enough.

## Hurwitz gate

Let `Omega` be a connected complex domain.  Suppose `f_N` is holomorphic and
zero-free on `Omega`, and

\[
f_N\longrightarrow f
\]

locally uniformly.  Hurwitz's theorem says that either `f` is zero-free or
`f` vanishes identically.

Choose one source-authorized base point `z_0` and normalize

\[
\widetilde f_N(z)=\frac{f_N(z)}{f_N(z_0)}.
\]

If the normalized sections converge locally uniformly, then their limit has
value one at `z_0` and cannot vanish identically.  It is therefore zero-free
throughout `Omega`.

This yields a sharp finite-to-infinite theorem:

> A normalized compact-open completion of zero-free finite sections cannot
> acquire an isolated zero.

No uniform lower bound for `|f_N(z)|` over all cutoffs is required as a
separate hypothesis.  Compact-open convergence plus one surviving
normalization already supplies the qualitative conclusion.

## What inverse escape really means

Inverse-norm escape remains important, but it is not itself the scalar
mechanism by which isolated zeros appear.  Under compact-open scalar
convergence, collapse can only produce the identically zero section.  An
anchored normalization excludes that possibility.

Therefore an isolated completed zero proves that at least one of the
following occurred:

1. the finite sections were not zero-free on one common domain;
2. the completion was not compact-open convergence of those scalar sections;
3. normalization was performed in incompatible moving frames;
4. the completed scalar was reconstructed after an operator or distributional
   limit rather than obtained as its locally uniform scalar limit;
5. the determinant-line transition ceased to be a genuine holomorphic unit.

This is the exact typing of Grothendieck's observation that finite
certification alone cannot settle the limit.  The unresolved point is not
merely small numerical margins.  It is whether the declared completion
functor preserves the holomorphic-unit topology.

## Infinite products

For finite transition units `g_n`, write locally

\[
f_N=f_0\prod_{n\leq N}g_n.
\]

A sufficient source-facing certificate is locally uniform convergence of a
consistent logarithmic cocycle

\[
\sum_n\log g_n.
\]

Equivalently, a standard stronger certificate is convergence of
`sum sup_K |g_n-1|` on every compact `K` after finitely many factors.  The
resulting product is a holomorphic unit.  If the real part of the logarithmic
cocycle tends to negative infinity instead, the product may collapse to zero;
the anchored relative normalization detects and removes only a common scalar
collapse, not a spatially varying failure of convergence.

The logarithms must be typed in one determinant-line frame.  Choosing a new
branch or base frame at every cutoff destroys the cocycle law and makes the
normalization theorem inapplicable.

## Scalar versus operator completion

The Hurwitz gate concerns scalar holomorphic sections.  It does not follow
from strong, weak, graph, or distributional convergence of operator
realizations.  In infinite dimension, invertible operators can converge to a
noninvertible operator through escaping approximate null vectors.  A scalar
determinant reconstructed afterward can consequently acquire a divisor even
though no compact-open limit of finite determinant units existed.

Thus two completion claims must be kept distinct:

- **operator completion:** convergence or closability of the rigged carrier;
- **determinant-line completion:** normalized compact-open convergence of its
  scalar units, natural under the same cutoff maps.

Neither implies the other without a determinant-continuity theorem.

## Role of the missing endpoint effect

Aspect's exact effect compiler finds that current forcing effects have rank
one and leave the pure endpoint line in the behavioral orthogonal complement.
The canonical rigged transpose is algebraically transverse with positive unit
pairing, but is not yet an executable completion-stable perturbation.

This identifies a possible role for reverse incidence in the Hurwitz gate.  A
source-authorized endpoint effect could supply the fixed nonzero base-point
normalization needed to reject total scalar collapse.  It still would not
prove compact-open convergence.  Transversality anchors the determinant line;
normal-family control completes it.

## Normal-family reformulation

Montel's theorem gives a practical decomposition.  It is enough to prove:

1. the normalized finite sections are locally bounded on `Omega`;
2. every convergent subsequence has the same source-derived limit;
3. the base-point value remains one.

Local boundedness produces compact-open subsequential limits.  Source
uniqueness removes subsequence ambiguity.  Hurwitz then makes the common limit
zero-free.

This may be more attainable than direct lower bounds.  It asks for an upper
energy estimate, a normalization port, and uniqueness of the completed
source section.

## Falsifiers

- Pointwise convergence asserted without local boundedness.
- Operator graph convergence substituted for scalar compact-open convergence.
- A base point that moves with the cutoff or crosses determinant frames.
- Cutoff-dependent logarithm branches violating the transition cocycle.
- Local uniform convergence only in the Euler half-plane, followed by
  untyped analytic continuation into the critical domain.
- A normalized family with two different subsequential limits.
- A transverse endpoint observer that is not an executable source operation.
- A completed scalar divisor reconstructed from a limit operator without a
  determinant-continuity theorem.

## Verdict

The finite-to-infinite zero problem has a sharper topological form:

> Do the normalized finite theta/Tate determinant units form a locally
> bounded, source-unique family converging in the compact-open topology on one
> off-seam domain?

If yes, Hurwitz forbids every isolated completed zero there.  If a completed
zero remains possible, the programme must identify exactly which compact-open
completion law fails.  Inverse-norm escape is then a witness to that failure,
not a substitute for its typing.
