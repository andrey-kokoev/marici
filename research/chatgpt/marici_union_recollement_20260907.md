# Genuine union-support recollement and persistence of both Q obstructions

Date: 2026-09-07  
Lane: Branch B — the existing target, coefficient operations, and lifting spaces

## Result and scope

The preceding finite union dual and its counit cone can be promoted to the genuine local-cohomology/open-complement triangle. This note constructs the promotion over all support thickenings, including every transition map and normal pole order. It is not obtained by simply renaming the finite cone a localization functor.

The new calculation has a stronger negative conclusion than the finite-layer test: **neither of the two previously computed obstruction annihilators changes on the open complement of the three pair supports**. The top target homology, the exact generic lifting ideal, and the entire top lifting-module extension are recovered from that open complement. The generic unit still has no closed lift. Every already-admissible coefficient has exactly the same discrete family of lifts as before.

The reason is geometric and explicit. The first obstruction has six minimal support components, each a branch-selected normal divisor. None is contained in the union of the three pairwise normal intersections. Thickening those intersections, even to all orders, cannot remove the obstruction on their complement.

This is a theorem about the fixed alternating/Rees target and the specified coefficient support. It does not identify this open complement with a physical deformation parameter, construct the native source, or produce the still-missing spatial endpoint connectors. A bivariant correspondence with a different source, variance, or independently defined support is not excluded.

## 1. Fixed coefficients and prior target data

Retain

\[
(s_1,t_1)=(t_{04},t_{35}),\quad
(s_2,t_2)=(t_{02},t_{15}),\quad
(s_3,t_3)=(t_{24},t_{13}).
\]

In words: these are the same three ordered normal pairs, with every label retained. Put

\[
\mathcal B=\mathcal A[s_1,t_1,s_2,t_2,s_3,t_3],
\]

where \(\mathcal A\) is the integral alternating occurrence ring, with all independent long occurrence and normal parameters. Its short occurrence ideals satisfy

\[
I_+=(X_{13},X_{35},X_{15}),\qquad
I_-=(X_{02},X_{24},X_{04}),\qquad I_+I_-=0.
\]

In words: opposite-sheet occurrence products vanish. No short Rees parameter is a zero divisor, since the six Rees variables are independent polynomial variables over \(\mathcal A\). The coefficient ring is Noetherian.

Set

\[
\tau_+=t_1t_2t_3,\quad \tau_-=s_1s_2s_3,\quad
J_i=(s_i,t_i),\quad J=J_1J_2J_3,\quad
Z=V(J),\quad U=\operatorname{Spec}\mathcal B\setminus Z.
\]

In words: \(Z\) is the union of the three closed pair supports; \(U\) is their common open complement. It is not the simultaneous closed intersection and is not assumed to be the physical generic fibre.

The independently replayed target calculations [P1, P2] give

\[
H_3(Q^{\mathrm{PC}})=\mathcal B\theta,\qquad
\operatorname{im}\bigl(H_3(E^{\mathrm{PC}})\to H_3(Q^{\mathrm{PC}})\bigr)
=\mathfrak a\theta,
\]

\[
\mathfrak a=(\tau_+\tau_-,\tau_+I_+,\tau_-I_-),\qquad
\mathcal B[\beta]\cong\mathcal B/\mathfrak a\subseteq H_2(A_\partial^{\mathrm{PC}}).
\]

In words: the supported connecting class \(\beta\) determines which multiples of the genuine top generic cycle admit closed lifts. The fixed top lifting module \(H=H_3(E^{\mathrm{PC}})\) fits into

\[
0\longrightarrow M\longrightarrow H\longrightarrow\mathfrak a\longrightarrow0,
\qquad M=I_+^{\oplus6}\oplus I_-^{\oplus6}.
\]

In words: \(M\) contains the boundary-supported ambiguity classes, with their original internal degree labels. The extension class \(e\) has

\[
\operatorname{Ann}_{\mathcal B}(e)=\mathfrak b,
\qquad \mathfrak b=I_++I_-+(\tau_+\tau_-).
\]

In words: this second obstruction prevents choosing all admissible lifts by one coefficient-linear map. These are prior full-target results, not inferred anew from the scalar support calculation below. The top modules agree in the absolute and specified PC models; the complete complexes need not agree in lower homology.

## 2. Construct all thickenings and their transition maps

Use the cofinal family

\[
J^{(n)}=\prod_{i=1}^3(s_i^n,t_i^n),\qquad
J^{2n-1}\subseteq J^{(n)}\subseteq J^n.
\]

