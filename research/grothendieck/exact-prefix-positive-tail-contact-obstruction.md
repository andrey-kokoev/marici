# Exact-prefix and positive-tail contact obstruction

## Question

Can a zero or negative shifted-Gaussian observation be shown nonconstructable once part of the arithmetic source is retained exactly and only the remaining positive tail is relaxed?

## Construction

Fix `t=0.275`, the slice already cross-validated at 60 decimal digits against the first 60 critical-line zeros. Split the positive von Mangoldt measure into

\[
\mu_t=\mu_{t,\le P}+\mu_{t,>P}.
\]

The prefix contribution to value, slope, and curvature is evaluated with its actual prime-power phases. The tail is allowed to be any positive measure having its actual moments `M0,M2,M4`. A hypothetical contact must then place its required tail value and slope inside the tail value--slope ellipse and its required curvature below the tail covariance upper bound.

This is a relaxation: failure of tail feasibility excludes the actual arithmetic tail, while feasibility does not construct it.

## Scout

Files:

- `research/grothendieck/checkers/exact_prefix_tail_contact_scout.py`
- `research/grothendieck/results/exact-prefix-tail-contact-scout.json`

The grid has spacing `0.01` on `xi in [0,25]`. The source quadrature uses 256 Gauss--Hermite nodes. The prime-power working cutoff is two million; at this `t`, terms above that cutoff are numerically negligible, but no interval tail certificate is claimed.

## Result

| exact prefix `n <= P` | exact terms | survivor fraction | principal surviving region |
|---:|---:|---:|---|
| 1 | 0 | 0.997 | `[0.07,25]` |
| 2 | 1 | 0.574 | `[0.07,11.47]`, `[16.43,19.36]` |
| 4 | 3 | 0.467 | `[0.07,10.88]`, `[17.16,18.02]` |
| 8 | 5 | 0.392 | principally `[0.29,9.95]` |
| 16 | 8 | 0.340 | principally `[0.33,8.70]` |
| 32 | 15 | 0.212 | principally `[3.39,7.66]` plus short fragments |
| 64 | 27 | 0.076 | principally `[5.29,6.60]` plus short fragments |
| 128 | 44 | 0 | none |

At `P=128`, the relaxed tail still has

\[
M_0^{>128}\approx6.31\times10^{-10},\quad
M_2^{>128}\approx1.56\times10^{-8},\quad
M_4^{>128}\approx3.87\times10^{-7},
\]

but every sampled character is excluded by the tail value--slope ellipse alone.

## Interpretation

The earlier generic moment body looked weak because it discarded all phase information. Retaining only 44 exact prime-power terms collapses the entire sampled contact region on the validated slice. The obstruction is therefore neither a zero-character-only phenomenon nor evidence that all compact characters are intrinsically hard. It is an arithmetic coherence effect carried by a very small source prefix.

This realizes the proposed positive-geometry reframing in a finite relaxed form:

1. the exact prefix is a source-derived positive atomic geometry;
2. the unknown tail remains inside a larger positive-measure cone;
3. contact prescribes an observation of that tail;
4. the prescribed observation lies outside its positive cone.

No use is made of zero locations in the exclusion test. The zero-side calculation only validates the numerical source implementation at selected points.

## Neighborhood stress test

The follow-up checker `prefix128_margin_neighborhood_scout.py` maps the ellipse margin on `t in [0.26,0.29]` with spacing `0.002`. The `P=128` certificate is robust at `t=0.26--0.264` and `0.268--0.276`; representative minimum margins are `31.18`, `1.54`, `2.00`, and `0.229`. It develops small feasible islands near `xi approximately 5` at `t=0.266` and from `t=0.278` upward. Even at `t=0.29`, however, `98.4%` of the character grid is excluded.

Thus the residual corridor is not centered at zero character. It is a narrow moving band near character five for this prefix and parameter neighborhood. The appropriate certificate should adapt the exact prefix size by box instead of forcing one global cutoff.

Additional files:

- `research/grothendieck/checkers/prefix128_margin_neighborhood_scout.py`
- `research/grothendieck/results/prefix128-margin-neighborhood-scout.json`

## Adaptive-prefix closure of the island

The checker `adaptive_prefix_residual_island_scout.py` retests only `xi in [4.5,6.2]` over `t in [0.264,0.300]` at finer spacings. With `P=128`, it reproduces the moving feasible island. With `P=256`, every sampled point is excluded and the minimum ellipse margin over the entire grid is `18.08`. Prefixes 512 and 1024 increase the margin further but are unnecessary for this region.

