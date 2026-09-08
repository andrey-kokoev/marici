# Endpoint multiplier coherence: nine lifts, eighteen relations, and an unchanged extension class

Date: 2026-09-07  
Lane: Branch B — coefficient descent and endpoint compatibility  
Input: `marici_normalization_endpoint_extension_20260907.md` and its explicit normalization sheaves on the open V  
Repository provenance inherited from the input: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and exact scope

The nine normal-product maps constructed previously are valid individually. They do **not** assemble into a coefficient-linear map on the ideal they generate. Their eighteen first relations give eighteen explicit, nonzero endpoint-valued discrepancies. All fifteen relations among those discrepancies are satisfied, with the full higher syzygy resolution retained.

This failure is not evidence of an additional independent arithmetic obstruction. The collective lifting class is the original endpoint extension class under a canonical isomorphism of global Ext groups. The same statement holds for every positive power of the normal-product ideal. Thus repeatedly increasing normal order cannot resolve this particular comparison while leaving its source sheaves, target and variance unchanged.

The calculation also constructs the precise derived-dual triangle behind that rigidity. Its extra sheaf cohomology is supported on the two opposite triple-normal loci and begins in cohomological degree two. Both endpoint labels and conormal determinant lines are retained.

All results concern the explicitly constructed, **target-residue-selected** sheaves S12 and S14. They do not identify either sheaf with the native scalar or logarithmic source, admit the test open as the physical generic deformation, or construct new spatial endpoint connector cells. No target carrier cells are added.

## 1. The fixed objects

Retain the two sets of short labels and the independent long parameters:

\[
S_+=\{13,15,35\},\qquad S_-=\{02,04,24\},\qquad
\mathcal C_0=\mathbb Z[X_l,u_l:l\in\{03,14,25\}].
\]

In words: these ordered short sets fix the Koszul bases below. A different source ordering is compared by its exterior-orientation sign, not by a fitted scalar sign.

Put

\[
\mathcal C=\mathcal C_0[t_s:s\in S_+\cup S_-],\qquad
\mathcal B=\mathcal C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: occurrence polynomials from opposite sheets multiply to zero. The six normal parameters remain independent variables over this occurrence ring. Long parameters are not specialized.

Define

\[
I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-),\quad
\tau_+=\prod_{p\in S_+}t_p,\quad \tau_-=\prod_{m\in S_-}t_m,
\]

\[
V=D(\tau_+\tau_-,\tau_+I_+,\tau_-I_-),\qquad
\mathfrak n_+=(t_p:p\in S_+),\quad \mathfrak n_-=(t_m:m\in S_-),\quad
K=\mathfrak n_+\mathfrak n_-.
\]

In words: V is exactly the previous seven-chart test open, not a new localization convention. K is the nine-generator normal-product ideal. Its ideal sheaf on V is denoted by \(\mathcal K\).

The preceding construction gives the exact sequence

\[
0\longrightarrow\mathcal N\longrightarrow\mathcal S_{14}
\xrightarrow{q}\mathcal S_{12}\longrightarrow0,
\qquad
\varepsilon\in\operatorname{Ext}^1_V(\mathcal S_{12},\mathcal N),
\]

\[
\mathcal N=\mathcal I_+\Gamma_{+,S_-}\oplus\mathcal I_-\Gamma_{-,S_+},\qquad
\operatorname{Ann}_{\mathcal B}(\varepsilon)=I_++I_-+K.
\]

In words: the kernel consists of the two actual endpoint families. Ext here means **global** Ext in the derived category of O_V-modules, not the sheaf of local Ext groups. The class is nonzero even though this exact sequence splits on every named affine chart. The preceding note proves the annihilator by the two triple-pole detectors and polynomial correction maps; its standalone checker was independently rerun here.

The source coordinates are a generic coefficient a and twelve normalization functions \(z_{\sigma,N}\), for nonempty proper subsets N of the opposite short set. They obey the actual conductor relations from that note. They are not twelve independent global scalar variables.

## 2. What must be assembled

Write

\[
a_i=t_{p_i},\quad b_j=t_{m_j},\quad g_{ij}=a_i b_j,\qquad
\mu:\mathcal K\otimes\mathcal S_{12}\longrightarrow\mathcal S_{12},\quad
\mu(k\otimes s)=ks.
\]

