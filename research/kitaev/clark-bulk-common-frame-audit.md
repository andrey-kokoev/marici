# Independent audit of the native Clark common-frame bulk

## Bounded disposition

Grothendieck's Clark packets supply the source datum missing from the abstract
quadrature theorem. With

\[
X=G+f,
\qquad
Y=a\partial_zG,
\]

the two source sheets are already written in one labelled module:

\[
H_a+f=X+iY,
\qquad
H_{-a}+f=X-iY.
\]

Thus no post-transport choice \(P=I\) is fitted to obtain positivity. The
identity is formed before sheet comparison.

## Exact finite matrix

Write \(X=x_r+ix_i\) and \(\partial_zG=z_r+iz_i\). Then

\[
E_+=|X+ia\partial_zG|^2=T+S,
\]

\[
E_-=|X-ia\partial_zG|^2=T-S,
\]

where

\[
T=|X|^2+a^2|\partial_zG|^2,
\qquad
S=2a\operatorname{Im}(X\overline{\partial_zG}).
\]

There is no third quadratic component, and the coefficients are exactly
equal. Their sum has real Gram matrix

\[
\operatorname{diag}(2,2,2a^2,2a^2),
\]

with determinant \(16a^4\). It is positive definite and rank four for real
\(a\ne0\). At \(a=0\) it has rank two, giving the required explicit
degeneration falsifier.

Because the identity is labelwise, every finite labelled cutoff is a direct
sum of these blocks. The checker verifies ranks \(4N\) for \(N=1,2,3,4\);
the symbolic block identity proves the same for every finite \(N\).

## The remaining faithfulness distinction

The Gram matrix is faithful on the **feature packet**

\[
(G+f,a\partial_zG).
\]

This does not alone prove faithfulness on the domain of admissible boundary
states. That stronger statement needs the source map

\[
J_X:\mathcal A_X\longrightarrow
\{(G+f,a\partial_zG)\}
\]

to satisfy \(\ker J_X=0\). Equivalently, a nonzero admissible state must not
obey simultaneously

\[
G+f=0,
\qquad
\partial_zG=0
\]

almost everywhere. Grothendieck's packet correctly identifies this as an
additional differential constraint, but does not yet exclude it as a theorem
on the full admissible state domain.

This is the same distinction as faithful endpoint algebra versus executable
physical control in the topological sector: a positive form on recorded
features cannot detect states erased by the state-to-feature constructor.

## Completion boundary

The finite positive Clark bulk is closed. The RH-bearing remainder consists
of two independent gates:

1. **State-feature injectivity:** \(\ker J_X=0\) at every cutoff and in the
   completed admissible domain.
2. **Completion coercivity:** a lower bound for the completed feature norm
   that does not collapse, after all primitive, \(k=1\), \(k=2\),
   archimedean, and reflection-coboundary defect channels are included.

The finite determinant \(16a^4\) does not control either gate because it is a
matrix on feature coordinates, not a uniform estimate for their construction
from boundary states.

## Falsifiers

- \(a=0\): the Clark derivative feature disappears and the Gram rank drops.
- A nonzero admissible state in \(\ker J_X\): finite feature positivity is
  blind to it.
- A cutoff sequence of normalized admissible states whose feature norms tend
  to zero: completion loses coercivity despite every finite matrix being
  positive definite.
- A surviving non-bulk indefinite residual in the full doubled Green form.

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_clark_bulk_common_frame_audit.py
```

The checker verifies the common-frame expansion, absence of a third quadratic
component, determinant, degeneration, and finite direct-sum ranks exactly.
