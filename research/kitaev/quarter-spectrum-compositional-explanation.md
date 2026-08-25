# Wilson quarter spectra form a compositional residue semiring

Owner: `marici.Kitaev`

Ledger: Entries 2476, 2478, 2480--2482  
Graph: `ev-000000003400-27d86ba0-b34f-49e1-8d56-6331120b8666`,
`ev-000000003402-d44e4179-d444-4674-8f3e-0ece5821eb47`,
`ev-000000003406-328e6aa2-9d64-4aff-8d3e-4a94b5f678ed`,
`ev-000000003408-94a1d013-011c-4291-ac99-23946bcd630a`,
`ev-000000003410-73fe0897-5a83-4e13-9ecb-06f0a66cabbb`

## Replacement DPC

For every typed Wilson sector, retain the residue-count packet

\[
  h_x=(n_0,n_1,n_2,n_3),
  \qquad
  n_r=\#\{a:\lambda_x(a)\equiv r\pmod4\}.
\]

The replacement Deutsch--Popper conjecture is structural:

> The quarter-spectrum packet is a symmetric monoidal invariant valued in the
> monoid semiring \(\mathbb N[(\mathbb Z/4,\cdot)]\). Product-double spectra
> are forced by residue-product convolution. No scalar quotient, including
> quantum dimension, is explanatory unless its fibers are separately proved
> homogeneous under this convolution.

Unlike the retired DPC-QW, this statement derives a risky product prediction
from the independently established tensor structure.

## Exact convolution law

For (a=(a_0,a_1,a_2,a_3)), (b=(b_0,b_1,b_2,b_3)), with
(A=\sum a_i), (B=\sum b_i), the product packet is

\[
\begin{aligned}
c_0&=a_0B+b_0A-a_0b_0+a_2b_2,\\
c_1&=a_1b_1+a_3b_3,\\
c_2&=a_1b_2+a_2b_1+a_2b_3+a_3b_2,\\
c_3&=a_1b_3+a_3b_1.
\end{aligned}
\]

The extra (a_2b_2) in (c_0) records the nilpotent-looking arithmetic
(2\cdot2=0\pmod4). This is why a scalar such as dimension cannot reconstruct
the product spectrum: it forgets how multiplicity is distributed among the
four residue channels.

The checker exhausts the basis multiplication table, verifies associativity,
commutativity, the residue-one unit, and the closed formula. It then reproduces
the (D(S_4\times D_4)) falsifier exactly.

## Triangular explanatory coordinates

The convolution becomes transparent after the invertible change of variables

\[
  N=n_0+n_1+n_2+n_3,\quad O=n_1+n_3,\quad
  T=n_2,\quad \Delta=n_1-n_3.
\]

Here (N) is total rank, (O) counts the odd phases (\pm i), (T) counts
the residue-two phase (-1), and (\Delta) records the oriented (i) versus
(-i) imbalance. Their product law triangularizes:

\[
\begin{aligned}
N'&=N_aN_b, & O'&=O_aO_b,\\
T'&=T_aO_b+O_aT_b, & \Delta'&=\Delta_a\Delta_b.
\end{aligned}
\]

Thus (O+T\varepsilon) behaves as a dual number with
(\varepsilon^2=0). The product-double falsifier has coordinates

\[
  (462,0,180,0)\neq(462,0,220,0),
\]

so the sole missing datum in that example is (T), the multiplicity of the
(-1) phase. Dimension and rank erase precisely this control-relevant
channel. For a fixed ambient rank the spectrum requires three independent
coordinates ((O,T,\Delta)), subject to the parity and positivity conditions
needed to reconstruct the four counts.

The whole packet is equivalently reconstructed from two spectral moments once
the rank is known. For (U=\exp(2\pi iW/4)), set

\[
  \tau_1=\operatorname{Tr}U,
  \qquad
  \tau_2=\operatorname{Tr}U^2.
\]

Then

\[
\tau_1=(N-O-2T)+i\Delta,
\qquad
\tau_2=N-2O,
\]

so

\[
O={N-\tau_2\over2},\qquad
\Delta=\operatorname{Im}\tau_1,\qquad
T={N-O-\operatorname{Re}\tau_1\over2}.
\]

Thus the minimal spectral readout packet is ((N,\tau_1,\tau_2)), rather than
four independent bin counts. This remains an identification theorem:
estimating traces presupposes an interferometric instrument and does not
synthesize (U) or controlled-(U).

## Product-sector power cancellation law

The dual-number form solves every repeated product exactly:

\[
N_k=N^k,\qquad O_k=O^k,\qquad
T_k=kTO^{k-1},\qquad \Delta_k=\Delta^k.
\]

This makes a sharp product-double prediction. If a packet is supported only on
residues zero and two, then (O=0). Every external product-sector power
(k\ge2) therefore has

\[
  h^{\star k}=(N^k,0,0,0),
\]

so the quarter evolution associated to the product-sector Wilson operator
\(W_{x^{\boxtimes k}}\) is spectrally the identity even when the factor-sector
quarter evolution is nontrivial. Both dimension-six product sectors in the
counterexample exhibit this collapse after forming their external square.

This is **not** cancellation of the parallel gate \(U_x\otimes U_x\).
Independent gate phases add, while Wilson eigenvalues for an external product
sector multiply. The theorem concerns
\(\exp(2\pi iW_{x\boxtimes x}/4)\), not
\(\exp(2\pi iW_x/4)\otimes\exp(2\pi iW_x/4)\).

This is not an assertion that a physical compiler automatically cancels its
implementation faults or resource-state preparation. It is an exact logical
target simplification predicted before compilation.

## Cross-factor interaction rank

For general factor residues (r,s\), the external-product target has phase

\[
  K_{rs}=i^{rs}.
\]

The exact four-by-four kernel has operator-Schmidt rank four. Therefore a
generic product-sector quarter evolution is an interacting diagonal gate and
cannot be replaced by a tensor product of factor-only unitaries. On the
even-by-even support \(\{0,2\}\times\{0,2\}\), however, the kernel is the
all-ones matrix and has rank one. That exceptional rank-one restriction is
the precise reason the external-square target becomes identity.

Thus the resource cancellation is source-aware and support-dependent: a
compiler may omit the product-sector gate only after proving the residue
support lies in this separable kernel. It may not implement the target by
blindly applying the two factor gates.

## Explanation versus capability

This is a proper compositional explanation of the counterexample: it derives
the product behavior and states precisely what information dimension loses.
It does not derive physical access to any Wilson gate. The shared Carrier
contributes tensor composition and multiplicity transport; the quantum
coefficient lens contributes the mod-four phase map; coherent controlled
access remains an instrument resource.

## Falsifiers

- Failure of histogram convolution for a directly constructed product-double
  modular matrix.
- Failure of associativity or the residue-one unit.
- A proposed scalar replacement whose equal-value fibers are not closed under
  convolution with every admitted packet.

## Artifacts

- Checker: `checkers/check_quarter_spectrum_compositional_semiring.py`
- Result: `results/quarter-spectrum-compositional-semiring.json`