In words: the collective question is whether the multiplier k can itself be treated linearly, independently of its expression in the nine generators.

A collective endpoint lift would be a map

\[
F:\mathcal K\otimes\mathcal S_{12}\longrightarrow\mathcal S_{14},
\qquad qF=\mu.
\]

In words: one map must lift multiplication by every allowed normal-product coefficient and respect every relation among those coefficients. This is stronger than producing nine maps \(F_{ij}\) satisfying \(qF_{ij}=g_{ij}\operatorname{id}\).

The old explicit maps remain unchanged. Let \(U_s=u_{\lambda(s)}\), where

\[
\lambda(02)=\lambda(35)=14,\quad
\lambda(04)=\lambda(13)=25,\quad
\lambda(24)=\lambda(15)=03.
\]

In words: these long-normal labels come from the noncrossing target incidence and the already computed residue identities.

The two endpoint coordinates of the old lift are

\[
(F_{ij})_+=a_i U_{m_j}\,z_{+,S_-\setminus\{m_j\}},\qquad
(F_{ij})_-=b_j U_{p_i}\,z_{-,S_+\setminus\{p_i\}}.
\]

In words: the generic coefficient and all twelve old coordinates are multiplied by \(a_i b_j\); the displayed expressions supply the two endpoint coordinates. There is no division by a normal or occurrence variable.

## 3. The complete ideal resolution

For a triple of independent normal variables, resolve its ideal by the truncated Koszul complex with ranks 3, 3, 1. Tensor the two ideal resolutions. This gives

\[
0\longrightarrow\mathcal B\longrightarrow\mathcal B^6
\longrightarrow\mathcal B^{15}\longrightarrow\mathcal B^{18}
\longrightarrow\mathcal B^9\longrightarrow K\longrightarrow0.
\]

In words: K has nine generators, eighteen first relations, fifteen second relations, six third relations and one fourth relation. These are coefficient-resolution generators, not additional geometric target cells. The quotient \(\mathcal B/K\) has free-resolution ranks \((1,9,18,15,6,1)\).

An explicit basis for homological degree r is indexed by nonempty subsets \(A\subseteq S_+\), \(B\subseteq S_-\) with \(|A|+|B|-2=r\). Its differential is

\[
\begin{aligned}
\partial[A,B]={}&
\sum_{a\in A,\ |A|>1}(-1)^{\operatorname{pos}_A(a)}t_a[A\setminus\{a\},B]\\
&+(-1)^{|A|-1}
\sum_{b\in B,\ |B|>1}(-1)^{\operatorname{pos}_B(b)}t_b[A,B\setminus\{b\}].
\end{aligned}
\]

In words: delete a positive or negative label with the ordinary tensor-Koszul sign. Positions begin at zero. On degree zero, the augmentation sends the singleton pair to its normal product.

**Integral exactness in all degrees.** At a fixed normal multidegree, the basis subsets are exactly the nonempty subsets of the positive support and negative support of that monomial. The complex is the tensor of the two simplex chain complexes, each augmenting to one integral copy. Choosing the least vertex contracts each augmented simplex integrally. If either support is empty there are no ideal generators; otherwise the only homology is the required monomial in degree zero. This proves exactness for arbitrary normal powers over the full occurrence coefficient ring. No field reduction or finite-degree extrapolation is used. The construction and tensor signs are the standard Koszul ones [M1].

The checker verifies all polynomial differential identities and independently reduces 729 integral fine-degree complexes, including repeated powers. It also checks the full labelled D3 action. Exchanging the two tensor factors contributes \((-1)^{(|A|-1)(|B|-1)}\); permutation signs within each exterior factor are retained.

## 4. Eighteen endpoint discrepancies

Let F0 be the map from nine copies of S12 to S14 given by the nine F_ij. Apply it to the first resolution differential:

\[
\mathscr D=F_0\partial_1.
\]

In words: this measures the dependence of the endpoint lift on how its multiplier is expressed. All generic and old boundary coordinates cancel. Its value lies in the actual endpoint kernel N.

There are nine positive-index relations and nine negative-index relations. With i less than k, the former have endpoint values

