# Audit of the positive-cut to exceptional-linking-cycle map

## Question

Does the current source material construct a homology map from the physical `q_G12` positive cut to either explicit exceptional meridian?

## Search result

A bounded search of all `q_G12` Benincasa artifacts for positive-cut chains, contours, chambers, inequalities, and relative chains returns no matches. The strict-transform packet specifies the positive square-root sheet and unit leading measure ratio, but not a chain, its boundary, or its homology class.

The independent cross-sector audit `research/aspect/semidefinite-admissibility-requires-route-nullspace-descent.md` records a stronger global absence: the current `q_G12` branch lacks the complete physical target form, base route, omitted route, and common target pairing. It explicitly states that a local soft positive-cut normalization does not define these global objects.

## First missing arrow

The required comparison is a source-derived map

\[
\Phi_{\rm cut}:H_1(C_{\rm physical},D_{\rm physical})
\longrightarrow
H_1(C_3,\{-1,\kappa\}),
\]

sending a declared physical cut chain to a specified combination of the meridians `gamma_-1` and `gamma_kappa`, with orientation and boundary compatibility. Neither endpoint signs, cut inequalities, nor a route-to-wall projection are present, so this arrow cannot be constructed.

## Excluded inference

The following established facts do not define `Phi_cut`:

- the exceptional bulk form uses the positive square-root sheet;
- the measure ratio is one;
- the sewn class is its oriented boundary residue;
- both exceptional meridian periods are nonzero;
- their signs reverse under sheet reversal.

These identify a cohomology class and local homology probes, not the physical chain.

## Acceptance test

A source packet must provide the physical target form and chain, its oriented boundary divisor, the strict-transform image in `(a,xi)`, and a homology reduction to integer coefficients of `gamma_-1` and `gamma_kappa`. Substitution into the exact periods must then predict the physical pairing without fitting the coefficients from the desired value.

## Disposition

No positive-cut-to-linking-cycle map exists in the available source material. The strongest result remains a nonzero positive-sheet exceptional linking period and an exact boundary-residue comparison. Physical pairing is deferred at the missing homology arrow and complete target pairing.

## Evidence

- `research/nima/qG12-grade1-exceptional-linking-period.md`
- `research/nima/qG12-grade1-positive-sheet-residue-comparison.md`
- `research/benincasa/x1-soft-physical-strict-transform.json`
- `research/aspect/semidefinite-admissibility-requires-route-nullspace-descent.md`
