# True multiport dark fringe versus scalar transfer zero

## Question

What optical test distinguishes destructive interference between admitted
ports from the vanishing of one scalar transfer amplitude after projection?

## Multiport dark fringe

A dark fringe requires an admitted input mode decomposition and a multiport
propagation law. In the exact two-port example, a balanced unitary sends the
relative-minus input to one dark output and one bright output. Total intensity
is conserved across the two recorded ports.

The decisive intervention is which-path dephasing. If `nu` is the retained
coherence, the dark and bright intensities become

```text
I_dark = (1-nu)/2
I_bright = (1+nu)/2.
```

Dephasing fills the dark port while preserving the complementary total. That
response identifies the zero as interference between the declared paths.

## Scalar transfer zero

For a one-dimensional transfer amplitude `h(s)`, the equation `h(s0)=0` does
not supply internal ports, a complementary record, or a which-path
intervention. Infinitely many two-term algebraic decompositions sum to the
same scalar transfer; none is physically preferred without source-labelled
mode maps.

A scalar zero on the physical parameter line is therefore a transfer null,
not automatically a dark fringe. It may acquire a multiport interpretation
only when a prior carrier supplies the ports and their recombination law.

## Analytic continuation

An off-axis zero of a continued amplitude is weaker still as a physical
optical claim. The checker uses a transfer with analytic zero at `1+i`; its
power on every real frequency is strictly positive. No laboratory dark record
occurs on the physical frequency axis.

## Application to the reciprocal-even carrier

Before even projection, the reciprocal grades may form two labelled ports.
After projection to the multiplicity-one logarithmic translation carrier, a
critical-line zero means the scalar fiber amplitude vanishes. Calling it
destructive interference would require transporting the pre-projection port
labels and a dephasing-sensitive recombiner through the projection. Without
that constructor, the correct optical analogue is a single-port transfer null.

Off-line zeros belong to nonunitary analytic continuation unless a separate
physical parameter map brings them onto an admitted measurement locus.

## Verification

Run:

```text
uv run --with sympy python research/aspect/checkers/check_dark_fringe_vs_scalar_transfer_zero.py
```

The checker verifies the conserved dark/bright pair, its exact dephasing
response, nonuniqueness of scalar decompositions, and an off-axis zero with no
real-frequency null.
