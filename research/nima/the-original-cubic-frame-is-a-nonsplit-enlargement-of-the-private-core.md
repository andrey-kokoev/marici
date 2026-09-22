# The original cubic frame is a nonsplit enlargement of the private core

## Result

The original four-sector cubic detector is now compiled into the actual old-plus-270 source-evaluation core. It is NOT redundant on the full source ideal.

There is an explicit two-term source h in I but not I^2 such that

`epsilon_core(h)=0`,

`normalized_original_detector(h)=1`.

Moreover the restriction from the enlarged observer to the private core is nonsplit as a source-bimodule map. Thus assembling the retained original frame is not merely an invertible change of private coordinates.

The export has 2,741 ambient contextual readouts, versus 2,720 for the core. Neither number is asserted to be the dimension of the evaluation image. Other historical cubic frames remain outside this export.

## 1. Compile the actual detector, not four guessed path coordinates

The original detector selects retained early/late seams in the first two diamonds and the first forgotten seam in the third. The recipe is the one in `source-action-saturation-builds-an-all-depth-residual-observer-tower.md`.

Normalize the entire family by its fixed positive late/late response. Its four sector coefficients become

`early/early: rho*sigma`,

`early/late: -rho`,

`late/early: -sigma`,

`late/late: 1`,

where

`rho=(mu_[2,4]-L)/(mu_[4,12]-L)`,

`sigma=(mu_[12,60]-L)/(mu_[60,420]-L)`.

These are fixed ideal quantities, not independent physical settings. The owning positive-window protocol supplies `0<rho<1` and `0<sigma<1`. The computation keeps them symbolic and preserves their tensor-product correlation.

Crucially, four selected analytical sectors do NOT mean four supported source paths. The early/late sector has a two-event vacuum buffer, which admits both orders. Expanding the actual seam blocks yields FIVE source paths, including the crossed order `(2,5,3,7,11,13)`.

The compiler enumerates those buffer orders, checks their selected seam coefficients, and then takes the entire source-action saturation of the ONE aggregated detector. It does not install four independently acquired sector rows.

## 2. A source the private core cannot see

Let

`p=path(2_forgotten,3_retained,5_forgotten,7_retained)`,

`t=forgotten(11,13)`,

`h=p*t`.

There are two terms, each of absolute coefficient one. Both have retained marks in positions two and four.

The terminal recorder kills h because t is an actual ideal relation. Its full first jet has a nonzero coefficient, with left potential word `(3,15)`, forgotten seam `15->31`, and empty right potential word, in Boolean-corner labels. Thus h is below I^2.

Every full-corner private pivot requires its retained features at first positions of its two-event blocks. It cannot see h's two second-position features. The shorter old detectors cannot see a full six-event source. No nonidentity context fits that source into another six-event seed.

The exporter checks zero against the whole compiled private-core evaluation, not just against a selected scalar target.

The original late/late sector does see h. Its canonical forgotten tail contributes one and the reversed tail does not match the selected final seam. The other sectors contribute zero. Hence the normalized original value is exactly one, independently of rho and sigma.

## 3. Why the observer restriction is nonsplit

The terminal two-event ideal corner has dimension two, spanned by the forgotten and mixed `(11,13)` diamonds. The original source certificate checks its recorder rank six on eight paths.

The private core already observes BOTH directions there: its contextual private rows include the forgotten and mixed coefficient functionals. The exporter checks the resulting rank two. Adding the original frame therefore cannot enlarge that corner, so restriction is an isomorphism on it.

Any hypothetical source-equivariant section must consequently lift epsilon_core(t) to the same-source enlarged evaluation of t. Acting on the left by p would then imply

`0 = section(p*epsilon_core(t))`

`  = p*epsilon_enlarged(t)`

`  = epsilon_enlarged(h)`,

contradicting the normalized original reading one.

This rules out every source-bimodule section, not merely a preferred coordinate section. It is a different extension question from the adjacent cubic pushout's filtered nonvanishing and unfiltered vanishing.

Optional all-vacuum acquisitions do not remove this particular obstruction: h has positive retained degree and remains invisible to such functionals, while the terminal ideal corner is already fully observed. The exported profile itself keeps the optional vacuum seed separate.

## 4. Agreement on all 270 cubic columns still misses the defect

Let P_0 denote the private coordinate of

`mixed(2,3) mixed(5,7) forgotten(11,13)`,

and P_x that of

`mixed(2,5) mixed(3,7) forgotten(11,13)`.

The original normalized detector has the same values on the 270 two-feature cubic basis products as

`(1-rho)(1-sigma) P_0 - rho P_x`.

The checker verifies all 270 equalities. Define the full-source correction

`R=original-(1-rho)(1-sigma)P_0+rho P_x`.

Then

`R(v_j)=0` for all 270 cubic basis products,

but

`R(h)=1`.

The correction is exported as an explicit six-path coefficient functional. It cannot be discarded merely because a top-layer task matrix says it is zero.

This is an actual source example of the distinction that motivated the coherence lane: task agreement is weaker than equality of source kernels and structural comparison maps.

## 5. What the new export verifies

The `--original-cubic` profile retains the entire previous core and appends the actual aggregate detector and its contextual rows.

Checks include:

- 273 seed families and 2,741 ambient readout rows;
- 4,644 formal source-action coefficient identities;
- 2,769 left/right context-commutation identities;
- the source-compatible restriction to the nine-dimensional O_2;
- exact agreement of the retained core rows and their action matrices;
- the hidden source, its nonzero first jet, and its two contrasting evaluations;
- the forced terminal-corner lift and all 270 top-column correction identities.

Restriction to the private core simply retains its first 2,720 readouts. Source compatibility follows from the common source evaluation; no inverse source comparison is supplied.

The background-two vacuum increment remains eight-dimensional for this particular enlarged profile, with inherited dimensions `(8,6,1,0)` and intrinsic ideal-power dimensions `(8,2,0)`. The checked vacuum-sector support argument still applies. These exact counts are not promoted to the larger, not-yet-assembled frame union.

## 6. Remaining gate

The two-private, sixteen-private and matched memory-block norming observers still need full-source compilation and comparison. Their agreement on cubic columns cannot authorize a frame-isomorphism cast.

The original retained detector has now provided a concrete warning: the correct comparison can be a nonsplit restriction rather than an invertible gain. Actual tower faces must retain that map type and its source-action data.

No four-tower tetrahedral certificate is claimed yet. No new measurement or physical parameter sweep was performed. The exact symbolic computation remains conditional on the owning fixed analytical normalization and source-category hypotheses.

## Verification

`uv run --with sympy python research/nima/checkers/export_actual_private_observer_core.py`

`uv run --with sympy python research/nima/checkers/export_actual_private_observer_core.py --original-cubic`

Both profiles pass.

Artifact:

`research/nima/results/actual-private-core-with-original-cubic.json`

This is a source-checked symbolic export, not yet an independent portable verifier for arbitrary submitted presentation JSON.
