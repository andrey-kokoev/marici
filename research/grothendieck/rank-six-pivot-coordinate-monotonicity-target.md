# Central rank-six pivot coordinate-monotonicity target

## Objective

For the certified central source coefficients `F_n`, let

\[
 H_r^{(i)}(x)=h_r(x_1,\ldots,x_{i+1})
\]

be the complete homogeneous polynomial in the first `i+1` ordered chord
coordinates, and define the symmetric rank-six Loewner matrix

\[
 A_{ij}(x)=\sum_{n\ge1}F_n
 \sum_{k=i}^{n-1-j}H_{k-i}^{(i)}(x)H_{n-1-k-j}^{(j)}(x),
 \qquad 0\le i,j<6.
\]

Write `d_1,...,d_6` for the diagonal pivots in the directed Newton--`LDL*`
factorization of `A`. The target is

\[
 d_6(x)>0,
 \qquad 0\le x_1\le\cdots\le x_6\le .01,
\]

preferably through the stronger coordinate theorem

\[
 \partial_{x_j}d_6(x)<0\quad(j=1,\ldots,6).
\]

One rigorously localized negative pivot, nonnegative derivative, failed
denominator, or excessive continuum remainder is the accepted falsifier.

## Initial directed audit

The source polynomial is retained through degree 39. Coefficients of degrees
39 and higher are bounded using `|F_n|<=6.038308` through degree 200 and a
geometric tail with ratio `.011`; no zeta-zero locations enter.

At the zero-confluent, upper-confluent, and mixed anchor
`(0,0,.002,.004,.007,.01)`, all six pivots are strictly positive. The sixth
pivot ranges from approximately `1.65125406e-32` at zero to
`1.65077876e-32` at the upper endpoint. Its directed interval width is about
`2e-46`, so the analytic source-tail uncertainty is fourteen orders below the
positivity margin.

Differentiating the full Newton--`LDL*` recursion analytically, including the
source tail, proves all eighteen probed coordinate derivatives negative. The
closest observed upper endpoint to zero is approximately `-2.85909709e-35`
at the upper-confluent anchor. The sixth-coordinate derivatives are near
`-3.32e-34`.

The prefix-cached grid audit is now complete. All `C(16,6)=8008`
nondecreasing anchors have six strictly positive directed pivots, and every
pivot minimum occurs at `(0.01,...,0.01)`. The weakest sixth-pivot interval is

`[1.6507787637605424e-32, 1.6507787637605621e-32]`.

Shared algebra reduces the audit to 12,376 prefix tables and 68,068 matrix
entries. The first-five continuum denominator gate also closes by prefix
inheritance: the first four determinant/Hadamard floors remain valid, while
the rank-five monotonicity theorem supplies `d_5>6.665113678415503e-26`.
The full 48,048-derivative cached audit is the next active gate.

That derivative audit is now complete. All 48,048 directed intervals are
strictly negative. The closest upper endpoint to zero is
`-2.859097087443228e-35`, at the upper-confluent anchor and zero-based
variable 3; the most negative lower endpoint is `-3.323751151851478e-34` at
the zero-confluent anchor, variable 5.

The seven ordered binary macro-centers have also been Hessian-certified. Their
largest row sum is `6.462475323242339e-35`, at the all-low center. A half-grid
cell has coordinate `linf` radius `.0005`.  Absolute Hessian row-sum norms pair
with `linf` displacement, so the derivative margin permits a uniform Hessian
ceiling `5.718194174886456e-32`. A binary macro-chart has coordinate `linf`
radius `.0025`; after subtracting the center Hessian, it is therefore enough to
prove the full third-tensor `l1` bound

`2.2846926798252854e-29`.

The earlier use of coordinate `l1` radii `.003` and `.015` was valid but
needlessly paid a factor six at each transport stage.  The norm-consistent
row-sum/`linf` pairing enlarges the admissible tensor ceiling by about 36.2
without changing any anchor or center certificate.

