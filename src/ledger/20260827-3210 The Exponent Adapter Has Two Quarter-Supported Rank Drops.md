# 3210 — The Exponent Adapter Has Two Quarter-Supported Rank Drops

## Question

Does the universal exponent pencil contain finite support not accounted for by the previously identified rational torsion points?

## Frozen object

At \((X_1,X_2,X_3)=(2,3,4)\), use the source-derived pencil

\[
M(\gamma)=M_0+\gamma M_1
\]

with 720 relation rows and 535 active labelled coordinates.  Append the 36 low-readout rows to form

\[
N(\gamma)=\begin{bmatrix}M(\gamma)\\L\end{bmatrix}.
\]

The relative low-readout rank is

\[
r_{\rm rel}(\gamma)=\operatorname{rank}N(\gamma)-\operatorname{rank}M(\gamma).
\]

No exceptional point or factor was inserted into the source pencil.

## Test

Two independent prime packets, 32003 and 32009, were evaluated by direct sparse elimination at a generic checkpoint and at the two reconstructed quarter points.  Separately, at prime 32003, maximal minors were adapted to the local rank-normal form before taking their gcd.  This prevents a fixed chart from contributing spurious factors.

## Result

At both primes:

\[
\begin{array}{c|c|c|c}
\gamma&\operatorname{rank}M&\operatorname{rank}N&r_{\rm rel}\\
\hline
17&479&505&26\\
-5/4&479&500&21\\
-7/4&479&498&19
\end{array}
\]

The adapted-minor gcd at prime 32003 has degree 266.  Previously certified rational torsion factors account for degree 254.  The residual degree-twelve factor is

\[
D_{\rm adapter}(\gamma)
\sim
(4\gamma+5)^5(4\gamma+7)^7.
\]

Thus the augmented readout loses five directions at \(\gamma=-5/4\) and seven directions at \(\gamma=-7/4\), while the source-relation rank remains regular.

## Narrow conclusion

The finite-field exponent adapter has two additional source-derived quarter-supported readout defects.  They are defects of the augmented readout relative to a regular source module, not rank losses of the source relations themselves.

The characteristic-zero polynomial with the same rational factors is strongly indicated but not proved by the present packet.  An exact rational minor or rank witness remains required before promoting it to a theorem over \(\mathbb Q\).

## Prohibited inference

The multiplicities five and seven must not be identified with five marked denominators and two base directions from dimension matching alone.  No carrier or coefficient interpretation is licensed until the defect spaces are decomposed in the frozen labelled basis.

## Next falsifier

Compute labelled kernel and cokernel packets at \(\gamma=-5/4\) and \(\gamma=-7/4\).  Test their occurrence permutation characters, pole-depth filtration, denominator-level support, and base-normal covariance.  The proposed mechanism survives only if these structures derive the multiplicities without a fitted splitting.

## Evidence

- `research/benincasa/checkers/exponent_adapter_quarter_divisor.py`
- `research/benincasa/results/exponent_adapter_quarter_divisor.json`
- `research/benincasa/results/exponent_adapter_full_pencil_32003.json`
- `research/benincasa/results/exponent_adapter_full_pencil_32009.json`
- `research/benincasa/results/exponent_adapter_adapted_gcd_32003.json`
- `research/benincasa/exponent-adapter-quarter-divisor-conventions.md`

Ledger number authority: `seqclaim-39a97141a783f232b8ac5c5f`.
