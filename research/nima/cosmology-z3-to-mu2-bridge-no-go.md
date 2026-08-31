# No torsion bridge from all-soft Z/3 to the mu2-odd nearby line

The all-soft character and the triple-incidence nearby line have incompatible
recorded descent types.

- The all-soft class is a flat relative differential character of order three.
- The triple-incidence physical coefficient is sheet-odd and asks for a
  \(\mu_2\)-twisted pairing.

A torsion-respecting bridge would have to include a nonzero homomorphism

\[
\mathbb Z/3 \longrightarrow \mathbb Z/2.
\]

But

\[
\operatorname{Hom}(\mathbb Z/3,\mathbb Z/2)=0,
\]

because the image of a generator must have order dividing both 3 and 2.  Thus
any source map factoring through the recorded all-soft torsion character is
zero on the \(\mu_2\)-odd nearby coefficient.

This closes the proposed all-soft activation route for the triple-incidence
line.  Remaining escape hatches must be independently sourced:

1. a non-torsion analytic-continuation contour;
2. a new coefficient object not factoring through the recorded \(Z/3\) class;
3. an all-soft physical chain coupling that is not the \(\mu_2\)-odd nearby
   line.

Artifact:

- `research/nima/checkers/check_cosmology_z3_to_mu2_bridge_no_go.py`
- `research/nima/results/cosmology_z3_to_mu2_bridge_no_go.json`
