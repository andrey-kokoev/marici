# Logarithmic normal-link excess pairing and the generic-Q comparison audit

Date: 2026-09-06  
Source: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and exact category

This note constructs an integral logarithmic **normal-link/coefficient** comparison. It preserves the source's labelled, line-normalized first Tor class, realizes both endpoint orientations, and compares the resulting pairing to the actual road readout by an explicit homotopy on the complete polynomial conductor-road complex. The construction works on arbitrary polynomial inputs, not just the primitive unit.

There is a separate negative result. On the marked barycentric occurrence complex used in source entry 396, the rule described in entry 397 that retains only top/long-only flags is not a chain map. A single mixed triangle witnesses the failure. Replacing it by an honest ordinary relative-chain quotient makes the displayed corrected roof a boundary. This does not disprove a framed, filtered derived Yoneda class; it shows that retaining its leading coefficient is not a proof of that class.

Consequently, a complete physical correspondence with a verified nonzero derived generic-Q leg has **not** been constructed here. The local logarithmic and endpoint pieces below are established. Their promotion to the literal ringed filtered BM/Cech endpoint-Q target is not asserted.

All complexes below have homological grading. The convention is `(C[s])_n=C_(n-s)`, with shifted differential `(-1)^s d`. In particular R[1] has its only term in degree one. R denotes an arbitrary commutative coefficient ring. The geometric Kato-Nakayama description is over the complexified local chart with integral, or constant R, coefficients; R-valued constructible coefficients are not silently identified with the raw structure sheaf of that chart.

## 1. The actual log chart, not ordinary product/intersection purity

Use the source relation

\[
u=Xt.
\]

In words: the two normal coordinates multiply to the base degeneration parameter. Give the base and source their standard divisorial logarithmic structures. At the crossing, their characteristic chart is

\[
\mathbb N\longrightarrow\mathbb N^2,
\qquad 1\longmapsto(1,1).
\]

In words: the log normal generator on the base maps to the sum of the two branch generators. The relative characteristic group is

\[
L=\mathbb Z^2/\mathbb Z(1,1),
\qquad [e_t]\longmapsto1,
\qquad [e_X]\longmapsto-1.
\]

In words: the chosen branch gives a primitive generator. The antisymmetric character e-t minus e-X would be **twice** this generator and must not be substituted for it.

At the source's positive-real base phase, the logarithmic fibre over the crossing is

\[
T=\{(\zeta_X,\zeta_t)\in(S^1)^2:\zeta_X\zeta_t=1\},
\qquad
\gamma(\theta)=(e^{-2\pi i\theta},e^{2\pi i\theta}).
\]

In words: the missing angular direction remains a circle. Its positively oriented t-winding is primitive. Branch exchange reverses its orientation. Kato-Nakayama nearby-cycle theory supplies this torus description; in this particular chart it also follows immediately from the displayed polar-coordinate equation. [M1]

The cycle is present on nearby smooth fibres, not just in a special-fibre normalization quotient. For positive r, the circles

\[
X=\sqrt r\,e^{-2\pi i\theta},\qquad
 t=\sqrt r\,e^{2\pi i\theta},\qquad u=r
\]

extend to the displayed log circle at r=0. In words: these are explicit vanishing-cycle cores in the local annuli. Using this nearby object avoids the invalid assertion that the normalization quotient of a smooth total space specializes to the normalization quotient of its nodal fibre.

### A finite model with the correct relative boundary

Cut the based circle at its marked point, retain both resulting endpoints, and subdivide the interval once. Orient both edges from the midpoint towards the endpoints. The relative chain complex is

\[
\mathcal L_t=[Rr_D\oplus Rr_1\xrightarrow{(-1,-1)}Rc],
\qquad \gamma=-r_D+r_1.
\]

In words: the two rays end at the two labelled endpoints, which have been made relative. The midpoint remains. The first term is in degree one and the second in degree zero. Its only homology is the primitive orientation line in degree one. Making only one endpoint relative would give an acyclic interval and would lose the required class.

The full based-circle packet has an R-linear model

\[
\mathcal T_t=R[0]\oplus\mathcal L_t.
\]

