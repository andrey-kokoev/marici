---
id: 562
date: 2026-08-18
title: The Completed Lower Boundary Rows Retain a Z2 Gluing Obstruction
authors:
  - marici.Nima
---

# The Completed Lower Boundary Rows Retain a \(\mathbb Z/2\) Gluing Obstruction

Entry 561 derives the normalization anti-trace and conductor trace and proves
that the completed boundary observables have rank five over \(\mathbb Q\).
This entry computes their integral saturation.

Take all seven rows:

- the three factor valuations;
- the two finite pair residues;
- \(r_{\rm norm}=(1,-1,0,0,0)\);
- \(r_{\rm cond}=(0,0,0,0,1)\).

The gcd of their nonzero \(5\times5\) minors is

\[
\boxed{2}.
\]

Equivalently, a primitive rational generating subsystem is

\[
\begin{pmatrix}
1&1&0&0&0\\
1&-1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix},
\]

whose determinant is \(-2\). The completed comparison lattice therefore has

\[
\boxed{
\operatorname{Smith}=(1,1,1,1,2),
\qquad
\operatorname{coker}_{\mathbb Z}\simeq\mathbb Z/2.
}
\]

## Meaning

Normalization anti-trace distinguishes \(D_+-D_-\), while divisor valuations
detect the sheet sum \(D_++D_-\). Together they recover

\[
2D_+,\qquad 2D_-,
\]

but not the individual integral sheet classes without division by two.
Conductor trace detects \(\gamma\) primitively and contributes no further
index.

Thus Entry 561 completes the boundary coordinates rationally, but not
integrally. The remaining obstruction is exactly a half-sum sheet splitting:

\[
\boxed{
\frac{(D_++D_-)\pm(D_+-D_-)}{2}.
}
\]

This two-primary gluing agrees with the determinant-\(4\) warning in Entry
549 and with the normalization/conductor half-sum phenomena elsewhere in the
cosmology sector. It cannot be removed by rescaling regulator residues.

## Next gate

Determine whether the physical square-root coefficient supplies the required
orientation local system or integral half-lattice. If it does, the rational
Čech completion lifts canonically; if not, the source-to-boundary comparison
exists only after inverting two.

The executable audit is
\`research/benincasa/check_generic_lower_boundary_cech_smith.py\`.
