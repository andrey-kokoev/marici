# Branch A: Milnor totalization, the complete conductor costalk, and its counit

Date: 2026-09-07.

## Result and scope

In the established occurrence-map degree zero and regulator-normal grade three, the complete affine conductor-costalk calculation gives

\[
\operatorname{Hom}_{D(R)}(A[2],N^{\mathrm{ext}})\cong\mathbb Z^{34}.
\]

The canonical counit has a rank-three image and a rank-thirty-one kernel. The entire previously surviving normalization-extension lattice is precisely that kernel. The three additional classes have nonzero images on the actual conductor unit, together with the source-generator homotopies necessary for them to be supported on the conductor.

The actual normalization-conductor structure-module totalization is quasi-isomorphic to \(R\). In the preceding degree-three placement its mapping group into the framed target is zero. Including the lower conductor and its diagonal comparison therefore does not eliminate any of the thirty-one remaining obstructions. This assertion concerns the structure-module totalization, not an arbitrary enriched physical kernel.

The exact sequence of tested lattices is

\[
0\longrightarrow\mathbb Z^{31}
\longrightarrow\mathbb Z^{34}
\xrightarrow{\epsilon_*}\mathbb Z^3
\longrightarrow0.
\]

With the established cellular/source reflection and transport through the occurrence labels \(35,15,13\), the corresponding invariant sequence is

\[
0\longrightarrow\mathbb Z^{10}
\longrightarrow\mathbb Z^{11}
\longrightarrow\mathbb Z
\longrightarrow0.
\]

Both sequences are saturated over the integers. Every invariant derived class has a strictly invariant cochain representative in this calculation; an integral index obstruction is not hidden in that assertion.

These are ranks of graded lattices of morphisms, not a finite count of classes. They do not describe every degree of the costalk. No physical conductor–Morse class is assigned.

## 1. Coefficients and the full target frame

Use

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]
/(X_aX_b:a\in\{02,04,24\},\ b\in\{13,15,35\}).
\]

Let

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad
I=I_-\oplus I_+,\qquad A=R/I.
\]

The target \(C_\beta\) contains all 430 states \([F,H,\varepsilon]\). Its differential has radial coefficients \(X_d\), native normal coefficients \(\beta X_d\), and the separate occurrence-normal coefficient \(X_{35}\). Its homological degree is \(3-|F|+|H|+\varepsilon\). The native and occurrence \(35\) factors remain distinct.

The actual endpoint set contains the 32 states over

\[
v_-=\{02,04,24\},\qquad v_+=\{13,15,35\}.
\]

The short-boundary subcomplex contains 416 states, and its quotient is the complete fourteen-state \(Q\)-complex. Write \(v\) for graded endpoint projection and \(q\) for this actual chain quotient. Define

\[
N^{\mathrm{ext}}_n
=\{c\in C_{\beta,n}:q(c)=0,\ v(c)=0,\ v(dc)=0\}.
\]

The incoming-endpoint equation is required: projection onto all endpoint states is not itself a chain map. The displayed conditions define an \(R\)-linear subcomplex. The coherent fibre of \(C_\beta\to C_\beta/N^{\mathrm{ext}}\) is equivalent to this subcomplex. The checker reconstructs its graded bases using the actual endpoint equations.

For a source generator of occurrence weight \(w\), an entry into \([F,H,\varepsilon]\) has its occurrence exponent forced to be

\[
w+\sum_{d\in F}\epsilon_d-\sum_{d\in H}\epsilon_d-\varepsilon\epsilon_{35}.
\]

Its regulator coefficient exponent is \(3-|H|\). Negative exponents or mixed-sheet monomials are excluded. Thus the integer matrices below describe entire homogeneous components, not a bounded polynomial search.

The regulator family is an integral coefficient model. Interpreting it through the exponential normal graph requires the separately stated characteristic-zero formal coefficients. The source's fixed-nonzero-regulator purity theorem has not thereby been extended to regulator zero.

## 2. The complete normalization-conductor totalization

Put

\[
R_-=R/I_+,\qquad R_+=R/I_-,\qquad\widetilde R=R_-\oplus R_+.
\]

The actual Milnor square gives the exact sequence

\[
0\longrightarrow R
\xrightarrow{j}\widetilde R\oplus A
\xrightarrow{t}A\oplus A
\longrightarrow0,
\]

where

\[
j(r)=(r_-,r_+,\bar r),\qquad
 t(b_-,b_+,a)=(\bar b_- -a,\bar b_+ -a).
\]

