# Rees transport of the whole native attachment triangle

Date: 2026-09-07  
Project: Marici, native-normalization comparison lane  
Pinned source commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result

The complete mixed-short-edge attachment triangle has been pulled to the six-short-normal Rees graph. Its source comparison, nullhomotopies, corrected generic cycle, and both endpoint composites remain in one chain diagram. The source-cone equivalence survives through its original 81 signed-unit cancellations.

The calculation also determines the entire polynomial Rees family in the fixed six-occurrence/three-long-normal frame. The endpoint-quotient mapping complex is quasi-isomorphic to a free rank-sixteen Rees module in cohomological degree two. Its generic map is projection to the empty-short-face generator. The other fifteen generators occupy positive Rees degrees; they are not fifteen alternative maps in the old degree-zero normalization problem.

Each endpoint mapping complex is a two-term **product-divisor** Čech complex in degrees two and three. The old endpoint composite is its residue class `1/tau`. A seven-term cochain in the actual endpoint mapping complex witnesses that multiplying this residue by `tau` makes it a boundary. After central Rees specialization that seven-term cochain leaves a primitive fully marked endpoint term, whereas the old residue map itself specializes to zero.

The ordered three-Rees Koszul/Gysin map is now composed into these actual endpoint complexes, with three presentations, three pair homotopies, and a triple coherence on each side. The full lower-component map survives centrally. This is not an identification of its source with the independent branch-pair excess complex, nor an identification with the separately prescribed geometric collar operators. Those identifications and physical reflection parity remain unproved.

## 2. Chart, gradings, and the actual change of coefficient domains

Let the short labels be `0,...,5`, and let the long labels be `D03,D14,D25`. The original chart has independent occurrence variables `X_a` and normals `u_a`. Pull it to

\[
\mathcal A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25},
 t_0,\ldots,t_5,u_{D03},u_{D14},u_{D25}],
\qquad u_i=t_iX_i\quad(0\le i\le5).
\]

In words: apply the source's three-normal Rees construction on both sheet-conjugate triples; leave the long normals independent. This is a declared polynomial Rees chart, not a specialization of physical channel coordinates. The normal, occurrence, and Rees families remain distinct. The corresponding source construction, including its retained conormal-valued Bockstein, is [S1].

For an original state `(S,H)`, write `L=S minus H`. Its coefficient module becomes

\[
\mathcal A[(t_iX_i)^{-1}:i\in L\cap\{0,\ldots,5\}]
 [u_\ell^{-1}:\ell\in L\cap\{D03,D14,D25\}].
\]

In words: only the originally unmarked coordinates are localized. Within a stalk that already inverts `t_i X_i`, each factor is necessarily a unit. Expressions such as `1/X_i` or `1/t_i` below are used only in those stalks, or in explicitly specified supported output modules. They do not invert an occurrence coordinate on the base.

This change of domains matters. One must not keep the old polynomial-in-occurrences test after pulling an existing normal localization to the Rees graph. Conversely, one must not invert `X_i` in a marked state or outside its permitted face.

The target's short radial coefficient becomes `1/t_i`; its marked-normal differential is still the signed localization inclusion. The inherited long radial coefficient is `X_ell/u_ell`. Every term of this substituted differential is checked, including its endpoint and short-support subcomplexes.

Let `P` be the fifty-generator native-node resolution. Its differential involves only occurrence variables. Define `C_Z` to be the derived mapping complex from `P` to a target `Z`, fixing short occurrence degree minus one in each of the six directions, long occurrence degree zero, and long-normal degree one in each of the three directions. Leave all six Rees degrees variable. Thus `C_Z` is a graded complex over

\[
R=\mathbb Z[t_0,\ldots,t_5].
\]

In words: this is the polynomial Rees coefficient family, not a single integer matrix slice. Unused external coefficient parameters can be restored as flat spectators. The exact homogeneous classification here is made before any optional nonhomogeneous localization at `1+t_iX_i`.

For source basis element `b`, let `w_i(b)` be its short occurrence degree. A target coefficient in Rees degree `alpha` has

\[
\deg_{X_i}c=w_i(b)-1,\qquad
\deg_{t_i}c=\alpha_i-\mathbf1_{i\in S}.
\]

In words: these two exponents are tested separately against the actual Rees stalk. A negative exponent in either coordinate requires that the corresponding short label be unmarked and present. This enumerates every homogeneous map and homotopy in the declared frame.

## 3. The entire source attachment triangle survives

Retain the source sequence

\[
0\longrightarrow L\xrightarrow{\mu}T\longrightarrow\mathfrak B\longrightarrow0,
\qquad
L=L_{03}\oplus L_{25}\oplus L_{41}.
\]

In words: `T` is the short-face ring, `mathfrak B` is the actual normalization node, and each bridge module retains its pair product and four complementary occurrence annihilators. These modules are not replaced by free road labels.