The durable transport-geometry audit
`central-rank-six-continuum-transport-geometry.json` verifies the count
`binomial(11+6-1,6)=8008`, all 48,048 anchor-coordinate derivatives, monotone
nearest-grid quantization with `linf` error `.0005`, and the seven ordered
low-prefix/high-suffix macro-patterns with `linf` radius `.0025`.  It also
checks by exact rational comparison that the stored downward-rounded tensor
ceiling does not exceed the exact two-stage transport allowance.  Therefore
any certified tensor slice-`l1` bound strictly below the stored ceiling
preserves every negative coordinate derivative on the full ordered simplex.
The transport-geometry checker now also requires the version-2 all-pivots grid
and the exact source-tail identity artifact, including both geometric-ratio
gates.  Hence the eventual continuum certificate cannot omit anchor pivot
positivity or analytic-tail provenance while checking only derivative signs.

A subsequent end-to-end rounding audit found that the shared anchor kernel,
its derivative-tail extension, and the center-Hessian evaluator formed some
factorial--power products before entering the upward Decimal context.  The
center Hessian row sums themselves also used ambient `sum`.  These paths are
now directed throughout, center row sums use upward accumulation, and the
`.0005` variation field is correctly identified as an `linf`-transport bound.
Regenerated anchor-derivative and center-Hessian artifacts must carry
`directed_scalar_arithmetic_version: 2`; until then, the previous 8,008-anchor
grid, seven center Hessians, and the transport ceiling derived from them are
superseded rather than certificates.  The repaired seven-center regeneration
is now complete: all seven rows carry version 2, all `.0005` variation fields
use the corrected `linf` label, and the maximum upward-rounded Hessian row sum
is `6.4624753232423386838825701036e-35`.  The repaired 8,008-anchor derivative
grid regeneration is in progress; the transport target remains superseded
until that margin is refreshed.

The shared-kernel repair also supersedes the earlier 8,008-anchor pivot grid,
not only the derivative grid.  A version-2 pivot-grid regeneration is queued
to re-establish all six positive LDL pivots and their coordinatewise weakest
floors.  The continuum-target generator now refuses to run unless both the
derivative grid and all seven center-Hessian rows carry version 2, so the
current mixed state cannot overwrite the transport target with stale input.

The version-2 all-pivots grid is now complete.  All 8,008 ordered anchors and
all six Newton--LDL pivots are strictly positive with no uncertified anchor.
The coordinatewise weakest pivots all occur at the upper-confluent anchor; the
sixth lower endpoint is
`1.6507787637605424271613037888e-32`.  This restores the grid-anchor positivity
gate after the shared-tail repair.

The small repaired anchor regeneration is complete.  All three anchors carry
version 2 and remain strictly positive; at the upper-confluent anchor the
fifth pivot lower endpoint is
`6.6651136784155034436891408400e-26`.  However, the legacy *global*
first-five-floor composer also depends on older rank-three/rank-four
determinant and rank-five continuum artifacts that have not passed the new
rounding audit.  It now refuses those unversioned inputs.  The intended
replacement is stronger and local to the actual proof: each of the seven
covering Taylor charts must certify all 15 rational LDL inverse floors.  Once
all seven pass, those chart-local floors establish denominator safety on the
entire ordered simplex without inheriting the unaudited global shortcut.

Before launching the fully current Taylor charts, the dominant polynomial
kernel was replaced by a semantics-preserving total-degree bucket algorithm.
A dense rank-six degree-eight jet has 3,003 monomials: naive multiplication
visits 9,018,009 pairs, whereas truncation permits only 125,970, a factor
`71.59` reduction.  Fifty randomized interval products agree exactly with the
reference kernel.  The discarded high-product remainder is even cheaper: its
norm depends only on total degree, so upward-rounded degree-bucket coefficient
norms reduce it to at most 81 degree pairs; in 30 randomized trials the new
bound dominates the fully enumerated reference componentwise.  New artifacts
carry `taylor_product_kernel_version: 2`.

