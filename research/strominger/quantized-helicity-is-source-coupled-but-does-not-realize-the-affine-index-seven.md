# Quantized helicity is source-coupled but does not realize the affine index seven

## First independently quantized candidate

For asymptotic quantum particle states, helicity supplies an integral or
half-integral lattice.  Normalize

\[
q_k=2h_k\in\mathbb Z.
\]

This is independent of the magnetic row calculation.  It also couples to the
correct physical channel: Appendix A of *New Gravitational Memories* gives

\[
\lim_{r\to\infty}r^2T^M_{uz}
=\sum_k\delta(u-u_k)
\left[L_{uz}(z_k)-\frac{i}{2}h_k\partial_z\right]
\frac{\delta^2(z-z_k)}{\gamma_{z\bar z}}.
\]

The same paper uses this angular-momentum flux to source spin memory.  Thus
the helicity lattice passes both the independent-quantization gate and the
magnetic-coupling gate.

## Formal determinant comparison

For two labelled particles or two labelled helicity ports, one has a charge
lattice \(\Lambda_h\cong\mathbb Z^2\).  If one simply inserts the affine frame

\[
F=\begin{pmatrix}2&7\\3&7\end{pmatrix}
\]

as a sublattice of \(\Lambda_h\), its Smith index is indeed

\[
[\Lambda_h:F\mathbb Z^2]=|\det F|=7.
\]

This calculation is exact but is not yet a physical comparison.

## Variance failure

The two lattices have different source types:

- \(\Lambda_h\) is covariant particle-source data;
- the two coordinates on which the cocircuit is supported are observation
  rows of the magnetic boundary matrix.

The affine columns are therefore changes of an observation presentation, not
declared shifts of particle helicity.

The soft Ward identity makes the mismatch operational.  The helicity term in
the hard charge is

\[
\frac{h_k}{2}D_zY^z(z_k).
\]

With labelled test fields whose values are independently supported at the two
particle directions, the two helicity coordinates are separately observable.
The resulting charge readout has full rank on \(\Lambda_h\otimes\mathbb Q\).
Consequently neither \((2,3)\) nor \((7,7)\) is in its kernel.

Declaring either affine column to be a physical equivalence would erase a
measurable helicity-charge difference.  The resulting order-seven quotient is
a fitted cross-typing, not source descent.

## Candidate audit

The nearby charge candidates separate cleanly:

| Candidate | Independently quantized | Couples to spin memory | Same integral comparison domain as \(F\) |
|---|---:|---:|---:|
| particle helicity | yes | yes | no |
| orbital angular momentum of scattering data | no; impact parameters and energies are continuous | yes | no |
| classical BMS or superrotation charge | no lattice in the grounded source | yes | no |
| ring optical mode number | yes | instrument only | no |
| NUT or dual gravitational charge | conditional global quantization | not the established PSZ helicity-flux map | no map established |

Particle helicity is therefore the unique current candidate passing the first
two gates, but it fails the decisive third gate.

## Smallest missing comparison theorem

A successful construction must provide a source-authorized span

```text
AffineHelicityComparison
  helicity_charge_lattice Lambda_h
  magnetic_observation_lattice Lambda_obs
  common_integral_carrier Lambda_common
  source maps Lambda_h -> Lambda_common <- Lambda_obs
  kernel or gauge theorem making F-columns physically null
  Smith index of the induced physical quotient
```

Computing \(|\det F|=7\) before constructing this span proves only the affine
index already known.  The next search should therefore target an integral
boundary charge whose source law identifies charge shifts with row
presentation changes, rather than another merely quantized integer.