\[
\begin{aligned}
\mathscr D^+_{ik;j}
&=a_iF_{kj}-a_kF_{ij},\\
(\mathscr D^+_{ik;j})_+&=0,\\
(\mathscr D^+_{ik;j})_-
&=b_j\bigl(a_iU_{p_k}z_{-,S_+\setminus\{p_k\}}
-a_kU_{p_i}z_{-,S_+\setminus\{p_i\}}\bigr).
\end{aligned}
\]

In words: changing the positive factor leaves an ambiguity at the negative endpoint. With j less than l, the negative-index relations give

\[
\begin{aligned}
\mathscr D^-_{i;jl}
&=b_jF_{il}-b_lF_{ij},\\
(\mathscr D^-_{i;jl})_+
&=a_i\bigl(b_jU_{m_l}z_{+,S_-\setminus\{m_l\}}
-b_lU_{m_j}z_{+,S_-\setminus\{m_j\}}\bigr),\\
(\mathscr D^-_{i;jl})_-&=0.
\end{aligned}
\]

In words: changing the negative factor leaves the polarity-conjugate endpoint ambiguity. Each discrepancy has exactly two coordinate terms and is nonzero as a sheaf map.

The old conductor identities imply that both expressions have conductor value zero. For example, \(U_{m_j}r_{+,S_-\setminus\{m_j\}}=b_jr_{+,S_-}\). Thus these discrepancies land in the ideal-valued endpoint kernel, not in arbitrary normalization functions.

### One literal target witness

For the two negative labels 02 and 04, with positive label 13,

\[
\bigl(t_{02}F_{13,04}-t_{04}F_{13,02}\bigr)_+
=t_{13}\bigl(t_{02}u_{25}z_{+,\{02,24\}}
-t_{04}u_{14}z_{+,\{04,24\}}\bigr).
\]

In words: the two coefficient products agree, but their endpoint values need not agree.

On the legitimate positive occurrence chart \(D(\tau_+X_{13})\), take generic coefficient zero, \(z_{+,\{02,24\}}=1\), and all other normalization coordinates zero. The conductor is empty on that chart, so this is an allowed source-kernel input. Its discrepancy is

\[
t_{13}t_{02}u_{25}\,\Gamma_{+,S_-}\ne0.
\]

In words: it is a nonzero multiple of the actual opposite, fully marked endpoint state. Both the absolute and PC differentials kill this endpoint chain. It has zero generic-Q projection. It cannot be a target boundary, because the unchanged target is bounded above by homological degree three and this chain is already in degree three.

This witness alone only rejects the displayed choices. Section 6 proves the stronger statement that **no choice of corrections** can make a collective lift.

### Higher relations are retained

The complete second differential satisfies

\[
\mathscr D\partial_2=0.
\]

In words: the eighteen discrepancies obey all fifteen second relations. The six third and one fourth relations are included in the same checked coefficient resolution. These identities are not claimed to exhibit nonzero homotopy groups; an exact resolution has higher presentation data even when the resolved object is concentrated in one degree.

## 5. Local geometry explains why the global obstruction is unchanged

On the common chart \(D(\tau_+\tau_-)\), K is the unit ideal. On a positive occurrence chart \(D(\tau_+X_p)\), all positive normal parameters and one positive occurrence are invertible. The negative occurrence sheet is zero there, and

\[
\mathcal K|_{V_{+,p}}=(t_{02},t_{04},t_{24}),\qquad
\mathcal S_{12}|_{V_{+,p}}\cong\mathcal O^{7},\qquad
\mathcal S_{14}|_{V_{+,p}}\cong\mathcal O^{8},\qquad
\mathcal N|_{V_{+,p}}\cong\mathcal O.
\]

In words: on that chart K is the ideal of three independent opposite normal coordinates. The source and endpoint modules are free there because the conductor is empty and the surviving occurrence ideal is the unit ideal. The negative occurrence charts give the exchanged statement. All seven chart restrictions are checked independently against their actual monomial inversions.

Hence, near the support of \(\mathcal O_V/\mathcal K\), it is a regular codimension-three quotient and N is locally free. The Koszul resolution gives

\[
\mathcal Ext^r_V(\mathcal O_V/\mathcal K,\mathcal N)=0\quad(r<3).
\]

