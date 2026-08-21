# 1556 — The Cubic Loop Zero Mode Cancels Before Bulk Counterterms

## Correction status

This entry replaces the original, incorrect claim that the three cubic
sectors reconstruct \(J_0\) by themselves. The error was omission of the
first subleading inner primitive on the combined-zero-frequency bulk route.

## Hard-to-vary claim

After restoring that route, the three source-normalized cubic sectors have
nonoscillatory second-grade ratio

\[
\boxed{
\text{bulk--bulk}:\text{mixed}:\text{boundary--boundary}=1:-2:1.
}
\]

Therefore

\[
\boxed{c_{0,\rm cubic}^{(2)}=0.}
\]

The printed \(-(1+p^2\eta^2)J_0\) in Eq. (19) cannot come from these three
cubic sectors alone. Its remaining source-defined location is the bulk
counterterm contribution included through
\(\bar H_I=H_I+H_{ct}\) in Eq. (18).

## Finite falsifier

The identity was checked at four independent generic \((q,k)\) samples. Each
sector is a common nonzero unit times \(1,-2,1\), and the sum vanishes below
relative tolerance \(2\times10^{-14}\).

## Artifacts

- `research/benincasa/checkers/finite_time_zero_mode_assembly.rs`
- `research/benincasa/results/finite-time-zero-mode-assembly.json`
- `research/benincasa/checkers/finite_time_bulk_bulk_route_census.rs`

## Narrow conclusion

The cubic boundary completion behaves as a discrete second difference in the
nonoscillatory second grade. Eq. (19) compares the completed cubic loop plus
bulk counterterms, not the cubic sectors alone.

## Next falsifier

Expand the finite-lower-end contribution of the three printed quadratic bulk
counterterms \(c_1,c_2,c_3\) at order \(\eta_0^2\), using the corrected labels
from Entry 1536. Require their zero mode to supply exactly

\[
-(1+p^2\eta^2)J_0
\]

while their oscillatory contribution reduces to the printed \(c_3\) term.
