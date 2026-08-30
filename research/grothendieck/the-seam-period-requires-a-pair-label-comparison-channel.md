# The Seam Period Requires a Pair-Label Comparison Channel

## Arity audit

The period comparing the two endpoint homotopies is

\[
\mathcal P(h)=\int_0^\infty\lVert h(q)\rVert^2dq.
\]

For a labelled source `h=sum h_n`, polarization gives

\[
\mathcal P(h)
=\sum_n\mathcal P(h_n)
+2\operatorname{Re}\sum_{n<m}
\int_0^\infty\langle h_n(q),h_m(q)\rangle dq.
\]

Therefore an additive list of one-label primitive or square energies does not
determine the seam period. It omits the pair-label interference matrix.

## Smallest hostile pair

Take two scalar labels

\[
h_1(q)=e^{-q},
\qquad
h_2(q)=\varepsilon e^{-q},
\qquad
\varepsilon\in\{+1,-1\}.
\]

In both cases the individual periods are

\[
\mathcal P(h_1)=\mathcal P(h_2)=\frac12.
\]

But their aggregate periods are different:

\[
\mathcal P(h_1+h_2)=2
\quad(\varepsilon=+1),
\qquad
\mathcal P(h_1+h_2)=0
\quad(\varepsilon=-1).
\]

The missing datum is the off-diagonal Gram entry

\[
\int_0^\infty h_1(q)\overline{h_2(q)}dq
=\frac{\varepsilon}{2}.
\]

## Consequence

The final seam-period comparison tower must begin on a pair-label or tensor
square object. It cannot be reconstructed from separately aggregated
one-label currents. Primitive and prime-square channels can contribute only
after a source-derived coproduct, polarization, or Gram constructor lifts them
to this pair space.

This does not add another independent tower to `3+2+2+1`. It identifies the
next rung inside the final `1` tower:

1. scalar seam period;
2. polarized pair-label Gram current;
3. coherence of that current with the two endpoint homotopies;
4. completion of the pair current over all arithmetic labels.

The next test is whether the positive Fock coproduct and Tate sewing derive
the required off-diagonal entries. If they provide only diagonal occupation
weights, the seam-current route fails.

