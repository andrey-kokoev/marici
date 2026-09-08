# The exact divisor complement admits local Q lifts but has a nontrivial descent torsor

Date: 2026-09-07  
Lane: Branch B — fixed target, coefficient support, and actual lifting spaces

## Result and scope

The preceding union-support calculation located the first obstruction on six branch-selected normal divisors. This note tests their **entire complement**, not just the complement of the three pair intersections.

Every point of this new open admits a coefficient-linear lift of the genuine top generic class. Seven explicit local cycles provide an affine cover of such lifts. They satisfy the local target equations, retain full coefficient dependence, and have a source-labelled dihedral action. They do **not** glue to a global closed lift. Their differences form a nonzero Cech torsor class in the already-computed top boundary module.

The class has twelve explicit labelled residue components and annihilator equal to the previous coefficient-linearity obstruction ideal. The image on global original coefficients enlarges from the first lifting ideal to the second obstruction ideal, but it still excludes the unit. Both endpoint discrepancies are recorded before passing to the endpoint quotient.

This is a target-side theorem for the fixed alternating/Rees coefficient model. The open is an algebraic test locus, not an identified physical generic fibre. Divisions below occur only on their stated principal opens. No inverse is adjoined to the native source, no carrier generator is added, and no physical source or missing endpoint connector is manufactured.

## 1. Fixed target and inputs

Retain the short and long labels

\[
S_+=\{13,35,15\},\qquad S_-=\{02,24,04\},\qquad
S=S_+\sqcup S_-,\qquad L=\{03,14,25\}.
\]

In words: the two sets of short labels are the alternating endpoint triangulations, and the three long labels remain separate.

The coefficient rings are

\[
\mathcal C=\mathbb Z[t_s\ (s\in S),X_l,u_l\ (l\in L)],\qquad
\mathcal B=\mathcal C[X_s:s\in S]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: all short Rees and long occurrence/normal variables stay independent. Opposite-sheet short-occurrence products vanish; same-sheet polynomials remain.

Write

\[
I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-),\quad
\tau_+=\prod_{p\in S_+}t_p,\quad \tau_-=\prod_{m\in S_-}t_m,\quad
T=\tau_+\tau_-.
\]

In words: each sheet has its own three-parameter Rees product. The product of all six Rees parameters is a non-zero-divisor, unlike the product of all six short normal coefficients after the alternating occurrence relations.

The actual source coefficient differential on the 215 loaded states is