The prefix homogeneous tables in the base jet, deep jet, and collapsed
known-remainder stages are now extended incrementally rather than rebuilt for
prefix lengths 1 through 6.  This reduces the prefix-node updates from 21 to
6 (factor 3.5).  Fresh-interpreter equivalence checks confirm exact interval
equality for the base and deep tables, and exact coefficient equality for the
collapsed remainder table; the first combined probe was discarded because a
deep import deliberately mutates the shared truncation order before the base
reference was reconstructed.

The fully repaired pipeline pilot at the all-high center, Taylor degree five,
and unique radius `.0024` is complete.  It carries directed arithmetic v2,
closed-binomial source remainder v1, product kernel v2, and all 15 positive
inverse floors; the minimum is
`6.6651316311404248960196133346e-26`.  Its certified C3 remainder is
`5.61189364862542590098e-24`, which is `245630.13` times the current
(still provisional until the v2 derivative grid completes) transport target.
Thus the pilot validates the pipeline and rigorously falsifies degree-five
adequacy on that chart, while leaving the degree-eight seven-chart attack open.
Its freed slot is now running the version-2 all-pivots grid.

That slot has subsequently moved to the first production Taylor chart, the
all-high binary center at radius `.0025` and degree eight.  Production outputs
use a `current-v2` filename tag, which the audit and seven-chart aggregator
require.  Late completion of retained legacy workers therefore cannot
overwrite or masquerade as current evidence.

The repaired prefix-cached derivative recurrence has been cross-checked at the
mixed anchor `(0,0,.002,.004,.007,.01)` against the standalone differentiated
LDL evaluator.  The sixth-pivot interval and all six derivative intervals
agree exactly; the largest derivative upper endpoint there remains negative,
`-2.85929466493688444315e-35`.  Thus the optimized 8,008-anchor path consumes
the repaired tails without changing the recurrence semantics.

The first single-chart run produced a large provisional obstruction. A
degree-seven Taylor model centered at `(.01,...,.01)` with radius `.01` had
the initially reported
degree-eight-and-higher `C3` remainder

`1.113728606315642e-13`,

which exceeded the then-used conservative `l1`-radius tensor ceiling by the factor
`1.764891248008721e17`. However, a post-run audit found that the generalized
analytic source tail still counted coordinate words with `5^(d+r)` rather
than `6^(d+r)`. That run and all concurrently launched pre-fix runs are
therefore explicitly superseded, not certificates. The checker now uses the
rank dynamically and stamps the coordinate multiplicity into every artifact;
the aggregators reject stale artifacts. Corrected full-radius and seven
radius-`.0025` runs are required before either obstruction or positivity is
claimed.

The corrected full-radius run has now stopped earlier, at the inverse-floor
gate: for at least one Taylor-model denominator, the certified polynomial
variation is no smaller than the constant-term lower bound.  Thus the single
radius-`.01` box cannot even certify the rational LDL recursion on its own
terms.  This is a rigorous obstruction to the one-chart carrier, not a
counterexample to pivot positivity.  Subsequent checker failures now report
the inversion index, center, radius, constant lower bound, variation upper
bound, and resulting lower bound so that the first failing denominator can be
localized exactly.

The seven-chart aggregator has also been audited before accepting any of the
expensive corrected artifacts.  Its induced Hessian row-sum norm is the
maximum of the six stored row budgets (not their sum), and every rescaling,
product, quotient, and power used in the tensor transport is now rounded
upward at 50 decimal digits.  This removes an unnecessary factor-of-six loss
without weakening the certificate.

A deeper directed-rounding audit then found that the Taylor source and
rational-remainder checkers sometimes formed factorial--power products in the
ambient Decimal context before handing the result to the upward context.  A
downward ambient rounding would invalidate the advertised enclosure.  Those
products, inverse-denominator powers, finite-jet budgets, and remainder
derivative scalings now remain inside the directed contexts throughout.  New
artifacts carry `directed_scalar_arithmetic_version: 2`; consumers reject any
artifact lacking that marker.  Consequently, all computations launched before
this repair remain useful performance probes only and are not certificates,
even if their coordinate-multiplicity marker is six.