In words: this family retains every normal thickness needed for local cohomology. The inclusions follow pair by pair: a degree \(2n-1\) monomial in two variables has an exponent at least \(n\).

The ideal \((s_i^n,t_i^n)\) has its ordered two-term free resolution with relation \((-t_i^n,s_i^n)\). Tensor the three ideal resolutions and augment their product into \(\mathcal B\). The resulting resolution \(F_n\) of \(\mathcal B/J^{(n)}\) has homological ranks

\[
(1,8,12,6,1).
\]

In words: the same 28 coefficient columns work at every thickness. No carrier cell is added. Exactness follows over any coefficient ring from the independent polynomial blocks; equivalently, their multigraded complexes are split integral resolutions of the monomial product ideal.

Index a non-unit basis by \(b=(b_1,b_2,b_3)\), with each \(b_i\) one of \(s,t,st\). The homological degree is one plus the number of \(st\) entries. Let \(m_b\) be the product of the indicated variables, using both for \(st\).

The chain map \(F_{n+1}\to F_n\) multiplies a pair's \(s,t,st\) generators by \(s_i,t_i,s_it_i\), respectively. On the product basis it multiplies by \(m_b\), and it is the identity in degree zero. This lifts the quotient map \(\mathcal B/J^{(n+1)}\to\mathcal B/J^{(n)}\).

Dualizing gives a direct system

\[
\mathcal U_n=\operatorname{Hom}_{\mathcal B}(F_n,\mathcal B),\qquad
b^\vee\longmapsto m_b b^\vee.
\]

In words: every transition is an explicit polynomial chain map, including its Hom-complex sign. It is compatible with the coefficient counit in every degree.

The stabilized object is

\[
\mathcal K_Z=\operatorname*{colim}_n\mathcal U_n
\simeq R\Gamma_Z(\mathcal B).
\]

In words: this is actual local cohomology, not the derived dual of just the reduced support. The identification follows from cofinality and Noetherian local cohomology [M1].

### Explicit localization realization

Map a non-unit dual basis to its localized copy by

\[
\iota_n(b^\vee)=m_b^{-n}b.
\]

In words: the denominator occurs only in that indicated localization summand. The degree-zero map is the identity. In every differential, the missing factor cancels precisely against the denominator change. The checker verifies the chain equation and compatibility with the thickness transitions. The formulas prove them for arbitrary \(n\).

Thus \(\mathcal K_Z\) has 28 **flat localization summands**, with counts \((1,8,12,6,1)\); these are not 28 finite free modules. Its differential is the signed localization incidence differential. Degree-wise sign changes identify it with the extended product Čech model.

Its counit and cone give

\[
\mathcal K_Z\otimes_{\mathcal B}^{L}N\longrightarrow N
\longrightarrow\mathcal G_Z\otimes_{\mathcal B}^{L}N,
\qquad
\mathcal G_Z\otimes_{\mathcal B}^{L}N
\simeq R\Gamma(U,\widetilde N|_U).
\]

In words: the supported part and the actual open-complement part are retained in one functorial triangle. This is the localization triangle [M2]. An explicit model for its last coefficient object is

\[
\mathcal G_Z\simeq\bigotimes_{i=1}^3
[\mathcal B_{s_i}\oplus\mathcal B_{t_i}\longrightarrow\mathcal B_{s_it_i}],
\qquad (a,b)\longmapsto b-a.
\]

In words: take the two-open Čech comparison for each pair, then totalize their product. The cochain degrees are zero through three, with 8, 12, 6, and 1 localization summands. This models the intersection of the three opens \(D(s_i)\cup D(t_i)\), which is exactly \(U\).

The standard localization identities are now valid:

\[
\mathcal K_Z\otimes^L\mathcal K_Z\simeq\mathcal K_Z,\qquad
\mathcal G_Z\otimes^L\mathcal G_Z\simeq\mathcal G_Z,\qquad
\mathcal K_Z\otimes^L\mathcal G_Z\simeq0.
\]

In words: the supported and open functors are idempotent and mutually orthogonal [M1, M2]. Both preserve every supplied target support triangle and every supplied endpoint map by functoriality. They do not generate an absent spatial connector.

## 3. The finite cone really is different

On the mathematical test open \(D(s_2s_3)\), the finite union dual reduces to the first pair's dual. Write \(D=\mathcal B_{s_2s_3}/(s_1,t_1)\). After derived tensor with \(D\), its Koszul dual has zero differential and ranks \((1,2,1)\), in cohomological degrees zero, one, two. Its counit is the identity on degree zero.

Consequently the finite counit cone satisfies

