# Static two-sided rank is only a protocol-relative type

## Correction

The matrix

\[
B_{ij}=q_{\rm out}(X_i)q_{\rm in}(X_j)
\]

proves rank-one representability for the currently declared sewing operation. It does not by itself prove that the residual remains one-dimensional under every admissible continuation.

A later constructor can distinguish two residual presentations having identical present pairings. Therefore

\[
\operatorname{rank}B=1
\]

means only

\[
\text{one-dimensional type relative to the frozen sewing protocol}.
\]

## Complete context lift

Let \(E^*\) be the monoid of admitted constructor words, including whatever shifts, refinements, reversals, and sewings are declared executable. For a residual presentation \(X\), define its two-sided context process

\[
f_X(u,v)=\operatorname{Observe}(uXv).
\]

The relevant Hankel matrix is

\[
H_X(u,v)=f_X(u,v).
\]

The minimal reusable linear type has dimension

\[
\boxed{\dim T_X=\operatorname{rank}H_X,}
\]

when this rank is finite and the context action is closed. The earlier matrix \(B\) is only one finite corner of \(H_X\).

## Congruence gate

Retyping is lawful only if behavioral equivalence is stable under every admitted constructor:

\[
X\sim Y
\Longrightarrow
eX\sim eY
\quad\text{and}\quad
Xe\sim Ye
\]

for all relevant left and right actions \(e\).

At finite context depth \(k\), successor maps generally have the graded type

\[
T_k\xrightarrow{e}T_{k-1},
\]

because applying one constructor consumes one unit of remaining observation depth. A stationary endomorphism \(T\to T\) is authorized only after partition/rank stabilization or an unbounded context-closure theorem.

## Relation to the residual recurrence

The bicharged residual package

\[
(L,q_{\rm in},q_{\rm out})
\]

is sufficient for contiguous rank-one sewing. To claim that it is the next primitive for the larger theory, one must show that every admitted continuation factors through these charges.

If additional contexts raise the Hankel rank, the correct retyped residual is a higher-dimensional state:

\[
(L,q_{\rm in},q_{\rm out})
\rightsquigarrow
(T_X,C_X,O_X).
\]

Thus the recursion remains valid, but its output dimension is protocol-relative.

## Correct higher-level law

```text
Type(X, admitted contexts)
=
minimal stabilized realization of X's complete two-sided behavior.
```

The word “complete” is essential. A finite pairing table certifies only the contexts it contains.

## Existing realization results

This correction aligns the boundary–Pfaffian construction with the repository's prior realization work:

- `research/sontag/finite-authorized-nerode-realization.md`;
- `research/sontag/realization-minimality-factorization.md`;
- `research/kitaev/the-complete-scalar-context-tower-reconstructs-a-minimal-ordered-realization.md`;
- `research/nima/contextual-equivalence-needs-stabilized-congruence.md`.

The new contribution is therefore not the general Hankel-rank theorem. It is the explicit Pfaffian boundary packet furnishing a rank-one residual for its finite sewing contexts, together with graph and cofiber transport that can now be tested for stabilization under the larger constructor alphabet.