The original resolution maps `phi` and `h` satisfy

\[
d_Ph+hd_L=\phi\mu.
\]

In words: the bridge inclusion becomes zero in the node through its actual resolution homotopy. Because all coefficients in this equation are polynomial in the occurrence variables, it persists on the Rees graph without any new choice.

The cap and its two endpoint composites obey

\[
d_KF-Fd_P=a_+f_+-a_-f_-.
\]

In words: the full corrected map is closed in the endpoint quotient, and its absolute defect is the specified difference of the two native endpoint maps. Neither endpoint is deleted before the comparison.

For `A_T=F phi` and `G_L=F h`, the complete bridge equation remains

\[
d_KG_L+G_Ld_L=A_T\mu+ah.
\]

In words: the source attachment and its endpoint term are transported simultaneously. The 112-generator source cone and its cap are included in the computation.

Every equation is verified after all 64 specializations obtained by setting a subset of the six short Rees parameters to zero. A localized stalk containing a parameter that is set to zero is the zero module. Fractions are never evaluated by numerical substitution at zero.

All source resolutions are finite free, and all target summands are localizations of the polynomial Rees ring. Consequently these termwise specializations compute derived base change of the displayed complexes. The source resolutions remain resolutions after this graph pullback because their equations use only the occurrence variables and the new chart is polynomial over that occurrence base. No general flatness assertion about the map from the old independent-normal chart is needed.

## 4. Sixteen explicit polynomial-natural Rees generators

Let `F_short` consist of the empty short face, the six singletons, and the nine compatible short pairs. The two endpoint triples are omitted. This is a set of sixteen faces, all taken from the original hexagon noncrossing rule.

For every such face `S`, the checker constructs an actual closed endpoint-quotient cochain `F_S`. It has Rees degree

\[
\beta_S=\sum_{i\in S}e_{t_i}.
\]

In words: the new marked-short components carry their Rees degree rather than being silently read as degree-zero coefficients. Its coefficient on the native top wedge mapping to the fully marked `S` state is a signed unit. Same-sheet pair generators are oriented so the endpoint restriction formula below has positive incidence.

The complete result is

\[
C_E\simeq\bigoplus_{S\in\mathcal F_{\rm short}}R\langle\beta_S\rangle[-2],
\qquad
C_Q\simeq R[-2].
\]

In words: angle brackets specify the degree of the free module generator; the cohomological shift places these modules in degree two. There is no other cohomology in this occurrence/long-normal frame.

The generic restriction is

\[
[F_\varnothing]\longmapsto[\omega],\qquad
[F_S]\longmapsto0\quad(S\ne\varnothing),
\]

\[
\omega=U_LT-\sum_{\ell\in\{D03,D14,D25\}}
X_\ell\frac{U_L}{u_\ell}M_\ell,
\qquad U_L=u_{D03}u_{D14}u_{D25}.
\]

In words: the empty-face generator is exactly the preceding 43-term native cap. Its generic value is the actual corrected chamber cycle, not a detached norm. All other generators have zero generic projection term by term.

### Proof of polynomial naturality and completeness

The sixteen cochains are explicit maps, extended by polynomial multiplication in `R`. Their comparison cone is integrally acyclic in every Rees degree. To establish this without a polynomial cutoff, classify each exponent as negative, zero, or positive. The stalk inequalities change only at zero and one. Source and target differentials preserve degree, and each permitted coefficient is a unique monomial. Multiplication identifies every negative magnitude with the negative representative and every positive magnitude with the positive representative. There are exactly 729 coefficient-domain shapes.

The checker reduces the cone of the **same sixteen polynomial maps** in all 729 shapes, using only signed-unit cancellations. All cones have zero remainder. It also checks the 192 multiplication arrows between nonnegative Boolean degrees. Thus no independently chosen cohomology basis is being substituted for a coefficient-natural map.

The new positive-degree directions do not contradict the earlier uniqueness statement. At Rees degree zero only the empty-face free generator is available.

## 5. Both endpoint complexes have explicit product-divisor models

Set

\[
\tau_+=t_1t_3t_5,\qquad \tau_-=t_0t_2t_4,
\qquad
\beta_+=e_{t_1}+e_{t_3}+e_{t_5},\quad
\beta_-=e_{t_0}+e_{t_2}+e_{t_4}.
\]

In words: each endpoint retains its own ordered three-Rees determinant degree. These are products of Rees parameters, not products of occurrence or long-normal variables.

The complete endpoint models are

\[
C_{V_\pm}\simeq
\left[R\langle\beta_\pm\rangle
\longrightarrow R[\tau_\pm^{-1}]\langle\beta_\pm\rangle\right],
\]

placed in degrees two and three. In words: the differential is the localization inclusion. Its degree-three cohomology is the local-cohomology module `R[tau^-1]/R`, with the displayed frame.

