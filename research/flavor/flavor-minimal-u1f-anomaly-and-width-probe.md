# A minimal gauged flavor spectrum leaves an exact charge-gap fiber

Work package: WP616  
Owner: marici.Figueiredo

## Bounded question

After forbidding exotic chiral spectators, do the complete local anomaly
equations of a minimal gauged single-spurion architecture force the WP614
charge gaps? If not, is there a source-calibrated observable that distinguishes
the surviving architectures?

## Frozen architecture

Admit one gauged \(U(1)_F\), a neutral Standard Model Higgs, one
charge-changing flavon, three Standard Model families, and one right-handed
neutrino per family. No additional chiral spectators are allowed.

For each family, give the physical left- and right-handed quarks the same
flavor charge \(q_i\), and give the physical charged lepton and Dirac neutrino
the same charge \(\ell_i\). In left-handed Weyl notation, the conjugate fields
therefore carry \(-q_i\) and \(-\ell_i\). A quark Yukawa operator between
families \(i,j\) has flavor charge \(q_i-q_j\), so a single flavon and its
conjugate generate the WP614 exponent rule

\[
n_{ij}=|q_i-q_j|.
\]

This field content and charge convention are frozen before comparing the
target and hostile charge assignments.

## Exact anomaly reduction

For one family, the color anomaly, hypercharge--flavor-squared anomaly,
cubic flavor anomaly, and gravitational flavor anomaly cancel between the
members of each vectorlike Dirac packet. Summing all three families leaves
only

\[
\begin{aligned}
A_{SU(2)^2F} &= \frac12\sum_i(3q_i+\ell_i),\\
A_{Y^2F} &= -\frac12\sum_i(3q_i+\ell_i).
\end{aligned}
\]

Thus the complete audited local anomaly packet imposes only

\[
\sum_i(3q_i+\ell_i)=0.
\]

Following Nima's affine audit, its typing is explicit:

- with \(\ell_i\) fixed, \(q_i\mapsto q_i+c\) changes the reduced anomaly by
  \(9c\), so it responds to the charge origin;
- simultaneous reversal of all charges changes the sign of the linear
  anomaly but preserves its zero locus, so it cannot choose an orientation;
- the integral lattice does not restore uniqueness in the hostile pair below.

The anomaly map sees a first moment, not the charge-gap geometry.

## Same-spectrum hostile pair

Freeze

\[
\ell=(-5,-5,-5)
\]

and compare

\[
q=(3,2,0),\qquad q'=(4,1,0).
\]

Both have quark-charge sum five, so both obey the same anomaly equation with
the same lepton charges and exactly the same fermion field content. Their
exponent matrices are

\[
\begin{pmatrix}0&1&3\\1&0&2\\3&2&0\end{pmatrix},
\qquad
\begin{pmatrix}0&3&4\\3&0&1\\4&1&0\end{pmatrix}.
\]

They are integral and are not related by translation or reflection. Minimal
spectrum and anomaly freedom therefore do not force the observed hierarchy
gaps. Perturbing one lepton charge from \(-5\) to \(-4\) produces the expected
nonzero \(SU(2)^2F\) and \(Y^2F\) residuals, providing the deliberate-failure
test.

## Independently executable discriminator

Gauging the source symmetry supplies a physical probe that the abstract
anomaly equation lacked. If the \(U(1)_F\) vector boson is produced above all
fermion thresholds, its fully inclusive massless partial widths obey

\[
\frac{\Gamma_q}{\Gamma_\ell}
=
\frac{3\sum_iq_i^2}{\sum_i\ell_i^2}.
\]

The common gauge coupling, resonance normalization, and unitary flavor-basis
rotations cancel in this ratio. The target and hostile architectures predict

\[
R_q=\frac{13}{25},
\qquad
R_q'=\frac{17}{25}.
\]

This is a source-derived, weak-basis-invariant discriminator of the two
charge architectures. It is not a selector: measuring the ratio identifies
or refutes a chosen charge assignment but does not explain why the source
prepared it.

Executability requires a resolved vector resonance, all relevant quark,
charged-lepton, and right-handed-neutrino channels to be open or separately
accounted for, and one calibrated line-shape fit with acceptance and invisible
width uncertainties. A measured ratio incompatible with \(13/25\), after
those support assumptions are verified, refutes the frozen target
architecture.

## Disposition

The minimal no-exotic spectrum removes WP615's mirror-completion freedom but
does not repair selection. Its anomaly family fixes one origin-sensitive
linear combination and leaves a large exact charge-gap fiber. The architecture
is a conditional hierarchy generator with an executable conditional
falsifier, not a hard-to-vary explanation of the target charge gaps.

A progressive successor must derive a representation, index, or source-vacuum
law that is sensitive to a second charge moment or to orientation while
remaining independent of the observed hierarchy. The gauged width experiment
then provides the appropriate criticism of that stronger constructor.

## Reproduction

Run:

    uv run --offline python research/flavor/checkers/wp616_minimal_u1f_anomaly_and_width_probe.py

The generated result is
`research/flavor/results/wp616_minimal_u1f_anomaly_and_width_probe.json`.