\[
\operatorname{Cone}(\mathcal U_1\to\mathcal B)\otimes^L D
\simeq D^{\oplus2}\oplus D[-1]\ne0.
\]

In words: two classes in cohomological degree zero and one in degree one remain. The new checker obtains them from the full 28-column finite differential, specialized after retaining a free resolution; it does not use an underived homology substitution.

In contrast,

\[
\mathcal G_Z\otimes^L D=0.
\]

In words: every open-complement term inverts at least one variable of the first pair, hence vanishes on this closed pair support. The finite cone and the true open functor are therefore not interchangeable.

This is a refinement of the scope stated in [P3], which already explicitly called its cone a finite support layer rather than full local cohomology.

## 4. All normal pole orders survive in the supported object

For a nonempty subset \(A\subseteq\{1,2,3\}\), define \(L_A\) as the module with basis

\[
\prod_{i\in A}s_i^{-a_i}t_i^{-b_i},\qquad a_i,b_i\ge1,
\]

over \(\mathcal A[s_j,t_j:j\notin A]\). In words: each selected pair contributes both negative exponents, while unselected pairs retain polynomial coefficients. Multiplication that makes a selected exponent nonnegative sends that term to zero in the residue quotient. Equivalently,

\[
L_A=H^{2|A|}_{(s_i,t_i:i\in A)}(\mathcal B).
\]

In words: this is the full top local-cohomology module of the selected coordinates, not just its one-dimensional first-pole layer.

The complete cohomology calculation is

\[
H^q(\mathcal K_Z)\cong
\bigoplus_{|A|=q-1}L_A\quad(q=2,3,4),
\qquad H^q(\mathcal K_Z)=0\quad(q\notin\{2,3,4\}),
\]

\[
H^0(\mathcal G_Z)=\mathcal B,\qquad
H^q(\mathcal G_Z)\cong\bigoplus_{|A|=q}L_A\quad(q=1,2,3).
\]

In words: the pair, pair-overlap, and triple-overlap support degrees remain two, three, and four, but each now includes every higher normal residue. These cohomology formulas do not assert formality of the full derived object.

**All-degree proof.** In one pair's open complex, a fine degree with both exponents nonnegative has two vertices and one edge; its only cohomology is one integral copy in degree zero. Exactly one negative exponent leaves an isomorphism from one vertex to the edge and is acyclic. Both negative exponents leave the edge alone, in degree one. Tensoring the three blocks gives the stated answer over any coefficient module. The matrices depend only on the 64 negative-support patterns; all their nonzero Smith factors are one. This proves the arbitrary-exponent and integral assertions.

At thickness \(n\), the selected-subset residue maps to the corresponding Čech class with coefficient

\[
\frac{1}{\prod_{i\in A}(s_it_i)^n}.
\]

In words: the thickness transitions include the finite residue as the first layer of an actual higher-pole system. For example,

\[
s_1\left[\frac1{s_1^2t_1}\right]
=\left[\frac1{s_1t_1}\right]\ne0.
\]

In words: a higher pole is not annihilated by the first normal parameter even though the primitive first-pole residue is. Thus replacing the complete support functor by a single finite normal fibre would lose real coefficient information.

All ordered normal determinant and cover signs are retained by the indexed Čech differential. No physical channel orientation is identified with them without an additional supplied comparison.

## 5. Exact support of the first obstruction

A new useful decomposition is

\[
\mathfrak a=
\bigcap_{p\in S_+}(I_-+(t_p))
\;\cap\!
\bigcap_{m\in S_-}(I_++(t_m)).
\]

In words: the obstruction has exactly six reduced components. On the positive occurrence sheet it is supported where one of that sheet's three normal parameters vanishes; on the negative sheet the roles reverse.

Each displayed ideal is prime: its quotient is a polynomial ring over the integers with one Rees variable removed. The decomposition is irredundant. It can be proved directly from the unique common/positive/negative branch expansion. A common term must contain all six normal factors; a positive branch term must contain its three positive factors; a negative branch term must contain its three negative factors. Those are exactly the generators of \(\mathfrak a\).

The checker independently proves equality of the monomial ideals by exact least-common-multiple intersections in the ambient twelve-variable polynomial ring, including all nine opposite-occurrence relations. The 960 admissible squarefree occurrence/normal supports provide an additional exhaustive support check. Higher powers do not change this squarefree ideal membership argument.

Likewise,

\[
\mathfrak b=\bigcap_{s\in S}(I_++I_-+(t_s)).
\]

In words: the second obstruction has six conductor-supported normal components.

None of these components is contained in \(Z\). The polynomial

