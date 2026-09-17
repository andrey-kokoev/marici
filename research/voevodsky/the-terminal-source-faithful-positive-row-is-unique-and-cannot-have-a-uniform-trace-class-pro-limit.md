# The terminal source-faithful positive row is unique and cannot have a uniform trace-class pro-limit

Fix `L` and let

\[
E_{\gamma,L}:PW_L\to\mathbb C^2,
\qquad E_{\gamma,L}f=(f(\gamma),f(-\gamma)).
\]

The terminal atomic form is

\[
A_{\gamma,L}(f,g)
=\langle E_{\gamma,L}f,E_{\gamma,L}g\rangle,
\]

and its canonical positive representative is

\[
P_{\gamma,L}=E_{\gamma,L}^*E_{\gamma,L}.
\]

## Uniqueness

Suppose a bounded positive operator `V_L` on `PW_L` is source-faithful for the
same terminal row, meaning

\[
\langle V_Lf,f\rangle=A_{\gamma,L}(f,f)
\quad\text{for every }f\in PW_L.
\]

Complex polarization recovers all mixed matrix elements from the diagonal
quadratic form.  Hence

\[
\langle V_Lf,g\rangle=A_{\gamma,L}(f,g)
=\langle P_{\gamma,L}f,g\rangle
\]

for all `f,g`, and therefore

\[
\boxed{V_L=P_{\gamma,L}.}
\]

Thus there is no different positive geometric row realizing the exact same
source functional on the same carrier.  Changing the representative requires
either changing the source map, retaining a relative pair rather than one
positive row, or enlarging the target category.

## Pro-limit obstruction

The two nonzero eigenvalues of `P_{gamma,L}` are

\[
\lambda_\pm={L\over\pi}\pm{\sin(2L\gamma)\over2\pi\gamma},
\]

so

\[
\|P_{\gamma,L}\|_1=\operatorname{Tr}P_{\gamma,L}={2L\over\pi}.
\]

By uniqueness, every exact source-faithful positive representative has this
same trace norm.  Consequently no such representatives form a uniformly
trace-bounded pro-object as `L` tends to infinity.

This is stronger than failure of the two scalar remedies.  It proves that the
terminal `6 -> 7` requirement is impossible in the currently declared
category if it simultaneously demands:

1. the fixed source carrier and exact atomic readout;
2. one ordinary positive operator representative at each level; and
3. a uniformly trace-class pro-limit.

A viable reformulation must use a relative/renormalized positive pair whose
common divergent row is retained and cancelled only after comparison, or a
rigged/source-graph topology in which point evaluation is continuous.  Such a
reformulation must then reprove compatibility with the other three faces; it
is not supplied by signed tetrahedral coherence.
