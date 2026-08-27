# Doubled valuation energy is an exact local seam detector

## Direct and reciprocal chain states

For one prime (p) and valuation depth (N\ge1), the bordered shift produces
the direct transfer state

\[
x_{q,N}=(I-qS)^{-1}e_0
=
\sum_{k=0}^{N}q^ke_k.
\]

Put

\[
q=p^{-s},
\qquad
r=p^{s-1}.
\]

These are the direct and Fourier--Tate reciprocal characters. Writing

\[
a=|q|^2=p^{-2\operatorname{Re}s},
\qquad
b=|r|^2=p^{2\operatorname{Re}s-2},
\]

their chain energies are

\[
E_N(a)=\lVert x_{q,N}\rVert^2=\sum_{k=0}^{N}a^k,
\]

and (E_N(b)).

## Finite Green identity

The recurrence (x_{q,N}-qSx_{q,N}=e_0) gives the exact defect balance

\[
(1-a)E_N(a)=1-a^{N+1}.
\]

The left boundary is the primitive defect and the last term is the terminal
cutoff defect. Thus the identity retains both boundary ports found in the
common colligation.

## Exact doubled factorization

Subtracting the reciprocal energy gives

\[
E_N(a)-E_N(b)
=
(a-b)H_N(a,b),
\]

where

\[
H_N(a,b)
=
\sum_{k=1}^{N}\sum_{j=0}^{k-1}a^{k-1-j}b^j.
\]

For (a,b>0) and (N\ge1),

\[
H_N(a,b)>0.
\]

Moreover,

\[
\log\frac ab
=
4\left(\frac12-\operatorname{Re}s\right)\log p.
\]

Therefore

\[
\operatorname{sgn}\bigl(E_N(a)-E_N(b)\bigr)
=
\operatorname{sgn}\left(\frac12-\operatorname{Re}s\right).
\]

The doubled valuation energy is zero exactly on the critical seam. Every
prime has the same orientation.

## Infinite-depth local limit

Inside the critical strip, both (a) and (b) lie in ((0,1)), and

\[
E_\infty(a)-E_\infty(b)
=
\frac{a-b}{(1-a)(1-b)}.
\]

Thus the sign survives the valuation-chain limit at each fixed prime.

## Relation to the fourth tower

This supplies the first state-level comparison invariant descending from the
common bordered colligation:

\[
\Delta_{p,N}(s)
=
\lVert x_{p^{-s},N}\rVert^2
-
\lVert x_{p^{s-1},N}\rVert^2.
\]

It is stronger than local transition-phase data: its sign is rigid throughout
each open half-strip and changes only on the Fourier--Tate seam.

## What remains missing

No theorem yet says that a completed theta zero forces the total doubled
valuation energy to vanish. That is the next comparison rung.

The global prime sum also cannot be taken naively. Its leading primitive and
square parts encounter the already identified divergent completion grades.
The correct global object must retain their boundary currents and
archimedean contribution before taking the restricted-product limit.

The target is therefore a source identity of the form

\[
\Xi(s)=0
\Longrightarrow
\Delta_{\mathrm{completed}}(s)=0,
\]

where (Delta_{\mathrm{completed}}) is constructed from the compatible
finite doubled Green identities. Since every finite prime component has the
same strict off-seam sign, such an implication would confine zeros to the
critical line without requiring local scalar-overlap positivity.

## Falsifiers

The route fails if:

- reciprocal sewing selects a different state than (x_{p^{s-1},N});
- archimedean or seam incidence adds an uncontrolled bulk term rather than a
  typed boundary current;
- completion reverses the finite prime orientation;
- a zero controls only a scalar transfer determinant and not the doubled
  energy comparison;
- the terminal defect is discarded before cutoff naturality is proved.