\[
f=\tau_++\tau_-\in J
\]

is a nonzero divisor on both \(\mathcal B/\mathfrak a\) and \(\mathcal B/\mathfrak b\). In words: modulo each displayed minimal prime exactly one of its two monomials survives, nonzero in that domain. Since the quotients embed into the product of these domains, multiplication by \(f\) is injective.

It follows that

\[
\mathfrak a:J^\infty=\mathfrak a,\qquad
\mathfrak b:J^\infty=\mathfrak b.
\]

In words: passing to the complement of the pair supports kills no nonzero coefficient multiple of either cyclic obstruction module. This is also checked by exact monomial saturation, not merely by finitely many choices of coefficient.

In particular,

\[
H_Z^0(\mathcal B/\mathfrak a)=0.
\]

In words: the first obstruction has no nonzero submodule supported entirely on the three pair intersections. Its restriction to \(U\) is faithful.

### A local witness, with the specialization caveat retained

For instance, take the positive-sheet local ring in which \(X_{13}\) and all five short Rees variables other than \(t_{13}\) are units, while \(t_{13}\) is not a unit. Such a locus is outside all three pair supports. The necessary top-cycle singleton equation in the PC target becomes

\[
U_L+t_{13}a_{13}=0,
\qquad U_L=u_{03}u_{14}u_{25}.
\]

In words: the candidate top coefficient would have to cancel the independent long-normal product by a multiple of \(t_{13}\). The relevant coefficient ring on the selected branch is a domain. Thus an equality in the row's localization implies the same equality before that normal is inverted. Reducing that necessary coefficient equation modulo \(t_{13}\) is impossible when \(U_L\) remains nonzero.

This is a local-ring obstruction **before** taking the non-flat closed fibre. It is not a claim that specializing the entire PC complex to a point preserves its homology. Indeed a summand inverting a now-zero normal vanishes on such a fibre, and new cycles may appear. The checker records six witnesses to the necessary unspecialized coefficient equation; it does not infer a base-change theorem from them.

## 6. The complete top lifting problem is unchanged on the open

The scalar computation above also works with an arbitrary coefficient \(\mathcal A\)-module, since its fine-degree contractions are integral. Therefore

\[
H_Z^0(M)=H_Z^1(M)=0,
\qquad H_Z^0(\mathcal B)=H_Z^1(\mathcal B)=0.
\]

In words: the boundary ambiguity ideals have no supported cohomology in the two lowest degrees; their independent Rees variables matter here.

From \(0\to\mathfrak a\to\mathcal B\to\mathcal B/\mathfrak a\to0\), the preceding saturation and local-cohomology sequence imply

\[
H_Z^0(\mathfrak a)=H_Z^1(\mathfrak a)=0.
\]

