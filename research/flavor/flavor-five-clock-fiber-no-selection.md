# Five compact clocks represent the target but do not select it

Work package: WP624  
Owner: marici.Figueiredo

## Process and optionality snapshot

Pre-objective activation:

- excitement: 9/10;
- confidence that five clocks are the minimal representation: 8/10;
- confidence that equal-weight symmetry uniquely selects the target: 2/10;
- expected information gain: 9/10;
- immediate reason: WP623 leaves multi-clock combinations as the smallest
  topological reopening;
- confound: independently derived interactions could lift the degeneracy.

Frozen optionality space:

- \(N\) identical compact clocks;
- the WP623 alphabet \(x_i\in\{-2,-1,0,1,2\}\);
- equal-weight readout \(r=(\sum_i x_i)/(2N)\);
- permutation equivalence under \(S_N\);
- no fitted weights or target-centered interaction;
- ten exact checks declared.

## Bounded question

What is the minimal identical-clock constructor that can represent
\(r=3/5\), and does its source symmetry select a unique clock orbit?

## Minimal multiplicity theorem

The target condition is

\[
\sum_{i=1}^N x_i=\frac{6N}{5}.
\]

The left side is integral. Since six and five are coprime, \(N\) must be
divisible by five. Therefore five clocks are minimal. One witness is

\[
(x_1,\ldots,x_5)=(1,1,1,1,2).
\]

Thus multi-clock topology repairs WP623's representability obstruction
without a continuous coefficient.

## Complete target fiber

Exact enumeration of the \(5^5\) labelled states finds 70 states with mean
\(r=3/5\). Quotienting by clock permutations leaves five occupancy classes.
Writing occupations in alphabet order \((-2,-1,0,1,2)\), they are

\[
\begin{aligned}
&(0,0,0,4,1), &&5,\\
&(0,0,1,2,2), &&30,\\
&(0,0,2,0,3), &&10,\\
&(0,1,0,1,3), &&20,\\
&(1,0,0,0,4), &&5.
\end{aligned}
\]

The states

\[
(-2,2,2,2,2)
\qquad
(1,1,1,1,2)
\]

have the same mean \(3/5\) but different occupation counts. They are not
related by \(S_5\). This is an exact hostile pair collapsed by the mean
readout.

## Selection audit

For uncoupled identical clocks, every alphabet tuple is a degenerate vacuum.
Equal weighting and permutation symmetry make the target representable but
do not prefer its 70-point fiber among all \(5^5\) states. They also do not
select one of the five target occupancy orbits.

A symmetric interaction

\[
\left(\sum_i x_i-6\right)^2
\]

would select the target mean. But six is precisely the target sum. Unless a
separate source law derives total charge six, this interaction transports the
answer as WP622 transported \(v=576/25\).

## Quotient and instrument typing

The equal-weight mean descends under \(S_5\), but is not faithful on the clock
quotient: five inequivalent occupancy classes share the target readout.
Coupling the mean to flavor still uses the WP618 \(H\) reference and defines a
relational stabilizer-groupoid experiment rather than a scalar on the
original full weak-basis quotient.

The smallest discriminating instrument must resolve all five clock records
or their occupation counts, plus the referenced flavor mass ratio, in one
source frame. A detector measuring only the mean cannot identify the source
clock state.

## Disposition

Five equal-weight compact clocks are the minimal discrete carrier of the
rational target. This is representability, not selection. The target
projection has a 70-point labelled fiber and a five-point
permutation-quotient fiber.

A progressive successor must derive both multiplicity five and a
permutation-invariant interaction selecting a total or occupation class
without importing the target. It must predict additional clock-sector
records accessible to a calibrated instrument.

## Post-objective process report

- excitement: 9/10;
- confidence in the exact fiber theorem: 10/10;
- confidence that the uncoupled grammar selects the target: 0/10;
- realized information gain: 10/10;
- immediate reason: representability begins at a forced multiplicity, but
  the hidden ambiguity is exactly enumerable;
- remaining confounds: source-derived total-charge constraints and clock
  interactions.

Raw optionality delta:

- single-clock exclusion is repaired at minimal multiplicity five;
- the complete target fiber has 70 labelled points;
- permutation quotienting reduces it to five, not one, classes;
- one exact hostile source pair is exhibited;
- a target-centered interaction is rejected as answer transport;
- mean descent and nonfaithfulness are separated;
- all ten declared exact checks pass;
- independently derived multiplicity and interaction remain open.

These process ratings are non-evidential.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp624_five_clock_fiber_no_selection.py

The generated result is
`research/flavor/results/wp624_five_clock_fiber_no_selection.json`.
