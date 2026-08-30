# Reference uncertainty in source-monitor calibration

## Question

What survives when the monitor records are exact but the injected optical
reference amplitude is known only within an interval?

## Exact interval calculation

Freeze the positive affine monitor law

```text
y = o + g x
```

and subtract an exact dark record. Let `B` be the bright-reference contrast,
`Z` the science contrast, and `R` the physical bright-reference amplitude.
Then `Z/B = x/R` exactly. If `R` lies in `[R_low,R_high]`, the physical science
input lies in

```text
[(Z/B) R_low, (Z/B) R_high].
```

The checker freezes an actual reference `51/100` whose declared interval is
`[1/2,13/25]`. For science input `1/4`, the observed contrast ratio is `25/51`,
so calibration returns `[25/102,13/51]`. The true input is contained, but the
interval has nonzero width `1/102`. Substituting the nominal lower endpoint as
though it were exact gives `25/102`, biased by `-1/204`.

## Identification versus selection

The instrument identifies a set of compatible physical inputs. It does not
select a point on a continuous source range. If an independently derived
source law admits only the candidates `{1/4,3/10}`, however, exactly `1/4`
intersects the calibration interval. The combined source-and-instrument
inverse is then unique.

This is the useful factorization: the optical reference supplies a likelihood
or compatibility set; the source theory supplies the admissible set. Neither
is allowed to impersonate the other.

The exact invariant under a common unknown reference scale is the dimensionless
ratio `x/R`. Absolute `x` remains uncertain until an absolute reference lineage
is supplied. Adding more records at the same unknown common scale improves the
response-shape audit but cannot create that missing unit.

## Claim boundary

The calculation assumes a static positive affine response, exact dark and
science records, and uncertainty only in one bright-reference amplitude.
Independent uncertainty across multiple levels, drift, saturation, uncertain
dark subtraction, and monitor-source crosstalk enlarge the compatible set and
need separate designs.

## Verification

Run:

```text
python research/aspect/checkers/check_reference_uncertainty_source_monitor.py
```

The checker verifies containment, the failure of nominal point substitution,
the nonzero interval width, and unique intersection with a frozen discrete
source candidate set.
