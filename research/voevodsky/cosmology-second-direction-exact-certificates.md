# Exact second-direction certificates

## Result

All 390 second-tangent targets that escaped their `nx`-optimized local spans have exact rational words in the complete A12 source image.

The full source rank is 8,793. Each word uses at most five source rows; the largest absolute numerator is 41 and the largest denominator is 1,440. Every word was replayed against integer rows reconstructed by four-prime CRT, with exact zero residual.

Therefore the second tangent `(3,0,-1)` has zero quotient class on all formerly unresolved targets. Since

\[
(-2,0,1)=(1,0,0)-(3,0,-1),
\]

and the `nx` class is exact, the derived unit-normal class is also zero at A12.

## Claim boundary

This proves characteristic-zero absorption in the labelled A12 algebraic presentation. It does not yet transport the new words to all even ambient degrees and does not construct a geometric normal bundle, specialization map, or exceptional Bockstein.

## Disposition

Transport the 390 exact words along both squared-axis maps and verify path independence. Combined with the 834 certificate-local replays, this will decide full integral normal-torsor independence throughout the all-even family.

## Verification

- `research/voevodsky/check_cosmology_second_direction_exact_certificates.py` — exit 0
- `research/voevodsky/results/cosmology_second_direction_exact_certificates.json`
- `research/voevodsky/results/cosmology_second_direction_exact_certificate_words.json` — 390 replayed words
