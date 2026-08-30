# 2870 — The Full Moving Fiber Retracts the Pointwise Soft-Torsor Pointing

## Physical fiber cycle

Write \(A=a^2\). The two Cayley–Menger roots on the exceptional family are

\[
\frac{A_\pm}{p^2}
=
5+4\kappa\xi
\pm
4\sqrt{(1-\kappa^2)(1-\xi^2)}.
\]

The physical \(a\)-cycle lies between the positive square roots of these two values.

On the exact hostile slice \(\kappa=0\):

\[
\xi=0:
\qquad
\frac{A_-}{p^2}=1,
\quad
\frac{A_+}{p^2}=9,
\]

while

\[
\xi=1:
\qquad
\frac{A_-}{p^2}
=
\frac{A_+}{p^2}
=5.
\]

Thus the physical fiber interval moves with \(\xi\) and collapses at the proposed pointing endpoint \(t=\xi+1=2\).

## Typing correction

The bulk chain is not a product

\[
[0,2]\times\Gamma_a.
\]

For generic fixed \(a\), there is no point of the \(t=2\) fiber on which to impose

\[
F(a,2)=0.
\]

Therefore Entry 2864's pointwise pointing is mistyped before integrating the moving fiber cycle.

## Corrected constructor

The admissible order is:

1. form the Gauss–Manin pushforward
   \[
   I(t)=\int_{\Gamma_a(t)}\Omega;
   \]
2. determine the logarithmic behavior of \(I(t)\) at \(t=0\);
3. point a primitive of the pushed-forward one-form by the base endpoint \(t=2\).

The opposite endpoint may still point the pushforward torsor. It cannot point the pre-pushforward \(a\)-dependent torsor.

## Consequence

Noncyclic and cyclic chart descent of the coordinate \(t\) remain valid, but they do not establish full-cycle compatibility. The next required object is the actual pushed-forward period \(I(t)\), including the moving-cycle endpoint contribution.

## Durable artifacts

- research/benincasa/check_soft_endpoint_full_a_cycle_compatibility.py
- research/benincasa/soft-endpoint-full-a-cycle-compatibility.json