\[
\begin{aligned}
|[F,H]|&=3-|F|+|H|,\\
d[F,H]&=\sum_a(-1)^{\#\{b\in F:b<a\}}X_a[F\cup\{a\},H]\\
&\quad+\sum_{h\in H}(-1)^{3-|F|+\operatorname{pos}_H(h)}u_h[F,H\setminus\{h\}],
\qquad u_s=t_sX_s\quad(s\in S).
\end{aligned}
\]

In words: add an allowed diagonal or remove a mark, retaining its occurrence or normal coefficient and the fixed incidence signs. The specified PC version localizes exactly at normals in the unmarked part of the cell. It replaces the radial coefficient by the indicated occurrence-to-normal ratio and the normal-removal coefficient by one. These are cellwise localizations, not global inversions.

The support triangle remains

\[
0\longrightarrow A_\partial=F_B/F_V\longrightarrow E=F_K/F_V
\xrightarrow{\pi}Q=F_K/F_B\longrightarrow0.
\]

In words: the endpoint, boundary and seven-state generic quotient are fixed before any new coefficient operation. These complexes have no homological degree above three.

The prerequisite target computations [P1, P2] give

\[
H_3(Q)=\mathcal B\theta,\qquad
0\longrightarrow M\longrightarrow H\longrightarrow\mathfrak a\longrightarrow0,
\qquad H=H_3(E),
\]

\[
M=I_+^{\oplus6}\oplus I_-^{\oplus6},\qquad
\mathfrak a=(T,\tau_+I_+,\tau_-I_-).
\]

In words: the image of the top generic coefficient map is the ideal shown, and the ambiguity module consists of twelve branch-ideal summands with their retained internal degree labels. The PC target has these same top modules; this does not identify the full complexes in lower degrees.

The connecting class and module extension have respectively

\[
\operatorname{Ann}_{\mathcal B}[\beta]=\mathfrak a,\qquad
\operatorname{Ann}_{\mathcal B}(e)=\mathfrak b,
\qquad\mathfrak b=I_++I_-+(T).
\]

In words: the first class obstructs a closed lift of one generic coefficient; the second obstructs a coefficient-linear choice of all admissible lifts. These prior results are inputs, not conclusions inferred from the new affine cover.

## 2. The exact local lifting locus and its seven-open atlas

Set

\[
V=\operatorname{Spec}\mathcal B\setminus V(\mathfrak a),\qquad
V_0=D(T),\quad V_{+,p}=D(\tau_+X_p),\quad V_{-,m}=D(\tau_-X_m).
\]

In words: use the complement of the complete support of the first cyclic obstruction. The displayed seven principal opens cover it. This is the maximal locus where the fixed class has a local closed lift: localization of the exact top-module sequence makes the image contain one precisely there.

No positive chart meets a negative chart, because their inverted occurrence product is zero. The nonzero intersections have Cech counts

\[
(7,12,8,2).
\]

In words: seven opens, twelve pairwise intersections, eight triple intersections, and two fourfold intersections. These are coefficient-cover terms, not new target cells. Every nonzero intersection is affine.

The resulting 29-term localization Cech complex computes derived sections on this open. Its augmentation gives the genuine localization triangle for this support, by [M1]. The differential retains all cover signs. In particular this construction is not a replacement of the diagram by its unlabelled nerve.

### Actual local cycles

Let \(\Lambda_0\) be the previously constructed full cycle lifting \(T\theta\). Let \(L_+\) be the bare positive-sheet sum, so \(\Lambda_+(f)=fL_+\) for \(f\in I_+\); define the negative version in the same way. Explicitly,

\[
\Lambda_0=\sum_F(-1)^{|F|(|F|+1)/2}
\left(\prod_{s\in S\setminus F}t_s\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L\setminus F}u_l\right)[F,F],
\]

\[
L_+=\sum_{F\subseteq S_+\cup L}(-1)^{|F|(|F|+1)/2}
\left(\prod_{p\in S_+\setminus F}t_p\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L\setminus F}u_l\right)[F,F].
\]

In words: both sums run only over actual noncrossing faces and include the endpoint faces in their full versions. The bare sheet sum is not asserted to be a cycle over the unspecialized glued ring. On a positive open, an inverted positive occurrence forces every negative occurrence to zero; there it is a cycle. This is why the following local formulas are valid.

Define

\[
s_0=\Lambda_0/T,\qquad
s_{+,p}=\Lambda_+(X_p)/(\tau_+X_p)=L_+/\tau_+,
\qquad s_{-,m}=L_-/\tau_-.
\]

In words: divide each already-constructed cycle only by the generator of its own principal open. These are full local target cycles, in both the absolute and PC models, and

\[
ds_i=0,\qquad\pi(s_i)=\theta.
\]

In words: every chart has a genuine lift of the same generic unit. On charts of the same sheet, the formulas agree exactly. The checker verifies the identities before endpoint quotienting as well as after it. The seven local sections are covariant under the six specified dihedral transformations without averaging.

## 3. Their overlap differences are not removable

On a pairwise overlap put

\[
\omega_{ij}=s_j-s_i\in\widetilde M(V_i\cap V_j),\qquad
\omega_{jk}-\omega_{ik}+\omega_{ij}=0.
\]

In words: differences of local lifts have zero generic image and are top boundary-supported cycles. They satisfy the exact Cech cocycle equation. The resulting cohomology class measures whether adjustments by local ambiguity sections can make the lifts agree. It is the class of the torsor of local lifts [M2].