All maps are \(R\)-linear. In the conductor-constant monomial component the matrices are

\[
j=\begin{pmatrix}1\\1\\1\end{pmatrix},\qquad
 t=\begin{pmatrix}1&0&-1\\0&1&-1\end{pmatrix}.
\]

The kernel of \(t\) is exactly the displayed diagonal and its quotient map is surjective, with a unit minor. For a nonconstant short monomial on either sheet, the sequence reduces to an identity between its occurrence in \(R\) and its occurrence in that sheet. A mixed-sheet monomial is zero everywhere. These cases exhaust arbitrary exponents. The checker records all 64 short-support types; their classifications are one constant type, seven nonempty types on each sheet, and 49 zero mixed types.

Consequently the two-term homotopy-fibre model

\[
\mathcal K_\nu=[\widetilde R\oplus A\xrightarrow{t}A\oplus A]
\]

in homological degrees zero and minus one has a canonical quasi-isomorphism \(R\to\mathcal K_\nu\). No strict \(R\)-linear splitting of the normalization quotient is asserted or used.

The full target calculation in the chosen weights gives

\[
H_3(N^{\mathrm{ext}})_{(0;3)}=0.
\]

It follows that

\[
\operatorname{Hom}_{D(R)}(\mathcal K_\nu[3],N^{\mathrm{ext}})_{(0;3)}=0.
\]

Thus this exact totalization is not a new same-degree extension mechanism. Tensoring it with additional source-defined dualizing, normal, or spatial objects changes the input and requires its own construction; it is not included in this vanishing statement.

## 3. Construct the affine extraordinary restriction

Let

\[
i:\operatorname{Spec}A\hookrightarrow\operatorname{Spec}R.
\]

The affine right adjoint to \(i_*\) is

\[
i^!N^{\mathrm{ext}}=R\operatorname{Hom}_R(A,N^{\mathrm{ext}}).
\]

Its counit is induced by \(R\to A\). This supplies a source-defined supported construction without asserting that the singular conductor immersion is a regular immersion or replacing its resolution by one conormal line.

The previously checked conductor-ideal resolution begins with ranks \(6,24,92\). Augmenting it gives a resolution \(P_A\to A\) with ranks

\[
1,6,24,92
\]

in degrees zero through three. The first map is

\[
de_a=X_ap.
\]

The next six relations are the same-sheet Koszul relations; the remaining eighteen are ordered mixed-sheet annihilations. The following 92 columns give the relations between these relations. The checker reconstructs these differentials and verifies their degrees, weights, and square-zero equations.

Exactness of these terms is the fibre-product resolution used in the preceding audit. A branchwise normal-form proof applies to arbitrary polynomial coefficients: the augmentation ideal on either sheet has its ordinary three-variable Koszul resolution, while its annihilator consists of the opposite augmentation ideal. Resolving these alternating annihilator modules yields the alternating exterior-block resolution. Appending later terms does not change the present calculation: after shifting \(P_A\) by two, degree-zero maps can only have values on its first three terms, and their last equations come from the 92 columns in source degree five.

A cochain map \(F:P_A[2]\to N^{\mathrm{ext}}\) consists of

\[
U=F(p)\in N^{\mathrm{ext}}_2,\qquad
Y_a=F(e_a)\in N^{\mathrm{ext}}_3,\qquad
V_r=F(r)\in N^{\mathrm{ext}}_4,
\]

satisfying

\[
dU=0,\qquad dY_a=X_aU,\qquad dV_r=F(dr),\qquad F(ds)=0.
\]

The coefficient conditions on \(Y_a\) express derived support: \(U\) need not be annihilated by \(I\) as a chain, but every generator of \(I\) annihilates it through a specified homotopy, with all source relations retained.

The complete matrix calculation gives:

| Coefficient requirement | Degree-zero cochain coefficients | Closed maps | Independent map boundaries | Morphism lattice rank |
| --- | ---: | ---: | ---: | ---: |
| Target \(N^{\mathrm{ext}}\) | 718 | 108 | 74 | 34 |
| Target constrained to \(IC_\beta\) | 664 | 54 | 0 | 54 |

In each case the equation matrix has rank 610. All homotopy-image factors in the first row are units. There are no degree-two map homotopies in these weights, and the degree-one Hom differential is injective. These statements specify the complete homotopy quotient in this component.