In words: no local Hom, first Ext, or second Ext appears before the three-normal residue degree. The conclusion is equally true for S12 and S14 in place of N. This follows directly from the local displayed bases; no assumption of global local-freeness along the conductor is needed. K is already the unit ideal at that conductor. Regular-ideal conventions are [M2].

Apply sheaf Hom to the actual ideal sequence. Multiplication gives canonical isomorphisms

\[
\mathcal N\xrightarrow{\sim}\mathcal Hom(\mathcal K,\mathcal N),\qquad
\mathcal S_{14}\xrightarrow{\sim}\mathcal Hom(\mathcal K,\mathcal S_{14}),\qquad
\mathcal Ext^1(\mathcal K,\mathcal N)=0.
\]

In words: a map defined on all products in K extends uniquely to multiplication by a section of the original module. The normal ideal has no common divisor that could supply a new scalar denominator. Crucially, these are the canonical multiplication maps, so they are compatible with q, all grading labels and transports.

## 6. A choice-independent theorem

Tensor-Hom adjunction now gives

\[
\operatorname{Hom}_V(\mathcal K\otimes\mathcal S_{12},\mathcal S_{14})
\cong\operatorname{Hom}_V(\mathcal S_{12},\mathcal S_{14}).
\]

In words: every proposed collective map F has the unique form \(F(k\otimes s)=kG(s)\) for a sheaf map G from S12 to S14.

Naturality with respect to q implies

\[
qF=\mu\quad\Longleftrightarrow\quad qG=\operatorname{id}_{\mathcal S_{12}}.
\]

In words: assembling all the individually valid multipliers would split the original endpoint sequence. The preceding triple-pole calculation proves that no such splitting exists. Therefore the space of collective lifts is empty. This rules out every endpoint-valued correction to the nine displayed maps, not merely corrections preserving a chosen normal form.

### Identify the actual Ext class

The same argument works at the derived level. Write \(D_{\mathcal K}(\mathcal N)=R\mathcal Hom(\mathcal K,\mathcal N)\). The cone of its natural map from N has no sheaf cohomology below degree two. Thus tensor-Hom adjunction and global derived Hom [M3, M4] give a canonical isomorphism

\[
\mu^*:
\operatorname{Ext}^1_V(\mathcal S_{12},\mathcal N)
\xrightarrow{\sim}
\operatorname{Ext}^1_V(\mathcal K\otimes^L\mathcal S_{12},\mathcal N).
\]

In words: pulling the endpoint extension back along multiplication preserves its complete first-extension class, not only a nonzero detector.

To justify the degree statement explicitly, the cone belongs to \(D^{\ge2}\). Derived sheaf Hom from a sheaf in degree zero, followed by derived global sections, preserves this lower bound. The associated long exact sequence therefore gives isomorphisms in degrees zero and one. On the common chart K is free, and on every occurrence chart S12 is free. Consequently the displayed derived tensor equals its ordinary tensor; no hidden Tor term has been suppressed.

Let \(\varepsilon_K=\mu^*\varepsilon\). Then

\[
\varepsilon_K\ne0,\qquad
\operatorname{Ann}_{\mathcal B}(\varepsilon_K)=I_++I_-+K.
\]

In words: the collective failure is **the original endpoint obstruction in a new presentation**. It is not a newly discovered independent rung of an arithmetic tower. The eighteen explicit discrepancies give a representative of the connecting obstruction after lifting the nine resolution generators; their image under the true derived comparison is this same class.

A derived map to the unchanged full target which realized the collective generic/boundary comparison would induce the forbidden map on third homology, identified with S14. Therefore passing to a resolution of the source does not evade the theorem.

### Every positive power has the same problem

For any integer n greater than zero, on a positive chart \(\mathcal K^n=\mathfrak n_-^n\). The three powers \(t_{02}^n,t_{04}^n,t_{24}^n\) lie in that ideal and form an N-regular sequence; the negative chart is analogous. Their Koszul resolution, or change of rings through the quotient by those powers, proves that \(R\mathcal Hom(\mathcal O/\mathcal K^n,\mathcal N)\) has no cohomology below degree three.

Repeating the same argument yields