In words: the unshifted unit is retained as well as the first normal class. This is a local based model, not a claim that every global nearby-cycle sheaf splits canonically into its cohomology sheaves.

### What it means here to preserve the original Tor class

For B=R[X,t], conductor C=Spec R, and u=Xt, the derived conductor fibre of K-B(u) has one copy of R in degrees zero and one. Its first Tor line is the fibre of the Cartier line I-u. The source's principal-line identification is

\[
I_u\cong I_X\otimes I_t.
\]

In words: this cancels occurrence and conductor normal lines as invertible modules, not by inverting coordinates in R. After the prescribed normal-line frames and relative orientation are retained, the comparison sends the normalized first Tor generator to gamma and the unshifted unit to the R summand. This is an explicit quasi-isomorphism of the resulting normal-link coefficient complexes. Reflection uses the relative log orientation, not an unmentioned change in the raw Koszul character.

This is **not** a B-linear map K(Xt) to K(X,t). The previous proof that every such ordinary map kills the first conductor Tor class remains valid. The new object is the logarithmic nearby normal link, and the comparison is made after the specified normal-line operation. No theorem equating raw coherent and Betti categories is inferred.

## 2. The mixed-variance comparison is an actual pairing

Use the polynomial node and its normalization:

\[
A=R[x,y]/(xy),\qquad N=R[x]\oplus R[y],
\qquad E_R=[A\xrightarrow{\nu}N].
\]

In words: node functions are relations on the two normalization sheets. A has degree one and N degree zero. Its degree-zero homology is the orientation quotient, with

\[
\delta(f,g)=f(0)-g(0).
\]

In words: the surviving endpoint coefficient is a sheet difference, not a common conductor value.

Define

\[
\begin{aligned}
\Pi_t:\mathcal L_t\otimes_R E_R&\longrightarrow R[1],\\
\Pi_t((a,b)\otimes(f,g))&=a\,g(0)+b\,f(0),\\
\Pi_t(c\otimes h)&=-c\,h(0).
\end{aligned}
\]

In words: the first formula pairs the two ray coefficients with the exchanged sheets; the second formula pairs the midpoint with the node relation, with its total-complex sign. All other degrees map to zero. These are maps on full polynomial modules.

### Chain equation

The only potentially nonzero image of a boundary comes from a ray vector tensored with a node function h. Its two images sum to

\[
(a+b)h(0)-(a+b)h(0)=0.
\]

In words: the midpoint-node term cancels the normalization-sheet term. Omitting that correction breaks the chain equation, even on the constant node function one.

On the primitive log class,

\[
\Pi_t(\gamma\otimes(f,g))=f(0)-g(0)=\delta(f,g).
\]

In words: the logarithmic pairing is exactly the source conductor quotient on arbitrary coefficients. A positive branch polynomial has a matching node boundary; no polynomial direction is deleted from the domain just to enforce the answer.

The pairing is a quasi-isomorphism. The interval has one primitive degree-one orientation class, E has one primitive degree-zero orientation class, and the pairing of those classes is one. The modules are R-free, and the polynomial comparison has the explicit identity-kernel contraction established in the preceding note, so this holds over every commutative R, without rational rank arguments.

### The endpoint connector and its variance

In the ordered ray and sheet bases the pairing matrix is

