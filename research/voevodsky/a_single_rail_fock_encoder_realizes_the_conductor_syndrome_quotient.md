# A single-rail Fock encoder realizes the conductor syndrome quotient

## Question

Can the conductor quotient be encoded into the three occupation channels required by the pairwise photon-parity probe?

## Claim boundary

This constructs a finite-dimensional quantum encoder and its logical observables. It is not an apparatus preparation protocol and does not identify conductor classes with naturally occurring photons.

## Logical quotient

Let

\[
Q=\operatorname{coker}J\cong(\mathbb Z/2)^2
\]

with syndrome coordinates

\[
s([v])=(a,b)
=igl(\ell_1v,\ell_2v\bigr)\pmod2.
\]

Because both characters vanish on \(\operatorname{im}J\), this is independent of the representative \(v\).

## Three-mode encoder

Use the single-rail Fock subspace with occupations zero or one in each mode. Define

\[
\mathcal E:Q\longrightarrow\mathcal H_{m Fock},
\qquad
\mathcal E(a,b)=|a,b,0\rangle.
\]

The four image states are orthonormal, so linear extension gives an isometry from the four-dimensional logical Hilbert space \(\mathbb C[Q]\) into the three-mode Fock space.

On the image, the pairwise parity operators act as

\[
O_1=(-1)^{N_1+N_3}=(-1)^a,
\]

\[
O_2=(-1)^{N_2+N_3}=(-1)^b.
\]

Thus number-resolving measurement followed by pairwise parity exactly reads the two conductor syndrome bits.

## Site exchange

The conductor site exchange sends

\[
(a,b)\longmapsto(b,a).
\]

The optical swap of modes one and two sends

\[
|a,b,0\rangle\longmapsto|b,a,0\rangle.
\]

Therefore the encoder intertwines the two exchange actions.

## Null-state interpretation

The trivial syndrome is encoded as the vacuum record state

\[
\mathcal E(0,0)=|0,0,0\rangle.
\]

This is not the zero vector. It is a normalized state on which both parity observables return \(+1\). Hence “null” can mean no syndrome excitation, without implying absence of a state or zero norm.

The other logical classes are

\[
(1,0)\mapsto|1,0,0\rangle,
\qquad
(0,1)\mapsto|0,1,0\rangle,
\qquad
(1,1)\mapsto|1,1,0\rangle.
\]

## Gauge choice

Fixing the third occupation to zero is a section of the syndrome map, not a source-derived necessity. Other representatives related by the kernel of the syndrome map give the same logical class. A physical implementation may use a nonzero shared ancilla mode, but must preserve the two pairwise parities.

## Disposition

A finite, site-equivariant, detector-compatible encoder of the conductor quotient is constructed. The remaining physical gate is an authorized preparation mechanism implementing this encoding, followed by the already specified response calibration and raw acquisition.