This gives a two-level finite architecture: use 44 exact terms through 128 on ordinary boxes, and at most 70 exact terms through 256 on the residual island. The large `P=256` margin is a better first interval-certification target than the marginal `P=128` boxes.

Additional files:

- `research/grothendieck/checkers/adaptive_prefix_residual_island_scout.py`
- `research/grothendieck/results/adaptive-prefix-residual-island-scout.json`

## Elementary infinite-tail majorant

To remove dependence on enumerating the tail through two million, use `Lambda(n) <= log(n)` and, once the summand is decreasing,

\[
\sum_{n>P}\frac{(\log n)^{j+1}}{\sqrt n}
e^{-(\log n)^2/(4t)}
\le f_{j,t}(P)+
\int_{\log P}^{\infty}y^{j+1}e^{y/2-y^2/(4t)}\,dy.
\]

The checker `integer_majorant_tail_scout.py` substitutes these deliberately loose all-integer upper bounds for the actual prime tail moments on the residual island. Prefix 256 leaves a few feasible points, but prefix 512 excludes the complete grid with minimum sampled ellipse margin above `2.17e5`. Thus 117 exact prime-power terms suffice even when the remaining infinite prime-power tail is replaced by an elementary majorant over every integer.

Additional files:

- `research/grothendieck/checkers/integer_majorant_tail_scout.py`
- `research/grothendieck/results/integer-majorant-tail-scout.json`

## Interval-certification obstruction

The first Arb box attempt is recorded in `arb_local_contact_box.py` and `arb-local-contact-box.json`. On the numerically weakest cell centered at `(t,xi)=(0.298,5.35)` with radii `(0.001,0.0025)`, direct natural interval evaluation expands the required tail coordinates to intervals of order one, although their point values are of order `1e-10`. The resulting lower margin is `-1` and proves nothing.

This is dependency inflation, not scientific counterevidence: the endpoint, digamma block, and 117 prefix terms vary substantially across the box and cancel pointwise. Enclosing each block independently destroys their correlation. Refining ordinary boxes until the width is below the `1e-10` residual would require an impractical number of cells.

Python-flint exposes certified `acb.integral`, so rigorous digamma quadrature is available. The missing numerical object is instead a correlated Taylor or affine enclosure of the combined residual