\[
\operatorname{Ext}^1_V(\mathcal S_{12},\mathcal N)
\xrightarrow{\sim}
\operatorname{Ext}^1_V(\mathcal K^n\otimes^L\mathcal S_{12},\mathcal N)
\quad(n\ge1).
\]

In words: higher normal order does not fix collective endpoint selection. Every individual element of K to any positive power still annihilates epsilon and has some lift, but those choices cannot be made into one coefficient-linear map. The all-n claim is a regular-sequence proof, not an extrapolation from finitely tested powers.

## 7. The derived information not visible to ordinary multiplier selection

Let \(W=V\cap V(K)\). It is the disjoint union of

\[
W_+=V\cap V(I_-,\mathfrak n_-),\qquad
W_-=V\cap V(I_+,\mathfrak n_+).
\]

In words: on a positive occurrence chart the three negative normal coordinates vanish; the other component is its polarity conjugate. The common chart meets neither component. On W+ at least one positive occurrence and all three positive normals are invertible; thus its endpoint ideal is the structure sheaf. The analogous statement holds on W-.

Retain the conormal determinant duals \(\ell_-^\vee\) and \(\ell_+^\vee\), respectively. With \(j_\pm:W_\pm\hookrightarrow V\), define

\[
\mathcal T=
 j_{+*}(\mathcal O_{W_+}\Gamma_{+,S_-}\otimes\ell_-^\vee)
 \oplus
 j_{-*}(\mathcal O_{W_-}\Gamma_{-,S_+}\otimes\ell_+^\vee).
\]

In words: T consists of the two actual endpoint coefficient lines on their opposite triple-normal supports, with the ordered dual normal determinants included.

Dualizing the ideal sequence constructs the full triangle

\[
\mathcal T[-3]\longrightarrow\mathcal N
\longrightarrow R\mathcal Hom(\mathcal K,\mathcal N)
\longrightarrow\mathcal T[-2].
\]

In words: this is the canonical codimension-three supported comparison. Shifts in this paragraph are cohomological; T minus three lies in degree three. Its first new sheaf cohomology occurs in degree two after comparing the ideal with the unit object:

\[
\mathcal H^0R\mathcal Hom(\mathcal K,\mathcal N)=\mathcal N,\qquad
\mathcal H^2R\mathcal Hom(\mathcal K,\mathcal N)=\mathcal T.
\]

In words: the two supported residue lines are retained rather than declared zero, but they do not alter the Hom or global first-Ext calculations above. The full triangle and its connecting morphism matter; no splitting into cohomology sheaves is asserted.

A finite representative of this triangle is obtained by applying Hom into N to the entire explicit ideal resolution. The differential is the signed transpose: for a cochain of degree r it is \((-1)^{r+1}\) times precomposition with the next homological differential. Thus the construction includes actual maps, not just a list of degrees.

### Affine control before restriction to V

Over the spectator polynomial ring C, the same ideal dual has cohomology in degrees zero, two and four. In fixed ordered frames,

\[
H^0R\operatorname{Hom}_{\mathcal C}(K,\mathcal C)=\mathcal C,\qquad
H^2\cong\mathcal C/\mathfrak n_+\oplus\mathcal C/\mathfrak n_-,\qquad
H^4\cong\mathcal C/(\mathfrak n_++\mathfrak n_-).
\]

In words: the two three-normal branches contribute degree two, while their six-normal intersection contributes degree four. The suppressed orientation factors here are the corresponding determinant duals; the top factor additionally retains the sign line of the normalization difference. Equivalently, use the tensor of the two triple determinant duals with the symmetry inherited from the truncated ideal resolutions. The checker preserves these tensor/exterior signs under every labelled dihedral transport.

This follows from the exact normalization sequence for C/K and the three- and six-variable Koszul resolutions. The checker independently verifies 4,096 integral dual multidegree/localization cases, covering every inverted-coordinate subset and every first-pole sign pattern. Coefficients of arbitrarily large exponent have the same incidence pattern; below exponent minus one there is no basis in a non-inverted coordinate. Those additional empty cases are also tested.

The degree-four term disappears on V because every named chart inverts at least one of its six normal parameters. Only the two degree-two terms remain. This is restriction of an explicit complex, not an unexplained regrading.

## 8. Where the repeated normal conductor lives

