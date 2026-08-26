# Deutschian explanatory scope of FDM-1

Work package: WP590  
Owner: marici.Figueiredo

## Explanatory question

FDM-1 is the strongest currently coherent source constructor whose own
prediction survives the complete fitted flavor ensemble. This packet asks
what it explains in the hard-to-vary sense, rather than merely whether its
checker passes.

## Source family

The symmetry and dynamical mechanism extend naturally to

\[
V_{a,\lambda}(s)
={\lambda\over4}(s^2-a^2)^2,
\qquad a>0,\quad\lambda>0.
\]

Every member is CP even. The CP-conserving point is unstable, while
\(s=\pm a\) are stable CP-conjugate vacua. For every admitted initial state
outside the separatrix, dissipative evolution selects nonzero CP orientation.

This part is hard to vary within the declared architecture: removing the
nonzero pair or stabilizing the origin destroys the CP-breaking mechanism.
Its independently criticizable qualitative prediction is

\[
J\ne0.
\]

WP87 tested this prediction on all 1,210 fitted sheets and all passed.

## Easy-to-vary numerical content

The physical map gives

\[
|J|=a\,j(q),
\]

where \(q\) denotes the remaining flavor moduli. Changing \(a\) from one to
two preserves CP symmetry, the double-well mechanism, the two stable vacua,
and the prediction \(J\ne0\), while doubling the predicted magnitude at
fixed \(q\).

Thus FDM-1 does not explain the observed magnitude of CP violation. Nor does
it constrain the other 15 local physical16 coordinates. Its successful
ensemble test establishes only that every fitted sheet lies outside the
CP-conserving locus; it does not discriminate among those sheets.

## Deutschian disposition

FDM-1 contains a genuine qualitative explanation candidate:

- source law: CP-even double-well dynamics;
- counterfactual: stabilizing \(s=0\) or eliminating the broken vacua removes
  CP violation;
- selector: exclusion of the CP-conserving locus;
- instrument: the CP-odd invariant readout described in WP87;
- class falsifier: an admitted physical point with \(J=0\).

It does not yet explain the observed flavor relations because its numerical
normalization and the remaining quotient moduli are freely variable without
damaging that mechanism. A measured value of \(|J|\) refutes a fixed
\(a\)-member, but not the architecture class, since \(a\) can be retuned.

The missing constructor must independently lock \(a\) to the remaining
physical flavor moduli or replace it by a discrete or dynamically fixed
quantity. Its resulting numerical relations must be preregistered and tested
on the complete physical16 ensemble.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp590_fdm1_deutschian_scope.py

The generated result is
research/flavor/results/wp590_fdm1_deutschian_scope.json.
