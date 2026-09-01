# Integral-lattice clock-orientation no-go: WP1099

## Question

Does an integral-polarized lattice alone select the integer lift \(n\) or the
clock orientation \(\sigma\)?

## Lattice gate

The witness values

\[
-1,0,1,2
\]

are all integral lattice points. Their clock values are

\[
6n^2=6,0,6,24.
\]

Thus integrality does not choose a lift or even a unique clock orbit.

## Orientation gate

Negation is an automorphism of \(\mathbb Z\). A rank-one lattice has the two
generators \(+g\) and \(-g\). Without an oriented normalized dual cycle or
other source orientation, no generator is preferred. Moreover

\[
6(-n)^2=6n^2,
\]

so the quadratic clock cannot itself repair the sign ambiguity.

## Classification

Negative gate. Integral-lattice membership may be a necessary repair
condition, but a bare lattice does not select \(n\), \(\sigma\), or the unit
orbit. The remaining gate is a source-authorized oriented normalized dual
cycle or generator.

Checker: `research/flavor/checkers/wp1099_integral_lattice_clock_orientation_no_go.py`

Result: `results/wp1099_integral_lattice_clock_orientation_no_go.json`
