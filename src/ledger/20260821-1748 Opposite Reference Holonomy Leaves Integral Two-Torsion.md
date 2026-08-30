# 1748 — Opposite Reference Holonomy Leaves Integral Two-Torsion

## Integral restoration

Entry 1747 computed the opposite-character extension after rationalization.
Over the source integral lattice,

\[
\chi-1=-2,
\]

and therefore

\[
\boxed{
H^1(S^1,\mathbb Z_-)=\operatorname{coker}(-2)=\mathbb Z/2.
}
\]

The parity of the unipotent shear is unchanged by every integral lift change

\[
a\longmapsto a-2b.
\]

Thus the extension discarded by rational coefficients is a genuine integral
torsion class.

## Born/readout test

Every additive map from \(\mathbb Z/2\) into a torsion-free scalar group is
zero. In particular, after extension of coefficients to \(\mathbb Q\),
\(\mathbb R\), or \(\mathbb C\), the class vanishes because the half-integral
lift \(b=a/2\) is allowed.

Therefore an ordinary complex Born scalar does not detect this class as an
additive extension invariant. Detection would require independently retained
integral-lattice, mod-two, or exponentiated discrete data.

## Narrow result

The filtered reference coefficient object has strictly more information over
\(\mathbb Z\) than its rational or complex realization:

\[
\boxed{
\text{opposite-character shear}=\mathbb Z/2
\quad\xrightarrow{\otimes\mathbb C}\quad0.
}
\]

This is coefficient torsion, not a new carrier stratum. It also warns that a
complex period or probability calculation cannot falsify the integral class.

## Durable artifacts

- `research/benincasa/checkers/integral_parabolic_torsion.rs`
- `research/benincasa/results/integral-parabolic-torsion.json`
- `research/benincasa/integral-parabolic-torsion.md`

## Next falsifier

Determine whether the frozen cosmological source provides an integral or
mod-two normalization of the reference lattice. Without such provenance, the
torsion class is mathematically canonical but physically unselected.
