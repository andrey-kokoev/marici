# Branch A: regulator-dependent endpoint–Q compatibility and the short-boundary transgression

Date: 2026-09-07.

## Results and scope

The complete regulator-family coefficient complex determines a new compatibility equation. In occurrence weight zero, every degree-three cycle is determined by two endpoint coefficients. Its image in the full long-facet quotient is `beta^2` times the negative-endpoint coefficient.

Three consequences are proved:

1. The endpoint correction required for the two previously recorded primitives is unique in this component. It changes the literal Q-chain by `beta^2 phi_Q`; no closed correction with those endpoint values has zero Q-projection.
2. The actual short-boundary attaching cycle `chi_beta = d(lift(phi_Q))` has exact cyclic module `Z[beta]/(beta^2)` in ordinary short-boundary homology. Its annihilating primitive has two necessary endpoint terms.
3. The Q-nullhomotopy of the previously computed supported-map difference has a nonzero lower lifting obstruction `beta[chi_beta]`. Thus the supported Q-projection can be nullhomotopic while its lift with the lower component fixed is obstructed.

All polynomial chain identities use the complete 430-state complex. The completeness statements about degree-three cycles and exact regulator annihilators concern the entire occurrence-weight-zero component, with arbitrary polynomial beta powers. They are not claims about every occurrence-weight component or the full occurrence-ring annihilator.

No physical conductor trivialization, identification with `Delta_J`, or geometric purity theorem at beta zero is claimed. Literal endpoint-coordinate framing is distinguished from a homotopy-coherent physical endpoint frame.

## 1. Coefficients, state labels, and the regulator family

Use the ordered diagonals

\[
\mathscr D=(02,03,04,13,14,15,24,25,35),
\]

with alternating sheets

\[
S_+=(13,15,35),\qquad S_-=(02,04,24),
\qquad L=(03,14,25).
\]

The universal normalized coefficient ring for this calculation is

\[
R=\mathbb Z[\beta,X_d:d\in\mathscr D]/(X_eX_o:e\in S_-,\ o\in S_+).
\]

The exponential graph factors as

\[
e^{\beta X_d}-1=\beta X_dv_d,
\qquad v_d=\sum_{n\geq0}\frac{(\beta X_d)^n}{(n+1)!}.
\]

The `v_d` are formal units at beta zero. Retaining their line changes separately gives the normalized native differential `beta X_d`. The independent occurrence-35 factor still has differential `X35`. There is no division by beta or any occurrence coordinate. Substitution of the actual exponential units is over characteristic zero; the normalized polynomial identities are integral.

A state is

\[
[F,H,\epsilon],\qquad H\subset F,\quad\epsilon\in\{0,1\},
\qquad \deg[F,H,\epsilon]=3-|F|+|H|+\epsilon.
\]

`F` is a noncrossing dissection and `epsilon` is the separate occurrence partner. The differential is the supplied signed radial/native-normal differential, tensored with this occurrence factor. It has radial coefficient `X_d`, native coefficient `beta X_d`, and occurrence coefficient `X35`.

Denote the full complex by `C_beta`, the short-boundary subcomplex by `B_beta`, and both endpoint packets by `V_beta`. Their sizes, and the size of the quotient, are

\[
|C_\beta|=430,\qquad |B_\beta|=416,\qquad |V_\beta|=32,
\qquad |Q_\beta|=14,
\qquad Q_\beta=C_\beta/B_\beta.
\]

The full quotient is used throughout. No projection onto three isolated generic edges is used.

Repository provenance is pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: signed radial/native differential and support subcomplexes.
- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: the independent occurrence correction.
- `research/voevodsky/check_d03_formal_support_purity.rs`: the exponential graph and the fixed-nonzero-beta scope of its geometric purity claim.
- Entry 93: alternating normalization coefficient ring.

The preceding beta-zero packet checker was replayed separately and reproduced its certificate byte-for-byte. Its certificate SHA-256 is

```text
9637135904ec497f5e87ca9caaff16960831fdf9780987164fcbd5c00850e276
```

The new standalone checker embeds the original four-chain inputs and rechecks their differential identities before transporting them. It does not depend on that earlier file at runtime.

## 2. The complete occurrence-weight-zero complex

Assign occurrence degree

\[
\deg_X[F,H,\epsilon]
=-\sum_{d\in F}\epsilon_d+\sum_{d\in H}\epsilon_d
+\epsilon\epsilon_{35}.
\]

To make occurrence degree zero, the coefficient monomial is forced:

\[
m_{F,H,\epsilon}
=\prod_d X_d^{\mathbf1_{d\in F}-\mathbf1_{d\in H}-\epsilon\mathbf1_{d=35}}.
\]

