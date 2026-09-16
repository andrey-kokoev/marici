# The Witt obstruction has a nonzero Landau--Widom edge coefficient

## Obstruction function

For the generic projection-pair contraction, positive common-face reduction is obstructed by

\[
\eta(t)
=
\frac{
\sqrt t+
\sqrt{1-t}-1
}{2}.
\]

It satisfies

\[
\eta(0)=\eta(1)=0.
\]

Thus it has no extensive Shannon bulk term in the Landau--Widom trace law. This does not imply that its trace vanishes.

## Widom coefficient

For a one-dimensional prolate contraction \(B_c\), the fixed-function trace law has the form

\[
\operatorname{Tr}f(B_c)
=
C_W\log c
\int_0^1
\frac{f(t)}{t(1-t)}dt
+O_f(1)
\]

when \(f(0)=f(1)=0\).

For \(f=\eta\), define

\[
I_\eta
=
\int_0^1
\frac{\eta(t)}{t(1-t)}dt.
\]

Set

\[
t=\sin^2\theta.
\]

Then

\[
dt=2\sin\theta\cos\theta\,d\theta.
\]

The coefficient becomes

\[
I_\eta
=
\int_0^{\pi/2}
\frac{
\sin\theta+
\cos\theta-1
}{
\sin\theta\cos\theta
}
\,d\theta.
\]

Split the integrand as

\[
(\sec\theta-\tan\theta)
+
(\csc\theta-\cot\theta).
\]

The first integral equals \(\log2\), and the second also equals \(\log2\). Therefore

\[
I_\eta=2\log2.
\]

## Trace asymptotic

Consequently

\[
\operatorname{Tr}\eta(B_c)
=
2C_W(\log2)\log c
+O(1).
\]

The positive-Witt obstruction has a nonzero universal edge coefficient. It is concentrated in the plunge sector and grows logarithmically with the time--band parameter.

## Consequence

The proposed condition

\[
\langle M_\alpha g,
\eta(B_\alpha)M_\alpha g\rangle
\longrightarrow0
\]

cannot be expected without an additional observer-weighted cancellation or normalization theorem. In the unweighted model it is false.

The obstruction is not a negligible regulator error. It is part of the universal positive edge mass.

## Correct decomposition of scales

The absolute fold contains at least three geometrically distinct contributions:

1. the extensive near-one volume bulk;
2. the logarithmic universal plunge edge;
3. the finite Tate/scattering residual.

The first common-face subtraction removes only the volume bulk. Positive Witt obstruction remains at the second scale.

Therefore direct convergence of the once-reduced absolute fold to the finite form of \(|\mathcal A_S|\) is generally impossible.

## Required second common feature

Let \(E_{c}^{edge}\) denote a positive feature whose Gram realizes the universal observer-weighted plunge law. Tate and reference folds must contain isometric copies of this feature.

After identifying those copies, define a twice-reduced residual by removing both:

\[
\text{volume common face}
\quad\text{and}\quad
\text{universal edge face}.
\]

Only that twice-reduced positive form is a candidate for a finite phase-energy boundary.

## Relation to signed relative traces

Signed Tate/reference subtraction automatically cancels universal translation contributions. This is why the relative trace has a finite gamma-derivative boundary even though each positive fold retains logarithmic plunge mass.

The positive lift must reproduce that cancellation through an actual isometric matching of edge features. Entrywise subtraction of divergent Gram matrices is insufficient.

## Observer-weighted target

The next analytic theorem must identify a positive observer-weighted edge Gram \(G_{edge}\) satisfying

\[
\frac1{\log c}
\operatorname{Gram}(E_c^{edge})
\longrightarrow
G_{edge}.
\]

It must then construct a source-natural isometry between the Tate and reference copies of this edge feature.

After this matching, the finite residual can be tested against the target form of \(|\mathcal A_S|\).

## Disposition

The exact Widom coefficient of the principal-angle obstruction is

\[
2\log2.
\]

Hence the obstruction does not decay. It is a universal logarithmic edge layer. The regular completion gate must include a second positive edge matching before any finite absolute-form convergence statement can be valid.
