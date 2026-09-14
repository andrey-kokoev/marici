# Branch A: the two-grade physical-collar target, conormal obstructions, and labelled enlargements

## Result and scope

This construction retains the complete relative dualizing complex, the two normalized trace diagrams, their common scalar value, the first-conormal extension, the source-relation correction, and the actual mixed quadratic products. It supplies:

* a universal dualizing/conormal target **over the specified dualizing truncation**;
* an explicit obstruction to replacing that target by the two-layer module alone;
* the complete six-by-twenty-four quadratic continuation calculation;
* a four-dimensional ordinary module for one compensated mixed continuation, and a six-dimensional labelled, reflection-closed version;
* an explicit homotopy-cofiber enlargement that cancels a specified mixed product only after changing the target;
* all 49 relative-operation generators in a labelled nested-commutator basis, and their complete rotation/reflection expansions, including decomposables;
* derived normalization-restriction and endpoint-interface tests;
* the exact obstruction and matching-space formulas for the physical endpoint and bare-Q attachments.

No map from the independently framed physical collar is asserted. The supplied task states the existence and primitivity of Branch C's bare-Q class but does not supply its product-Cartier resolution, determinant generator, or the comparison into the present duality target. It likewise does not supply the physical endpoint-to-duality maps. Those missing arrows prevent evaluating the final physical matching obstruction or declaring that its homotopy fibre is inhabited or contractible.

The scalar, conormal, dualizing, and operation comparisons below are constructed on the coefficient sources actually specified. They are not identified with the physical Pochhammer–Cousin or conductor–Morse operation.

## 1. Coefficient ring, conventions, and lines

Use

\[
 A=\mathbb Z[\beta,X_{03},X_{14},X_{25}],\qquad
 R=A[X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}]/(I_-I_+),
\]

\[
 I_-=(X_{02},X_{04},X_{24}),\qquad
 I_+=(X_{13},X_{15},X_{35}),\qquad I=I_-+I_+.
\]

The conductor is the quotient A=R/I. The ordered short labels are

\[
 (02,04,24,13,15,35).
\]

Complexes use homological degrees h; a module M[r] is in degree h=r. Equivalently it is in cohomological degree -r. The convention for extensions is

\[
 \operatorname{Ext}_R^n(M,N)=\operatorname{Hom}_{D(R)}(M,N[n]).
\]

For a degree-n cohomological map f, the Hom differential is

\[
 \delta f=d f-(-1)^n f d.
\]

The occurrence-normal line \(\mathcal L_i=A\ell_i\) has occurrence weight \(\epsilon_i\). Its dual class \(\eta_i\) has extension degree one and occurrence weight \(-\epsilon_i\). The unshifted raw class \(\beta\eta_i\otimes\ell_i\) has regulator order one. A second such extension has regulator order two and coefficient line \(\mathcal L_j\otimes\mathcal L_i\).

An exactly homogeneous presentation of \(X_i u=\beta v_i\) gives \(u\) occurrence/regulator weight \((0,0)\) and \(v_i\) weight \((\epsilon_i,-1)\). This is the kernel-line regrading \(\mathcal L_i\langle-1\rangle_\beta\). It does not divide by beta. When raw readouts are displayed, the original unshifted occurrence line and the explicit regulator order are used instead. The target constructions can be made in the beta-adically filtered derived category; this avoids falsely regarding the raw extension matrix as a beta-degree-zero matrix with unshifted kernel.

Retain separately:

* \(\Omega_- =dX_{02}\wedge dX_{04}\wedge dX_{24}\), and \(\Omega_+=dX_{13}\wedge dX_{15}\wedge dX_{35}\);
* \(\Omega_6=\Omega_-\wedge\Omega_+\);
* the polarity line \(\Pi\), odd under a sheet exchange;
* the oriented native pair \(\mathfrak o_{02,35}\), whose shift [2] is already included in the ten-state trace target;
* the interval orientation line, with the interval degree already present in its chain complex;
* the separate occurrence line \(\mathcal L_{35}\);
* the physical long-normal line and any product-Cartier determinant carried by a physical source.

No second copy of an interval or normal shift is added. Line tensor factors are suppressed in some scalar matrix displays only; their occurrence and regulator weights are checked in the module constructions.

## 2. Complete dualizing/conormal target

Let

\[
 S=A[X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}],\qquad
 \omega=R\operatorname{Hom}_S(R,S\Omega_6)[6].
\]

The complete ambient resolution has ranks

\[
 (1,9,18,15,6,1).
\]

For n>=1 a basis in degree n is a pair of nonempty exterior subsets (J_-,J_+) with total size n+1. Its first differential is the corresponding mixed product; all later differentials are the tensor differential on the two truncated Koszul resolutions. The executable reconstructs every column and its dual, not only the cohomology ranks.

