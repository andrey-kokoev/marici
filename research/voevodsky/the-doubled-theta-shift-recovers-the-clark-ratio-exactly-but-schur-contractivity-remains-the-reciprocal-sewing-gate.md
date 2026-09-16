# The doubled theta shift recovers the Clark ratio exactly, but Schur contractivity remains the reciprocal sewing gate

## One-sided transfer

Let

\[
F(s)=
\int_0^\infty
\Phi(u)e^{-su}\,du.
\]

The weighted shift spectral section is

\[
e_s(u)=e^{-su}.
\]

The two moment observations are

\[
Y_0(s)=
\langle 1,e_s\rangle_\Phi
=
F(s),
\]

\[
Y_1(s)=
\langle u,e_s\rangle_\Phi
=
-F'(s).
\]

Thus the passive shift recovers the required zeroth and first theta moments directly.

## Reciprocal doubling

Use the critical-line spectral coordinate \(z\) and put

\[
s=-iz.
\]

The completed even transform is

\[
X(z)
=
\frac12
\left[
F(s)+F(-s)
\right].
\]

Differentiating gives

\[
iX'(z)
=
\frac12
\left[
F'(s)-F'(-s)
\right].
\]

Therefore the two Clark boundary functions are

\[
E(z)=X(z)+iX'(z)
=
\frac12
\left[
F(s)+F(-s)+F'(s)-F'(-s)
\right],
\]

\[
E^*(z)=X(z)-iX'(z)
=
\frac12
\left[
F(s)+F(-s)-F'(s)+F'(-s)
\right].
\]

These are exactly the codiagonal readouts of the two reciprocal weighted-shift systems and their first-moment observations.

The Clark transfer is consequently

\[
\Theta(z)
=
\frac{E^*(z)}{E(z)}
=
\frac{
F(s)+F(-s)-F'(s)+F'(-s)
}{
F(s)+F(-s)+F'(s)-F'(-s)
}.
\]

No zero product or fitted operator is used. The determinant/readout identification is algebraically complete.

## Control interpretation

Each half-line system has common storage

\[
P=I
\]

and the passive Green balance derived from the theta weight.

The completed Xi system is not one of these half-line systems. It is the reciprocal feedback interconnection of the \(s\) and \(-s\) systems.

The even codiagonal produces \(X\). The odd first-moment codiagonal produces \(iX'\). Their Cayley output is the Clark ratio.

## Why passivity does not yet prove contractivity

One-sided passivity controls each tail in its natural half-plane orientation. Reciprocal doubling couples a stable orientation to its reflected orientation. Passivity of the components does not automatically imply passivity of this feedback interconnection.

The remaining condition is

\[
|E^*(z)|
<
|E(z)|
\]

in the upper half-plane, equivalently

\[
1-|
\Theta(z)
|^2
>0.
\]

Using the exact readouts,

\[
|E(z)|^2-|E^*(z)|^2
=
4|X(z)|^2
\operatorname{Im}
\left(-\frac{X'(z)}{X(z)}\right).
\]

Thus the unresolved condition is precisely passivity of the reciprocal interconnection, not identification of its transfer function.

## Constructed versus open

Constructed:

1. the theta-weighted state space;
2. the shift generator;
3. the common storage operator;
4. the one-sided KYP identity;
5. the zeroth and first moment observations;
6. the reciprocal doubled readout;
7. the exact Clark transfer formula.

Open:

1. positivity of the feedback storage after reciprocal sewing;
2. Schur contractivity of \(\Theta\);
3. positivity of the associated de Branges kernel.

## Next control-theoretic target

Write the doubled state as

\[
\mathbf e_s=
\begin{pmatrix}
e_s\\e_{-s}
\end{pmatrix}
\]

and seek a source-derived off-diagonal storage correction \(K\) such that

\[
P_{\rm dbl}
=
\begin{pmatrix}
I&K^*\\
K&I
\end{pmatrix}
\]

is positive and satisfies the doubled KYP inequality with the Clark incoming and outgoing ports.

Positivity requires

\[
\|K\|\le1.
\]

The diagonal choices alone reproduce the two one-sided energies but miss reciprocal interference. The operator \(K\) is now the precise missing common-storage component.

It must be derived from modular reflection. Choosing it to force \(|E^*|\le|E|\) would be circular.

## Disposition

The physical Xi boundary quotient has been recovered exactly as the transfer function of the reciprocally doubled theta shift. The remaining RH-strength problem is the positive off-diagonal storage coupling for that doubled interconnection.