\[
(A/C-R_{\le P},\,-A'/C-I_{1,\le P}),
\]

followed by an interval lower bound for its normalized squared norm. Certification must expand the combined residual about each box center and enclose its derivatives; it must not interval-enclose the three cancelling blocks separately.

Additional files:

- `research/grothendieck/checkers/arb_local_contact_box.py`
- `research/grothendieck/results/arb-local-contact-box.json`

## Stable dual-witness discovery

A first dual-witness grid built from double-precision source residuals failed on 515 of 6,120 cells because source cancellation corrupted the witness direction. This is a witness-generation defect: the normalized tail scale amplifies source errors.

The replacement `stable_dual_witness_scout.py` computes the same residual stably as actual tail plus the first-60-zero value and derivative. The zero side is used only to discover witness directions; it is not admissible certificate evidence. Frozen center witnesses then separate all four corners of every one of the 6,120 cells, with minimum corner dual margin `8.65`.

This demonstrates that a moderately sized atlas of fixed separating hyperplanes exists at the sampled resolution. The source-only verifier need not rediscover their directions. It must verify each frozen scalar witness through the combined Taylor enclosure described above.

Additional files:

- `research/grothendieck/checkers/dual_witness_cell_scout.py`
- `research/grothendieck/results/dual-witness-cell-scout.json`
- `research/grothendieck/checkers/stable_dual_witness_scout.py`
- `research/grothendieck/results/stable-dual-witness-scout.json`

## Source-only Taylor test of the weakest cell

The weakest atlas cell has center `(0.299,4.5025)`, radii `(0.001,0.0025)`, and frozen witness approximately

\[
(\alpha,\beta)=(6.81774492766686\times10^{12},
-9.972284718881238\times10^{11}).
\]

`dual_witness_taylor_scout.py` reevaluates this witness entirely from the endpoint, digamma integral, 117-term prefix, and elementary infinite-tail majorant at 60 decimal digits. It obtains center margin `9.85057`; the four corner margins agree with the stable discovery calculation and have minimum `8.64764`. A deliberately pessimistic quadratic estimate using absolute first- and second-derivative contributions gives lower margin `8.54462` on the cell.

This is not yet a certificate because the derivative estimates are finite differences and the quadratures are not interval enclosed. It does establish that a second-order combined Taylor enclosure has ample room: the remainder budget may consume more than eight normalized units before separation fails.

Additional files:

- `research/grothendieck/checkers/dual_witness_taylor_scout.py`
- `research/grothendieck/results/dual-witness-taylor-scout.json`

## Arb center certificate

`arb_dual_witness_center.py` now evaluates the weakest cell center with certified `acb.integral` on `|y|<=8` and Arb arithmetic for the endpoint and all 117 prefix terms. After reserving `1e-27` absolute error for each omitted Gaussian-digamma tail coordinate and using the rounded tail-moment bounds `M0<=1.3e-13`, `M2<=5e-12`, Arb returns

\[
D_{\alpha,\beta}(0.299,4.5025)
\in 9.6480298922185\mathbin{+/-}2.28\times10^{-14}.
\]

Both conditions are now discharged by Arb checkers. For the digamma tail, the recurrence and convergent series give

\[
|\psi(1/4+iu/2)|
\le \gamma+4+\frac{\pi^2}{6}|1/4+iu/2|.
\]

Closed Gaussian tail moments then bound the omitted value coordinate by `6.05e-29` and the slope coordinate by `5.32e-28`, both below `1e-27`. Separately, the all-integer integral majorant gives `M0<=1.070e-13` and `M2<=4.294e-12`, below the rounded constants consumed by the center verifier. The weakest center is therefore machine-certified from source data without a zero-location premise. This separates completed point certification from continuum Taylor certification.

Additional files:

- `research/grothendieck/checkers/arb_dual_witness_center.py`
- `research/grothendieck/results/arb-dual-witness-center.json`
- `research/grothendieck/checkers/digamma_gaussian_tail_bound.py`
- `research/grothendieck/results/digamma-gaussian-tail-bound.json`
- `research/grothendieck/checkers/integer_tail_moment_arb_bound.py`
- `research/grothendieck/results/integer-tail-moment-arb-bound.json`

## Certified character-direction Taylor cell

At fixed `t=0.299`, `arb_dual_x_taylor_cell.py` constructs the degree-six Taylor polynomial of the combined dual witness on

\[
|\xi-4.5025|\le0.0025.
\]

Endpoint and prefix coefficients are computed by Arb power series. Digamma coefficients are certified integrals of the corresponding polygamma derivatives on `|y|<=8`. A triangle bound for the seventh-order remainder gives `0.847`. The resulting dual-margin enclosure has lower endpoint

\[
8.643088549819968\ldots>0.
\]

This proves that correlated Taylor arithmetic eliminates the dependency inflation seen in natural intervals. `polygamma_gaussian_tail_bounds.py` now discharges the remaining condition through order seven using

\[
|\psi^{(k)}(z)|
\le k!\left(4^{k+1}+\frac{4^k}{k}\right),
\qquad \Re z=1/4,
\]

and Arb evaluation of the Gaussian tail. The largest normalized Taylor-coefficient tail is below `2.98e-27`; the Taylor checker reserves `1e-26`. The character interval is therefore fully source-certified at fixed `t=0.299`.

Additional files:

- `research/grothendieck/checkers/arb_dual_x_taylor_cell.py`
- `research/grothendieck/results/arb-dual-x-taylor-cell.json`
- `research/grothendieck/checkers/polygamma_gaussian_tail_bounds.py`
- `research/grothendieck/results/polygamma-gaussian-tail-bounds.json`

## Parameter-direction Taylor coefficients

`arb_dual_t_series_scout.py` constructs the degree-ten `t` series of the same combined dual witness at fixed `xi=4.5025`. The digamma dependence is composed as a power series in `t`; each coefficient is then enclosed by certified `acb.integral` on `|y|<=8`. On

\[
|t-0.299|\le0.001,
\]

the enclosed polynomial part lies between `8.61978` and `10.67628`. Terms of degrees seven through ten contribute less than `9.94e-11` in absolute value on this interval. Thus the second continuum direction also preserves a large positive margin when correlation is retained, and increasing the truncation degree from six to ten leaves the displayed range unchanged.

This remains a coefficient-level result rather than a certificate. It needs an order-eleven `t` remainder, omitted mixed `t`--polygamma Gaussian-tail bounds, and bivariate composition with the character Taylor model. The observed high-order contribution localizes the proof obligation but does not bound the uncomputed remainder.

Additional files:

- `research/grothendieck/checkers/arb_dual_t_series_scout.py`
- `research/grothendieck/results/arb-dual-t-series-scout.json`

## Parameter remainder core

`arb_t_remainder_bound.py` evaluates the order-eleven combined coefficient with the Taylor base itself ranging over the full `t` cell. This encloses the Lagrange-form core remainder rather than extrapolating from observed coefficients. After multiplication by `0.001^11`, the endpoint, finite prefix, and `|y|<=8` digamma contribution are bounded by `5.43e-10` in normalized dual margin.

This is negligible against the polynomial lower margin `8.61978`. Direct Arb interval rectangles on `8<=|y|<=20` bound the mixed-tail remainder by `8.38e-44`. Beyond 20, even the deliberately enormous envelope `1e100(1+|y|)^11` gives a Gaussian remainder below `4.07e-91`. `mixed_t_coefficient_envelope.py` derives the actual coefficient bound `2.36e83` from composition counts, `t^{-1/2}` coefficients, and polygamma bounds, discharging that condition. The omitted tails of polynomial coefficients one through ten contribute less than `7.95e-17`. The composite `dual-t-interval-manifest.json` therefore passes: at `xi=4.5025`, contact is excluded for every `t in [.298,.300]`. The bivariate rectangle composition remains separate.

Additional files:

- `research/grothendieck/checkers/arb_t_remainder_bound.py`
- `research/grothendieck/results/arb-t-remainder-bound.json`
- `research/grothendieck/checkers/mixed_t_polygamma_far_tail.py`
- `research/grothendieck/results/mixed-t-polygamma-far-tail.json`
- `research/grothendieck/checkers/mixed_t_coefficient_envelope.py`
- `research/grothendieck/results/mixed-t-coefficient-envelope.json`
- `research/grothendieck/checkers/mixed_t_polynomial_tail_bounds.py`
- `research/grothendieck/results/mixed-t-polynomial-tail-bounds.json`
- `research/grothendieck/checkers/check_dual_t_interval_manifest.py`
- `research/grothendieck/results/dual-t-interval-manifest.json`

## First bivariate rectangle certificate

The bivariate step can avoid a full two-variable Taylor algebra. Starting from the certified `t` line at `xi=4.5025`, bound the character derivative of the same scalar dual witness uniformly in `t` and apply the mean-value inequality.

`arb_dual_x_derivative_t_series.py` encloses the degree-ten derivative polynomial between `57.43` and `68.51` on `t in [.298,.300]`. Its order-eleven core remainder is below `1.35e-8`; the mixed polynomial tails are below `1.01e-12`, the `8<=|y|<=20` order-eleven tail is below `5.80e-44`, and the established far-tail envelope applies. Using the rounded derivative bound `68.507001` across character radius `0.0025` gives the rectangle lower margin

\[
8.6197-10^{-9}-68.507001(0.0025)
=8.4484324965>0.
\]

The composite rectangle manifest therefore passes on

\[
(t,\xi)\in[0.298,0.300]\times[4.5000,4.5050].
\]

This is the first source-only two-dimensional contact-exclusion box produced by the positive-tail separation architecture.

Additional files:

- `research/grothendieck/checkers/arb_dual_x_derivative_t_series.py`
- `research/grothendieck/results/arb-dual-x-derivative-t-series.json`
- `research/grothendieck/checkers/arb_dual_x_derivative_remainder.py`
- `research/grothendieck/results/arb-dual-x-derivative-remainder.json`
- `research/grothendieck/checkers/dual_x_derivative_mixed_tail_bounds.py`
- `research/grothendieck/results/dual-x-derivative-mixed-tail-bounds.json`
- `research/grothendieck/checkers/check_dual_rectangle_manifest.py`
- `research/grothendieck/results/dual-rectangle-manifest.json`

## Strongest falsification attempt and residual

The hostile alternative was that exact low-prime phases would not improve the generic three-moment body. It is rejected numerically: survivor fraction falls from `0.997` to zero as `P` rises from 1 to 128.

The residual is certification. Floating-point quadrature, grid sampling, and an unenclosed prime tail cannot prove the continuum theorem. In particular, the near-zero exclusion depends on detecting a very small positive margin and must be handled separately with high precision or an analytic zero-character inequality.

## Smallest next theorem

On compact boxes containing `t=0.275`, prove interval enclosures for:

- the exact prefix value and slope for `n<=128`;
- the digamma value and slope;
- the tail moments and the omitted `n>2,000,000` remainder;
- the scalar function `ellipse_margin(t,xi)-1`.

A subdivision certificate showing this margin positive would establish that no double contact is constructable on those boxes while preserving positivity of the arithmetic tail. With actual tail moments, `P=256` closes the moving island; with the elementary all-integer infinite-tail majorant, `P=512` closes it with a very large sampled margin. Direct natural intervals fail because they erase cancellation. The next certificate must use a joint Taylor enclosure of the combined residual and certified `acb.integral` derivatives. The zero-character boundary should use its saturation-specific inequality rather than floating subtraction.

## Disposition

The constructability reframing is numerically productive. A 44-term exact arithmetic prefix plus a generic positive tail excludes every point on the tested slice. Promotion requires interval arithmetic over a two-dimensional neighborhood and a separate stable treatment of zero character.

## Global minimum-prefix scout

`global_minimum_prefix_scout.py` maps the least dyadic prefix in `128,...,65536` whose exact source geometry separates each point, using the first 80 critical-line zeros only to stabilize witness discovery. On `xi in [0,25]`, every sampled point is separated through `t=0.374`, but the maximum required prefix grows rapidly:

| `t` | maximum `P_min` |
|---:|---:|
| 0.160 | 128 |
| 0.173 | 256 |
| 0.202 | 512 |
| 0.218 | 1024 |
| 0.254 | 2048 |
| 0.275 | 4096 |
| 0.297 | 8192 |
| 0.321 | 16384 |
| 0.346 | 32768 |
| 0.374 | 65536 |

At `t approximately 0.404`, a central interval `xi in [0,0.85]` remains unresolved even at 65536. That interval expands with `t`, reaching approximately `[0,9.2]` near `t=1.02` and `[0,23.85]` at `t=3`. The finite-prefix method therefore does not show a practical uniform cutoff over the full exploratory rectangle. Its hard locus is a growing central character corridor at larger `t`, not the moving character-five island seen near `t=0.28`.

This is discovery evidence only. Above moderate `t`, the actual prime tail was truncated at two million and the all-integer positive-tail majorant becomes increasingly loose. The result diagnoses where a stronger structural inequality is needed; it does not prove prefix divergence or contact feasibility.

Additional files:

- `research/grothendieck/checkers/global_minimum_prefix_scout.py`
- `research/grothendieck/results/global-minimum-prefix-scout.json`

## Is the global corridor only a loose-tail artifact?

`actual_vs_integer_tail_corridor.py` repeats representative larger-`t` slices using the actual positive tail moments through two million instead of the all-integer majorants. The corridor narrows only modestly. At `t=0.4`, unresolved points fall from 15 to 10; at `t=1`, from 183 to 177; at `t=3`, from 386 to 354. The actual-tail unresolved spans remain approximately `[0,0.45]`, `[0,8.8]`, and `[0,23.5]`, respectively.

Thus the expanding central corridor is not principally caused by replacing primes with all integers. It reflects scale separation: near central character and larger `t`, the positive observation is governed by the first zero scale, approximately `exp(-t(gamma_1-xi)^2)`, while a prefix certificate must push its omitted prime tail below that quantity. Balancing Gaussian exponents suggests

\[
\log P\ \text{of order}\ 2t(\gamma_1-\xi)
\]

up to lower-order saddle terms. At `t=3, xi=0`, this predicts an astronomically large direct prefix. This asymptotic diagnosis uses zero-side values only as discovery evidence; it is not a proof input.

The finite-prefix architecture is therefore suitable for moderate `t` and characters nearer the first spectral scale, but brute prefix enlargement is not a plausible global RH route. The larger-`t` central corridor needs a structural resummation, Euler-product block certificate, or a separate analytic positivity theorem that captures the exponentially small observation without termwise cancellation.

Additional files:

- `research/grothendieck/checkers/actual_vs_integer_tail_corridor.py`
- `research/grothendieck/results/actual-vs-integer-tail-corridor.json`

## Defect: float64 cancellation in discovery-scout demands

The discovery scouts (`global_minimum_prefix_scout.py`, `actual_vs_integer_tail_corridor.py`, `escape_crossover_scout.py`, `stable_dual_witness_scout.py`) evaluate the tail demand `rr=(e+g0)/c-R_P` and `ii=-(e1+g1)/c-I_P` in float64. Both subtract `O(1)` quantities, so the absolute error floor is of order `1e-16`. Whenever the all-integer tail bound `U0` falls below that floor (it reaches `1e-20` to `1e-36` at prefixes 8192 to 65536), the computed sign of the margin `rr^2/U0^2+ii^2/(U0*U2)-1` is cancellation noise.

Consequences:

- the prefix-growth table, the expanding central corridor, and the moving character-five island from those scouts are discovery hypotheses, not established residues. They require re-evaluation at 40+ digit precision before use;
- the corrected-normalization escape grid (`escape_crossover_scout.py`) has the additional caveat that `np.longdouble` equals float64 on this Windows/MSVC platform, so its attempted precision upgrade did not take effect; its JSON is annotated accordingly;
- results that survive: the Arb rectangle certificate at `(t,xi) in [.298,.300] x [4.500,4.505]` (70-digit arithmetic, margin `8.44`, demand `O(10)`); the cancellation-free coercivity frontier bounds below; the log-sum-exp verified-zero dominance; the 60-digit identity validation in `high_precision_source_spot_audit.py`.

Disposition: the required high-precision rerun is now materialized in `high_precision_escape_demand_scout.py`. It evaluates the prefix, endpoint, and 96-node Gauss--Hermite digamma block at 50 decimal digits. The repaired grid finds no feasible points for `t=0.3,0.4,0.5` with `P=8192`; their float64 apparent residues were cancellation artifacts. For larger `t`, the repaired frontiers agree with the stable float64 rows because their tail scales exceed the cancellation floor:

| `t` | grid step | last feasible sampled `xi` |
|---:|---:|---:|
| 0.3 | 0.1 | none through 6 |
| 0.4 | 0.1 | none through 8 |
| 0.5 | 0.1 | none through 10 |
| 0.7 | 0.1 | 8.1 |
| 1.0 | 0.1 | 10.1 |
| 1.5 | 0.2 | 28.0 |
| 2.0 | 0.5 | 109.0 |
| 3.0 | 1.0 | 644.0 |

The repaired calculation is still discovery evidence: fixed Gauss--Hermite quadrature and a finite character grid are not interval certificates. It establishes that the corridor onset near `t=0.4` was numerical, while the larger-`t` frontiers from `t>=0.7` persist at 50 digits.

Adaptive larger-prefix reruns show that these frontiers are not monotone in cutoff because thin almost-periodic feasible islands can move. At `t=2`, increasing from `P=8192` to `P=65536` reduces the last sampled feasible character from `109` to `45.5`. At `t=3`, `P=65536` leaves only 49 feasible integer-grid points but its last one is `652`. A denser 50-digit rerun with `P=262144` and character step `0.25` on `[0,150]` leaves 131 feasible points and a last sampled character of `136.5`. Increasing to `P=1048576` on the same grid leaves 97 feasible points and moves the last sampled character to `109.25`. The survivors form separated bands, including central character, neighborhoods near `16--19`, and isolated bands near `35`, `46`, `63`, `74`, `91`, and `109`. Testing only those 97 candidates with `P=4194304` and a conservative `1e-12` float64 coordinate guard leaves 77 candidates, with the last at `xi=63`. Its tail moments remain `U0=5.83e-5` and `U2=1.44e-2`, far above the arithmetic guard. Thus source-side escape becomes effective before even the twentieth computed ordinate (`77.145`) on the sampled `t=3` slice. A separate guarded `P=4194304` scan of every integer character from `63` through `800` finds only `xi=63` feasible; all integer samples `64,...,800` are excluded. The interval theorem must still control the open intervals between those samples and replace the finite endpoint `800` by analytic coercivity; neither follows from the integer census.

Additional files:

- `research/grothendieck/checkers/high_precision_escape_demand_scout.py`
- `research/grothendieck/results/high-precision-escape-demand-scout.json`
- `research/grothendieck/checkers/high_precision_large_prefix_escape_scout.py`
- `research/grothendieck/results/high-precision-large-prefix-escape-scout.json`
- `research/grothendieck/checkers/high_precision_p262144_escape_scout.py`
- `research/grothendieck/results/high-precision-p262144-escape-scout.json`
- `research/grothendieck/checkers/high_precision_p1048576_escape_scout.py`
- `research/grothendieck/results/high-precision-p1048576-escape-scout.json`
- `research/grothendieck/checkers/adaptive_p4194304_residual_scout.py`
- `research/grothendieck/results/adaptive-p4194304-residual-scout.json`
- `research/grothendieck/checkers/p4194304_halfline_grid_scout.py`
- `research/grothendieck/results/p4194304-halfline-grid-scout.json`

## First-contact jet audit

The upstream audit identified a stricter requirement: value--slope cone exclusion at every point discards the curvature inequality carried by a first contact. `high_precision_first_contact_jet_scout.py` restores this condition. For any positive tail,

\[
I_1^2\le (U_0+R)(U_2-R_2),
\]

so the prescribed value and slope imply

\[
R_2\le U_2-\frac{I_1^2}{U_0+R}.
\]

At a character-local minimum, `F_xixi>=0` imposes a lower bound on the same tail curvature. If that lower bound exceeds the displayed upper bound, first contact is impossible.

The 50-digit scout with `P=8192` finds that curvature removes only three of 87 value--slope-feasible samples at `t=1`; it removes none at `t=0.7,1.5,2,3`. Thus omitting first-contact curvature was logically stricter but does not explain the observed relaxed-tail residue. The stronger inflation is the replacement of the discrete prime-power tail by an arbitrary positive measure with only two moments, compounded by the all-integer moment majorant. Further progress must preserve more tail phase/support structure rather than add curvature alone.

Additional files:

- `research/grothendieck/checkers/high_precision_first_contact_jet_scout.py`
- `research/grothendieck/results/high-precision-first-contact-jet-scout.json`

## Phase-local tail cone

The generic moment ellipse permits arbitrary redistribution across all omitted logarithmic frequencies. `phase_block_tail_cone_scout.py` instead partitions the actual prime-power tail through two million into character-phase cells, retains each cell's exact positive mass, and permits redistribution only inside that cell. This preserves finite tail phase/support information while remaining a relaxation.

At `t=3`, `P=8192`, and integer `xi in [0,150]`, the global ellipse leaves 83 samples feasible. Phase cells of width `pi/8` exclude 51 of them; width `pi/32` excludes 57, leaving 26; width `pi/128` excludes 61, leaving 22. The ultrafine cone also removes `xi=45,74,81,109`. Its survivors are exactly `1,...,12`, `16,...,19`, `23`, `27--28`, `35`, `46`, and `63`.

The diminishing gain identifies two different residues. The high-character isolated islands are artifacts of lost phase localization and disappear under refinement. The central band persists because the actual source demand differs from the actual tail by the exponentially small positive zero-side value, of scale approximately `exp(-t(gamma_1-xi)^2)`. Any relaxed cone that permits perturbations larger than that gap will retain central feasibility. Closing this band source-only requires either an exact structural positivity inequality or arithmetic control at the scale of that gap; merely refining generic convex relaxations will not suffice.

This falsifies the claim that generic curvature was the principal missing constraint and supports the stronger diagnosis: retained tail phase information supplies a substantial reduction. The construction is not yet a certificate because it uses actual block masses only through two million, a direction grid, and point samples. A certificate version needs Arb-enclosed block masses, continuous maximization of each block support function, and a separate bound beyond the finite tail cutoff.

Additional files:

- `research/grothendieck/checkers/phase_block_tail_cone_scout.py`
- `research/grothendieck/results/phase-block-tail-cone-scout.json`
- `research/grothendieck/checkers/phase_block_tail_cone_fine_scout.py`
- `research/grothendieck/results/phase-block-tail-cone-fine-scout.json`
- `research/grothendieck/checkers/phase_block_tail_cone_ultrafine_scout.py`
- `research/grothendieck/results/phase-block-tail-cone-ultrafine-scout.json`

## Upstream scope defect: no justified upper bound `t<=3`

The computations above treat `t=3` as an outer slice, but no source-derived theorem makes it an endpoint of the RH reduction. Positivity of every shifted Gaussian requires an unbounded scale family unless a separate promotion theorem proves finite-scale determination. A first contact, if one exists, is finite, but that statement has quantifier order

\[
\text{for each counterexample there exists a finite contact parameter},
\]

not

\[
\text{there exists one finite upper bound containing every possible first contact}.
\]

The latter has not been proved. Consequently, confining the `t=3` residual below character `63` does not produce a finite global RH certificate. As `t` grows at central character, the positive gap behaves like `exp(-t gamma_1^2)` while direct arithmetic cancellation must resolve that scale; fixed-prefix convex certificates become progressively less plausible.

This is a stopping condition for brute atlas extension. The next required theorem is one of:

1. a source-derived finite-scale determination theorem for Gaussian Weil positivity;
2. a uniform large-`t` source positivity theorem;
3. permission to use finite rigorous low-zero verification, which supplies the missing large-`t` dominant term but violates the current source-only evidence constraint.

Without one of these arrows, further certification at larger finite `t` only moves an unbounded frontier and does not reduce RH to a finite object.

The three candidate arrows do not presently supply a noncircular escape:

- Finite-scale determination is false for the unconstrained heat family. A hypothetical quartet displaced horizontally by `delta` carries an amplification `exp(t delta^2)` and an oscillatory phase whose first adverse scale can be delayed beyond any prescribed finite cutoff by taking `delta` sufficiently small. Any theorem preventing that delay needs a quantitative lower bound on nonzero horizontal displacement or another rigidity input not supplied by finite-scale positivity.
- Uniform large-`t` positivity is not a weaker lemma. An off-line zero has `delta!=0`; its `exp(t delta^2)` amplification can be localized against contributions with smaller horizontal displacement. Excluding that mechanism for all sufficiently large `t` is already an RH-strength assertion.
- Finite low-zero verification controls only a bounded ordinate range. A first off-line zero can lie above every fixed verified height. Using verification therefore yields increasing finite-stage coverage, not one finite proof, unless coupled to an independent global theorem.

Disposition: the finite-contact programme has produced valid local exclusion machinery and diagnosed useful arithmetic structure, but it has not converted RH into a finite certificate. The irreducible residual is uniform control over arbitrarily small horizontal displacement at arbitrarily high ordinate. Any next programme must attack that typed residual directly rather than enlarge the present atlas.

## Escape answer: coercivity frontier versus verification height

The demand has the exact lower bound

\[
rr(t,\xi) \ge \tfrac{1}{2}\log(\xi/2) - K(t) - M_0(\le P,t), \qquad
|ii(t,\xi)| \le M_1'(\le P,t) + \text{(decaying archimedean slope)},
\]

where `M_0(\u003c=P,t)` is the prefix mass (a sum of positive terms) and `K(t)` bounds `(e+g0)/c - log(xi/2)/2` (numerically `K \u003c= 1.43` for `t \u003c= 3`). The tail cone is `|rr| \u003e U_0(P,t)` or `|ii| \u003e sqrt(U_0*U_2)`. All quantities in this comparison are positive-term sums or certified integrals, so the following frontier bounds are cancellation-free:

| `t` | `P` | coercivity frontier `\u003c` |
|---:|---:|---:|
| 1.0 | 8192 | `1.3e4` |
| 2.0 | 8192 | `5.9e7` |
| 3.0 | 8192 | `4.5e12` |
| 3.0 | 65536 | `8.5e11` |

Against a rigorous verification height of order `3e9` (Platt--Trudgian; larger claimed computations exist), source-side escape is effective well inside the verified range for `t \u003c= 2` (margin two to five orders of magnitude). At `t = 3` the coarse bound slightly exceeds `3e9`, but the bound is far from sharp: the true frontier is plausibly much lower, and enlarging the prefix moves the bound down (`8.5e11` at `P=65536`).

This answers the escape question affirmatively in the certified range `t \u003c= 2` without any zero input: characters beyond the frontier are excluded source-only, and the frontier lies far below any height that rigorously verified zeros would reach. Locating the true frontier precisely, and resolving the `t \u003e= 3` case, require high-precision demand evaluation (the repair above) plus the existing interval-extension machinery.

Additional files:

- `research/grothendieck/checkers/escape_crossover_scout.py`
- `research/grothendieck/results/escape-crossover-scout.json`

## Verified-zero dominance as a separate large-scale certificate

The central corridor can be treated without source cancellation by admitting a finite, rigorously verified initial zero set and bounding every unverified zero adversarially. For a zero `beta+i gamma`, the shifted Gaussian contribution has magnitude at most the corresponding ordinate Gaussian multiplied by `exp(t/4)`, since `|beta-1/2|<=1/2`. A crude unit-bin bound using total zero counts then controls all ordinates beyond the verified range.

`verified_zero_dominance_scout.py` uses the first 20 computed critical-line ordinates, ending at approximately `77.145`, and deliberately overcounts each later unit bin by `(k+1)log(k+1)`. On the grid `t in [.02,3]`, `xi in [0,25]`, the positive contribution of those 20 zeros dominates the adversarial tail everywhere. The weakest logarithmic dominance is still `47.0`, a factor above `e^47`.

This is not yet a theorem: the computed ordinates must be replaced by a rigorous zero-verification certificate, and the unit-bin count by a cited explicit inequality. More importantly, it does not solve all characters. Near an unverified high ordinate, a hypothetical off-line zero is not Gaussian-suppressed. Finite-zero dominance can cover only a character range lying safely below the verified height. Therefore it closes the observed larger-`t` central corridor in principle, but RH still requires either an effective source-side escape radius below the verification height or certificates that move with arbitrarily high character.

An expanded diagnostic uses the first 100 computed critical-line ordinates, ending at `236.524`, against the same adversarial unit-bin tail. On `t in [0.7,3]` and `xi in [0,110]`, every sampled point is dominated; the weakest logarithmic ratio is still above `11103`. Thus the entire million-prefix residual lies deep inside a range that finite rigorous zero verification would settle. This is not admissible certificate evidence under the present source-only constraint: it is only a validation and localization result.

Additional files:

- `research/grothendieck/checkers/verified_zero_dominance_scout.py`
- `research/grothendieck/results/verified-zero-dominance-scout.json`
- `research/grothendieck/checkers/verified_zero_dominance_expanded_scout.py`
- `research/grothendieck/results/verified-zero-dominance-expanded-scout.json`
