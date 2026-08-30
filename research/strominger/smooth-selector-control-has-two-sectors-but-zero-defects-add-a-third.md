# Smooth Selector Control Has Two Sectors but Zero Defects Add a Third

## Question

What are the irreducible degrees of freedom of the remaining global relative
one-form \(b\)?

## Smooth global control

On the closed celestial sphere, Hodge decomposition gives

\[
b=d\lambda+\star d\mu
\]

because \(H^1(S^2)=0\). There is no harmonic one-form sector.

The exact component has zero curvature:

\[
d(d\lambda)=0.
\]

The coexact component carries all smooth bulk curvature:

\[
d(\star d\mu)=(\Delta\mu)\,\mathrm{vol}_{S^2}.
\]

Constants in \(\lambda\) and \(\mu\) are invisible. Every nonconstant
spherical harmonic has positive Laplacian eigenvalue and zero mean, so the
coexact curvature automatically preserves the fixed total degree.

Thus a smooth selector has two potential sectors but only one
curvature-bearing bulk sector. The exact sector can matter only through
declared boundaries, ports, or singularities.

## Punctured attachment domain

The unavoidable polarization zeros change the topology. If \(Z\) consists of
\(N\) distinct punctures, then

\[
\dim H^1(S^2\setminus Z)=N-1.
\]

The relative control decomposition becomes

\[
b=d\lambda+\star d\mu+h_Z,
\]

where \(h_Z\) is determined by puncture periods subject to one total-sum
relation.

For a transverse spin-two section, local indices are \(\pm1\) and sum to four.
Hence \(N\ge4\), so the defect-period sector has dimension at least three.

## Prediction

The selector-control type changes discontinuously when zero attachments are
admitted:

```text
smooth full sphere
  longitudinal exact sector
  transverse curvature sector

punctured zero attachment
  longitudinal exact sector
  transverse curvature sector
  at least three independent defect-period modes
```

A two-puncture model cannot represent a generic transverse spin-two selector
packet. It necessarily misses at least two independent period directions.

## Claim boundary

The dimension-three lower bound assumes transverse isolated zeros. Degenerate
zeros can merge points while retaining higher local index; their attachment
type then requires jets or multiplicities rather than three distinct period
cycles.

## Disposition

The missing variable control is classified. Smooth bulk action is coexact;
exact modes are boundary-sensitive; and the forced zero divisor adds a finite
harmonic period sector whose minimum generic dimension is three.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/hodge_selector_control_classification_checks.py
```
