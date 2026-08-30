# 1750 — The Total-Energy Cusp Carries a Source-Defined Integral Unipotent Extension

## Return to a source-defined lattice

Entry 1749 forbids identifying an abstract reference lattice with the
fiberwise Betti lattice. The homogeneous elliptic subsystem avoids that
problem: it is already identified as

\[
\mathcal K_{B^{-1/2}}\otimes m^*\mathbb H_{\rm Leg},
\qquad m=A/B,
\]

where \(\mathbb H_{\rm Leg}\) has its native integral homology lattice.

At total energy \(E_T=0\),

\[
B=\ell_3E_T,
\]

so the inverse Legendre modulus \(B/A\) is a linear local coordinate at
generic nonsoft kinematics. At this infinity cusp the Legendre factor has,
up to integral symplectic conjugacy and orientation,

\[
\boxed{
T_{\rm Leg}=\begin{pmatrix}-1&-2\\0&-1\end{pmatrix}.
}
\]

The Kummer factor contributes the second semisimple sign. The signs cancel
in the source-normalized tensor product, as directly computed in Entry 289:

\[
T_{\rm src}=(-1)T_{\rm Leg}
=\begin{pmatrix}1&2\\0&1\end{pmatrix},
\qquad N=T_{\rm src}-I,
\qquad \operatorname{rank}N=1,
\qquad N^2=0.
\]

The image of \(N\) has index two in the saturated invariant line. This
integer is the source-defined level-two cusp width, not an imposed reference
normalization.

## Established integral frontier

This rechecks the width-two input already used in Entries 1147 and 1152. It
does not determine whether the elliptic \(\mathbb Z/2\) coinvariant survives
in the full rank-nine lattice. Entry 1152 reduces that question to

\[
( \mathbb Z/2)^2
\]

along the algebraic plane \(\langle e_6,v_{\rm alg}\rangle\).

## Narrow result

The actual three-site cosmological coefficient system contains a canonical
integral unipotent extension at the scattering degeneration. Unlike the
abstract \(\mathbb Z/2\) reference class of Entry 1748, the width-two
elliptic coinvariant is source-defined by the Legendre Betti lattice itself.
Its integral gluing into the complete rank-nine lattice remains unresolved.

It is coefficient monodromy over the existing total-energy carrier divisor.
No new Cut stratum is required.

## Durable artifacts

- `research/benincasa/checkers/legendre_integral_cusp.rs`
- `research/benincasa/results/legendre-integral-cusp.json`
- `research/benincasa/legendre-integral-cusp.md`

## Next falsifier

Resume Entry 1152's finite test: compute the parity of twice one elliptic
coinvariant lift along \((e_6,v_{\rm alg})\). This determines one of the four
classes in \((\mathbb Z/2)^2\) without conflating a Betti cycle with an
abstract reference frame.