The old common-to-branch defects give a useful complete coordinate formula. Write \(a\sim b\) when the two labelled diagonals are noncrossing. For an inactive nonempty proper subset \(N\subset S_-\), let

\[
P_N=\{p\in S_+:\forall n\in N,\ p\sim n\},\qquad
L_N=\{l\in L:\forall n\in N,\ l\sim n\}.
\]

In words: these are the active short and long labels compatible with the fixed inactive marks.

The earlier ambiguity generator is

\[
\Gamma_{+,N}=\sum_{N\subseteq F\subseteq N\cup P_N\cup L_N}
(-1)^{|F|(|F|+1)/2}
\left(\prod_{p\in P_N\setminus F}t_p\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L_N\setminus F}u_l\right)[F,F].
\]

In words: it is used globally with coefficients in the positive branch ideal, and with localized coefficients where that ideal becomes the full local ring. Only noncrossing faces occur; the endpoint quotient uses proper inactive subsets.

Define the residue coefficient

\[
r_{+,N}=\frac{\prod_{l\in L\setminus L_N}u_l}
{\left(\prod_{n\in N}t_n\right)\left(\prod_{p\in P_N}t_p\right)}.
\]

In words: the numerator retains all missing long-normal factors. The denominator is allowed on the overlap with the central open. It is not a scalar evaluation of a conormal symbol.

The complete overlap identity is

\[
s_0-s_{+,p}=\sum_{\varnothing\ne N\subsetneq S_-}r_{+,N}\Gamma_{+,N}
\in\Gamma(V_0\cap V_{+,p},\widetilde E_3).
\]

In words: six independent boundary families occur, with no dependence on which positive occurrence was inverted. The negative overlaps have the reflected six families. This equation is verified on the actual target chain coordinates, not assigned as an abstract presentation relation.

With the convention for \(\omega_{ij}\) above, its components on central-to-positive overlaps are the negatives of these residues. The sign does not affect their nonvanishing or annihilator; it is retained in the actual cover cocycle.

## 4. Compute the cohomology in which the torsor lives

Put

\[
\mathcal C_+=\mathcal C[\tau_+^{-1}],\qquad
\mathcal C_-=\mathcal C[\tau_-^{-1}],\qquad
\mathcal C_T=\mathcal C[T^{-1}],
\]

\[
D_+=\mathcal C_+[X_p:p\in S_+],\qquad
D_-=\mathcal C_-[X_m:m\in S_-].
\]

In words: each normalized branch may invert its own normal product. Both products are invertible on the remaining conductor.

The preimage of \(V\) on the positive normalization branch is

\[
V_+=\operatorname{Spec}D_+\setminus V(I_+,\tau_-),
\]

and the negative version exchanges the signs. In words: the omitted locus on this branch has the three occurrence coordinates and the opposite normal product as a regular sequence. The remaining conductor is the affine scheme \(\operatorname{Spec}\mathcal C_T\).

The ordinary four-element localization Cech complex, or the regular-sequence calculation, gives

\[
\Gamma(V_+,\mathcal O)=D_+,\qquad H^1(V_+,\mathcal O)=H^2(V_+,\mathcal O)=0.
\]

In words: removing this codimension-four locus does not introduce lower-degree functions or cohomology on the normal branch. The product \(\tau_-\) is not assumed irreducible; it is a non-zero-divisor, and the three independent occurrence variables remain regular after quotienting by it.

Restrict the exact ideal sequence on this branch to \(V_+\). Its conductor quotient has global sections \(\mathcal C_T\), while the image of branch functions is only \(\mathcal C_+\). Therefore

\[
\Gamma(V,\widetilde I_+)=I_+D_+,\qquad
H^1(V,\widetilde I_+)\cong\mathcal C_T/\mathcal C_+.
\]

In words: global ambiguity coefficients retain positive occurrence order, but their first cohomology records the opposite-normal poles needed to compare those coefficients across the conductor. The reflected formula holds for \(I_-\).