This support is the divisor union `V(tau_pm)`, not the triple intersection cut out by the three individual Rees parameters. Extended Čech complexes and derived base change distinguish those operations [M1].

### Actual maps into the unreduced endpoint complex

The comparison is supplied by two explicit cochains on each endpoint:

\[
\mathsf d j_{0,\pm}=j_{1,\pm}=\tau_\pm a_\pm^{\rm nat}.
\]

In words: `j0` has seven actual target terms; `j1` has three; `a_pm^nat` is the corresponding endpoint component of the full native cap equation. The differential is the complete source-to-target Hom differential, not only the target normal boundary.

Every target row of `j1` has all three endpoint normals unmarked, so it accepts the entire permitted module `R[tau^-1]`. The seven rows of `j0` range over all nonempty marked subsets, with their necessary reciprocal occurrence factors only in the remaining unmarked Rees stalks. The comparison map is an isomorphism in every derived coefficient degree: its cone is checked in all 729 shapes.

There is also a direct algebraic proof. Before excluding the empty odd or even source subset, each endpoint factor has two localized states and one polynomial state. Its differential is the row `(-1,1)`, and the two identical localized terms contract. The product of the three factors retracts to `R`. The excluded all-missing source subset is `R[tau^-1]`; the induced map from the product retraction to that quotient is ordinary localization. Its homotopy fibre is exactly the displayed two-term endpoint complex. This uses an allowed localization inclusion, not an inverse between unequal stalks.

### The endpoint row of the whole cap

Let `t_S` denote the product of the Rees variables in a short face, and put `E_plus={1,3,5}`, `E_minus={0,2,4}`. With the chosen compatible orientations,

\[
\partial_\pm[F_S]=
\begin{cases}
[t_S/\tau_\pm],&S\subseteq E_\pm,\\
0,&S\nsubseteq E_\pm.
\end{cases}
\]

In words: a face contributes to an endpoint precisely when it is contained in that endpoint triangle. The formula has actual cochain comparison homotopies for every generator; it is not inferred from scalar values.

In particular, the old normalized cap has endpoint values

\[
[1/\tau_+],\qquad[1/\tau_-],
\qquad
\operatorname{Ann}_R[1/\tau_\pm]=(\tau_\pm).
\]

In words: these are primitive product-divisor residues. A single Rees factor generally does not annihilate the residue; the full endpoint product does. This differs from multiplication by an internal normal in the earlier independent-normal calculation.

## 6. Central specialization separates the old maps from their Gysin continuations

Let `R0=R/(t0,...,t5)`. Flat Čech models give

\[
C_{V_\pm}\otimes_R^L R_0
\simeq R_0\langle\beta_\pm\rangle[-2].
\]

In words: the endpoint **object** survives, one degree earlier than its generic residue cohomology. The localized term disappears; the lower polynomial term remains.

However, the old free-source residue map to `C_V[1]` specializes to zero. In the actual cap, every old endpoint term lies in a stalk that inverts its three endpoint Rees parameters. The generic cycle `omega` involves no short Rees inverse and survives unchanged.

This is a result about the complete morphisms. It is not a rule for substituting zero into a residue class. Because base change preserves cochain homotopies, changing the old representative cannot make its zero specialized endpoint map into a nonzero one [M2].

The seven-term `j0` has a different central value:

\[
j_{0,+}(p_{E_0,O_0})=-U_L[v_+,v_+],\qquad
j_{0,-}(p_{E_0,O_0})=-U_L[v_-,v_-].
\]

In words: after specialization, exactly the fully marked endpoint row remains on each side. The minus signs are the computed source/target orientation signs; they are not physical parity assignments. Each row is primitive in its own determinant frame.

The entire central homogeneous mapping problem was independently recomputed in all 64 Boolean Rees degrees. A noncrossing short face supplies one primitive degree-two absolute class; an endpoint triple supplies its endpoint class; an incompatible face supplies none. The generic quotient has a class only in Rees degree zero. In particular:

| Central Rees degree | Generic class | Endpoint classes |
|---|---|---|
| Zero | One primitive class | None |
| `beta_plus` | None | One primitive plus class |
| `beta_minus` | None | One primitive minus class |

The table refers to one fixed degree at a time. In words: the three surviving classes cannot be identified as one homogeneous scalar-normalized triple. Their conormal transitions are part of the required construction.

## 7. The full Gysin maps now land in the actual endpoint Hom complexes

For an ordered endpoint triple `a,b,c`, let `K^.(t_a,t_b,t_c)` be the cohomological Koszul complex with wedge differential. Use the product-divisor Čech target `C_tau=[R -> R[tau^-1]]`. There are three presentations, indexed by a selected label `i`, of the same derived support map:

\[
g_i^0=1,\qquad g_i^1(e_j)=\delta_{ij}/t_i,
\qquad g_i^p=0\quad(p\ge2).
\]

In words: retain the lower unit and one single-localization component. This is the ordered Koszul residue followed by the support inclusion from the closed triple intersection to the divisor union. It does not identify those supports.

For `i<j`, the pair homotopy has its only nonzero entry

\[
h_{ij}(e_i\wedge e_j)=1/(t_it_j),\qquad
\mathsf d h_{ij}=g_j-g_i.
\]

In words: both local trace presentations are joined by an explicit permitted localized comparison. The triple coherence is

\[
v_{ijk}(e_i\wedge e_j\wedge e_k)=-1/(t_it_jt_k),\qquad
\mathsf d v_{ijk}=h_{jk}-h_{ik}+h_{ij}.
\]

In words: the three comparisons close through the existing top Koszul component, not through averaging.

Composing these maps with the actual `j0,j1` endpoint comparison gives the complete Gysin morphisms into the unreduced native-source/endpoint Hom complexes. All their source and target differential equations are checked. At the central face the localized components vanish and `j0` retains the primitive marked row. Relative to the common degree-two marking shift, the source retains the three-direction Gysin shift and its ordered determinant. A bare free generic source cannot be substituted for this Koszul source [M3].

These maps do not turn the vanished old residue morphism into a nonzero morphism with the same source and degree. They construct its required extended source channel explicitly.

## 8. Independent excess and the limit of the result

On this graph the selected branch-pair source is still the 32-state complex

\[
D_x=K(X_1,X_3,X_5,t_0X_0,t_3X_3),\qquad
\eta_x=t_3h_3^+-h_3^{03}.
\]

In words: its repeated equation supplies a closed, independent excess generator. The change from the repeated generator to `eta_x` has determinant minus one, so this is an integral basis change. At the central Rees face the coefficient of `h3_pair` remains minus one.

The whole source attachment triangle, cap, and endpoint equations can be tensored with this actual complex. Their differential signs and all 32 source wedges are retained; no excess class is replaced by a target-normal multiple. This is formal tensor compatibility with an explicitly specified source complex. It does not supply a morphism identifying that excess channel with either of the endpoint Gysin inputs of Section 7.

The distinction is now testable rather than hidden: such a comparison must carry the independent excess into the two ordered three-Rees Gysin sources, preserve the native generic cap, and preserve the coupled normalization homotopy. Ordinary specialization alone cannot satisfy those requirements, because it has already been computed and kills the old endpoint morphisms.

No equality with the complete ringed supported-Verdier functor, no identification with the independently framed physical collars, and no physical reflection parity are asserted. The cochain signs are fixed, but signs in an explicitly constructed coefficient map are not by themselves the unresolved physical comparison parity.

## 9. Reproduction and verification

Run:

```sh
python check_marici_joint_triangle_rees_gysin.py \
  --output marici_joint_triangle_rees_gysin_certificate.json
```

The self-contained standard-library checker performs **256,205 exact assertions**. Its approximately thirty-second runtime is from the present environment, not a performance promise. It includes:

- the full source-cone equivalence and complete coupled maps on all 64 central Rees faces;
- sixteen explicit polynomial-natural Rees generators, with acyclic comparison cones in all 729 integer-degree domain shapes;
- the actual endpoint two-term comparison cones in all those shapes, the endpoint restriction homotopies, and 192 coefficient transitions;
- all 64 central target-Hom frames, the retained corrected generic cycle, both seven-term endpoint homotopies, and their primitive marked limits;
- both full Gysin maps into the actual endpoint complexes, their pair and triple comparisons, and the independent selected excess differential.

The arbitrary-exponent statements use the exact degree-domain classification and explicit module maps. They are not extrapolated from an exponent cutoff. This is executable algebraic verification plus the proofs above, not proof-assistant certification. No repository files were changed.

## References and direct inputs

[S1] `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: source graph, independent conormal symbols, and the distinction between carrier/coefficient and full loaded correspondence.

[S2] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: native node, sheet labels, conductor difference, and polarity.

[S3] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: actual target states, incidence signs, and localization domains.

[M1] Stacks Project, Local cohomology, tag `0952`, especially Lemmas 47.9.1 and 47.9.3: `https://stacks.math.columbia.edu/tag/0952`.

[M2] Stacks Project, Hom complexes, tag `0A8H`: `https://stacks.math.columbia.edu/tag/0A8H`.

[M3] Stacks Project, The Koszul complex, tag `0621`: `https://stacks.math.columbia.edu/tag/0621`.

Direct calculation inputs: `marici_mixed_short_edge_generic_attachment_triangle.md` and its checker; `marici_joint_conductor_spatial_cap_comparison.md` and its checker. Their source-channel, support, and physical-scope distinctions remain in force. The new executable includes the needed algorithms and does not require those earlier files at runtime.
