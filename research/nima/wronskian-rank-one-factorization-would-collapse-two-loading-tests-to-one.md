# Wronskian rank-one factorization would collapse two loading tests to one

## Source odd column

The completed reciprocal-odd endpoint column is fixed:

\[
j_\theta
=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}.
\]

Suppose the endpoint-to-auxiliary incidence of the eliminated odd carrier
factors through this source column:

\[
C_{p,\mathrm{odd}}
=
j_\theta\,c_p^*,
\]

where \(c_p\) is one typed vector in the reduced odd auxiliary space.

This is the natural rank-one factorization if the Wronskian odd port is the
only endpoint channel entering that auxiliary block.

## Schur return

For either reciprocal sheet, define

\[
q_{p,\pm}
=
\left\langle
c_p,
D_{p,\pm}^{\dagger}c_p
\right\rangle.
\]

Then

\[
R_{p,\pm}
=
C_{p,\mathrm{odd}}
D_{p,\pm}^{\dagger}
C_{p,\mathrm{odd}}^*
=
q_{p,\pm}
|j_\theta\rangle\langle j_\theta|.
\]

Therefore

\[
R_{p,\pm}
=
\frac{q_{p,\pm}}{16}
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\]

The two diagonal loadings are equal:

\[
r_{11,p}^{\pm}
=
r_{22,p}^{\pm}
=
\frac{q_{p,\pm}}{16}.
\]

## One surviving margin

The Stieltjes endpoint norms satisfy

\[
a_p\le b_p.
\]

Consequently both Pauli diagonal residuals are positive exactly when

\[
\frac{q_{p,\pm}}{16}<a_p.
\]

Uniform completion reduces to

\[
\sup_{p,\pm}
\frac{q_{p,\pm}}{16a_p}
<1.
\]

The primitive endpoint, having the smaller source energy, is the controlling
channel. The square endpoint then passes automatically.

This is sharper than treating \(C_p^*e_1\) and \(C_p^*e_2\) as unrelated
incidence vectors.

## Quarter-gap sufficient estimate

If

\[
D_{p,\pm}
\ge
\frac{\delta_{\mathrm{aux}}}{4}I,
\]

then

\[
q_{p,\pm}
\le
\frac4{\delta_{\mathrm{aux}}}
\|c_p\|^2.
\]

A sufficient uniform condition becomes

\[
\|c_p\|^2
<
4\delta_{\mathrm{aux}}a_p.
\]

The factor four is source-fixed by the quarter-amplitude Wronskian column; it
is not an adjustable normalization.

## Pauli-twirled effective frame

Under this rank-one return,

\[
XA_p^{\mathrm{eff}}X
+
YA_p^{\mathrm{eff}}Y
=
2
\begin{pmatrix}
b_p-q_{p,\pm}/16&0\\
0&a_p-q_{p,\pm}/16
\end{pmatrix}.
\]

The odd Schur return loads both Pauli coordinates equally even though it lies
entirely in the endpoint disagreement direction before twirling.

This is precisely why raw disagreement softness does not force loss of the
doubled arithmetic frame.

## Authority condition

The factorization

\[
C_{p,\mathrm{odd}}=j_\theta c_p^*
\]

must be derived from the source Green incidence. Rank one and the correct
returned matrix are not sufficient after the fact.

The theorem must establish:

- the eliminated block is purely reciprocal-odd;
- its endpoint trace lands in \(\mathbb Cj_\theta\);
- the coefficient wall is kept outside this elimination;
- no second zero-trace interior incidence reaches the endpoint plane;
- reciprocal reflection transforms \(c_p\) and \(D_{p,+}\) into their
  minus-sheet counterparts;
- the factorization survives closure and prime completion.

If any even wall or independent interior channel enters \(C_p\), the two
loading tests remain genuinely independent.

## Minimal hostiles

1. The returned matrix has rank one but its endpoint vector is not
   \(j_\theta\).
2. A hidden even-wall incidence adds unequal diagonal loading.
3. The factorization holds algebraically but the closed incidence range gains
   a second endpoint direction.
4. Both sheets have rank one but use incompatible vectors \(c_{p,+}\) and
   \(c_{p,-}\).
5. Fit \(c_p\) from the desired Schur return rather than derive it from the
   Wronskian Green identity.

## Verdict

If the source Wronskian column is the sole endpoint incidence of the odd
auxiliary carrier, the two Pauli Schur margins collapse to one scalar
resolvent inequality:

\[
q_{p,\pm}<16a_p.
\]

The next source audit should therefore test the rank-one factorization of
\(C_{p,\mathrm{odd}}\). Passing it reduces the local completion problem to
the spectral measure of one causal-history vector per prime and reciprocal
sheet.