In words: the lifting ideal itself has the same extension-across-the-open property. Every module \(H'\) fitting into an extension of \(\mathfrak a\) by \(M\) consequently has \(H_Z^0(H')=H_Z^1(H')=0\).

The open/local-cohomology exact sequence [M2] now gives

\[
\Gamma(U,\widetilde M)=M,\quad
\Gamma(U,\widetilde{\mathfrak a})=\mathfrak a,\quad
\Gamma(U,\widetilde H)=H.
\]

In words: these top coefficient modules are completely recovered by sections on the pair-support complement. There are no additional regular top sections hiding there.

Since the original targets have no homological groups above degree three, the lowest-degree edge of the open hypercohomology spectral sequence gives

\[
H_3(\mathcal G_Z\otimes^L E^{\mathrm{PC}})=H_3(E^{\mathrm{PC}}),
\qquad
H_3(\mathcal G_Z\otimes^L Q^{\mathrm{PC}})=\mathcal B\theta.
\]

In words: there are no possible higher-cohomology contributions or differentials into the top degree. The map is still the original top coefficient map, and its image is still \(\mathfrak a\theta\).

Thus the derived space of closed lifts of the generic unit is empty even after applying the genuine open-complement functor. For each coefficient \(k\in\mathfrak a\), its nonempty lift space is still a discrete torsor for \(M\). Higher homotopy groups of these lift spaces vanish because these totalized targets still have no chain cohomology above homological degree three. This statement concerns the same ungraded marking problem as the prior theorem; it does not add or remove a physical grading constraint.

### The second obstruction also survives as an extension class

There is an injective restriction map

\[
\operatorname{Ext}^1_{\mathcal B}(\mathfrak a,M)
\longrightarrow
\operatorname{Ext}^1_{\mathcal O_U}
(\widetilde{\mathfrak a}|_U,\widetilde M|_U).
\]

In words: an extension cannot become split merely by removing the three pair supports. To prove injectivity, take any extension with these ends. The preceding vanishing shows that its middle module is recovered by sections on \(U\). A splitting on \(U\), followed by global sections, would therefore be a splitting over \(\mathcal B\). This applies also to every scalar multiple of the extension class.

Consequently

\[
\operatorname{Ann}_{\mathcal B}(e|_U)=\mathfrak b,
\qquad
\operatorname{Ann}_{\mathcal B}([\beta]|_U)=\mathfrak a.
\]

In words: the exact coefficient-linearity and individual-lifting obstructions both persist, not just one selected numerical detector. The second statement holds already for the cohomology sheaf; it also forbids a vanished hypercohomology obstruction, since that would vanish on every open stalk.

## 7. A support-placement test for further constructions

Let

\[
W=V(\mathfrak a)
=\bigcup_{p\in S_+}V(I_-,t_p)
\;\cup\!
\bigcup_{m\in S_-}V(I_+,t_m).
\]

In words: \(W\) is the actual support of the first cyclic obstruction. It is not the union of the three codimension-two pair supports.

A modification with a comparison that remains an equivalence outside \(Z\), while retaining the same target generic unit and projection there, cannot remove this closed-lift obstruction: its restriction still encounters every component of \(W\setminus Z\). The statement applies to all thickenings supported on those pairs, not only the finite duals tested previously.

This does not instruct us to erase \(W\) by fiat. An admissible physical repair must independently derive what it does on the branch-selected normal divisors, or use a genuinely different mixed-variance source whose connecting boundary is mapped to \(\beta\) rather than requiring it to vanish. The exact graded/line placement and both endpoint connectors remain required.

The support quotient named \(Q\) remains the fixed seven-state quotient. It has not been equated with localization at any of the six short parameters, and the new open \(U\) has not been identified with a physical deformation time.

## 8. Verification and reproducibility

Run:

```sh
python check_marici_union_recollement_20260907.py --output marici_union_recollement_certificate_20260907.json
```

The new standalone checker passes **4,001 exact assertions**. It checks:

- all 28-column free/dual differential identities, thickness transitions, and rational chain maps for four explicit levels, with arbitrary-level formulas proved above;
- every one of the 64 stable normal-support patterns by integral unit Smith reductions;
- the seven residue families, their transitions, higher-pole behavior and primitive nonboundary tests;
- the finite cone's derived closed fibre and the genuine open complex's zero closed fibre;
- exact primary decompositions and saturations of the two obstruction ideals, plus all 960 admissible occurrence/normal support patterns;
- six localized coefficient obstructions with the original normal labels retained.

The following independent prior checkers were rerun successfully in this runtime:

- `check_marici_q_alternating_rees_base_change.py`: **114,594** assertions;
- `check_marici_q_lift_naturality_20260907.py`: **138,416** assertions;
- `check_marici_orbit_source_admissibility_20260907.py`: **65,252** assertions.

Their replay outputs and input hashes are recorded in the companion manifest. The new checker does not silently execute those dependencies on every run. The all-degree, support, and derived-category conclusions follow from the proofs above and the declared prior target theorems, not from extrapolating the finite examples. No proof assistant, repository modification, or construction of the native physical source is claimed.

## References

[P1] `marici_filtered_q_alternating_rees_update_20260907.md` and its standalone checker/certificate: full target, seven lifts, cyclic obstruction ideal, and top boundary module.

[P2] `marici_q_graded_lift_naturality_20260907.md` and its standalone checker/certificate: full 43-generator/174-relation lifting module, six relation defects, exact extension annihilator, and PC top-module comparison.

[P3] `marici_orbit_source_admissibility_20260907.md` and its standalone checker/certificate: finite union resolution, endpoint-line distinctions, source-generic test, and finite counit cone scope.

All three are active-runtime artifacts from this conversation. Their repository inputs are pinned to `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`, as specified in those notes; no newer repository state is assumed here.

[M1] Stacks Project, Sections 47.9 and 47.10, tags `0952` and `0BJD`: extended Čech models, derived tensor base change, idempotence, and Noetherian local cohomology as the colimit of Ext over all thickenings. https://stacks.math.columbia.edu/tag/0952 ; https://stacks.math.columbia.edu/tag/0BJD

[M2] Stacks Project, Section 51.2, especially Lemmas 51.2.1 and 51.2.2, tag `0DWQ`: the supported/open triangle and the exact sequence recovering sections on the open complement. https://stacks.math.columbia.edu/tag/0DWQ
