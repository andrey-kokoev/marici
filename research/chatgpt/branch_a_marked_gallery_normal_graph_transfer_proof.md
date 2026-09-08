# Branch A — marked-gallery normal-graph transfer and endpoint comparison

Date: 2026-09-07.

## Result and scope

There is an explicit coefficient-level support retraction from the entire short facet 35 to the actual marked D03 gallery after adjoining the inverses of two native-normal slopes. Its matrix has 64 rows, 124 columns, and 92 nonzero monomial entries. Multiplication by the product of those two slopes gives a polynomial map. Its ordered double-slope symbol is a primitive four-state normal insertion at the actual middle vertex {03,13,35}.

Both physical endpoint packets can be retained by adding the unchanged negative endpoint. The resulting 80-by-140 map is the identity on all 32 endpoint states. It also has an explicitly computed, nonzero off-diagonal endpoint comparison. Identity on the endpoint subcomplex must not be confused with preservation of zero endpoint components of arbitrary input chains and their boundaries.

The construction transfers the two previously computed 35-facet comparison homotopies to zero and to a two-term marked-gallery chain. The second image has one nonzero incoming endpoint term. The global version sends the nine coherent normalization comparisons to a three-dimensional local image; their three invariant families have a one-dimensional image. Every nonzero image changes at least one of the previously fixed endpoint values or incoming endpoint terms.

This is a chain-level support operation derived from the full normal-graph differential. It is not identified here with a six-functor Gysin transformation or with the physical conductor–Morse class. The graph parameters introduced below distinguish a slope divisor from an occurrence/channel divisor. Their ordered double-slope symbol must not be renamed the physical normal residue without a further comparison.

## 1. Complete coefficient model

Let

\[
\mathcal D=\{02,03,04,13,14,15,24,25,35\},
\qquad
P=\{13,15,35\},\quad M=\{02,04,24\}.
\]

Work over

\[
R_0=\mathbb Z[X_d:d\in\mathcal D]/(X_mX_p:m\in M,\ p\in P).
\]

The two ideals are the normalization-sheet conductor ideals. Use independent graph parameters \(\lambda_d\) to write

\[
u_d=\lambda_dX_d.
\]

This is an explicit base change from the independent-monodromy coefficient ring. The new parameters are normal slopes; they are not asserted to be the original six spectator Rees coordinates or physical channel coordinates. The ring used by the checker includes an additional independent variable beta for the subsequent common-regulator specialization.

A state is \([F,H,e]\), where \(F\) is a noncrossing face, \(H\subseteq F\) is the native-circle subset, and \(e=0,1\) retains the separate occurrence-35 factor. Its homological degree is

\[
3-|F|+|H|+e.
\]

The differential is the source's radial differential with coefficient \(X_a\), the signed native boundary with coefficient \(\lambda_aX_a\), and the signed separate occurrence boundary with coefficient \(X_{35}\). The checker reconstructs all 430 states and verifies the complete polynomial square-zero equation.

The known physical graph, after scalar extraction, has

\[
u_d=e^{\beta X_d}-1=\beta v_d(X_d)X_d,
\qquad v_d(0)=1.
\]

At fixed nonzero beta in characteristic-zero completion, each \(\lambda_d=\beta v_d\) is a unit. The coefficient retraction therefore specializes there without inverting an occurrence coordinate or \(u_d\). Rescaling the native basis by the independently prescribed units \(v_d\) gives the common-slope family \(\lambda_d=\beta\). At beta zero that latter family is not a unit-slope model.

## 2. A triangular normal-basis change removes radial off-diagonal blocks

Write \(d_{\mathrm v}\) for the native and occurrence differential alone. It preserves the face label. For an admissible added set \(A\), with \(k=|A|\), define