Consequently, with every \(\Gamma\)-degree label retained,

\[
H^1(V,\widetilde M)\cong
\bigoplus_{\varnothing\ne N\subsetneq S_-}(\mathcal C_T/\mathcal C_+)\Gamma_{+,N}
\oplus
\bigoplus_{\varnothing\ne N\subsetneq S_+}(\mathcal C_T/\mathcal C_-)\Gamma_{-,N}.
\]

In words: the twelve residue components are in an explicitly computed group, not merely formal overlaps. The torsor component is \(-[r_{+,N}]\) in the first type of quotient, and similarly on the negative side.

### A primitive nonboundary detector

For the inactive singleton \(N=\{02\}\), the compatible active set is \(\{35\}\), and the compatible long labels are \(\{03,25\}\). Hence

\[
[r_{+,\{02\}}]=\left[\frac{u_{14}}{t_{02}t_{35}}\right]
\in(\mathcal C_T/\mathcal C_+)\setminus\{0\}.
\]

In words: the allowed positive normal denominator does not remove the forbidden negative-sheet pole. In this exact fine degree there is no Cech zero-cochain in the ambiguity module, whereas the three central-to-positive edges carry a nonzero integral cocycle. It cannot be a coboundary.

Thus

\[
[\omega]\ne0.
\]

In words: all local equations are solvable, but no changes of local lifts can make them agree globally. This conclusion does not rely on preserving a grading: any purported polynomial correction decomposes into fine degrees, and the displayed component has no correction in its own degree.

For comparison, normalization descent also gives

\[
\Gamma(V,\mathcal O_V)=\mathcal R
=\mathcal C\oplus I_+D_+\oplus I_-D_-,
\qquad
H^1(V,\mathcal O_V)=\mathcal C_T/(\mathcal C_++\mathcal C_-).
\]

In words: the common conductor coefficient remains polynomial; positive branch terms may have their own normal poles. The structure sheaf itself has nonzero first cohomology. For example a monomial with a negative normal exponent on each sheet survives in the displayed quotient, so this open is not affine.

### Independent all-degree verification

The standalone checker forms the actual 29-term localization incidence complex for the structure sheaf and both branch ideals. It examines 6,848 exhaustive sign-pattern degrees: each occurrence exponent is negative, zero, or positive, and each normal exponent is negative or nonnegative. Long variables factor as a common polynomial coefficient module.

The existence of a monomial on an intersection depends only on these signs and on whether its branch-ideal order is zero. Thus this is a finite exhaustive classification, not an extrapolation from a maximum polynomial degree. All nonzero Smith factors of every relevant differential are one. It verifies the displayed degree-zero and degree-one formulas, the degree-two vanishing, and the higher branch degree-three groups as a control. The finite-affine-cover theorem [M1] identifies these Cech calculations with sheaf and derived cohomology.

## 5. Exact annihilator and the new global lifting ideal

Multiplication by any short occurrence kills every torsor component. On the active side, multiplication moves the coefficient into the actual branch ideal and supplies a Cech zero-cochain; on the opposite side it annihilates that branch module. The checker tests these as boundaries, not as a change of the chosen residue definition.

For coefficients in \(\mathcal C\), all positive-family residues vanish precisely when the coefficient is divisible by \(\tau_-\). Indeed the singleton inactive subsets detect all three opposite factors, and the longer subsets require no additional factors. The negative family similarly requires \(\tau_+\). Independent long parameters introduce no extra annihilators. Therefore

\[
\operatorname{Ann}_{\mathcal B}[\omega]=I_++I_-+(T)=\mathfrak b,
\qquad
\mathcal B[\omega]\cong\mathcal C/(T).
\]

In words: the old coefficient-linearity obstruction is now visible as an explicit global descent class, even though the local lifting obstruction has disappeared everywhere on the open. Its additive order is infinite, and it remains nonzero over the rationals; this is not an integer-prime torsion effect.

