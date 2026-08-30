# Multiplicity-One Odd Boundary Protection Audit

## Question

Can an anomaly-forced odd endpoint representation derive the dark corner and
protect it through all symmetry-preserving thresholds?

## Claim boundary

Let endpoint exchange act on the two portal ports by

\[
R=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Its nontrivial character has the unique normalized carrier

\[
d=\frac{(-1,1)}{\sqrt2},
\]

while the trivial character has carrier

\[
b=\frac{(1,1)}{\sqrt2}.
\]

Every (R)-equivariant endpoint operator is (aI+bR), so it preserves both
lines.  If the odd character occurs with multiplicity one in the complete
source Hilbert space, every equivariant threshold operation preserves the
dark line exactly.  Combined with WP866's canonical conditional expectation,
this gives an exact normalized difference ray and a unique global basin.  The
character Fourier transform is the lossless bright/dark readout.

This is a valid conditional protection theorem.  Ordinary anomaly matching
does not establish its key hypothesis.  A nonzero (mathbb Z_2) anomaly is
self-inverse and records only a mod-two class.  Adding two heavy odd carriers
preserves that class while increasing the odd multiplicity from one to three.
The equivariant commutant then contains rotations between the portal dark line
and a heavy odd line.  Such a rotation preserves the symmetry and anomaly but
attenuates the light portal projection.

Hence the implication

\[
\text{anomaly matching}
\Longrightarrow
\text{multiplicity-one threshold protection}
\]

is false.  A full representation-valued threshold memory could retain the
multiplicity, as anticipated in WP846, but WP847 proves that the existing
incidence complex does not derive that equivariant character.  Even a retained
character does not by itself mark which copy is the detector-coupled boundary
copy when multiplicity exceeds one.

## Gate classification

- Relative sign and magnitude: the odd character fixes the normalized
  difference ray, conditional on the exchange action and odd-sector source
  charge.
- Basin: the WP866 conditional expectation fixes the dimensionless basin once
  the odd corner is admitted.
- Threshold: exact only under global multiplicity one or a stronger marked
  boundary superselection projector; ordinary anomaly matching is too coarse.
- Readout: the endpoint Fourier transform gives a source-level bright/dark
  instrument, but heavy copies can rotate its boundary attachment.
- Physical realization: no calibrated map from the odd character port to
  `physical16` detector units is currently admitted.

## Smallest exact falsifier

In the basis ((d,b,h_1,h_2)), take

\[
R_{\rm full}=\operatorname{diag}(-1,1,-1,-1).
\]

A rotation of (d) with (h_1) by cosine (3/4) commutes with
(R_{\rm full}).  The odd multiplicity changes by two, so the mod-two anomaly
class is unchanged, while the retained light norm of (d) becomes (9/16).
This is the smallest anomaly-neutral multiplicity hostile.

## Disposition

Progressive conditional theorem and negative anomaly derivation.  A
multiplicity-one odd boundary sector would unify relative sign, normalized
magnitude, the conditional-expectation basin, and selector-level threshold
survival.  The current anomaly data do not force multiplicity one and therefore
cannot make the portal unavoidable.  The missing source object is a marked
representation-valued boundary index whose complete threshold theorem retains
both multiplicity and detector attachment, followed by calibrated `physical16`
realization.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp867_multiplicity_one_odd_boundary_protection_audit.py
```
