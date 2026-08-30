# The minimal Mellin chain has continuous finite traces but zero traces at both logarithmic ends

## Scope

The minimal joint graph closes the derivative commuting square. Its trace behavior can now be determined exactly. The result is mixed: finite comoving endpoint traces are continuous, but every Hilbert trace at \(q=\pm\infty\) vanishes. A nonzero wall residue therefore cannot live as an ordinary endpoint value inside the minimal graph.

Let

\[
Q_-=
\left(\partial_q-\frac32\right)
\left(\partial_q-\frac12\right),
\]

\[
P_+=\partial_q^2-\frac14,
\]

and

\[
h=\widehat{\mathsf D}g
=
e^{-q}\left(\partial_q-\frac12\right)g.
\]

The minimal chain norm controls

\[
g,\quad Q_-g,\quad h,\quad P_+h
\]

in \(L^2(\mathbb R)\).

## Elliptic graph equivalence

The Fourier symbol of \(Q_-\) is

\[
(i\xi-\tfrac32)(i\xi-\tfrac12).
\]

Its modulus is bounded below and grows quadratically. Consequently,

\[
\|g\|_2+\|Q_-g\|_2
\]

is equivalent to the standard \(H^2(\mathbb R)\) norm.

Likewise, the symbol of \(P_+\) is

\[
-\xi^2-\frac14,
\]

so

\[
\|h\|_2+\|P_+h\|_2
\]

is equivalent to \(\|h\|_{H^2}\).

Therefore every vector in the minimal chain domain satisfies

\[
g\in H^2(\mathbb R),
\qquad
h\in H^2(\mathbb R).
\]

## Finite traces

Sobolev evaluation gives continuous maps

\[
g\longmapsto g(q_0),
\qquad
g\longmapsto g'(q_0),
\]

and similarly for \(h\), at every finite \(q_0\).

Because the \(H^2\) norm is translation invariant, the evaluation constants may be chosen independently of \(q_0\):

\[
|g(q_0)|+|g'(q_0)|
\le
C\|g\|_{H^2}.
\]

Thus finite comoving endpoint traces are uniformly controlled by the minimal chain graph.

This closes the ordinary finite-interval trace gate.

## End traces vanish

Every \(H^1(\mathbb R)\) function has a continuous representative tending to zero at both ends. Since \(g,h\in H^2\),

\[
g(q),\ g'(q),\ h(q),\ h'(q)
\longrightarrow0
\]

as \(q\to\pm\infty\).

Therefore the ordinary Hilbert boundary form at the logarithmic ends is zero on the minimal chain domain.

In particular, a nonzero constant wall, delta wall, principal-value residue, or seam charge cannot be represented as an ordinary endpoint trace of \(g\) or \(h\) inside this Hilbert graph.

## Constructor consequence

The completed source must distinguish:

1. finite comoving endpoint traces, which are bounded on the minimal graph;
2. logarithmic-end Hilbert traces, which vanish;
3. distributional wall residues, which require an enlarged boundary or dual carrier.

A nonzero wall can be retained by a source-authorized construction such as:

- a boundary triple attached to the maximal operator;
- an affine extension by a fixed singular representative;
- a rigged dual quotient recording asymptotic coefficients;
- or a relative Green form subtracting a declared wall before entering the minimal graph.

It cannot be obtained by merely evaluating a minimal-domain Hilbert vector at \(q=\pm\infty\).

## Minimal versus maximal domain

The trace result also identifies the substantive meaning of the unresolved minimal-versus-maximal question. Enlarging the domain is not needed for finite endpoint evaluation. It is needed only if the source demands nonzero asymptotic boundary data.

Any such enlargement must preserve the chain identity and type the boundary quotient explicitly. Otherwise it reintroduces invisible wall states or an unauthorized normalization.

## Result

The minimal Mellin chain provides a rigorous closed bulk constructor with uniform finite traces:

\[
\mathcal X_{\min}\to
\mathbb C^4,
\qquad
g\mapsto
\bigl(g(q_0),g'(q_0),h(q_0),h'(q_0)\bigr).
\]

But its end trace is identically zero. Hence the wall/seam residue is not bulk Hilbert data; it must be an independently typed boundary object. The next theorem is a boundary-quotient or affine-extension theorem, not another Sobolev estimate.