More precisely, since \(\mathfrak a|_V=\mathcal O_V\), restriction of the old top-module extension gives

\[
0\longrightarrow\widetilde M|_V\longrightarrow\widetilde H|_V
\longrightarrow\mathcal O_V\longrightarrow0.
\]

In words: its local splitting torsor is exactly the seven-chart construction above. Under the standard identification of extensions of the structure sheaf with first sheaf cohomology, the restricted extension class is \([\omega]\). A global Ext-class annihilator must not be confused with the support of a sheaf of local Ext-groups: this extension is locally split on every chart but still globally non-split.

The connecting homomorphism sends the global unit to the torsor class. Its exact kernel is

\[
\operatorname{im}\left(\Gamma(V,\widetilde H)\longrightarrow\mathcal R\right)
=T\mathcal C\oplus I_+D_+\oplus I_-D_-.
\]

In words: after this open restriction, all global branch tails lift, but the common coefficient must still contain all six Rees factors.

This is constructive. A common coefficient \(Tc\) is lifted by \(c\Lambda_0\). For a global positive branch tail \(f\in I_+D_+\), use \(fL_+/\tau_+\) on the central and positive charts and zero on the negative charts. It is regular on those charts, agrees on intersections, is a genuine target cycle, and has generic coefficient \(f\). The negative formula is reflected. These prescriptions retain every long coefficient and use only the denominators already present in the open.

For coefficients coming from the original ring, the result becomes

\[
\{k\in\mathcal B:k\theta\in\operatorname{im}(H_3(R\Gamma(V,E))\to H_3(R\Gamma(V,Q)))\}=\mathfrak b.
\]

In words: the admissible original coefficients enlarge from \(\mathfrak a\) to \(\mathfrak b\). In particular \(X_{13}\theta\) now lifts, though it did not lift over the original affine base. The unit still does not.

The ambiguity of each nonempty global lifting space is

\[
\Gamma(V,\widetilde M)
=(I_+D_+)^{\oplus6}\oplus(I_-D_-)^{\oplus6}.
\]

In words: ambiguity may include the newly permitted branch-normal poles. These are still branch ideals, not twelve free coefficient lines.

## 6. Why a vanished local homology class does not settle derived descent

The cyclic sheaf generated by \([\beta]\) restricts to zero on \(V\), since its annihilator ideal becomes the unit ideal there. That statement is correct. It does not provide compatible nullhomotopies for the map representing the class.

Apply derived sections to the target support triangle. Each chart has the nullhomotopy supplied by its local lift. Comparing those nullhomotopies produces exactly the Cech cycle above. Since the target has no homology above degree three, the top-edge exact sequence gives an injection

\[
H^1(V,\mathcal H_3(A_\partial))\hookrightarrow
H_2(R\Gamma(V,A_\partial)).
\]

In words: the first cohomology of the top boundary module survives in the relative totalization. There is no higher internal degree from which a differential could remove it. The derived connecting image of \(\theta\) is the image of \([\omega]\) under this injection, up to the common declared connecting sign.

This computes the entire issue, rather than declaring the original torsion class zero and stopping at the first homology sheaf.

For the precise unit-lifting infinity-groupoid,

\[
\mathscr L_V(\theta)=\operatorname{hofib}_{\theta}
\left(\operatorname{Map}(\mathcal O_V[3],E|_V)
\longrightarrow\operatorname{Map}(\mathcal O_V[3],Q|_V)\right),
\qquad \mathscr L_V(\theta)=\varnothing.
\]

In words: there is no global object of the fixed covariant unit-lifting problem, even though there are local objects on the seven affine charts. The shift is homological. For admissible global coefficients, the lifting space is a discrete torsor under the displayed global ambiguity module; there are no higher paths, because the totalized complexes have no homological degree above three.

This is a concrete example of a local solution with a higher descent obstruction. It does not assert new nonzero higher homotopy groups of the local marking spaces.

