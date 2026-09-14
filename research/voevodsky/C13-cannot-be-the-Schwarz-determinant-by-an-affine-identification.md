# C13 cannot be the Schwarz determinant by an affine identification

The four-point positive geometry uses the affine relation

\[
X_{13}+X_{24}=C_{13}.
\]

The rung-four Schwarz obstruction for real Gram coordinates is

\[
D(a,b,c)=ac-b^2.
\]

These have incompatible algebraic degrees. On any open domain of unconstrained Gram data, no affine expression

\[
\alpha a+\beta b+\gamma c+\delta
\]

can equal \(ac-b^2\).

Even on the slice \(b=0\), the mixed second difference of \(ac\) is nonzero, whereas every affine coordinate has zero mixed second difference.

Therefore a direct source-coordinate identification

\[
C_{13}=ac-|b|^2
\]

is impossible within the affine kinematic-space realization.

Three options survive:

1. construct a nonlinear determinant-line lift from the observer square to the positive geometry;
2. prove that the arithmetic source lies on a special slice where the determinant reduces to an affine coordinate;
3. identify \(X_{13},X_{24}\) with eigenvalues or Schur pivots through a separately sourced nonlinear map.

The third option is geometrically attractive:

\[
X_{13}=a,
\qquad
X_{24}=c-\frac{|b|^2}{a}.
\]

Then positivity of both channel coordinates is equivalent to Schwarz positivity. But this Schur coordinate already contains the determinant:

\[
X_{24}=\frac{ac-|b|^2}{a}.
\]

Declaring it without an independent source derivation would merely rename the RH gate.

Hence the next legitimate construction is not an affine equality with \(C_{13}\), but a source-derived determinant-line or Schur-coordinate map whose pullback is the primitive/prime-prime observation square.

## Verification

```text
python research/voevodsky/checkers/check_C13_schwarz_determinant_affine_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_C13_schwarz_determinant_affine_no_go.py`
- `research/voevodsky/results/C13_schwarz_determinant_affine_no_go.json`
