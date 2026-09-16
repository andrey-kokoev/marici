# The analytic Cech tetrahedron does not by itself lift to the positive polarized cell

## Question

Do the complete lattice-cell analytic equations immediately imply

\[
G_{phys,\alpha}^T-
\widehat G_\alpha^T
=
G_{phys,\alpha}^0-
\widehat G_\alpha^0
\succeq0?
\]

## What the analytic cell proves

The four presentation charts have the common source graph

\[
\Psi_S(g)
=(S_1g,S_2g,S_3g,S_4g).
\]

On essential images,

\[
C_{ij}=S_jR_i.
\]

Therefore every face and tetrahedral route commutes strictly:

\[
C_{jk}C_{ij}=C_{ik}.
\]

Equivalently, the rank-one cell is the Cech tetrahedron of the source-rooted chart equivalences.

This is an exact analytic result.

## Level at which it is proved

The source-rooted comparison involving \(C_{34}\) is identified at signed Hermitian-form strength:

\[
\mathcal Q_3(g,h)
=W_S(g*h^*)
=\mathcal Q_4(g,h).
\]

The existing Cech filler therefore lives in the category of complete analytic or Hermitian-form presentations.

It does not automatically live in a category whose objects include a chosen positive polarization

\[
G=G^+-G^-.
\]

The forgetful map

\[
(G^+,G^-)
\longmapsto
G^+-G^-
\]

is not faithful: adding the same positive Gram \(B^*B\) to both legs leaves the signed form unchanged.

## The desired local square

At fixed lattice coordinate \(\alpha\), the required polarized square is

\[
\begin{array}{ccc}
X_{phys,\alpha}^T&\longrightarrow&\widehat X_\alpha^T\\
\downarrow&&\downarrow\\
X_{phys,\alpha}^0&\longrightarrow&\widehat X_\alpha^0.
\end{array}
\]

Commutativity means that the two complementary face maps have the same source Gram. Thus there must be a feature \(B_\alpha\) and isometries on generated ranges such that

\[
X_{phys,\alpha}^T
\simeq
B_\alpha\oplus\widehat X_\alpha^T,
\]

\[
X_{phys,\alpha}^0
\simeq
B_\alpha\oplus\widehat X_\alpha^0.
\]

Taking Grams gives the desired identity immediately.

## What is already available positively

For \(C_{34}\), the finite-cutoff four-leg and ordered eight-leg projection dilations are exact. The Hadamard common/difference rows satisfy

\[
C^*C+D^*D=I,
\]

\[
C^*J_2D+D^*J_2C=Q_T-Q_0.
\]

They construct a regulator-relative positive lift of the signed \(C_{34}\) edge. Dyadic and conductor refinements preserve this lift.

Hence a positive local cell exists internally in the relative-feature presentation.

## Missing comparison

What has not been supplied by the analytic Cech equations is a natural isometric comparison between:

1. the independently named physical positive polarization
   \[
   X_{phys,\alpha}^{T,0};
   \]
2. the four/eight-leg relative-feature polarization
   \[
   \widehat X_\alpha^{T,0}.
   \]

The signed analytic cell only proves

\[
G_{phys,\alpha}^T-G_{phys,\alpha}^0
=
\widehat G_\alpha^T-
\widehat G_\alpha^0
\]

when the physical signed edge has been identified with the same \(C_{34}\) form. This is equality after applying the nonfaithful forgetful functor. It does not select the common summand.

## Precise lifting problem

Let \(\mathsf{PosFeat}_\alpha\) be the category of regulated positive features and isometric intertwiners, and let \(\mathsf{Herm}_\alpha\) be the category of signed Hermitian forms. There is a forgetful functor

\[
U:\mathsf{PosFeat}_\alpha\to\mathsf{Herm}_\alpha.
\]

The analytic lattice supplies a commuting tetrahedron in \(\mathsf{Herm}_\alpha\). The desired equation asks for a commuting lift of the relevant two polarized sub-tetrahedra through \(U\).

Thus the remaining datum is a 2-cell in \(\mathsf{PosFeat}_\alpha\), not another equality in \(\mathsf{Herm}_\alpha\).

## Easy case

If the phrase “physical positive feature” is defined to mean the exact transported four/eight-leg projection dilation, then both polarizations are already parts of the same feature object. The local square commutes by construction, and the common remainder is its shared common row.

In that convention the theorem is formal and should not be listed as an open analytic gate.

## Nontrivial case

If \(X_{phys,\alpha}^{T,0}\) denotes an independently normalized prolate/Widom positive feature, then one must provide a natural isometry from that feature to the transported relative dilation. The analytic Cech equations do not contain this isometry.

This is exactly the distinction between:

- an internal positive polarization of the already coherent \(C_{34}\) cell;
- comparison with an external physical positive realization.

## Decision required

The notation \(G_{phys,\alpha}^{T,0}\) must be fixed in one of two ways.

### Internal meaning

\[
G_{phys,\alpha}^{T,0}
:=
\text{Grams of the transported exact positive dilation}.
\]

Then the polarized sub-tetrahedron diagram is immediate and the common-remainder identity is formal.

### External meaning

\[
G_{phys,\alpha}^{T,0}
:=
\text{independently normalized prolate/Widom Grams}.
\]

Then the cell equations prove only their signed shadow, and the positive comparison remains a separate lifting theorem.

## Disposition

The full analytic lattice cell does make the desired diagram easy **after the positive polarization is declared internal to the cell**. It does not recover a chosen external positive Gram from signed chart commutativity.

The apparent obstruction is therefore primarily a typing ambiguity in \(G_{phys,\alpha}^{T,0}\): internal relative-feature Gram or external prolate/Widom Gram.
