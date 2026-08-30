# The reciprocal-odd curvature carrier is an infinite cyclic dilation module

## Exact band formula

Let

\[
f_j(x)=x^j e^{-\pi x^2},
\qquad
A=x\partial_x,
\qquad
P=A(A+1).
\]

The elementary action is

\[
Af_j=jf_j-2\pi f_{j+2}.
\]

Applying \(A\) once more gives

\[
Pf_j
=
j(j+1)f_j
-
2\pi(2j+3)f_{j+2}
+
4\pi^2f_{j+4}.
\]

Thus \(P\) preserves parity but raises polynomial degree by four with a
nonzero leading coefficient.

## Odd curvature seed

The connection-curvature seed obtained from the even Gaussian is

\[
g_{\mathrm{odd}}
=
8\pi f_1-8\pi^2f_3.
\]

Its cyclic theta-completion carrier is

\[
\mathcal K_{\mathrm{odd}}
=
\overline{\operatorname{span}}
\{P^ng_{\mathrm{odd}}:n\ge0\}.
\]

This carrier is not two-dimensional. Indeed, if a nonzero finite Gaussian
polynomial has highest term \(c f_m\), then its image under \(P\) has
highest term

\[
4\pi^2c f_{m+4}.
\]

No nonzero finite-dimensional subspace of Gaussian polynomials containing
\(g_{\mathrm{odd}}\) is invariant under \(P\).

## First connection column

For reference,

\[
Pf_1
=
2f_1-10\pi f_3+4\pi^2f_5,
\]

and

\[
Pf_3
=
12f_3-18\pi f_5+4\pi^2f_7.
\]

Hence

\[
Pg_{\mathrm{odd}}
=
16\pi f_1
-
176\pi^2f_3
+
176\pi^3f_5
-
32\pi^4f_7.
\]

The first curvature column already reaches degree seven. Any finite packet is
therefore a quotient, truncation, or observer image, never the full invariant
odd carrier.

## Reciprocal grading

The completed comparison domain has the graded form

\[
\mathcal K_{\mathrm{even}}
\oplus
\mathcal K_{\mathrm{odd}}.
\]

The completion operator is diagonal in parity,

\[
P=
\begin{pmatrix}
P_{\mathrm e}&0\\
0&P_{\mathrm o}
\end{pmatrix},
\]

while the ray connection is off-diagonal. Reflection exchanges the two ray
copies of \(\mathcal K_{\mathrm{odd}}\) with a sign. Thus the odd carrier
is exactly where reciprocal orientation can survive without being inserted
as an imaginary endpoint coefficient.

## Consequence for Schur elimination

Earlier finite auxiliary-block models remain valid only as compressed
observers. A source-authorized Schur return must begin with the closed odd
cyclic carrier and then prove that the endpoint incidence sees a controlled
finite-rank or compact part of its resolvent.

The required object is schematically

\[
C_{\mathrm{eo}}
D_{\mathrm o}^{-1}
C_{\mathrm{oe}},
\]

where \(D_{\mathrm o}\) is the Green operator on the full reduced odd
carrier. Replacing \(D_{\mathrm o}\) by a fitted one-coordinate phase cell
is not authorized.

## New analytic gate

The next theorem must establish:

1. a closed Green form on \(\mathcal K_{\mathrm{odd}}\);
2. reflection-odd self-adjoint typing of its auxiliary block;
3. radical compatibility of the even--odd incidence;
4. resolvent control on the incidence range;
5. compactness, determinant class, or a declared rigged-form substitute for
   the Schur return;
6. a uniform bound over primes and compact off-seam parameter sets.

The full odd operator need not be compact. What matters first is whether the
sandwiched return through the endpoint incidence is controlled.

## Hostile

Retain only \(f_1\) and \(f_3\), compute a positive finite auxiliary
matrix, and call it invariant. The next application of \(P\) produces
\(f_5\) and \(f_7\), so the omitted tail can alter the Schur return while
all first-column scalar probes remain unchanged.

## Frontier

The source-native orientation carrier is now explicit at algebraic level:

\[
g_{\mathrm{odd}}
\xrightarrow{\;P\;}
Pg_{\mathrm{odd}}
\xrightarrow{\;P\;}
P^2g_{\mathrm{odd}}
\longrightarrow\cdots.
\]

The first Adams edge depends on a Green/resolvent theorem for this infinite
reciprocal-odd cyclic module, not on another finite phase ansatz.