## 7. Keep the endpoint discrepancies

The endpoint-inclusive local sums also satisfy the chain equations. Before quotienting by the two endpoint cubes, the central and positive sections have the additional discrepancy

\[
(s_0-s_+)\big|_{F_V}=
\frac{U_L}{\tau_-}[S_-,S_-],\qquad
(s_0-s_-)\big|_{F_V}=
\frac{U_L}{\tau_+}[S_+,S_+],
\qquad U_L=\prod_{l\in L}u_l.
\]

In words: the positive overlap retains the opposite endpoint term, and the negative overlap retains its polarity conjugate. Both signs follow from the full-face orientation. The checker verifies these identities before endpoint quotienting. It does not silently claim that the local representatives already preserve a globally fixed endpoint framing.

The twelve proper inactive-subset residues are the obstruction in the endpoint-relative target; the two full inactive-subset terms record the further endpoint data any spatial comparison must carry. No endpoint connector two-cell or its filling is deduced from these coefficient identities.

## 8. Relation to the other lanes and the next source test

This calculation stays on the target side. It neither repeats a whole-triple Rees/Gysin source calculation nor replaces the complementary-support reverse pairing by a forbidden direct covariant map. The genuine top class \(\theta\) remains distinct from the exact Morse roof and from a chosen physical endpoint unit.

The result supplies explicit comparison data for those source constructions: twelve overlap residues, the two retained endpoint terms, their coefficient annihilator, and the full cover differential. A native source with its own boundary and variance could map into these data without admitting a global closed section of the generic module alone. The theorem does not obstruct that broader mixed-variance problem.

What is now ruled out is the shortcut of removing all local obstruction divisors and treating local primitive lifts as automatically coherent. An admissible source comparison must account for their nontrivial Cech class, or change the source/target operation for an independently derived reason.

## 9. Reproducibility and provenance

Run:

```sh
python check_marici_divisor_complement_descent_20260907.py \
  --output marici_divisor_complement_descent_certificate_20260907.json
```

The new standalone program passes **44,523 exact assertions**, including 6,848 exhaustive integral Cech sign-pattern calculations. It reconstructs the 215-state target, verifies seven actual local lifts in both coefficient models, every pair and triple comparison, the full twelve-family chain decomposition, both endpoint discrepancies, the exact cyclic annihilator, constructive global lifts of its seven generators, and the six labelled dihedral transformations.

The following prerequisite programs were independently rerun successfully in this runtime:

- `check_marici_q_lift_naturality_20260907.py`: 138,416 assertions;
- `check_marici_union_recollement_20260907.py`: 4,001 assertions.

Replay counts and hashes are in the certificate when those replay files are present. The new checker is otherwise standalone. Its all-polynomial claims are proved by the localization/normalization arguments above and the exhaustive coefficient sign classification, not by a bounded-polynomial extrapolation. This is not proof-assistant verification.

The target data are pinned, through the prerequisite artifacts, to repository `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`. No newer repository state is assumed and no repository files were modified.

## References

[P1] `marici_filtered_q_alternating_rees_update_20260907.md`: target top modules, first lifting ideal, and explicit common/branch cycles.

[P2] `marici_q_graded_lift_naturality_20260907.md`: twelve boundary-ideal summands, common-to-branch defects, and the non-split top lifting extension.

[P3] `marici_union_recollement_20260907.md`: all-thickenings pair support and the exact six-divisor support decomposition. These are verified local artifacts from this conversation, not invented external references.

[M1] Stacks Project, Section 51.2, Lemmas 51.2.1 and 51.2.2, tag `0DWQ`: finite localization Cech complexes, the supported/open triangle, and cohomology of the open complement. https://stacks.math.columbia.edu/tag/0DWQ

[M2] Stacks Project, Section 20.4, especially Lemmas 20.4.2 and 20.4.3, tag `02FN`: torsors, global trivializations, and first sheaf cohomology. https://stacks.math.columbia.edu/tag/02FN