The second row is a control with a different target. Its rank 54 is not the earlier rank 40: the earlier source was \(I[3]\); the present source is \(A[2]\), including its unit and all its annihilator homotopies.

## 4. The counit separates obstruction classes from supported primary classes

On the chosen resolution, the canonical counit evaluates the unit column:

\[
\epsilon_*[F]=[F(p)].
\]

The codomain in this component is

\[
H_2(N^{\mathrm{ext}})_{(0;3)}\cong\mathbb Z^5.
\]

The checker finds 46 cycle coordinates and 41 independent boundaries, all with unit integral invariant factors. The same 41 columns exhaust the degree-three target group, verifying \(H_3=0\).

The complete counit matrix has size \(5\times34\). Its rank is three and its nonzero invariant factors are \(1,1,1\). Thus its image is a primitive \(\mathbb Z^3\) inside the target \(\mathbb Z^5\).

Now compare the two source sequences

\[
0\to I\to R\to A\to0,
\qquad
0\to I\to\widetilde R\to A\oplus A\to0.
\]

The natural map between them is identity on \(I\), normalization on \(R\), and the diagonal on \(A\). Pullback of the second sequence along that diagonal is the first sequence. Their connecting maps therefore satisfy

\[
\partial_R=\partial_\nu\circ\Delta,
\qquad
\Delta(a)=(a,a).
\]

There is no division by two or independent choice of a sheet section. On a resolved map from \(I[3]\), composition with \(\partial_R\) places its generator and relation images in the corresponding columns of \(P_A[2]\) and has zero unit image.

The matrix from the original forty ideal-map coordinates to the 34 costalk coordinates has rank 31, all invariant factors one, and exactly the same rank-nine kernel as the preceding extension audit. Its composition with the counit is zero. Its image is saturated and has the full rank of the counit's kernel. Therefore

\[
\ker\epsilon_*=\operatorname{im}\partial_R^*\cong\mathbb Z^{31}.
\]

The mapping sequence for \(0\to I\to R\to A\to0\), together with \(H_3(N^{\mathrm{ext}})_{(0;3)}=0\), identifies this kernel with the entire relaxed ideal-map group in these weights. The previous rank-31 calculation had only asserted a surviving image; the present complete costalk calculation proves that it exhausts this kernel.

Combining the two upper-conductor components with their actual diagonal thus does not cancel any further obstruction. The three additional costalk directions are instead classes with nonzero supported primary values on the lower conductor unit.

## 5. An explicit twelve-term supported map

Set

\[
\begin{aligned}
L_{13}={}&\beta[\{04,13\},\{04,13\},0]\
&-[\{04,13,14\},\{04,13,14\},0]\
&-[\{03,04,13\},\{03,04,13\},0].
\end{aligned}
\]

Take the positive-sheet part of its complete boundary:

\[
\begin{aligned}
U_{13}={}&\beta^2X_{13}[\{04,13\},\{04\},0]\
&+\beta X_{13}[\{04,13,14\},\{04,14\},0]\
&-\beta X_{13}[\{03,04,13\},\{03,04\},0].
\end{aligned}
\]

The other three terms of \(dL_{13}\) have negative-sheet coefficients. Direct calculation gives \(dU_{13}=0\). Hence the following map satisfies every source equation:

\[
\mathcal G_{13}(p)=U_{13},
\]

\[
\mathcal G_{13}(e_a)=
\begin{cases}
X_aL_{13},&a\in\{13,15,35\},\\
0,&a\in\{02,04,24\},
\end{cases}
\]

with zero values on all 24 relation generators and every later source term.

For a positive-sheet generator, multiplication by \(X_a\) kills the negative-sheet terms of \(dL_{13}\), giving \(d(X_aL_{13})=X_aU_{13}\). A negative-sheet generator annihilates \(U_{13}\) directly. The same-sheet relations cancel by commutativity, and mixed products vanish. The 92 next equations hold because all relation images are zero.

There are twelve nonzero polynomial terms in the complete map: three in the unit column and nine across its three positive generator columns. Every target term and its boundary satisfy the full endpoint and \(Q\) frame.

The integral target-homology coordinates of \(U_{13}\) are

\[
(-1,0,0,0,0)
\]

in the exported basis. An integral class detector therefore evaluates it to one and annihilates all target boundaries. Both \([U_{13}]\) and \([\mathcal G_{13}]\) are primitive and nonzero in their indicated lattices.