A state occurs exactly when all these exponents are nonnegative and the monomial survives the alternating-sheet relations. Its coefficient may then be any polynomial in beta. Write `Lambda=Z[beta]`.

The resulting free Lambda-complex has ranks

\[
(8,59,108,56)
\]

in homological degrees zero through three. There is no occurrence-weight-zero degree-four state. This is an exhaustive component, not a cutoff on coefficient degree.

The full fourteen-state Q quotient contributes seven states to this component. The other seven have positive occurrence-35 degree and cannot be compensated by a polynomial occurrence coefficient. In bases

\[
(T,h_{03},h_{14},h_{25}),\qquad
(\lambda_{03},\lambda_{14},\lambda_{25}),
\qquad \lambda_l=X_lp_l,
\]

its differential is

\[
\begin{pmatrix}
1&\beta&0&0\\
1&0&\beta&0\\
1&0&0&\beta
\end{pmatrix}.
\]

Hence

\[
H_3(Q_\beta)_{(0)}=\Lambda\varphi_Q,
\qquad
\varphi_Q=\beta T-h_{03}-h_{14}-h_{25}.
\]

In particular, the entire top-plus-three-normal cycle, rather than a selected edge, determines this group.

## 3. All top cycles are determined by two endpoint coefficients

The previously recorded cycle is

\[
Z_\beta=P_\beta\Psi_\beta,
\]

where

\[
\Psi_\beta=
\sum_F(-1)^{|F|(|F|+1)/2}\beta^{3-|F|}[F,F,0].
\]

The map `P_beta` replaces a native 35 mark by `beta` times the occurrence-35 partner and kills states already containing both. It is the previously verified face-preserving chain idempotent.

Define

\[
Z_-=Z_\beta,\qquad Z_+=\Psi_\beta-Z_\beta.
\]

Both are closed. Let

\[
E_-=[S_-,S_-,0],\qquad
E_{+,\mathrm{nat}}=[S_+,S_+,0],\qquad
E_{+,\mathrm{occ}}=[S_+,\{13,15\},1].
\]

The full endpoint restrictions are

\[
\operatorname{pr}_V Z_-=E_-+\beta E_{+,\mathrm{occ}},
\]

\[
\operatorname{pr}_V Z_+=E_{+,\mathrm{nat}}-\beta E_{+,\mathrm{occ}}.
\]

The coefficient of `E_-` and that of `E_+,nat` give an identity matrix on `(Z_-,Z_+)`.

### Completeness proof

Delete these two endpoint-coordinate columns from the 56-column degree-three differential. The checker exports a 54-by-54 minor whose determinant is exactly

\[
\beta^{48}.
\]

Every entry is homogeneous: its beta exponent is the native-mark count of the source basis state minus that of the target basis state. Thus all determinant terms have the same beta exponent. The corresponding integer determinant after stripping these weights is `+1`; it is computed by fraction-free elimination. Evaluation at beta one alone is not the proof.

Since beta is a nonzero divisor in Lambda, the remaining 54 columns are injective over Lambda. For an arbitrary closed chain, subtract its two endpoint coefficients times `Z_-` and `Z_+`. The remainder is closed and has those endpoint coordinates zero, hence vanishes by this minor.

Therefore

\[
Z_3(C_\beta)_{(0)}=H_3(C_\beta)_{(0)}
=\Lambda Z_-\oplus\Lambda Z_+.
\]

This is a full polynomial-beta classification of this occurrence component. It extends to a torsion-free formal beta base. It does not apply unchanged to a nonflat specialization such as beta zero, where the determinant vanishes and extra cycles can appear.

For

\[
Y=aZ_-+bZ_+,
\]

all endpoint and Q coefficients are consequently forced:

\[
\operatorname{pr}_VY
=aE_-+bE_{+,\mathrm{nat}}+\beta(a-b)E_{+,\mathrm{occ}},
\]

\[
\pi_QY=\beta^2a\varphi_Q.
\]

This is the endpoint–Q compatibility equation. It is derived from the full matrices.

### Consequence for the recorded primitives

The inherited packet supplies

\[
dH_\beta=dG_\beta=\beta A_\beta,
\qquad G_\beta-H_\beta=Z_-.
\]

A correction to `G_beta` which preserves its boundary and changes its endpoint components to those of `H_beta` must be a closed chain with endpoint coefficients `(1,0)`. It is therefore exactly `Z_-` in this component. Its Q-change is necessarily `beta^2 phi_Q`.

There is no alternative closed correction with these endpoint values and zero Q-projection. Endpoint-local subtraction also fails: the endpoint part of `Z_-` is not closed. Its six outgoing differential terms require the retained nonendpoint correction terms.