The analytic source remainder no longer relies on the undocumented operation
of doubling the accumulated degrees through 50.  For each source monomial
through degree 200, the checker now sums every omitted Taylor degree using
the binomial identity after the fixed matrix-entry and readout derivatives.
For source degrees at least 201 it permits all Taylor degrees, evaluates the
result at the enlarged scalar radius `.01 + 6*.0025 = .025`, and closes the
remaining source-degree series geometrically.  Across all matrix indices and
the first three readout derivatives, the worst consecutive-term ratio is
`0.02671957671957672`, safely below one.  Accepted artifacts therefore also
carry `source_remainder_binomial_version: 1`.

The coefficient envelope itself is not an empirical assumption.  The directed
unit-disk certificate gives
`sup |F'| = 6.0383070503172... < 6.038308` on the independently certified
zero-free disk.  Cauchy's coefficient estimate therefore yields
`|F_p| <= 6.038308/p <= 6.038308` for every `p>=1`.  Future Taylor artifacts
record this bound, its source certificate, the enveloped degrees `39..200`,
the enlarged radius, and their actual geometric ratio; consumers verify these
fields rather than trusting a bare tail-version label.
The durable audit now reads that independent Rouché artifact directly:
its directed margin `0.1189109327416954519584974028` strictly exceeds the
copied `0.1189` margin used by the `F'` certificate, and its centered unit disk
is marked zero-free.  Thus the coefficient envelope is linked mechanically
all the way back to the zero-free-disk premise without using zero locations.

The durable identity audit
`central-rank-six-source-remainder-binomial-identity.json` checks all 723,492
relevant factorial--binomial instances for first omitted Taylor degrees 6, 8,
and 9, fixed derivative orders 0 through 13, and source degrees 39 through
200.  Every identity holds exactly, the imported directed `F'` envelope is
strictly below `6.038308`, and the source-degree tail ratio is certified below
one.  This closes the algebraic source-tail adequacy subgate independently of
the long LDL remainder propagation.

The same audit now checks the narrower geometric tail used directly by the
anchor, derivative, and Hessian evaluators.  For every fixed derivative order
0 through 13, its largest consecutive source-degree ratio is
`0.01068783068783069`, below the encoded allowance `.011`; division by
`.989 = 1-.011` is therefore a valid upward tail closure.

The rational Taylor-model inversion gate is now sign-aware as well.  A
constant interval contributes a nonzero floor only when it lies strictly on
one side of zero; an interval crossing zero receives floor zero and produces
an explicit obstruction.  A successful rank-six chart must expose all 15 LDL
division floors and their positive minimum.  The artifact audit rejects a
chart unless that count, sign test, and minimum are present, preventing the
earlier endpoint-magnitude shortcut from silently accepting a zero-crossing
constant interval.

## First current-v2 degree-eight obstruction

The authoritative derivative grid is complete.  All 48,048 coordinate
derivative intervals at the 8,008 ordered anchors are strictly negative.  The
closest upper endpoint to zero is

`-2.8590970874432279262324681755815801863811387084e-35`,

at the all-`.01` anchor in coordinate 3.  Combining that margin with the
version-2 binary-center Hessian certificate and the exact row-sum/slice-l1
versus coordinate-linf duality gives the downward-rounded sufficient uniform
third-tensor ceiling

`2.2846926798252854055124215124238241491049109667426e-29`.

The first tagged production chart, centered at
`(.0075,.0075,.0075,.0075,.0075,.0075)` with radius `.0025` and Taylor degree
eight, is interval-certified and exposes all 15 positive inverse floors.  Its
minimum inverse floor is
`6.6651136445973377878082569761893280732921991602e-26`.  Nevertheless, its
post-degree-eight C3 remainder alone is

`1.0538616121990491760484807226908508570870178988e-23`,

