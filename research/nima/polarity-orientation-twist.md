# The polarity–time mismatch is a spatial-orientation twist

## Character quotient

Use two candidate involutions:

\[
r=\text{road reflection / spatial reflection},
\qquad
t=\text{core exchange / time reversal}.
\]

The exact source calculations give the Carrier polarity character

\[
\chi_{\rm pol}(r,t)=(-1,-1).
\]

Physical time orientation has character

\[
\chi_{\rm time}(r,t)=(+1,-1).
\]

Their ratio is

\[
\chi_{\rm space}
=
\chi_{\rm time}\chi_{\rm pol}^{-1}
=
(-1,+1).
\]

This is precisely the character of a spatial-orientation or parity line: it
reverses under spatial reflection and is unchanged by time reversal.

Therefore the failed direct comparison has a unique character-level repair:

\[
\boxed{
L_{\rm time}
\cong
L_{\rm pol}\otimes L_{\rm space}.
}
\]

Among all four real characters of \(\mathbb Z_2\times\mathbb Z_2\), the checker
verifies that \((-1,+1)\) is the unique twist converting Carrier polarity into
time orientation.

## Meaning

The previous zero-intertwiner obstruction was not telling us that Carrier
polarity and causal direction are unrelated. It identified one missing
orientation factor.

The three lines form a closed character triangle:

\[
L_{\rm time}=L_{\rm pol}\otimes L_{\rm space},
\]

\[
L_{\rm space}=L_{\rm pol}\otimes L_{\rm time},
\]

\[
L_{\rm pol}=L_{\rm time}\otimes L_{\rm space}.
\]

This resembles the familiar relation between spacetime, spatial, and temporal
orientation lines, but the present result is only a character identity under
a declared generator comparison.

## Typing boundary

Two pieces remain unproved:

1. Carrier road reflection has not been physically identified with spacetime
   parity.
2. The required spatial-orientation line has not been derived from the bare
   Carrier.

The scattering real form already supplies spacetime orientation, time
orientation, and a Lorentz metric as source data. It may therefore supply the
twist in that sector. The question for a shared Marici construction is whether
the same twist arises naturally in radiative gravity and cosmology.

## Consequence for the \(c\) program

The prospective derivation now has the form

\[
\text{Carrier incidence}
\to
\text{finite unoriented reachability},
\]

\[
L_{\rm pol}\otimes L_{\rm space}
\to
L_{\rm time}
\to
\text{directed finite probe cone},
\]

\[
\text{frame naturality}
\to
\kappa>0,\quad c=L.
\]

Thus the minimal extra causal coefficient is no longer unspecified. It is a
parity/spatial-orientation line and a typed comparison of involutions.

## Next falsifier

Construct the twist independently in two physical sectors. For each sector,
verify the characters of:

- Carrier polarity/core exchange;
- physical spatial reflection;
- physical time reversal;
- the proposed tensor comparison.

A disagreement in either character or transport falsifies a universal twist.
Agreement in scattering and radiative gravity would be the first cross-sector
evidence that causal orientation is a sector realization of one shared
orientation calculus.

Exact artifacts:

- \`research/nima/checkers/check_polarity_orientation_twist.py\`
- \`research/nima/results/polarity_orientation_twist.json\`