\[
\epsilon(F,H;A)=
(-1)^{k(3-|F|)-k(k-1)/2+
\sum_{a\in A}(\#\{f\in F:f<a\}+\#\{h\in H:h<a\})}.
\]

The ordered normal-basis change is

\[
\mathcal U[F,H,e]=
\sum_A
\frac{\epsilon(F,H;A)}{\prod_{a\in A}\lambda_a}
[F\cup A,H\cup A,e].
\]

The inverse is the same sum with an extra factor \((-1)^{|A|}\). Here the sum runs over sets A disjoint from F for which F union A is a noncrossing face. No additional unlabelled cell is introduced.

One can obtain the formula as an ordered product of square-zero marked-coface insertion operators. Operators for different added diagonals commute when the simultaneous face exists and have zero composite when it does not. Expanding the product gives the displayed signs, with no integer factorial denominator.

The full symbolic matrices satisfy

\[
\mathcal U^{-1}\mathcal U=\mathcal U\mathcal U^{-1}=1,
\qquad d\mathcal U=\mathcal U d_{\mathrm v}.
\]

For a finite free complex, checking these equations on every basis column over the polynomial/Laurent coefficient ring proves them for every coefficient, not just for a bounded degree sample.

Every term has the same homological and occurrence degree as its source. The increase of native normal grade is compensated by the displayed slope inverses. Every image face is a coface of the original face; closed-support subcomplexes are preserved. Ordered native-mark signs and the separate occurrence factor are retained.

The construction is natural under the source's relabellings, including its base-cell orientation sign. The checker verifies rotation and reflection on all 430 states in each transported occurrence label. A relabelling changes the marked gallery when its labels change; no reflection action within a non-invariant gallery is assumed.

Koszul functoriality and invertible normal-basis changes are described by Stacks tag 0621. The extra marked-coface terms here are provided explicitly and their full chain equation is independently checked.

## 3. Project in the split basis and return to the loaded basis

Let \(C_{35}\) consist of all states whose face contains 35. Let \(C_\Gamma\) be the marked gallery with faces

\[
\{13,35\},\quad\{03,35\},\quad
\{13,15,35\},\quad\{03,13,35\},\quad\{02,03,35\}.
\]

Their ranks are 124 and 64. They are actual subcomplexes of the full coefficient model, and the gallery is the one specified in Marici Entry 106.

Because \(d_{\mathrm v}\) is face-diagonal, its face projection \(P_\Gamma\) is a chain map. Set

\[
r_\Gamma=\mathcal U P_\Gamma\mathcal U^{-1}.
\]

Then

\[
dr_\Gamma=r_\Gamma d,
\qquad r_\Gamma|_{C_\Gamma}=1,
\qquad r_\Gamma^2=r_\Gamma.
\]

This retraction is fixed by the displayed normal splitting and the given marked face set. No uniqueness among all possible retractions is asserted.

Although the intermediate splitting uses all slope inverses, its restriction to \(C_{35}\) involves only \(\lambda_{03}^{-1}\) and \(\lambda_{13}^{-1}\). Put \(a=\lambda_{03}\) and \(b=\lambda_{13}\). A closed formula for every column is:

- On every gallery face, \(r_\Gamma\) is the identity.
- On the four states over the facet 35,

\[
\begin{aligned}
r_\Gamma[\{35\},H,e]={}&
-a^{-1}[\{03,35\},H\cup\{03\},e]\
&-b^{-1}[\{13,35\},H\cup\{13\},e]\
&+(ab)^{-1}[\{03,13,35\},H\cup\{03,13\},e].
\end{aligned}
\]

- On the edge \(\{02,35\}\),

\[
r_\Gamma[\{02,35\},H,e]
=
(-1)^{1+\mathbf1_{02\in H}}a^{-1}
[\{02,03,35\},H\cup\{03\},e].
\]

- On the edge \(\{15,35\}\),

\[
r_\Gamma[\{15,35\},H,e]
=b^{-1}[\{13,15,35\},H\cup\{13\},e].
\]

- Every remaining facet-35 source column is zero.

All 124 case formulas agree with the independently computed conjugation matrix.

The regulator poles are not poles in \(X_d\) or in \(q_d-1\). The ordered pair \((a,b)\) labels the slopes of the normals meeting at the source's middle vertex. It is distinct from the earlier ordered spectator pair \((t_{04},t_{35})\).

## 4. Polynomial regularization and its ordered normal symbol

Define

\[
\mathcal G_\Gamma=ab\,r_\Gamma:C_{35}\longrightarrow C_\Gamma.
\]

Every entry is polynomial. The map remains a chain map, and

\[
\mathcal G_\Gamma|_{C_\Gamma}=ab\,1.
\]

It is a regularized transfer, not a retraction over the slope-zero locus. Its independent normal-grade shift is \(\epsilon_a+\epsilon_b\).

At \(a=b=0\), the only nonzero columns are

\[
[\{35\},H,e]
\longmapsto
[\{03,13,35\},H\cup\{03,13\},e],
\qquad H\subseteq\{35\},\quad e\in\{0,1\}.
\]

Every coefficient is +1 with the order \(03<13\). This is a four-state chain map. It retains the native 35 normal and its independent occurrence partner, including all mixed differential signs. Its endpoint and Q components are zero.

The two new native marks become closed on this slope-zero locus. Thus the symbol identifies the facet's four-state vertical quotient with the corresponding two-mark subcomplex at the middle vertex. The degree is unchanged: the loss of two spatial dimensions is accompanied by two retained normal marks. The ordered normal determinant is not evaluated away.

This symbol is not asserted to be a physical Gysin counit. It is the exact leading two-slope symbol of the constructed polynomial matrix. In particular, slope vanishing is not channel vanishing.

### The localization cannot be omitted

Consider the unmarked edge \(\{02,35\}\). A coface-only retraction fixing the gallery must send its \(X_{03}\)-boundary to the unmarked vertex \(\{02,03,35\}\). Its degree-one image can use only the three native circles at that vertex and the separate occurrence circle. Modulo

\[
a=X_{02}=X_{35}=0,
\]

all four possible target boundaries vanish, whereas the source boundary retains \(X_{03}\). This is a contradiction for any polynomial coface-only retraction.

The edge \(\{15,35\}\) gives the corresponding obstruction at

\[
b=X_{15}=X_{35}=0,
\]

where the source retains \(X_{13}\).

These arguments exclude a polynomial coface-only retraction across either slope divisor. They do not exclude arbitrary extraordinary correspondences. On the common-slope specialization \(a=b=\beta\), the constructed retraction has exact pole order two. Its regularization \(\beta^2r_\Gamma\) is polynomial, with the preceding middle-vertex symbol on the central fibre.

## 5. Retain both endpoint packets and compute the comparison cell

The facet-35 complex contains the full positive endpoint. Retain the full negative endpoint as an additional unchanged direct summand. Define

\[
D=C_{35}\oplus V_-,
\qquad G=C_\Gamma\oplus V_-.
\]

Their ranks are 140 and 80. Both contain all 32 states in \(V=V_+\oplus V_-\). The transfer is the previous retraction on the facet and the identity on \(V_-\). It has 108 nonzero entries and fixes \(V\) pointwise.

The graded projections onto V are not chain maps. Use the actual short exact sequences with quotients \(E_D=D/V\) and \(E_G=G/V\). In the labelled graded splittings,

\[
d_D=\begin{pmatrix}d_V&\kappa_D\\0&d_{E_D}\end{pmatrix},
\qquad
d_G=\begin{pmatrix}d_V&\kappa_G\\0&d_{E_G}\end{pmatrix},
\]

\[
r=\begin{pmatrix}1&A\\0&r_E\end{pmatrix}.
\]

The full chain equation gives

\[
\kappa_G r_E-\kappa_D
=A d_{E_D}-d_VA.
\]

The eight nonzero columns of A are exactly

\[
A[\{15,35\},H,e]
=b^{-1}[V_+,H\cup\{13\},e],
\qquad H\subseteq\{15,35\},\quad e=0,1.
\]

All remaining columns are zero, and there is no negative-endpoint contribution. This is an explicit comparison of both endpoint connecting maps. It is not replaced by equality of their scalar signatures. The signs agree with the standard cone/Hom conventions (Stacks tags 014D and 0A8H).

Identity on the endpoint subcomplex does not imply that a chain and its boundary remain endpoint-zero after applying r. The nonzero A is exactly the additional data that must be retained when transporting that frame.

## 6. Apply the transfer to the two actual facet comparisons

Specialize all slopes to beta in the already unit-normalized coefficient model. For a face F write \(E_F=[F,F,1]\), retaining the occurrence factor.

The preceding facet homotopies were

\[
U_a=E_{\{02,03,35\}}+E_{\{02,25,35\}}-\beta E_{\{02,35\}},
\]

\[
U_b=\beta^2E_{\{35\}}+\beta E_{\{03,35\}}+\beta E_{\{25,35\}}.
\]

The computed values are

\[
r(U_a)=0,
\qquad
r(U_b)=L_{03}^{\mathrm{occ}}
=E_{\{03,13,35\}}-\beta E_{\{13,35\}}.
\]

Thus the D25 terms are removed by a chain operation that simultaneously changes other columns. Simply discarding them would not reproduce this result.

The output has zero endpoint coefficient but a nonzero incoming endpoint boundary:

\[
v(L_{03}^{\mathrm{occ}})=0,
\qquad
v(dL_{03}^{\mathrm{occ}})
=\beta X_{15}[V_+,\{13,35\},1].
\]

The off-diagonal comparison supplies it exactly:

\[
A(U_b)=0,
\qquad
A(dU_b)=\beta X_{15}[V_+,\{13,35\},1].
\]

This is a coefficient-one defect, with its beta and occurrence factors retained. The transfer is a map of the endpoint support triangles with the displayed comparison cell. It is not a map between the previously chosen strict zero-value/zero-incoming-endpoint kernels unless that correction is transported as part of the frame.

## 7. Transfer the complete nine-dimensional family

For the global calculation use

\[
r_{\Gamma\cup V_-}=\mathcal U P_{\Gamma\cup V_-}\mathcal U^{-1}:
C\longrightarrow C_\Gamma\oplus V_-.
\]

Its 80-by-430 matrix has 192 nonzero entries. Unlike the restricted facet map, its universal formula can involve other slope inverses. At the physical unit-slope graph these are allowed formal units.

The checker reconstructs the nine allowed input homotopies directly. A homogeneous degree-four value on the source generator \(a_{35}\) is a combination of the 45 fully native-marked faces with the factor \(\beta^{3-|F|}\). Endpoint and Q values are set to zero, incoming endpoint equations are imposed, and the conductor-constant part of its differential is required to vanish. Exact integer elimination gives a saturated rank-nine kernel. No previous certificate is read.

For every H, all source maps are reconstructed as \(f=\delta H\) on the six ideal generators, the 24 relations, and the 92 next compatibility equations. The transfer satisfies

\[
\delta(rH)=rf,
\]

including all relation components. Every resulting coefficient is polynomial in beta and the occurrences, despite the intermediate localized retraction.

The image has rank three, with basis

\[
L_{03}^{\mathrm{occ}},\qquad E_{V_-},\qquad E_{V_+}.
\]

The kernel has rank six. The three elementary endpoint readouts are: the coefficient of \(E_{V_-}\), the coefficient of \(E_{V_+}\), and the coefficient of
\(\beta X_{15}[V_+,\{13,35\},1]\) in the differential. Their matrix on this basis is

\[
\begin{pmatrix}
0&1&0\\
0&0&1\\
1&0&-1
\end{pmatrix}.
\]

Its determinant is one. Therefore no nonzero transferred image satisfies all the old zero endpoint values and zero incoming endpoint conditions. This statement is exact over the integers, not a rank test over selected primes.

The three reflection-invariant input homotopies have a one-dimensional image, generated by

\[
L_{03}^{\mathrm{occ}}+E_{V_+}.
\]

This is a local chart value of an equivariant family. Reflection transports the marked D03 gallery to its actual D25-labelled image; it is not an action fixing this local carrier. Rotation also moves the separate occurrence label. All six transported diagrams satisfy the full chain equation.

The invariant local image has a primitive nonzero endpoint-top coefficient. It is not a remaining endpoint-fixed deformation. No scalar coefficient has been selected to declare it the physical conductor map.

## 8. Consequences and remaining physical comparison

The construction supplies an explicit localized support-changing coefficient map, a polynomial two-slope regularization, and its primitive middle-vertex symbol. It also computes the eight-column endpoint comparison required to use that map coherently.

The strict marked-gallery support exclusion from the preceding step is not contradicted. The new operation mixes spatial and normal basis states and is first defined at unit slopes. Its nonzero images do not retain the earlier zero endpoint-comparison conditions unchanged. On the particular nine input maps the Laurent factors cancel, but the computed endpoint discrepancy remains.

No physical six-functor interpretation or value of Delta_J follows merely from the unit middle-vertex symbol. The next comparison is now explicit: determine whether the eight-column A is the endpoint comparison supplied by the actual normalization/logarithmic Gysin correspondence. The scalar first conductor symbol cannot replace this comparison.

## Reproduction

Run the standalone file

```sh
python branch_a_marked_gallery_normal_graph_transfer_checker.py
```

It uses only the Python standard library. It reconstructs the 430-state model, the universal normal splitting and its inverse, both support retractions, the two-slope regularization, the endpoint comparison, all nine input maps, the source relations, and the transported symmetry equations.

The completed run verified 69,839 exact identities. A separate directory containing only the checker was run with PYTHONHASHSEED=24539. Its JSON certificate agreed byte-for-byte with the original.

The mathematical-data SHA-256 is

```
2b06ac26e828730c78caee34233f6bfda93c8b05e00ecd627a5e7f89db315372
```

The checker and certificate filenames are purpose-specific and no archive is required.

## Sources and provenance

Repository: andrey-kokoev/marici, commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61.

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, blob b967151cb0ee822e2361b9334a4ab26082c12682: actual labelled states, radial/native differential, support sets, and orientation transport.
- `src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md`, blob d9ac9420e7360013ff6acde34df51a4941b34101: the source-defined two-edge marked D03 gallery.
- `research/voevodsky/check_d03_formal_support_purity.rs`, blob acaabf367b24029d9dbfa371ee1983d392b393fa: physical normal graph at fixed nonzero beta and its unit-basis comparison. Its physical theorem is not extended to beta zero here.
- Prior local artifact `branch_a_full_conductor_square_and_d03_support_checker.py`: conventions for the conductor ideal resolution and prior nine-dimensional family. The present checker reconstructs that family and never imports the prior file or reads its certificate.
- Stacks Project 0621: Koszul complexes and changes of generators.
- Stacks Project 014D: cones and the comparison correction for homotopy-commutative diagrams.
- Stacks Project 0A8H: Hom-complex differential and composition signs.
