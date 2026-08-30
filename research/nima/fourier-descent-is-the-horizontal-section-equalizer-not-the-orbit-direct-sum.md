# Fourier descent is the horizontal-section equalizer, not the orbit direct sum

## Orbit packet

Let \(X_j\), \(j\in\mathbb Z/4\), be the four Fourier presentations, with
unitary transition maps

\[
F_j:X_j\longrightarrow X_{j+1},
\]

satisfying the order-four cocycle

\[
F_3F_2F_1F_0=I.
\]

Let

\[
D_j(s):X_j\longrightarrow Y_j
\]

be the conjugate boundary pencils, with corresponding transitions on the
targets and exact naturality

\[
D_{j+1}(s)F_j
=
F_jD_j(s).
\]

The diagnostic orbit direct sum is

\[
D_{\mathrm{orb}}(s)=\bigoplus_{j=0}^{3}D_j(s).
\]

Its determinant is the product of the four conjugate determinants and
therefore has fourth-power multiplicity when they coincide.

## Horizontal-section descent

Define the source descent object by the equalizer conditions

\[
X_{\mathrm{hor}}
=
\left\{
(x_0,x_1,x_2,x_3):
x_{j+1}=F_jx_j
\right\}.
\]

Every horizontal section is uniquely determined by \(x_0\). The map

\[
\Delta_F:X_0\longrightarrow X_{\mathrm{hor}},
\]

\[
\Delta_Fx
=
\left(
x,\,
F_0x,\,
F_1F_0x,\,
F_2F_1F_0x
\right)
\]

is an isomorphism. With the orbit-sum metric, the normalized map
\(\frac12\Delta_F\) is unitary.

Define \(Y_{\mathrm{hor}}\) analogously. Naturality implies

\[
D_{\mathrm{orb}}(s)X_{\mathrm{hor}}
\subseteq
Y_{\mathrm{hor}}.
\]

Hence the descended pencil is

\[
D_{\mathrm{desc}}(s)
=
D_{\mathrm{orb}}(s)|_{X_{\mathrm{hor}}}.
\]

Under \(\Delta_F\),

\[
D_{\mathrm{desc}}(s)
\cong
D_0(s).
\]

## Determinant fidelity

Whenever the determinant line is defined,

\[
\det_{\mathrm{rel}}D_{\mathrm{desc}}(s)
=
\det_{\mathrm{rel}}D_0(s),
\]

up to the constant nonzero normalization induced by the chosen horizontal
frame.

There is no fourth power. The four presentations are coordinate charts of one
equivariant object, not four independent state copies.

Likewise,

\[
\ker D_{\mathrm{desc}}(s)
\cong
\ker D_0(s),
\]

so algebraic and geometric kernel multiplicities are preserved exactly.

## Response packet survives

Although a horizontal section is determined by one component, it retains all
four response presentations:

\[
r_j'=M_ju_j,
\qquad
r_{j+1}'=F_jr_j'.
\]

They are not discarded; they are related by the equalizer equations. Thus the
descended state has one divisor multiplicity and a complete sewing-compatible
response trace.

The boundary trace of a horizontal kernel state lies in the graph of the
Fourier transition, with contragredient transport on response duals. Therefore
the maximal isotropic response relation survives descent.

## Cutoffs and restricted products

Prime cutoff projections commute with every \(F_j\) and \(D_j\). Hence they
preserve \(X_{\mathrm{hor}}\), and

\[
P_XD_{\mathrm{desc}}
=
D_{\mathrm{desc}}P_X.
\]

At unramified places the vacuum is fixed by Fourier, so the restricted-product
horizontal section has only finitely many non-vacuum coordinates on the
cylinder core. Completion is therefore taken after descent, not as an
infinite direct sum of four independent products.

## Categorical interpretation

The orbit direct sum is the coinduced diagnostic object. The physical
Fourier-sewn carrier is its descent equalizer.

Equivalently, it is the space of flat sections of the finite presentation
groupoid. Because the order-four holonomy is trivial on the declared source
object, evaluation at one chart is an equivalence.

A nontrivial central metaplectic sign must be retained in the coefficient
system. In that case the horizontal condition is twisted by the authorized
line character rather than replaced by strict equality. The determinant
remains one copy after twisting.

## Completion gates

The finite descent theorem is exact. Completion requires:

1. closedness of the equalizer in the saturated pro-Gram;
2. continuous transition maps on all three response strata;
3. compatibility of endpoint and archimedean lines with the cocycle;
4. no nontrivial holonomy outside the declared metaplectic character;
5. determinant-line continuity under the horizontal equivalence.

Unitary transitions and the saturated metric close the first norm issue. The
three-stratum transpose actions and anomaly-line trivialization remain the
source-specific checks.

## Hostiles

1. Use \(\bigoplus_jD_j\) as the physical pencil and obtain \(\Xi^4\).
2. Quotient the orbit sum by identifying vectors without enforcing transition
   compatibility.
3. Keep only \(x_0\) and discard the response presentations.
4. Ignore a metaplectic central sign.
5. Descend scalar determinants without descending kernels and boundary traces.
6. Complete before proving the equalizer is closed.

## Verdict

Determinant-faithful Fourier descent is the horizontal-section equalizer of
the four presentation orbit. It is unitarily equivalent to one presentation,
so it retains one copy of the \(\Xi\) divisor while preserving the complete
Fourier response packet.

The remaining gate is now the three-stratum completion of this equalizer,
especially the transpose sewing action on primitive currents and the
archimedean trivialization of the anomaly lines.