This construction retains \(X_{13}\), every displayed power of \(\beta\), and every support label. It does not turn a conductor factor into a scalar residue. It is a derived supported map, not a strict map from the quotient module obtained by ignoring its resolution.

## 6. The actual symmetry has one additional primary direction

Use the inherited source-generator action and the cellular action

\[
r(v)=v+2\pmod6,\qquad s(v)=2-v\pmod6,
\]

with the supplied cellular top signs and normal-mark permutation signs. The lower conductor unit is fixed. Rotation transports the occurrence correction through \(35,15,13\); it is not imposed within one fixed corrected complex.

The action on the rank-34 costalk quotient has an invariant lattice of rank eleven. The rank-31 kernel has invariant rank ten. In a computed basis of the rank-three primary quotient, reflection is

\[
\begin{pmatrix}
0&-1&0\\
-1&0&0\\
0&0&-1
\end{pmatrix}.
\]

Its invariant lattice has rank one. The induced map from the rank-eleven invariant costalk lattice onto this line has invariant factor one, giving

\[
0\to\mathbb Z^{10}\to\mathbb Z^{11}\to\mathbb Z\to0.
\]

The closed-cochain invariant space has rank 42. Its projection onto the eleven invariant derived classes is surjective with eleven unit invariant factors. The checker constructs a strictly invariant representative of each class and verifies its complete rotated source equations in all three occurrence complexes.

A direct example is

\[
\mathcal G_{13}+s\mathcal G_{13}.
\]

It has 24 polynomial terms, including six in its unit column, and maps to the primitive generator of the invariant primary line. This is not a scalar normalization imposed after taking invariants: it is the sum of the computed map and its source-and-target reflection. No averaging denominator is used.

The preceding ten invariant obstruction directions remain independent. In particular, the two relation-only directions remain present. Fixing the new primitive primary image still leaves a rank-ten affine lattice of invariant supported lifts in this model.

## 7. The previously obstructed transgression is not automatically admitted

Retain the actual labelled lift

\[
\widetilde\varphi_Q=\beta T-h_{03}-h_{14}-h_{25},\qquad
\chi_\beta=d\widetilde\varphi_Q.
\]

Its grade-three representative is \(\beta^2\chi_\beta\). The target-homology quotient by the counit's image is free of rank two. The computed class of \(\beta^2\chi_\beta\) has coordinates

\[
(-1,-1)
\]

in that quotient.

It therefore does not belong to the image of this conductor counit in the tested grading. The new supported-primary classes do not erase the earlier endpoint/\(Q\) transgression by a change of notation. Their actual unit columns pass a different, explicitly calculated support-lifting test.

## 8. Verification and remaining physical identification

The checker is standalone, uses only the Python standard library, and contains its inherited algebraic routines. It does not read companion certificates, import a private package, or access the network. It reconstructs the source resolutions, the full target differential, the endpoint frame equations, the prior forty maps and nine boundaries, and all new costalk matrices.

The new computation verifies 349,317 exact checks and replays 337,571 inherited checks. A fresh isolated execution containing only the checker reproduced the certificate byte for byte. Its mathematical content hash is

```text
e9052263024375d892f814b8935780bdc0fa52c9d5b99b7e2dd892eceb60ec00
```

The costalk is the genuine affine right-adjoint construction for this coefficient immersion. No regular-immersion purity identification, geometric \(\beta=0\) theorem, or comparison with the physical conductor–Morse source is inferred from it.

The explicit remaining comparison is between the independently marked spatial Gysin kernel and the constructed conductor costalk/counit. An actual physical source map would need to determine its primary image and its position in the residual kernel; the scalar conductor symbol and an equality of residues do not determine those data.

## References and reproducibility

Repository inputs are pinned to commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61` of `andrey-kokoev/marici`:

- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the two normalization sheets, doubled upper conductor, exact sequences, and polarity convention.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: the complete signed radial and native-normal differential and cellular transport.
- `research/voevodsky/check_d03_formal_support_purity.rs`: the fixed-nonzero-regulator scope of the physical normal-graph comparison.

Standard categorical facts used here are Stacks Project tags `08KG` and `0D2G` for fibre-product modules, `014D` for cone/triangle constructions, `0A8H` for the Hom differential, `064B` for maps computed by projective source resolutions, and `0A74` for closed-immersion extraordinary restriction and its counit.

Run:

```bash
python branch_a_milnor_totalization_conductor_costalk_checker.py \
  --output branch_a_milnor_totalization_conductor_costalk_certificate.json
```
