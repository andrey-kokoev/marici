# Endpoint incidence requires a groupoid cocycle beyond a bare translation trace

## The proposed common-operator gate

Third-order determinant totalization requires primitive and square currents to
be the first two trace coefficients of the same operator whose connected part
enters \(\det_3\). The natural first proposal is to use prime translations on
the tail as that operator.

Let

\[
S_\ell G(q)=G(q+\ell)
\]

and define the endpoint increment

\[
b_G(\ell)
=
(E_\ell-E_0)G
=
G(\ell)-G(0).
\]

For prime powers, \(\ell=k\log p\), and the weighted endpoint current is built
from \(b_G(k\log p)\).

A linear functional on the bare commutative translation algebra can be fitted to these values, but that encoding forgets the moving coefficient state and does not derive the endpoint law.

## Cocycle law

For \(\ell_1,\ell_2\ge0\),

\[
b_G(\ell_1+\ell_2)
=
b_G(\ell_1)
+
b_{S_{\ell_1}G}(\ell_2).
\]

Equivalently,

\[
E_{\ell_1+\ell_2}-E_0
=
(E_{\ell_1}-E_0)
+
(E_{\ell_2}-E_0)S_{\ell_1}.
\]

The coefficient state changes after the first translation. Thus \(b\) is a
one-cocycle of the translation action with values in endpoint functionals. It is not a character of the translation semigroup. A bare linear trace may record its values, but cannot carry this coefficient-state cocycle.

## Why the bare trace model is insufficient

On the commutative semigroup algebra generated only by translations, one may define a linear trace \(\tau_G\) by

\[
\tau_G(S_\ell)=b_G(\ell).
\]

Since \(S_{\ell_1}S_{\ell_2}=S_{\ell_1+\ell_2}\), this would only assign

\[
\tau_G(S_{\ell_1}S_{\ell_2})
=
b_G(\ell_1+\ell_2).
\]

This reproduces the scalar values of powers of one prime block:

\[
\frac1k\tau_G(S_{\log p}^k)
=
\frac1k b_G(k\log p).
\]

The equality is consistent on the bare commutative algebra. However, trace linearity and cyclicity do not encode the transported second segment

\[
b_G(2\ell)
=
b_G(\ell)+b_{S_\ell G}(\ell).
\]

The second term depends on the translated source state. Recording only its fixed trace value erases the coefficient action that supplies interval provenance.

More sharply, on an algebra containing multiplication operators
\(M_f\), the crossed-product relation is

\[
S_\ell M_f=M_{S_\ell f}S_\ell.
\]

A trace would require

\[
\tau_G(S_\ell M_f)=\tau_G(M_fS_\ell),
\]

while endpoint evaluation distinguishes \(f(0)\) from \(f(\ell)\). For generic
\(f\), the boundary functional is not cyclic. Therefore the fitted trace on the bare translation algebra does not extend to an ordinary trace on the full coefficient-sensitive crossed product that represents endpoint incidence.

## Correct categorical carrier

The correct object is the action groupoid of tail states and translations.
Its objects are source states \(G\); an arrow

\[
(G,\ell):G\longrightarrow S_\ell G
\]

carries the boundary cocycle \(b_G(\ell)\).

Composition is

\[
(S_{\ell_1}G,\ell_2)\circ(G,\ell_1)
=
(G,\ell_1+\ell_2),
\]

and the cocycle law becomes

\[
b(G,\ell_1+\ell_2)
=
b(G,\ell_1)+b(S_{\ell_1}G,\ell_2).
\]

This retains exactly the moving coefficient state that a scalar semigroup
trace forgets.

The common operator required for determinant totalization must therefore live
on a groupoid or correspondence carrier that includes both the source state
and its translation arrow.

## From cocycle to determinant line

A one-cocycle exponentiates to a multiplicative arrow character:

\[
\beta(G,\ell)=\exp(b_G(\ell)).
\]

Then

\[
\beta(G,\ell_1+\ell_2)
=
\beta(G,\ell_1)
\beta(S_{\ell_1}G,\ell_2).
\]

This is a genuine line character on the action groupoid. It is not yet the
third-order determinant character because the primitive and square
regularization must be applied grade-wise and the endpoint currents may be
complex.

For the full packet, one needs a regularized groupoid character

\[
\Beta_3(G,\ell)
=
\exp\!\left(
J^{(1)}(G,\ell)+J^{(2)}(G,\ell)
\right)
D_3(G,\ell),
\]

where \(D_3\) is the connected determinant section and all three factors obey
the same transported composition law.

## Prime-power provenance

For one prime,

\[
b_G(k\log p)
=
\sum_{j=0}^{k-1}
b_{S_{j\log p}G}(\log p).
\]

Thus the grade-\(k\) current is a sum over \(k\) translated primitive segments.
It is not \(k\) copies of one fixed scalar segment.

This explains why the square current cannot be identified with
\(\frac12(\operatorname{Tr}K)^2\), nor with the square of one endpoint
increment. Its source form is a transported two-step path.

The factor \(1/k\) in the Euler coefficient averages the complete cyclic
prime-power path; it does not collapse the \(k\) translated segments to an
untyped scalar.

## Relative trace replacement

A determinant construction can still exist through one of two source-derived
repairs:

1. a groupoid determinant functor whose logarithm is the transported cocycle;
2. a crossed-product representation with a boundary trace defect
   \[
   \tau(XY)-\tau(YX)=\partial\tau(X,Y),
   \]
   where the seam interval supplies the declared defect and totalization
   cancels it.

The first route preserves the cocycle directly. The second packages it as a
relative or cyclic-cohomology trace. An ordinary trace with zero defect is
not admissible unless the endpoint orbit collapses to rank one.

## Finite decisive test

For two prime steps \(p,q\), construct the four groupoid arrows based at

\[
G,\quad S_{\log p}G,\quad S_{\log q}G.
\]

Verify

\[
b_G(\log p)
+
b_{S_{\log p}G}(\log q)
=
b_G(\log q)
+
b_{S_{\log q}G}(\log p).
\]

Both sides equal \(b_G(\log p+\log q)\). Then compare the proposed determinant
factors along the two paths.

A valid groupoid determinant must give the same total arrow character while
retaining different intermediate coefficient states. A scalar trace model
that records only the common endpoint passes the equality but fails
provenance.

## Consequence for categorical RH

The previous common-operator gate must be refined. The endpoint currents need
not be ordinary traces of a single state-independent translation operator.
They must be the low-order logarithmic components of one source-derived
groupoid determinant or relative trace-defect packet.

This removes a false target. The next constructor is now exact:

- build the finite prime-translation action groupoid;
- lift its endpoint one-cocycle to a third-order determinant-line character;
- identify the Gaussian Mellin character as its archimedean line component;
- prove completion and reciprocal descent.

## Verdict

Endpoint incidence is naturally a one-cocycle on the translation action
groupoid. Its scalar values can be fitted by a trace on the bare commutative
translation algebra, but that trace forgets coefficient transport and has no
ordinary extension to the full crossed product. Categorical RH therefore needs
a groupoid determinant or a relative trace-defect construction, not a naive
single-operator determinant fitted to endpoint scalars.
