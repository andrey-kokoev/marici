# All-soft torsion does not activate the triple-incidence nearby line

The triple-incidence construction and the all-soft construction are both real,
but the current source data do not identify them.

- Triple incidence supplies a universal logarithmic rank-one nearby line at
  \(p=x+y+3z=0\).  Its restricted coefficient is sheet-odd and needs a
  \(\mu_2\)-twisted physical pairing.
- The all-soft packet supplies a flat relative differential character of order
  three, with holonomy \(\exp(2\pi i/3)\), zero curvature, and zero de Rham rank
  contribution.

These are separated specialization regimes.  The all-soft origin is a boundary
specialization, not the generic positive-energy chamber, and the existing
all-soft character has no constructed Cayley--Menger relative-chain coupling.
Thus it cannot be imported as the missing physical activation of the
sheet-odd nearby line.

Current conclusion:

\[
\text{all-soft } Z/3 \text{ character}
\not\Rightarrow
\text{activated } \mu_2\text{-odd triple-incidence period}.
\]

A future bridge would need a new source map from the all-soft relative
character to the \(\mu_2\)-odd nearby coefficient, plus the physical twisted
pairing.  Without that bridge, the two readouts remain disjoint.

Artifact:

- `research/nima/checkers/check_cosmology_triple_incidence_all_soft_separation.py`
- `research/nima/results/cosmology_triple_incidence_all_soft_separation.json`