which exceeds the transport ceiling by the upward-rounded factor
`461270.62142976703791103134369656574044110504065716`.  Including the finite
jet raises the uniform chart bound slightly to
`1.0538661591184984584478523243321161777697657113e-23`.

This is the first rigorous localized obstruction to the current seven-chart,
degree-eight carrier: its assumption that the present Taylor/analytic-tail
majorant is below the derivative-transport ceiling fails already on the
required all-high chart.  It is not a negative pivot, a counterexample to
rank-six positivity, or evidence against RH.  A sharper analytic source-tail
propagation, a higher Taylor order, or a finer correlated cover may still
close the continuum argument.  The machine-readable certificate is
`central-rank-six-degree-eight-all-high-chart-obstruction.json`.

## Degree-49 source repair and reopened continuum route

Component isolation showed that the obstruction above was not caused by the
rational LDL recursion.  The largest raw matrix-entry C3 remainder was
`1.05377186607081721612702924948e-23`, while the propagated final-pivot value
was only about `0.0085%` larger.  A directed standalone split assigned
`1.05377186607081721612675249137e-23` of the raw bound to the uniform Cauchy
envelope beginning at source degree 39.  The known degree-at-most-38
polynomial remainder was negligible on that scale.

The centered source computation has therefore been extended without changing
its analytic model: it now certifies `F_0,...,F_49` as directed intervals and
retains the old degree-29 and degree-39 arrays for compatibility.  Applying
the same `6.038308` envelope only from degree 50 reduces its isolated raw C3
contribution to
`1.09633241507670558557602566069e-39`, roughly ten orders below the required
transport ceiling.

The hostile all-high chart has completed again under a distinct `current-v3`
tag.  It has all 15 positive inverse floors, minimum
`6.66511364459739599865850030827e-26`, and final post-degree-eight C3
remainder `1.09967152638247165127573347926e-39`.  After adding the complete
finite degree-3-through-8 jet budget, its uniform third-tensor bound is
`3.76471153932640501894770158366e-37`, below the exact sufficient ceiling
`2.28469267982528540551242151242e-29` by a safety factor of about
`6.07e7`.  Thus the earlier obstruction remains a valid falsifier of the v2
cutoff but is superseded as an obstacle to the theorem route.  Consumers now
require exact source degree 49, first enveloped degree 50, and `current-v3`
filenames.  Six further ordered binary charts remain to complete the finite
cover.

## Certified rank-six continuum theorem

All seven `current-v3` binary charts are now complete and pass the exact-source
degree 49, first-enveloped degree 50, directed-arithmetic, closed-binomial,
product-kernel, and 15-positive-inverse-floor gates.  Their largest uniform
third-tensor slice-l1 bound is attained on the all-low chart and equals

`3.7654233628084175387336242074856613126923718748624e-37`,

strictly below the downward-rounded sufficient ceiling
`2.2846926798252854055124215124238241491049109667426e-29`.

The corrected linf transport gives maximum continuum Hessian row sum
`6.4625694588264088943210384442051871415328173092969e-35` and derivative
transport loss
`3.2312847294132044471605192221025935707664086546485e-38`.  Subtracting this
loss from the smallest of the 48,048 certified anchor derivative margins
leaves the directed positive margin

`2.8558658027138147217853076563594775928103722997736e-35`.

Consequently the sixth Newton--LDL pivot is strictly decreasing in every
coordinate throughout `0 <= x1 <= ... <= x6 <= .01`; its minimum is at the
all-`.01` endpoint, where the directed grid certificate is strictly positive.
Together with the established rank-five continuum theorem for the preceding
principal pivots, all six Newton--LDL pivots are strictly positive throughout
the ordered rank-six simplex.  The machine-readable terminal certificates are
`central-rank-six-third-tensor-seven-chart-cover.json` and
`central-rank-six-global-coordinate-monotonicity.json`.

This is a finite rank-six positivity theorem for the specified central
Loewner system.  It is not a rank-uniform theorem and does not prove RH.

RH is not proved.