\[
M=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

In words: the two labels are exchanged. This is precisely the source endpoint matrix selected by boundary orientation and the common counit in entry 400. It has determinant minus one. [S2]

Simultaneous branch exchange swaps both ray and sheet vectors, leaving the pairing invariant. The first log class and the endpoint quotient are separately odd; their evaluation is even. This realizes the compensating relative orientation and must not be counted as an additional second polarity twist.

Do not replace this pairing by the different operation of sending the boundary vector into the sheet module and then taking its difference. That composite gives

\[
\delta\bigl(M(-1,1)^T\bigr)=2.
\]

In words: the endpoint boundary and the dual evaluation are different arrows. The construction pairs gamma against the primitive sheet quotient; it does not divide that twice-primitive boundary vector by two.

### A nonzero generic dual nearby object

The adjoint of the pairing is an A-linear quasi-isomorphism

\[
E_R\longrightarrow\operatorname{Hom}_R(\mathcal L_t,R)[1].
\]

In words: the nodal relative normalization object is identified with the dual of the logarithmic interval, with its explicit shift. On degree zero this map sends (f,g) to the two values (g(0),f(0)); on degree one it sends h to minus h(0). Its kernel is the same identity complex of positive branch ideals as before.

Extend the **dual nearby-cycle object**, rather than the normalization quotient of the smooth total chart. Its local generic fibre remains the dual of the vanishing-cycle interval. At the special normal link, the displayed polynomial map identifies it with E-R. This is a genuine constructible normal-link replacement of the failed normalization-specialization shortcut. It is not yet a morphism of the full raw ringed support-PC diagrams.

## 3. Retain the road resolution and both endpoint connectors

The complete source endpoint complex is

\[
\begin{aligned}
P_3&=R,&d_3(c)&=(0,(c,c,c)),\\
P_2&=A\oplus R^3,&d_2(h,t)&=(\nu(h),(1-r)t),\\
P_1&=N\oplus R^3,&d_1(s,q)&=\delta(s)-\epsilon(q),\\
P_0&=R_{\rm or},&&\epsilon(q)=q_0+q_1+q_2.
\end{aligned}
\]

In words: both normalization sheets, the triangle relations, the top norm, and the endpoint comparison remain. The physical unit is z=((1,0);(1,0,0)), not the common-conductor pair.

Define the full mixed-variance excess evaluation

\[
\begin{aligned}
\Xi_t:\mathcal L_t\otimes_R P_R&\longrightarrow R[2],\\
\Xi_t((a,b)\otimes((f,g),q))&=a\,g(0)+b\,f(0),\\
\Xi_t(c\otimes(h,t))&=-c\,h(0).
\end{aligned}
\]

In words: these formulas act on total degree two. Every other total degree maps to zero. The same cancellation proves the chain equation; the road and norm terms are not omitted, but their images vanish by their actual augmentation identities.

The primitive and opposite endpoint values are

\[
\Xi_t(\gamma\otimes z)=1,\qquad
\Xi_t(\gamma\otimes sz)=-1,\qquad
\Xi_t(s\gamma\otimes sz)=1.
\]

In words: both endpoint orientations are present and simultaneous reflection is compatible. This map is a quasi-isomorphism of R-complexes. Keeping the full log packet gives

\[
(R\oplus\mathcal L_t)\otimes_R P_R
\simeq P_R\oplus R[2].
\]

In words: the unshifted-normal and shifted-normal sectors both remain, in adjacent endpoint homology degrees one and two. No first Tor grade has been contracted away before evaluating its dual.

### An explicit comparison to the generic interval trace and road readout

The source interval trace selects the r-one coordinate. Define the positively normalized road comparison on total degree two by

\[
\chi_{\rm road}((a,b)\otimes(s,q))=b\,\epsilon(q),
\]

and zero on midpoint-times-degree-two terms. In words: this is the interval trace followed by the source's road augmentation, with the displayed tensor sign convention. It is also a chain map.

They agree by a homotopy on the **complete** complex, not just on homology. Set, on total degree one,

\[
K(c\otimes((f,g),q))=-c\,g(0),\qquad
K((a,b)\otimes o)=-b\,o.
\]

In words: the first term retains the second sheet endpoint, and the second retains the actual endpoint comparison term P-zero. Then

\[
\Xi_t-\chi_{\rm road}=K d.
\]

In words: the two physically prescribed readout routes are explicitly homotopic. The equation also holds on node relations and triangle tags. It is natural under coefficient-ring maps and coefficient localizations. A comparison that drops the endpoint term cannot use this homotopy.

### A necessary coefficient-category warning

All tensor products in this construction are over R. Changing them to derived tensor products over the singular node A is not harmless. From the alternating node resolution,

\[
\operatorname{Tor}_0^A(R,R)=R,\qquad
\operatorname{Tor}_n^A(R,R)=R^2\quad(n\ge1).
\]

In words: a coherent derived tensor over A carries additional degrees. The displayed R-linear evaluation is not asserted to be a quasi-isomorphism for that different operation. The raw six-functor promotion must specify its actual variance and tensor base.

## 4. Keep the actual generic roof, then test its claimed projection

Source entry 396 gives weighted chains H, xi, and q-J, and their normalized blowdown. In the downstairs marked complex they satisfy

\[
 dH=q_J-X_3\xi,
\qquad
q_J=-[\top,v_+]+[\top,D]+X_D[D,c_0].
\]

In words: H is the five-triangle descended Morse comparison, xi is its four-edge broken path, and q-J contains an actual top-to-long-facet flag with coefficient one. D denotes D03 and c-zero is the labelled road vertex. These are not new cells added to obtain a chosen answer. The checker reconstructs them from the seven upstairs triangles and the source occurrence labels. [S3]

The local logarithmic evaluation respects this *entire identity*. Put w=gamma tensor z, a closed degree-two class with Xi-t(w)=1. Then

\[
 d(H\otimes w)=q_J\otimes w-X_3\xi\otimes w.
\]

In words: applying the excess evaluation returns the source identity with every occurrence coefficient unchanged. The even degree of w introduces no hidden tensor differential sign. Normalized blowdown, coefficient multiplication, and this evaluation commute. Thus the logarithmic pairing does not erase the literal generic coface or either end of the marked identity.

This does **not**, by itself, prove that q-J is a nonzero class in the required derived generic-Q target.

### A one-triangle counterexample to the erasure shortcut

Source entry 397 describes a projection that keeps the flags involving only the top face and long facets, discarding the terms over short and endpoint strata. As a literal erasure map on the marked barycentric complex of entry 396, it fails the chain equation. [S4]

Let b be the face with labels D, x-one, x-three. The mixed triangle

\[
 h=[\top,D,b]
\]

is one of the actual descended Morse triangles. In words: its last vertex lies over a short-boundary stratum, but its first two vertices are top and long-facet vertices.

Its boundary is

\[
 dh=X_D[D,b]-[\top,b]+[\top,D].
\]

In words: the occurrence weight on deleting the first vertex is exactly X-D; the last face is the proposed primitive generic edge.

For the stated erasure rule e-two,

\[
 e_2(h)=0,
\qquad e_2(dh)=[\top,D]\ne0=d\,e_2(h).
\]

In words: the triangle is discarded but one of its boundary edges survives. Therefore that rule is not a chain map on this complex. It cannot alone define the required derived Q comparison.

The complete five-triangle test gives the same result:

\[
 e_2(H)=0,
\qquad e_2(dH)=[\top,D].
\]

In words: the other four triangles do not cancel the defect. The certificate records all five triangles with their exact coefficients.

This finding is narrowly typed. It rejects the literal erasure as a chain comparison between these particular models. A genuine associated-graded construction in a different filtered resolution can exist, but its filtration, differentials, and comparison to these marked flags must be given. The calculation does not assert that every support-Yoneda class vanishes.

### What an honest ordinary relative quotient says

Instead quotient by the subcomplex of flags wholly contained in the short-facet boundary. A flag lies in that subcomplex exactly when its initial face already contains a short label. This is a genuine subcomplex, and its quotient projection commutes with d on every marked subflag.

In this quotient xi is zero, while the mixed triangles of H survive. Thus

\[
 d\overline H=\overline q_J.
\]

In words: the displayed roof is an ordinary relative boundary. The nonzero coefficient on a top/long edge does not certify a nonzero ordinary relative homology class.

The intended source invariant may instead be a framed filtered derived morphism, where a proposed null-homotopy is forbidden to change the prescribed endpoint data. Such an invariant must be calculated in that actual mapping fibre. It cannot be inferred either from retaining one coefficient or from computing ordinary relative homology alone. No such full filtered mapping-fibre calculation is asserted in this note.

## 5. What has been constructed, and the remaining precise problem

Established here:

- The log normal circle and both normal grades, with the primitive branch orientation rather than its twice-primitive antisymmetric character.
- An explicit polynomial relative-normalization/interval duality map, replacing the failed ordinary crossing identification at the normal-link level.
- The full endpoint pairing, including its midpoint-node correction and the complete road resolution.
- A chain homotopy between that pairing and the prescribed interval-trace/road-readout route, on arbitrary coefficients.
- Preservation of the exact marked Morse identity and its literal generic coface under the local transfer.
- A concrete defect in the proposed top/long-only erasure, and the different answer obtained from an honest ordinary relative quotient.

The local evaluation does not provide a global nonzero derived Q morphism automatically. The next required comparison has to retain the mixed flags and satisfy the actual chain equation

\[
 d_Q\rho_Q(H)=\rho_Q(q_J)-X_3\rho_Q(\xi).
\]

In words: its image of the comparison cell must have exactly the prescribed generic-minus-boundary differential. If the boundary image is made zero in an ordinary quotient, the formula makes the roof a boundary there. A nonzero framed obstruction must therefore be located in the correctly specified relative mapping object, with its constraints and degrees retained.

The remaining ringed promotion must also specify how this constructible log-normal pairing acts in the full occurrence/Rees/Cartier BM-Cech category. Coefficient naturality over R does not justify changing the tensor base to A or treating the nearby dual object as a coherent normalization quotient of the smooth total space.

Thus the complete requested physical comparison is still unestablished. This is a specific unresolved comparison after a proved local construction and a reproduced chain-level counterexample, not a claimed obstruction to all logarithmic or nearby-cycle constructions.

## 6. Reproduction

The bundle contains the new checker and the earlier polynomial endpoint checker it imports. Run:

```sh
python check_source_defined_branch_comparison.py --output endpoint_recheck.json
python check_logarithmic_excess.py --output logarithmic_excess_certificate.json
```

The checkers use integer arithmetic and sparse polynomial symbols. A degree bound selects input tests, not a quotient of the coefficient ring. The all-degree statements follow from the explicit formulas, the normalization exact sequence, the interval contraction, and R-linearity. The certificate records the actual assertion count. Counts are not a substitute for these proofs, and no proof-assistant verification is claimed.

The new checker verifies the characteristic lattice; interval orientation and primitive class; local pairing; all selected polynomial endpoint differentials; the explicit readout homotopy; rotation and reflection; every marked subflag under normalized blowdown; the weighted Morse identity; and both the invalid erasure and the valid relative quotient as separate controls. The earlier endpoint checker is re-executed independently. No repository files are modified.

## References and pinned source inputs

[M1] Piotr Achinger and Arthur Ogus, *Monodromy and Log Geometry*, Tunisian Journal of Mathematics 2 (2020), 455–534; arXiv:1802.02234. The relative log torus, nearby-cycle description, and local normal orientations are used. The elementary interval and pairing computations above are explicit calculations, not quotations of an unproved global comparison theorem.

[S1] `research/voevodsky/check_d03_labelled_log_odd_counit.rs`, blob `f347f6994fac975ff58e088eb74e348db9a10c5d`: labelled characteristic lattice, positive-real marking, local interval scope.

[S2] `src/ledger/20260817-400 The Log Rays Select the Normalization Branches and the Even Endpoint Class.md`, blob `306c5a299e3438bc664d2dc14fc6232702042bff`: source ray/sheet matrix and its two normalization equations. We reproduce the matrix, not the entry's entire global parity conclusion.

[S3] `research/voevodsky/check_d03_normalized_blowdown_counit.py`, blob `0fcbbf37a4f70dc0c2787ad7cb954287b9e97403`; and ledger entry 396, blob `69f913a8d079575382ac79327ef68d167802caf8`: actual weighted Morse chains and their normalized blowdown. Our checker uses the standard unaugmented differential on vertices; this does not change any of the source's displayed triangle/edge identities.

[S4] `src/ledger/20260817-397 The Descended qJ Roof Is the Canonical D03 Yoneda Generator.md`, blob `6e345710841d3340025afe626d822c160cbaa374`: the top/long-only projection claim tested above. The explicit counterexample concerns its use on the marked barycentric complex from [S3].

[S5] `src/ledger/20260814-108 Local D03 Exit Class and the Generic-Q Kernel Criterion.md`, blob `0be216e2b24d0df5b6ccbc6135e7a46bcc190a5e`: source-level generic support must not be replaced by ambient generic support.

Earlier calculation inputs: `source_defined_branch_comparison.md`, `check_source_defined_branch_comparison.py`, and `rees_physical_extension.md`, all available in this conversation. Their distinction between coefficient models and the complete physical functor is retained.