Retain the actual triangle

\[
 W_{\rm sh}[3]\longrightarrow\omega
 \xrightarrow{c_\omega} A\Pi^\vee[1]
 \xrightarrow{k_\omega}W_{\rm sh}[4],
\]

where \(W_{\rm sh}=\Omega^3_{R_-/A}\oplus\Omega^3_{R_+/A}\). Its connecting components are the ordered coefficients (-1,+1). They are nonzero modulo the corresponding branch ideals. Thus the triangle is not replaced by its two cohomology modules. Its cohomology is in cohomological degrees -3 and -1.

Put z=35 and retain the actual extension

\[
 0\longrightarrow A\mathcal L_z\longrightarrow E_{\beta,z}
 \xrightarrow{p_z}A\longrightarrow0,
 \qquad X_z u=\beta v,\quad X_z v=0,
\]

with all other short actions zero. The regulator regrading described in Section 1 is understood for homogeneous maps. Let

\[
 \kappa_z=\beta\eta_z\otimes\ell_z.
\]

A coefficient target retaining both the dualizing attachment and this extension is the following **marked homotopy-pullback diagram**:

\[
\begin{matrix}
 \mathbb D_z&\longrightarrow&E_{\beta,z}\Pi^\vee[3]\\
 \downarrow p&&\downarrow p_z[3]\\
 \omega[2]&\xrightarrow{c_\omega[2]}&A\Pi^\vee[3].
\end{matrix}
\]

All four arrows have homological degree zero. They are covariant in the target; the construction is on the conductor/normalization coefficient diagram, not a new spatial support correspondence. The regulator-filtered pullback is taken with the raw beta order retained. Equivalently, regrade the kernel as above and take the homogeneous pullback with the resulting shifts recorded.

The defining fibre triangle is

\[
 A\mathcal L_z\Pi^\vee[3]\longrightarrow\mathbb D_z
 \xrightarrow{p}\omega[2]
 \xrightarrow{\kappa_z[3]c_\omega[2]}
 A\mathcal L_z\Pi^\vee[4].
\]

This specifies every connecting map. The whole omega-triangle is part of the marked target, including its primitive k-invariant. The pullback does not assert that omega splits or that its scalar cohomology determines it. It is universal over this specified truncation square, not a claim of minimality among all possible physical categories.

The other fibre sequence of the same pullback is

\[
 W_{\rm sh}[5]\longrightarrow\mathbb D_z
 \longrightarrow E_{\beta,z}\Pi^\vee[3]
 \xrightarrow{k_\omega[2]p_z[3]}W_{\rm sh}[6].
\]

Thus its two nonzero homology modules occur in homological degrees five and three: the former is the full sheet-volume module and the latter is the actual nonsplit conormal extension. This is not used to replace the diagram by those modules; the displayed connecting map and the projection to the original omega remain part of the data.


For quadratic information retain, in the same diagram category, the composable arrows

\[
 A\xrightarrow{\kappa_j}A\mathcal L_j[1]
 \xrightarrow{\kappa_i[1]}A\mathcal L_i\mathcal L_j[2],
 \qquad b_{ij}=\kappa_i[1]\kappa_j.
\]

A nonzero b_ij is retained as an arrow, not labelled a zero composite. Turning this diagram into a three-step filtered object with rank-one layers is a separate lifting problem.

The scalar projection is induced by

\[
 R\operatorname{Hom}_R(A[2],\mathbb D_z)
 \longrightarrow R\operatorname{Hom}_R(A[2],\omega[2])\simeq A.
\]

The last equivalence is conductor duality. It is a projection from the richer mapping object, not a replacement for it.

## 3. The normalized trace source is not T alone

Retain the ten-state trace target

\[
 T=(P_E\otimes K_R(X_{35}))\otimes\mathfrak o_{02,35}[2],
\]

\[
 dg=X_{03}p_{03}+X_{25}p_{25},\quad
 dh_{03}=\beta X_{03}p_{03},\quad dh_{25}=\beta X_{25}p_{25},\quad dk=X_{35}.
\]

It has ranks 2,5,3 in homological degrees 2,3,4. Its interval cycle is

\[
 \xi=h_{03}+h_{25}-\beta g,\qquad d\xi=0,\qquad d(\xi k)=-X_{35}\xi.
\]

The relative interval quotient is \(q:T\to K_R(X_{35})[3]\). Its endpoint connecting maps remain

\[
 \partial(g)=X_{03}p_{03}+X_{25}p_{25},\quad
 \partial(gk)=(X_{03}p_{03}+X_{25}p_{25})k.
\]

These are the edge endpoints W03,W25, not the independent physical endpoint modules of Branch B.

Write \(\widetilde R=R_-\oplus R_+\). The normalization-aware source is

