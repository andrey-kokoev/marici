# The unconditional co-defect is the Krein--Langer model space, and the positive filler exists exactly when its negative part vanishes

## Generalized Schur realization

Before the Clark transfer \(\Theta\) is known to be Schur, the ordinary model space

\[
H^2\ominus\Theta H^2
\]

is not yet an admitted positive Hilbert quotient. The unconditional replacement is the Krein--Langer factorization

\[
\Theta=B^{-1}S,
\]

where \(S\) is Schur and \(B\) is the inner denominator carrying the negative squares.

The associated kernel decomposes into a positive Schur part and a negative Blaschke/model-space part. In finite index, the negative index is

\[
\dim K_B,
\qquad
K_B=H^2\ominus BH^2.
\]

Thus the co-defect can be constructed unconditionally as a Pontryagin-space object. Its negative component is exactly the interior divisor obstruction.

## Existing tetrahedral result

Prior research already identifies the metric residual of the positive tetrahedral lift as

\[
R_r
=
A_{S,r}^*A_{S,r}
-
A_{B,r}^*A_{B,r}.
\]

A positive filler exists exactly when

\[
R_r\ge0.
\]

The translated Gaussian source features are total in the Hardy boundary carrier. Therefore no negative direction in \(K_B\) can be hidden by restricting to the physical source image.

Consequently

\[
R_r\ge0
\]

holds exactly when

\[
K_B=\{0\}.
\]

Equivalently, \(B\) is constant and \(\Theta\) is Schur.

Primary reference:

`research/voevodsky/the-combined-positive-tetrahedral-lift-is-equivalent-to-vanishing-of-the-interior-krein-langer-defect.md`

## Functional interpretation

The signed coherence tetrahedron always closes. Its unconditional filler lives in a Krein or Pontryagin space.

The positive lift asks whether the negative model-space component is absent. Because the source observers are total, no coordinate change, higher successor coherence, or alternative Gram gauge can remove it.

The positive co-defect is therefore not missing from the formalism. It is obstructed by the interior Krein--Langer denominator.

## Endpoint channel

After the interior denominator vanishes, a separate odd endpoint channel can remain. If represented independently, the augmented residual is

\[
R_r^{\rm aug}
=
A_{S,r}^*A_{S,r}
-
b_r^*b_r.
\]

It requires the endpoint leverage inequality

\[
b_r^*b_r
\le
A_{S,r}^*A_{S,r}.
\]

Alternatively, one may include the endpoint direction in a generalized denominator, in which case positivity requires the combined defect to vanish.

## Disposition

The desired construction is already known at the correct unconditional level:

- signed/Pontryagin filler: constructed;
- negative component: \(K_B\);
- positive filler: exists exactly when \(K_B\) vanishes;
- remaining boundary issue after interior positivity: odd endpoint leverage.

Thus the positive coherence element is not recoverable by further formal assembly. Its existence is the substantive zero-confinement theorem.
