# Two tiny tails in a coupled two-system

## Question

What new effects can arise when two individually tiny coherence tails interact across a two-system?

## Claim boundary

Let two completed systems have comparison operators \(A_1:H_1\to K_1\) and \(A_2:H_2\to K_2\). Their coupled comparison has block form

\[
\mathcal A_\varepsilon=
\begin{pmatrix}
A_1&\varepsilon U_{12}\\
\varepsilon U_{21}&A_2
\end{pmatrix}.
\]

The coefficient \(\varepsilon\) measures tail size. The operator type and incidence of \(U_{12},U_{21}\), not \(\varepsilon\) alone, determine the result.

### Uncoupled addition

If the two tails only add inside separate diagonal blocks, no new relational information appears. Two compact tails are still compact on the finite direct sum. They cannot open a gap across an essential approximate kernel.

Thus

\[
\text{tiny tail} + \text{tiny tail}
\]

is not automatically stronger than one tail. Parallel repetition without a comparison arrow merely duplicates the blind sector.

### Direct zero-mode splitting

Suppose \(A_1\) and \(A_2\) each have one hidden mode and the cross-coupling pairs them. On that two-dimensional hidden subspace,

\[
\mathcal A_\varepsilon^{\mathrm{hid}}
=
\begin{pmatrix}
0&\varepsilon u\\
\varepsilon\bar u&0
\end{pmatrix}.
\]

Its eigenvalues are \(\pm\varepsilon|u|\). The interaction splits the two zero modes and opens a gap of size \(\varepsilon|u|\). Each tail alone was invisible; their typed relation is observable.

This is the same mechanism as forming bonding and antibonding modes, a Dirac mass from two chiral modes, or an equality comparator from two otherwise unreferenced replicas.

### Second-order induced repair

If system 2 is already gapped and can be eliminated, the effective operator on system 1 is the Schur complement

\[
A_{\mathrm{eff}}
=
A_1-\varepsilon^2U_{12}A_2^{-1}U_{21}.
\]

The induced correction is second order. A tiny interaction can therefore create a still tinier but structurally new self-energy, sign, or boundary condition in system 1. This mechanism fails if \(A_2^{-1}\) is uncontrolled at completion.

### Symmetric and antisymmetric shadows

For two equivalent systems with exchange symmetry, pass to common and differential modes:

\[
x_+=x_1+x_2,\qquad x_-=x_1-x_2.
\]

Equal tail contributions reinforce in the even channel and cancel in the odd channel. Opposite tail contributions cancel in the even channel and reinforce in the odd channel.

If only the sum is observed, the differential mode remains invisible. Hence two tails plus scalar aggregation can be less faithful than either typed tail packet. An equality or orientation port is required to expose \(x_-\).

### Topological charge pairing

Suppose the character-resolved indices are opposite:

\[
\operatorname{ind}A_1=+1,\qquad
\operatorname{ind}A_2=-1.
\]

The total index is zero, but uncoupled compact repairs cannot make the individual blocks invertible. A cross-system arrow can pair the kernel of one system with the cokernel of the other and annihilate the combined defect.

This is genuine interaction-enabled closure. It is allowed only if the constructor theory authorizes mixing those sectors. If Fourier character, sheet parity, or source label forbids the coupling, the opposite charges merely cancel in the scalar ledger while the typed obstruction persists.

### Completion test

On infinitely many escaping modes, a compact cross-coupling still cannot open a uniform gap. For completion-stable repair, the interaction must be bounded below on the paired hidden sector:

\[
\|U_{21}v\|\ge c\|v\|
\]

with a cutoff-independent \(c>0\), or the coupled dynamics must yield an equivalent observability estimate.

A tiny coefficient \(\varepsilon\) then gives a small but genuine gap \(\varepsilon c\). Without that extensive support, finite zero-mode splitting can coexist with essential-spectrum escape.

### Interpretation for two modular tails

Two modular tails can interact in four qualitatively distinct ways:

1. reinforce the same forward seam identity;
2. cancel in the scalar-even channel while leaving an odd typed residue;
3. generate a second-order effective correction through a gapped intermediate system;
4. pair opposite kernel/cokernel or index defects through a new reverse-incidence arrow.

Only the fourth can solve the missing two-system mate at the topological level. It is not supplied by having two tails; it is supplied by the authorized cross-tail constructor.

## Disposition

Two tiny tails become qualitatively new only through their interaction map. The simplest useful two-system model is an off-diagonal coupling on the hidden sectors. It predicts a split pair of gains \(\pm\varepsilon|u|\), an even/odd readout decomposition, and possible annihilation of opposite Fredholm charges.

For the current programme, the decisive question is whether reciprocal modular tails merely coexist or whether theta/Tate transport derives an odd, reverse-incidence coupling between them. If that coupling is extensive on the completed hidden sector, two tiny tails can open a genuine mate gap. If it is absent or compact, their interaction produces only finite or scalar shadows.