\[
 \mathcal N(T)=\operatorname{fib}(T\to\widetilde R\otimes_RT).
\]

A point of \(\operatorname{Map}_R(A[2],\mathcal N(T))\) includes its two branch nullhomotopies. The two supplied points have

\[
 H_E^+(p_A)=H_R^+(p_A)=\xi,\qquad H_R^+(e_{35})=\xi k.
\]

The other normalized homotopy columns are zero. The relative normalization readout lands in

\[
 J_z=A[2]\oplus A\mathcal L_z[3]
\]

and has matrix

\[
 -\beta\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

This is a statement about maps from the resolved conductor source, with their branch homotopies. It is not a map out of an unframed coefficient cycle selected only by its scalar value.

The source-relation correction is retained:

\[
 \nu_E-\nu_R-\delta U=\kappa_{\rm rel},\qquad U(e_{35})=-\xi k,
\]

\[
 \kappa_{\rm rel}(m_{a,35})=X_a\xi k,\qquad a=02,04,24.
\]

The executable reconstructs these columns and the complete source equations.

### Coefficient lifts to the marked dualizing target

Let \(\mathbf u:A[2]\to\omega[2]\) be the ordered scalar conductor-unit morphism. It factors through either branch dualizing module: dualize the actual factorizations \(R\to R_\pm\to A\). Therefore \(c_\omega[2]\mathbf u\) has a specified nullhomotopy from that normalization triangle. In particular the composite with \(\kappa_z[3]\) vanishes.

Choose the positive-branch factorization already used by the normalized trace diagram; it determines a lift \(\widetilde{\mathbf u}:A[2]\to\mathbb D_z\). If \(\iota\) is the fibre inclusion, then

\[
 \widetilde\nu_E=-\beta\widetilde{\mathbf u},\qquad
 \widetilde\nu_R=-\beta\widetilde{\mathbf u}-\iota(\beta\eta_z\otimes\ell_z)
\]

give coefficient lifts with the required scalar and conormal differences. These formulas are derived morphisms represented using the original normalization triangle, the actual extension, and the conductor resolution. The choice of common origin comes from the recorded branch comparison, not a new physical normalization. This specifies the two distinguished coefficient lift classes and their common origin. It does not assert a newly constructed functor on every map out of the entire normalization-aware source, and it does not provide the missing map from the independently framed physical collar.

The fibre of the scalar comparison is modelled, after this origin choice, by

\[
 \operatorname{Map}_R(A[2],A\mathcal L_z\Pi^\vee[3]).
\]

Before imposing fine internal degrees it has pi_0 equal to \(\operatorname{Ext}^1_R(A,A\mathcal L_z\Pi^\vee)\), pi_1 equal to the corresponding Hom group, and no higher pi_n. It is not a unique lift merely because the scalar is normalized.

### A different, obstructed source problem

Replacing the whole richer target by E_beta,z[2] would require a lift of the scalar map -beta through \(E_{\beta,z}[2]\to A[2]\). Its obstruction is

\[
 \kappa_z(-\beta)=-\beta^2\eta_z\otimes\ell_z\ne0.
\]

Thus even the supplied coefficient trace cannot be interpreted as a section of that two-layer module over its common scalar. A universal repaired source for this different problem is

\[
 P_{-\beta}=A[2]\times^h_{A[2]}E_{\beta,z}[2],
\]

where the first arrow is -beta. It is represented by the rank-two extension with \(X_z u'=-\beta^2v'\), and its map to E_beta,z is \(u'\mapsto-\beta u,\ v'\mapsto v\). All its R-linearity equations are checked. Replacing a physical source by this pullback is a change of source, not an equivalence claimed by the computation.

## 4. Exact quadratic continuation, including the lines

The alternating-block conductor resolution P_A has ranks

\[
 1,6,24,92,354,1362,5240,20160,\ldots.
\]

Its differential applies the Koszul differential to the first exterior block. All differential coefficients are in I, so \(\operatorname{Hom}_R(P_A,A)\) has zero differential. The explicit augmented contraction proves exactness for arbitrary polynomial exponents. Finite implementation checks are not substituted for that proof.

Use the ordered degree-two dual basis

\[
 k_{ij}^\vee\quad(i<j\text{ in one sheet}),\qquad
 m_{ij}^\vee\quad(i,j\text{ in opposite sheets}),
\]

where \(dk_{ij}=X_i e_j-X_j e_i\) and \(dm_{ij}=X_i e_j\). In the retained Yoneda sign convention,

\[
 \eta_i\eta_j=-m_{ij}^\vee\quad\text{across sheets},\qquad
 \eta_i\eta_j=-k_{ij}^\vee\quad(i<j\text{ on one sheet}).
\]

The other same-sheet order has the opposite sign, and every square is zero.

Right composition with \(\beta\eta_{35}\) has exactly these five nonzero columns:

\[
\begin{array}{c|c}
 \eta_{02}&-\beta m_{02,35}^\vee\\
 \eta_{04}&-\beta m_{04,35}^\vee\\
 \eta_{24}&-\beta m_{24,35}^\vee\\
 \eta_{13}&-\beta k_{13,35}^\vee\\
 \eta_{15}&-\beta k_{15,35}^\vee\\
 \eta_{35}&0.
\end{array}
\]

For an actual next conormal line i, tensor its column with \(\mathcal L_i\otimes\mathcal L_{35}\). If its coefficient is also beta, every nonzero entry is multiplied by one further beta. The five target multidegrees remain independent.

Over A,

\[
 \ker o_\beta=A\eta_{35},\qquad
 \operatorname{coker}o_\beta\cong A^{19}\oplus(A/(\beta))^5.
\]

The unscaled image is a primitive rank-five summand. The beta-scaled image is not saturated at beta=0. At beta=0 the map is zero; at invertible beta it has the same rank-five image as the unscaled map. Under arbitrary base change beta->b, each transverse kernel coefficient must belong to Ann(b). For two beta-weighted adjacent extensions, replace b by b^2.

Same-direction continuation has a three-dimensional module with \(X_{35}u=\beta v\), \(X_{35}v=\beta w\), \(X_{35}w=0\). Same-sheet transverse continuation is obstructed by a nonzero exterior product. Mixed-sheet continuation is obstructed by its ordered mixed relation. In particular

\[
 b_{04,35}=-\beta^2m_{04,35}^\vee\otimes\ell_{04}\ell_{35}\ne0.
\]

A derived or A-infinity replacement with the same objects and the same two adjacent Ext classes does not erase this product. In a dg enhancement the required equation would be

\[
 \delta h=-\kappa_{04}[1]\kappa_{35},\qquad
 h\in\operatorname{Hom}^1_R(P_A,A\mathcal L_{04}\mathcal L_{35}).
\]

The right side has nonzero cohomology class, so no such h exists in that mapping complex. Higher operations cannot repair failure of this first product equation while keeping its source, target, and cohomology product unchanged.

## 5. Explicit minimal labelled enlargements

### One ordered mixed continuation

An ordinary four-dimensional A-module works after enlarging the middle layer. Use basis \(u,v,c,w\) and actions

\[
 X_{35}u=\beta(v+c),\qquad X_{04}v=\beta w,\qquad X_{04}c=-\beta w.
\]

All other short actions are zero. Then

\[
 X_{04}X_{35}u=\beta^2(w-w)=0,\qquad X_{35}X_{04}=0.
\]

The first quotient map sends u to u, v to v, and c,w to zero in E_beta,35. The prescribed 04-extension is retained on the designated v,w submodule. It is cancelled in the total composite by the additional c-path, not declared zero on that designated subquotient.

Both v and c carry \(\mathcal L_{35}\) with regulator shift -1; w carries \(\mathcal L_{04}\mathcal L_{35}\) with shift -2. This is occurrence-homogeneous. One middle direction was impossible; two suffice. This is minimal for the fixed ordered construction with its specified nonzero subquotient arrows.

### Reflection-closed labelled continuation

A shared compensator cannot have both the 35 and 04 occurrence weights. Retain six A-basis vectors

\[
 u,\ v_{35},c_{35},\ v_{04},c_{04},\ w.
\]

Their nonzero actions are

\[
\begin{aligned}
 X_{35}u&=\beta(v_{35}+c_{35}),&
 X_{04}u&=\beta(v_{04}+c_{04}),\\
 X_{04}v_{35}&=\beta w,&X_{04}c_{35}&=-\beta w,\\
 X_{35}v_{04}&=\beta w,&X_{35}c_{04}&=-\beta w.
\end{aligned}
\]

Every mixed product is zero. The reflection exchanges the two middle pairs and fixes u,w, while transporting \(\mathcal L_{35}\mathcal L_{04}\) to \(\mathcal L_{04}\mathcal L_{35}\). It squares to the identity.

For each normal weight one ordinary path is insufficient to cancel the prescribed nonzero product; a second path of that same weight is necessary. With both primitive labelled first extensions and both prescribed opposite continuations retained, four middle lines are therefore necessary and sufficient. Together with the common top and bottom, this gives rank six. This minimum is for these explicitly fixed labelled subquotient conditions, not a theorem about every possible physical enlargement.

The action preserves the actual ring R. No mixed quadratic monomial is restored. Projection onto either first extension recovers E_beta,35 or E_beta,04. The ordered determinant sign is separate from the even tensor interchange of the two coefficient lines.

### A universal derived alternative

For \(b:A\to K[2]\), \(K=A\mathcal L_{04}\mathcal L_{35}\), representing the nonzero mixed product, form

\[
 C_b=\operatorname{Cone}(b),\qquad K[2]\xrightarrow{j}C_b.
\]

On a free resolution the homological cone differential is

\[
 d_{C_b}(k,p)=(d_Kk+bp,-d_Pp).
\]

The canonical degree-plus-one homotopy \(H(p)=(0,p)\) satisfies

\[
 dH+Hd=jb.
\]

Thus jb, not b in its original target, becomes nullhomotopic. This attaches one shifted conductor object, which means its whole free resolution over R, not one free R-generator. The checker verifies the explicit cone and homotopy on all retained resolution degrees. Its all-degree equation follows from the displayed formula. Reflection requires the correspondingly labelled cone for the reflected product or their paired diagram.

## 6. Relationship to Branch B's relative operation algebra

Use the coefficient dictionary

\[
 (\xi_1,\xi_2,\xi_3)=(\eta_{02},\eta_{04},\eta_{24}),\qquad
 (\upsilon_1,\upsilon_2,\upsilon_3)=(\eta_{13},\eta_{15},\eta_{35}).
\]

The algebra is

\[
 \mathcal E=\Lambda_A(\xi_1,\xi_2,\xi_3)*_A
 \Lambda_A(\upsilon_1,\upsilon_2,\upsilon_3).
\]

For opposite-sheet labels,

\[
 r_{ij}=\eta_i\eta_j+\eta_j\eta_i.
\]

The ordered obstruction \(\eta_{04}\eta_{35}\) is **not** in the relative Hopf kernel: its exterior-quotient image is the nonzero element \(\eta_{04}\wedge\eta_{35}\). Instead,

\[
 b_{04,35}+b_{35,04}
 =\beta^2r_{04,35}\otimes\ell_{04}\ell_{35},
\]

after the ordinary coefficient-line interchange. This retains the two orders integrally; no division by two is used.

A dg representative \(\operatorname{End}_R(P_A)\) acts by precomposition on \(R\operatorname{Hom}_R(A,X)\) for any target X. Its cohomology gives the canonical right Yoneda action; \(R\operatorname{Hom}_R(X,A)\) has the corresponding left action. Restriction to the supplied relative Hopf algebra gives an operation action on these derived mapping objects. It is not an automatically defined action of that Hopf algebra on the underlying ordinary module E_beta,35. A chain-level strict model of the homology-algebra action requires a model choice; the derived composition action is already typed and coherent.

The new finite action calculation gives

\[
 \operatorname{rank}\{r_{ij}\eta_{35}\}_{i\in -,j\in +}=9.
\]

Every quadratic relative generator acts nontrivially and independently on the first-conormal class by Yoneda composition. The resulting operations are in extension degree three. They are not values of the degree-one readout itself.

For the forty higher indecomposable generators, the right-action ranks on eta35 are respectively 18,15,6,1 in output degrees 4,5,6,7. The executable checks every one. Those are available higher products; a physical diagram need not require each to vanish.

The degree-two continuation obstruction is not, by itself, an obstruction to relative-operation equivariance. For a generator g of operation degree d, equivariance of a degree-one conormal arrow requires

\[
 \delta H_g=\rho_1(g)\kappa-(-1)^d\kappa\rho_0(g),
 \qquad |H_g|=d.
\]

Its obstruction is in degree d+1. In particular the first relative generators give degree-three equivariance equations, not the degree-two product equation. A separate centrality control has rank six:

\[
 \operatorname{rank}\{[r_{ij},\eta_{35}]\}=6.
\]

The three generators r_i,35 commute with eta35 but still act nontrivially. Thus centrality, annihilation, and equivariance are different tests.

Branch B's endpoint identities are checked in the actual free-product algebra:

\[
 r_{ij}\eta_i=\eta_i\eta_j\eta_i\ne0,\qquad
 r_{ij}\eta_j=\eta_j\eta_i\eta_j\ne0.
\]

A scalar or exterior-quotient model cannot preserve these actions. No coefficient Ext product is identified with a physical Whitehead product.

## 7. All labelled symmetry formulas

Let \(r(v)=v+1\pmod6\) and \(f(v)=3-v\pmod6\). On the ordered short labels:

\[
 r:(02,04,24,13,15,35)\mapsto(13,15,35,24,02,04),
\]

\[
 f:(02,04,24,13,15,35)\mapsto(13,35,15,02,24,04).
\]

Both fix beta. Their long-coordinate actions are induced by the same vertex permutation. The order-three rotation used in some earlier calculations is r^2, not a new action.

For every label permutation sigma,

\[
 \sigma(X_i)=X_{\sigma i},\quad
 \sigma(\eta_i)=\eta_{\sigma i},\quad
 \sigma(\ell_i)=\ell_{\sigma i},\quad
 \sigma(ab)=\sigma(a)\sigma(b).
\]

The order of an Ext product is not reversed by reflection. The ordered determinant, rather than the associative product, receives its exterior permutation sign.

A complete labelled primitive basis is indexed by nonempty subsets J_- and J_+ of the two triples. Start with \([\eta_{\min J_-},\eta_{\min J_+}]\), apply adjoints by the remaining negative labels in increasing order, then by the remaining positive labels in increasing order. Here

\[
 [a,b]=ab-(-1)^{|a||b|}ba.
\]

This gives 9,18,15,6,1 generators in degrees 2 through 6. Their coproducts are checked to be primitive. Using Branch B's established free-generator degrees, the unit-pivot bases through degree six identify these as a free primitive-generator basis. Multiplicativity then determines their action in all degrees.

Transport is computed by substituting every label in these actual words and reducing only within same-sheet exterior blocks. The certificate contains both generator and decomposable components of every rotation/reflection image. For example,

\[
 r(g_{02,04;13,15})
 =g_{02,24;13,15}+[r_{02,15},r_{24,13}],
\]

\[
 f(g_{02,04;13,15})
 =-g_{02,24;13,35}-[r_{02,13},r_{24,35}].
\]

The commutators in these two formulas are products of quadratic relative generators. Omitting them changes the operation.

The checker verifies r^6=1, f^2=1 and frf=r^-1 on all 49 generators, and reconstructs every expansion integrally. Since the algebra is free on these generators, these are the group relations on every product.

The determinant transport is:

| Line | r | f |
|---|---|---|
| \(\Omega_-\) | \(+\Omega_+\) | \(-\Omega_+\) |
| \(\Omega_+\) | \(+\Omega_-\) | \(-\Omega_-\) |
| \(\Omega_6\) | -1 | -1 |
| polarity \(\Pi\) | -1 | -1 |
| ordered pair \(\mathfrak o_{02,35}\) to its sorted image | -1 | -1 |

The interval and physical long-normal lines retain the supplied endpoint ordering under each transported interval. They are not assigned extra scalar signs to force a desired residue. Under f the 35 occurrence complex becomes the 04 occurrence complex, and the W25 endpoint becomes its W14-labelled counterpart. The original physical endpoint arrows are additional data, not these coefficient endpoint labels.

In particular \(f(E_{\beta,35})=E_{\beta,04}\) and f^2 is the identity. The nonzero mixed composition does not obstruct that transport. An internal reflection on a two-axis continuation is supplied by the six-state enlarged module of Section 5.

## 8. Endpoint restrictions and their higher term

The ordinary restrictions to the two normalization sheets are computable. They are not the physical endpoint functors.

On the positive sheet, the extension remains E_beta,35 and is nonsplit. On the negative sheet,

\[
 R_-\otimes_RE_{\beta,35}
 =Au\oplus(A/(\beta))v.
\]

The latter does not mean the derived restriction of the extension is trivial. The long exact Tor sequence contains

\[
 \operatorname{Tor}_1^R(R_-,A)\longrightarrow A\mathcal L_{35},
 \qquad e_{35}\longmapsto\beta v,
\]

with the other two positive normal columns zero. On the positive-sheet restriction the corresponding Tor boundary on the three negative normals is zero.

At invertible beta the underived negative-sheet restriction loses v; its Tor comparison is essential. At beta=0 the original extension splits and derived restriction preserves that split extension. Neither statement splits omega.

A physical endpoint source \(P_\pm^{\rm phys}\) needs a specified morphism

\[
 P_\pm^{\rm phys}\longrightarrow
 \nu_\pm^!\mathbb D_z,
 \qquad \nu_\pm^!\mathbb D_z=R\operatorname{Hom}_R(R_\pm,\mathbb D_z),
\]

or a different bivariant correspondence explicitly identifying its support. The existing dualizing and occurrence lines remain in this target. No regular codimension shift is inserted for the singular normalization-sheet immersion.

The coefficient relative tangential map has zero endpoint restriction, so its composite cannot substitute for an independently specified nonzero endpoint connector. The Tor boundary above and Branch B's nonzero relative-operation actions explain why neither the underived restriction nor a scalar augmentation is an adequate endpoint replacement. The physical endpoint maps themselves are not contained in the attached data, so their restrictions cannot be numerically evaluated here.

## 9. Bare-Q compatibility and the physical matching problem

Retain Branch C's primitive bare-Q class as

\[
 q_C:\mathsf S_Q\longrightarrow Q.
\]

The symbol \(\mathsf S_Q\) denotes its actual product-Cartier resolved source, including its supplied degree-four placement, normal product generator, and determinant line. This notation does not replace that source by A[4] and does not tensor Q with the old unevaluated auxiliary factor.

The task states primitivity, contractibility of its coefficient-level lift space, and null endpoint composites. It does not give the differential of \(\mathsf S_Q\), its determinant generator, or an arrow from Q to the present duality target. Consequently no scalar, conormal, or dualizing image follows solely from that statement.

For a specified comparison \(a_Q:Q\to\omega[2]\), the exact obstruction to lifting its composition through \(\mathbb D_z\) is

\[
 o_Q=\kappa_z[3]c_\omega[2]a_Qq_C
 \in\operatorname{Hom}_{D(R)}
 (\mathsf S_Q,A\mathcal L_z\Pi^\vee[4]).
\]

This formula retains the entire product-Cartier source and determinant degree. If o_Q vanishes, a choice of its nullhomotopy is required. The choices form a torsor for

\[
 \operatorname{Hom}_{D(R)}
 (\mathsf S_Q,A\mathcal L_z\Pi^\vee[3]),
\]

with higher automorphisms given by the corresponding negatively shifted mapping groups. A scalar coefficient +1 or -beta does not evaluate o_Q.

The operation compatibility test is separate. If g acts on the endpoints and acts by augmentation on Q, an intertwiner a must satisfy a rho_endpoint(g)=0 in the target homotopy category, with specified nullhomotopies at chain level. Nonzero endpoint words such as r_ij eta_i cannot be removed by declaring a scalar generic coefficient primitive. No action on the entire bare-Q complex is inferred from its coefficient-line action.

### The pullback leg with every restriction typed

For a proposed physical collar P carrying its endpoint/normal/Čech/product-Cartier boundary diagram \(\partial P\), and a specified scalar-duality map \(a_0:P\to\omega[2]\), define

\[
 \mathscr L(P;a_0)
 =\operatorname{hofib}_{a_0}
 \bigl(\operatorname{Map}_R(P,\mathbb D_z)
 \to\operatorname{Map}_R(P,\omega[2])\bigr).
\]

Each boundary arrow \(j_\lambda:P_\lambda\to P\) induces restriction by precomposition. With its given coefficient actions, support labels, and determinant lines retained, the physical matching space is

\[
 \mathscr L_{\rm phys}
 =\operatorname{hofib}_{\mathbf b}
 \left(
 \mathscr L(P;a_0)
 \longrightarrow
 \operatorname*{holim}_{\lambda\in\partial P}
 \mathscr L(P_\lambda;a_0j_\lambda)
 \right).
\]

Here the boundary point \(\mathbf b\) consists of Branch B's endpoint-operation maps and their normal/Čech comparisons, Branch C's q_C and its endpoint homotopies, and the normalized trace diagrams. All displayed restriction arrows have degree zero and are contravariant in their source. The target maps are covariant; the dualizing construction has the variance stated in its RHom definition. Support and determinant compatibility are part of \(\partial P\), not extra equalities of scalar signatures.

This is an explicit obstruction-theoretic definition of the required leg. It is not an instantiated physical pullback until P, its boundary inclusions, a_Q, and the endpoint upper-shriek comparisons are supplied. The current normalized coefficient source, T, its interval quotient, and the independent physical collar are not identified.

## 10. Higher obstructions and uniqueness

The conormal endomorphism algebra has Hilbert series

\[
 \sum_{n\ge0}\operatorname{rank}_A\operatorname{Ext}_R^n(A,A)t^n
 =\frac{(1+t)^3}{2-(1+t)^3}.
\]

Its initial ranks are

\[
 1,6,24,92,354,1362,5240,20160.
\]

The checker verifies the resolution through degree four and the rank recurrence through degree seven. The all-degree series follows from alternating exterior blocks; it is not extrapolated from the finite numbers.

For a filtered extension with fixed graded pieces A_j, a dg upper-triangular twisting matrix q has degree-one entries and satisfies

\[
 \delta q_{ij}+\sum_{i<k<j}q_{kj}q_{ik}=0.
\]

Once lower entries are chosen, the right-hand sum is a closed degree-two cochain. Its class in \(\operatorname{Ext}_R^2(A_i,A_j)\) is the next existence obstruction. If it vanishes, choices modulo the fixed lower data form the corresponding Ext^1 torsor; automorphisms lie in Ext^0. Longer compatibility and operation equations retain the actual higher mapping groups. The forty higher primitive relative generators do not, by freeness alone, require forty additional vanishing equations.

For the fixed 35 first extension with identified ends, ungraded automorphisms are

\[
 u\mapsto u+c v,\qquad v\mapsto v.
\]

Their group is additive \(\operatorname{Hom}_R(A,A\mathcal L_{35})\) with the regulator regrading retained. With every occurrence and regulator degree fixed as in Section 1, no coefficient of the needed negative short weight exists in A; hence no nonzero such graded shear is allowed. The chosen fine-graded extension component is contractible. This does not make the physical-collar lift space contractible.

For a prescribed quadratic product b, the space of its nullhomotopies is empty if [b] is nonzero. When [b]=0 and the adjacent maps are fixed, its components are an Ext^1 torsor and its automorphisms are Ext^0, with appropriate line factors. For the fixed repeated-35 fine grading, these indeterminacies are eliminated by the absence of the required weights; the explicit three-layer repeated-axis module realizes the unique such graded continuation. The compensated enlargements admit further choices not fixed by the original problem; the matrices in Section 5 are constructions, not a uniqueness claim about them.

The full physical matching space cannot yet be classified as empty or contractible. Branch C's contractible coefficient lift space concerns only its own already-fixed target problem. A homotopy pullback with the additional endpoint, dualizing, normal, and operation constraints need not retain that property.

## 11. Regulator summary

| Condition | First extension | Ordered mixed continuation | Complete omega |
|---|---|---|---|
| Polynomial beta | nonsplit; raw order one | nonzero order-two obstruction | nonsplit attachment retained |
| beta=0 | splits | the beta-weighted product is zero | does not split for that reason; primitive (-1,+1) remains |
| beta invertible | first labelled axis thickening after frame change | still nonzero, with beta^2 a unit | same nonsplit normalization attachment |

At a nonreduced regulator specialization such as beta^2=0, two beta-weighted successive extensions can satisfy the mixed relation even when the original polynomial extension cannot. This is base change of the obstruction coefficient, not proof of a polynomial-family lift.

The higher compensated modules and cone constructions are polynomial in beta and require no regulator inverse. Their reflections act between labelled normal lines and square to one.

## 12. Verification and remaining physical inputs

The standalone checker uses only the Python standard library. It reconstructs:

* the ten-state target, both trace maps, all normalized branch homotopies, and the relation-only correction;
* the conductor resolution and the finite contraction controls;
* all 36 ordered quadratic products and all 216 triple products, with their actual source-resolution coordinates;
* the fifty-summand ambient dualizing complex and its primitive attaching components;
* the scalar-source pullback module, ordered and reflection-closed compensating modules, their actual R-actions, occurrence/regulator weights, and endpoint Tor rows;
* the obstruction cofiber and its canonical homotopy;
* all 49 primitive relative generators, their coproducts, their full rotation/reflection decompositions, and the algebra action tests;
* normal, branch determinant, polarity, and ordered-pair signs.

The certificate contains every finite matrix or polynomial formula used for the new rank and independence claims. The universal pullback and mapping-space formulas are categorical constructions; the certificate explicitly marks the physical endpoint and Q arrows as uninstantiated. No finite check is claimed for missing physical maps.

Run:

```sh
python branch_a_physical_collar_conormal_checker.py --output branch_a_physical_collar_conormal_certificate.json
```

The run completed 18,533 counted exact checks. A clean-directory replay, with a different Python hash seed and only the checker present, reproduced the certificate byte-for-byte.

The unresolved physical inputs are now exact types of maps, rather than scalar normalization choices:

1. the collar-to-normalized-trace comparison preserving the recorded branch homotopies and relation columns;
2. the endpoint maps into the appropriate sheet upper-shriek targets, with their operation actions;
3. Branch C's product-Cartier source, its determinant generator, and the comparison a_Q into omega[2];
4. a physical decision between retaining a nonzero quadratic obstruction as part of the diagram, the labelled larger-middle module, or the explicitly changed cofiber target.

None of these is produced merely by assigning a unit to the common scalar readout.

## Sources and provenance

User task: `Pasted text(2).txt`, “Branch A task: two-grade duality and obstructed conormal-extension leg of the physical-collar pullback”. The specified Branch A source files are retained as input, not silently replaced:

* `branch_a_full_normalization_duality_and_two_grade_trace_proof.md`;
* `branch_a_full_conductor_dualizing_residue_proof.md`;
* `branch_a_tangential_duality_scalar_pairing_proof.md`;
* `branch_a_conormal_trace_extension_and_mixed_obstruction_proof.md`.

The exact local source and sign conventions are reconstructed from the last of their accompanying checkers. The new calculation additionally uses the Branch B task sheet's established free-product and relative-Hopf-algebra statements; no claim of a physical loop-space realization is imported.

Standard categorical conventions: Stacks Project 06XP (Ext and Yoneda composition, including the obstruction to splicing into a three-step filtration), 0A8H (Hom-complex signs), 0A74 (closed-immersion right adjoints), 014D (cones and connecting maps), 0A7A (duality). The fibre-product cohomology context is W. Frank Moore, “Cohomology of Fiber Products of Local Rings”, arXiv:0704.3631. The all-degree integral resolution used here has its direct branchwise contraction argument; a field-only statement is not used as a substitute for that argument.