The earlier cyclic global obstruction module was \(\mathcal C/K\). Its fibre-product presentation in the six normal variables remains correct. But it is the coefficient support of a **global Ext class**, not automatically a new physical stratum inside V.

Indeed, with \(H=I_++I_-+K\),

\[
V\cap V(H)=\varnothing,\qquad \widetilde H|_V=\mathcal O_V.
\]

In words: the common chart inverts an element of K, and each occurrence chart inverts an element of its occurrence ideal. The module generated by the global obstruction has no support on those charts. This is consistent with local splitting and global failure of gluing. It must not be confused with the nonempty support W of the new **sheaf** Ext degree-two terms in Section 7.

As a further check, asking to assemble lifts for all six occurrence generators together with the nine normal-product generators simply asks for a splitting of the original sequence: their full ideal sheaf is already O_V. The obstruction is therefore not bypassed by enlarging the list of individually permitted multipliers.

## 9. Research consequence

The computation supplies the complete coefficient relations a physical source comparison would have to preserve. It excludes a particular shortcut: treating independently normalized endpoint multipliers as one coefficient-linear operation. Resolving their ideal or taking higher powers does not change the original endpoint class.

The remaining route may change support or variance, as the supported-dual constructions in the other lanes explicitly do. This calculation does not exclude that route. It now provides a canonical test object for it: the codimension-three triangle of Section 7, with both endpoint lines, long-normal coefficients and all multiplier syzygies retained. Mapping a native source into that triangle remains to be constructed. The triangle is not itself a scalar trace, and its two residues must not be assigned the value one by dropping their independent long-normal factors.

No new generic unit is produced, no nonzero native source class is declared homotopic to zero, and no equivalence between arithmetic resolution degree and homotopy dimension is claimed.

## 10. Reproduction and provenance

Run:

```sh
python check_marici_endpoint_multiplier_coherence_20260907.py \
  --output marici_endpoint_multiplier_coherence_certificate_20260907.json
```

The standard-library checker is standalone. It embeds the predecessor's target definitions, but not its main calculation. It verifies the 215-state differentials; both endpoint families; all nine polynomial maps; all eighteen nonzero relation discrepancies; all fifteen second-syzygy equations; the entire 49-generator ideal resolution and its dihedral signs; 729 integral ideal strands; 4,096 dual localization strands; and the actual seven-chart regular-ideal calculation. It passes **73,866 exact assertions**. Every nonzero matrix Smith factor encountered is one. These tests do not replace the all-polynomial, global-Ext and all-power proofs above.

The preceding endpoint checker was independently rerun and passed **120,909 exact assertions**. Its SHA-256 is

```text
345213ec7be1e59461dad8f9c01e644bcb86c92f7b42ff48bb2b082a2f16c727
```

The new certificate records its own executable hash and the prerequisite rerun-certificate hash. No repository files were changed. No fresh audit of the repository's current branch head is claimed; the mathematical input is the pinned model and current conversation artifacts stated above. This is executable algebra together with explicit proofs, not proof-assistant certification.

## References

[P1] `marici_normalization_endpoint_extension_20260907.md` and `check_marici_normalization_endpoint_extension_20260907.py`: the exact normalization sources, endpoint extension, residue vector, nine maps, target chains and annihilator proof.

[P2] `marici_obstruction_complement_descent_20260907.md`: the seven-chart test open, its normalization sheets, conductor, local lifts and twelve initial residue coordinates.

[M1] Stacks Project, Section 15.29, *The Koszul complex*, tag `0621`: `https://stacks.math.columbia.edu/tag/0621`.

[M2] Stacks Project, Section 31.21, *Regular ideal sheaves*, tag `067M`: `https://stacks.math.columbia.edu/tag/067M`.

[M3] Stacks Project, Section 20.50, *Duals*, tag `0FP7`: `https://stacks.math.columbia.edu/tag/0FP7`; tensor duality for the finite perfect ideal resolution.

[M4] Stacks Project, Section 20.44, *Global derived hom*, tag `0B6A`: `https://stacks.math.columbia.edu/tag/0B6A`; distinction between sheaf and global derived Hom.

[M5] Stacks Project, Section 12.6, *Extensions*, tag `010I`: `https://stacks.math.columbia.edu/tag/010I`; pullback of an extension and its splitting class.
