# A single compact clock excludes the observed rational flavor lens

Work package: WP623  
Owner: marici.Figueiredo

## Process and optionality snapshot

Pre-objective activation:

- excitement: 9/10;
- confidence in the exclusion theorem: 8/10;
- expected information gain: 8/10;
- immediate reason: a compact clock is the smallest constructor that could
  make neighboring vacuum values impossible;
- confound: multiple clocks or a nonlinear source-derived readout can evade
  the single-clock grammar.

Frozen optionality space:

- one compact phase with fixed period;
- integer harmonics;
- the fixed readout (r=\cos\theta);
- the (H)-referenced relational stabilizer groupoid;
- one fitted affine-readout deliberate failure;
- ten exact checks declared.

## Bounded question

Can a single compact source clock isolate the observed (r=3/5) without
inserting a flavor-derived coefficient?

## Frozen constructor

Take a compact phase (	heta) and the integer-harmonic potential

\[
U_n(\theta)=\Lambda^4[1-\cos(n\theta)].
\]

Its minima satisfy

\[
\theta=\frac{2\pi k}{n}.
\]

Freeze the relational flavor readout as (r=\cos\theta). Neither the period,
integer harmonic, nor readout map may be fitted after seeing the flavor
target.

## Exact exclusion theorem

Let (zeta=e^{i\theta}). At every clock minimum, (zeta) is a root of
unity. Therefore

\[
x=\zeta+\zeta^{-1}=2\cos\theta
\]

is an algebraic integer. If (cos\theta) is rational, then (x) is a
rational algebraic integer and hence an integer. Since (|x|\leq2),

\[
x\in\{-2,-1,0,1,2\}.
\]

Thus the complete rational clock readout is

\[
r\in\left\{-1,-\frac12,0,\frac12,1\right\}.
\]

The observed target gives (2r=6/5), which is rational but not integral.
It is excluded for every integer (n), not merely for a finite scan of
harmonics.

## Smallest hostile residual

The nearest allowed positive clock value is (r=1/2), at exact distance

\[
\frac35-\frac12=\frac1{10}.
\]

Changing (n) cannot remove this residual while the one-clock cosine grammar
is retained.

An affine readout (r=a+b\cos\theta) can trivially reach the target by taking
(a=0), (b=3/5), and (	heta=0). This is the deliberate failure: the
instrument coefficient now contains the desired answer. Algebraic span is
not a source-derived flavor constructor.

## Quotient and instrument typing

The compact clock has a legitimate source groupoid and its winding sectors
can be discrete. The map to flavor still uses the WP618 (H) reference.
Consequently the combined operation defines a relational experiment over the
reference stabilizer groupoid; it does not reveal an absolute coordinate of
the original weak-basis experiment.

The required same-lineage instrument must measure:

1. the compact-field period;
2. the active harmonic number (n);
3. winding or domain-wall sectors;
4. the phase-to-flavor transfer function without flavor calibration;
5. the WP618 root-vector mass ratio and referenced interference.

No admitted apparatus currently establishes the fixed cosine transfer from a
compact clock to the flavor lens.

## Disposition

The one-clock topology branch is a genuine discrete source selector, but it
selects the wrong admissible set: it excludes (r=3/5). It therefore cannot
explain WP622's transported scale.

A multi-clock construction or independently derived nonlinear transfer map
may evade the theorem. Such a successor must be frozen before comparison
with flavor data and must predict additional clock-sector records. Merely
choosing a transfer coefficient equal to (3/5) is a degenerating shift.

## Post-objective process report

- excitement: 9/10;
- confidence in the exact theorem: 10/10;
- confidence in the one-clock target route: 0/10;
- realized information gain: 9/10;
- immediate reason: an unbounded harmonic family closes by one algebraic-
  integer obstruction;
- remaining confounds: multi-clock cyclotomic combinations and independently
  normalized nonlinear maps.

Raw optionality delta:

- the one-clock topological constructor is fully typed;
- all integer harmonics are eliminated at once for the rational target;
- the contextual rational partition has exactly five cells;
- the nearest exact residual is (1/10);
- one fitted affine evasion is identified and rejected;
- reference-stabilizer descent is explicit;
- all ten declared exact checks pass;
- multi-clock and source-derived nonlinear-map branches remain open.

These process ratings are non-evidential.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp623_root_of_unity_selector_no_go.py

The generated result is
`research/flavor/results/wp623_root_of_unity_selector_no_go.json`.
