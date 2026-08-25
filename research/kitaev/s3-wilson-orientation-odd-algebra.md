# The Wilson D/E pair already spans the complete orientation-odd algebra

Owner: `marici.Kitaev`

## Even and odd sectors

Translation by the sign charge (B) acts on diagonal functions of sector
labels. The eight-dimensional diagonal algebra decomposes as

\[
\mathcal D=\mathcal D^+\oplus\mathcal D^-,
\qquad
\dim\mathcal D^+=6,quad\dim\mathcal D^-=2.
\]

The even algebra consists of functions on the six (B)-translation orbits.
The odd algebra measures the two antisymmetric directions (A-B) and (D-E).

## Wilson basis for orientation

The two odd Wilson coordinates form a basis of the entire odd algebra:

\[
Q_A-Q_B=\frac{W_D+W_E}{6},
\qquad
Q_D-Q_E=\frac{W_D-W_E}{2}.
\]

Both (W_D) and (W_E) change sign under (B\otimes-). Therefore no new
non-Wilson observable is mathematically required. Any minimum faithful family
already contains one of these coordinates, and a trusted sign for that port
selects the (C_2) sheet.

## Canonical normalization

The tensor unit fixes the sign:

\[
W_D(A)=W_E(A)=3=d_D=d_E>0,
\]

whereas

\[
W_D(B)=W_E(B)=-3.
\]

Thus the abstract theory has a canonical orientation: normalize Wilson loops
positively on the vacuum. The ambiguity arises only after forgetting which
sector is the tensor unit or allowing an unobserved interface fault to reverse
the signed Wilson coordinate.

## Operational bottom

The remaining problem is not to invent another observable. It is to derive a
sign-preserving physical constructor. Either:

1. prepare and identify the tensor-unit sector (A), then calibrate
   (W_x(A)=d_x>0); or
2. derive the Wilson sign directly from a microscopic oriented ribbon
   convention and prove the ququart/binary interface preserves it.

Local torus syndrome does not select (A), so the first route is a global
preparation contract. The second is precisely the missing interface
fault-action homomorphism.

## Carrier versus quantum lens

Carrier geometry supplies the (6+2) even/odd splitting of a two-sheet torsor.
The quantum lens identifies the odd coordinates as (W_D,W_E), supplies the
vacuum normalization, and types their physical implementation.

## Falsifiers

- The odd diagonal algebra has dimension other than two.
- (W_D,W_E) fail to span it.
- Either displayed projector-difference identity fails.
- Vacuum Wilson normalization is not (W_x(A)=d_x>0).
- A local torus protocol prepares (A) without a global logical choice.

## Artifacts

- Checker: `checkers/check_s3_wilson_orientation_odd_algebra.py`
- Result: `results/s3-wilson-orientation-odd-algebra.json`
- Result SHA256:
  `2DDE42F63E11CF95A01A80C62916E83C4B818A4C822EFD293091452826ADEE21`
- Graph admission: `ev-000000003525-7ca24ec1-40df-40ea-8433-5c004b63c0b2`
- Ledger: entry 2528, `seqclaim-62fa62bf5d4a09b26ef2ee97`