## 4. The source-defined attaching cycle has exact regulator order two

Let `tilde phi_Q` be the labelled four-term lift of `phi_Q` to `C_beta`. Define

\[
\chi_\beta=d\widetilde\varphi_Q.
\]

Since `phi_Q` is closed in the actual quotient,

\[
\chi_\beta\in B_{\beta,2},\qquad d\chi_\beta=0.
\]

It has eighteen terms: six terms `beta X_s p_s` on short facets and twelve radial terms on compatible long/short pairs with the long mark retained. Its endpoint and Q components are both literally zero.

Define the complete short-boundary primitive

\[
W_\beta=\beta^2\widetilde\varphi_Q-Z_-.
\]

It has forty-one terms and satisfies

\[
W_\beta\in B_{\beta,3},\qquad
 dW_\beta=\beta^2\chi_\beta,
\]

\[
\operatorname{pr}_VW_\beta=-E_--\beta E_{+,\mathrm{occ}}.
\]

The boundary of its endpoint part has six nonzero terms. Deleting those endpoint terms changes the boundary equation by exactly those six terms.

### Exact annihilator

The actual short exact sequence

\[
0\longrightarrow B_\beta\longrightarrow C_\beta
\longrightarrow Q_\beta\longrightarrow0
\]

has connecting homomorphism

\[
\partial[\varphi_Q]=[\chi_\beta].
\]

The calculation of Section 3 gives

\[
\operatorname{im}\bigl(H_3(C_\beta)_{(0)}\to
H_3(Q_\beta)_{(0)}\bigr)=\beta^2\Lambda\varphi_Q.
\]

Exactness of the homology sequence therefore proves

\[
\Lambda[\chi_\beta]\cong\Lambda/(\beta^2).
\]

In particular `beta[chi_beta]` is nonzero, and `beta^2[chi_beta]` is zero. This is regulator-parameter torsion with no integer-prime torsion. It is a cyclic submodule of the full short-boundary homology, not a claimed classification of that entire homology group.

An independent central-fibre check contracts the complete short-boundary occurrence-zero complex integrally. One of its integer homology coordinate functionals evaluates `chi_beta mod beta` to `1`. Thus the leading attaching class is primitive and nonzero, rather than an artifact of a nonsaturated lattice calculation.

The two-state complex with differential `beta^2`, placed in degrees three and two, has the explicit map

\[
p\mapsto\chi_\beta,\qquad e\mapsto W_\beta.
\]

It should not be confused with the excess complex `K(beta,beta)`: a single nonreduced regulator equation and two coincident normal equations are different complexes.

## 5. The supported Q-nullhomotopy has a nonzero lower lifting obstruction

Retain the preceding source

\[
S_\beta=[Re\xrightarrow{\beta}Rp],
\qquad |e|=3,\quad |p|=2.
\]

The actual difference of the two supported maps is

\[
D_\beta(p)=0,\qquad D_\beta(e)=Z_-.
\]

Its Q-projection is nullhomotopic. In occurrence weight zero, the unique degree-one homotopy is

\[
K_Q(p)=\beta\varphi_Q,\qquad K_Q(e)=0.
\]

Indeed `d_Q(phi_Q)=0`, and the top Hom equation is

\[
\beta K_Q(p)=\beta^2\varphi_Q.
\]

There is no degree-four Q state in this occurrence component, and its coefficient modules have no beta torsion. These facts prove uniqueness, not merely existence of this particular expression.

Lift that homotopy by the actual labelled section:

\[
U(p)=\beta\widetilde\varphi_Q,\qquad U(e)=0.
\]

The full Hom differential gives

\[
\delta U(p)=\beta\chi_\beta,\qquad
\delta U(e)=\beta^2\widetilde\varphi_Q.
\]

The bottom defect is not removable by a different short-supported choice of lift. Such a change modifies it by a boundary in `B_beta`, whereas

\[
\beta[\chi_\beta]\ne0.
\]

Equivalently, a closed lift of `beta phi_Q` would require that element to lie in the image `beta^2 Lambda phi_Q`, which it does not.

The difference can still be represented by a genuine short-supported map after this ordinary homotopy:

\[
D_\beta-\delta U:
\quad
p\longmapsto-\beta\chi_\beta,
\qquad
 e\longmapsto-W_\beta.
\]

The checker verifies both source columns against all target differential terms. Its Q-projection is zero. Its top image retains the original endpoint discrepancy, and its bottom image is no longer zero.

Thus this homotopy does not preserve the originally common bottom cochain `A_beta`. A nullhomotopy seen only after Q-projection conceals precisely the lower class `beta[chi_beta]`.

## 6. Holding the endpoint coordinates literally fixed changes the annihilator problem

Define the actual subcomplex

\[
B^\circ_{\beta,n}
=\{c\in B_{\beta,n}:\operatorname{pr}_Vc=0,
\ \operatorname{pr}_Vdc=0\}.
\]

The second condition is essential: coordinate projection onto a subcomplex is not generally a chain map. These two conditions make `B_beta^circ` closed under its differential.

The cycle `chi_beta` belongs to this subcomplex. Suppose a polynomial `p(beta)` times it were a boundary there:

\[
dY=p(\beta)\chi_\beta,
\qquad Y\in B^\circ_{\beta,3,(0)}.
\]

Then

\[
p(\beta)\widetilde\varphi_Q-Y
\]

would be a closed degree-three chain of the full complex with zero endpoint coefficients. Section 3 forces it to vanish. Its Q-projection is `p(beta) phi_Q`, forcing `p=0`.

Consequently

\[
\Lambda[\chi_\beta]\cong\Lambda
\quad\text{inside }H_2(B^\circ_\beta)_{(0)}.
\]

Forgetting this strict endpoint constraint maps the displayed cyclic submodule to `Lambda/(beta^2)`. The ordinary annihilating primitive is excluded by its explicitly computed endpoint terms. No inference is made that this strict subcomplex is the full physical homotopy-coherent frame category.

This result concerns an attaching cycle in short-boundary degree two. It is not a contradiction to earlier uniqueness statements for Q-fillings with a fixed attaching chain; those classify a different mapping problem.

## 7. All twelve extra central endpoint-fixed top classes fail at first order

At beta zero, the complete occurrence-zero complex has homology ranks

\[
H_1:\ 6,\qquad H_2:\ 21,\qquad H_3:\ 14.
\]

The fourteen top classes are the fourteen fully native-marked triangulations. Fixing the two native endpoint coefficients leaves twelve top classes.

Write

\[
d_\beta=d_0+\beta d_1.
\]

For a central cycle `Y0`, first-order extension requires

\[
d_0Y_1=-d_1Y_0.
\]

Using the complete integral contraction `(p0,i0,h0)` of `d0`, the obstruction is the actual matrix

\[
b_1=p_0d_1i_0:H_3(C_0)_{(0)}\to H_2(C_0)_{(0)}.
\]

Its restriction to the twelve endpoint-zero top classes has a 12-by-12 minor of determinant `-1`. Thus no nonzero one of those twelve classes extends even to the first infinitesimal beta thickening. The central reductions of `Psi_beta` and `Z_beta` span the remaining two-dimensional kernel and have their already displayed polynomial lifts.

This computation precludes interpreting the extra central top classes as uncomputed endpoint-fixed family deformations. It does not assume fixed-nonzero-beta purity at the singular parameter value.

## 8. Verification and remaining physical question

The new standalone verifier checks 13,114 exact identities. It includes:

- all 430 states, all endpoint and short-support conditions, and the actual fourteen-state quotient;
- the inherited four-chain packet and its graph/unit change;
- the two endpoint-top quotient maps and their explicit global sections;
- the exact `beta^48` top-kernel minor and its weight factorization;
- all eighteen transgression terms, forty-one primitive terms, and six endpoint corrections;
- the supported Q-homotopy and its lower defect;
- the full central contraction and the integral first-order obstruction minor.

All new polynomial witnesses are embedded in the certificate with face labels, mark subsets, occurrence bits, and coefficient exponents. No companion files or external libraries are required to run the checker.

Run:

```sh
python branch_a_beta_endpoint_q_transgression_checker.py \
  --output branch_a_beta_endpoint_q_transgression_certificate.json
```

The newly explicit compatibility obstruction is `beta[chi_beta]`, obtained from the existing support exact sequence. It is not assigned the name `Delta_J`: the independently constructed physical conductor and Morse maps have not been compared with this supported map pair. The long-facet cycle uses all three long normals; it is not a new D03-only residue.

The next physical input must specify whether the lower cochain and endpoint comparisons are to be fixed strictly or coherently, and supply their actual transport. The equations above give its nonzero obstruction and the endpoint/Q changes needed to remove it in the computed coefficient model.

## Mathematical references

- Stacks Project, [Hom complexes, tag 0A8H](https://stacks.math.columbia.edu/tag/0A8H): mapping degrees, differential, and homotopy signs.
- Stacks Project, [Lemma 12.13.12, tag 0117](https://stacks.math.columbia.edu/tag/0117): the connecting map of an actual short exact sequence of complexes.
- Stacks Project, [The Koszul complex, tag 0621](https://stacks.math.columbia.edu/tag/0621): parameter homotopies and normal-generator comparisons.
