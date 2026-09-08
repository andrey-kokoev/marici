# Branch A: W03 branchwise Čech support and reciprocal-trace descent

## Result

The two reciprocal trace classes admit explicit, independent lifts through the local-cohomology counit for the coefficient support

\[
Z=V(X_{02},X_{35}).
\]

The complete homogeneous supported Hom calculation has dimensions \((9,66,151)\), differential ranks \((9,55)\), and rank-two cohomology. Its two displayed generators, together with the nine homotopy boundaries, form an integral cycle basis with determinant \(-1\).

This construction does not use the literal tangential Laurent target of Entry 97. That target cannot be base-changed nontrivially to the current normalization ring: it requires simultaneous inverses of opposite-sheet coordinates whose product is zero. Keeping the separate localized target terms and their homotopy fibre preserves the two trace classes.

The computation does not construct a scalar trace, a new geometric Gysin correspondence, or the physical conductor–Morse class. Coefficient support in \(\operatorname{Spec}R\) remains distinct from the spatial face support. Both edge endpoints, including \(W_{25}\), remain.

## 1. Rings, source, and the existing normal trace

Use

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]/(I_-I_+),
\]

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad A=R/(I_-+I_+).
\]

Set \(y=X_{02}\), \(z=X_{35}\), \(x=X_{03}\), and \(v=X_{25}\). In particular \(yz=0\).

The source is the conductor resolution \(P_A[2]\), with relevant ranks \(1,6,24,92\) in homological degrees \(2,3,4,5\). Its first differential is \(de_i=X_i p_A\). The next differential includes six same-sheet Koszul relations and eighteen mixed-sheet relations. All ninety-two following equations are retained. Higher source terms cannot contribute to the present maps or their positive-degree homotopies because the target ends in degree four.

The complete opposite-edge factor is

\[
C_E=P_E\otimes K_R(\beta y,\beta z,z),
\]

\[
dg=xp_{03}+vp_{25},\qquad dh_{03}=\beta xp_{03},\qquad
 dh_{25}=\beta vp_{25}.
\]

It has forty states and is embedded in the full 430-state cellular complex by the actual signed basis map. The common native factors have generators \(a,b\), and the separate occurrence factor has generator \(k\):

\[
da=\beta y,\qquad db=\beta z,\qquad dk=z.
\]

Retain

\[
\xi=h_{03}+h_{25}-\beta g,\qquad d\xi=0,
\qquad \eta=b-\beta k,\qquad d\eta=0.
\]

The preceding reciprocal two-native-normal pairing gives a chain map to

\[
T=(P_E\otimes K_R(z))\otimes\mathfrak o_{02,35}[2].
\]

The ordered normal line carries occurrence weight \(\epsilon_{02}+\epsilon_{35}\), regulator-normal weight two, and the stated homological shift. The target has ten states. Its two nonzero trace classes are represented by

\[
\nu_E(p_A)=0,\qquad \nu_E(e_i)=X_i\xi\quad(i\in\{13,15,35\}),
\]

and

\[
\nu_R(p_A)=0,\qquad \nu_R(e_i)=X_i\xi\quad(i=13,15),\qquad \nu_R(e_{35})=0,
\]

\[
\nu_R(c_{i,35})=X_i\xi k\quad(i=13,15).
\]

Other columns are zero. Both are checked again against the complete source differential.

The recorded original conductor map is \(G=\beta P+E\). The normal trace sends it to \(\nu_E\); its collapsed version \(\beta P\) has zero trace.

## 2. The literal mixed Laurent continuation is zero

Entry 97's tangential coefficient target inverts both \(x_0=X_{02}\) and \(x_3=X_{35}\), among other coordinates. Any \(R\)-algebra in which both are invertible satisfies

\[
1=y^{-1}z^{-1}(yz)=0.
\]

Thus

\[
R[y^{-1},z^{-1}]=0.
\]

This is not a failure of the reciprocal normal pairing, which uses only monodromy units. It is a failure of the proposed literal occurrence-Laurent base change to the singular normalization ring. Localization is flat; using derived tensor product with that same localization does not produce a missing nonzero Tor term.

The separate localizations are nonzero:

\[
R_y=R_-[y^{-1}],\qquad R_z=R_+[z^{-1}],
\]

where \(R_-=R/I_+\), \(R_+=R/I_-\). Inverting a negative-sheet coordinate annihilates the positive-sheet ideal, and conversely. These are localized target modules, not changes to the global source ring.

No assertion about an independently constructed support-valued or before-specialization trace is inferred from this literal-localization obstruction.

## 3. The correct coefficient-support object

For \(Z=V(y,z)\), the augmented Čech complex is

\[
[R\longrightarrow R_y\oplus R_z\longrightarrow R_{yz}]
=[R\longrightarrow R_y\oplus R_z].
\]

It computes local cohomology, rather than the ordinary cohomology of the punctured open alone. For the target \(T\), use the signed homological model

\[
\mathscr C_Z(T)_n=T_n\oplus(T_y)_{n+1}\oplus(T_z)_{n+1},
\]

\[
D(t,h_-,h_+)=(dt,\ell_-(t)-dh_-,\ell_+(t)-dh_+).
\]

Its counit is \(\varepsilon(t,h_-,h_+)=t\). The target has thirty module summands: ten over \(R\), ten over \(R_y\), and ten over \(R_z\). This is not a thirty-dimensional free \(R\)-module.

The same construction on \(C_E\) has 120 module summands. The componentwise normal trace gives a checked \(30\)-by-\(120\) map between these complexes.

The coefficient normalizer permits negative powers only of \(y\) in the \(R_y\) terms and only of \(z\) in the \(R_z\) terms. It kills the entire opposite ideal in each localized term, including expressions whose displayed monomial contains no positive power of the inverted variable. This distinction is necessary when checking the module equations.

## 4. Explicit lifts of both excess traces

On \(R_y\), both maps \(\nu_E\) and \(\nu_R\) are identically zero because their nonzero coefficients lie in \(I_+\).

On \(R_z\), define homotopies by

\[
H_E^+(p_A)=\xi,
\]

\[
H_R^+(p_A)=\xi,\qquad H_R^+(e_{35})=\xi k,
\]

with all other columns zero. The complete equations are

\[
dH_E^++H_E^+d=\nu_E|_{R_z},\qquad
 dH_R^++H_R^+d=\nu_R|_{R_z}.
\]

For example, on \(e_{35}\),

\[
d(\xi k)+H_R^+(z p_A)=-z\xi+z\xi=0.
\]

On \(c_{i,35}\), the source term gives exactly \(X_i\xi k\). The mixed negative-sheet coefficients vanish in \(R_z\), not in the unlocalized source.

The supported maps are therefore

\[
\widehat\nu_E=(\nu_E,0,H_E^+),\qquad
\widehat\nu_R=(\nu_R,0,H_R^+).
\]

They have twelve and eighteen polynomial entries. The counit returns the original maps exactly.

The lifts also exist before the normal pairing. In the full edge target, the positive-open homotopies for \(P,E,R\) have respective unit values

\[
\xi ak,\qquad \xi a(b-\beta k),\qquad \xi a(b-\beta k),
\]

and the third has the extra value \(e_{35}\mapsto\xi abk\). The recorded map \(G\) has the single unit homotopy \(p_A\mapsto\xi ab\). The negative-open restrictions vanish. Applying the normal trace carries these full-edge supported lifts to the displayed lifts of \(0,\nu_E,\nu_R\), and \(\nu_E\), respectively. Every square is a chain identity.

### Keeping the conductor-unit columns zero

The displayed supported lifts have a local comparison value on \(p_A\). That value is exact in the supported target; it is not a new supported primary class.

On the positive open, \(K_R(z)\) contracts. The target homotopy is

\[
h_z(t\otimes1)=(-1)^{|t|}z^{-1}t\otimes k,\qquad
h_z(t\otimes k)=0,
\]

\[
dh_z+h_zd=1.
\]

Using \(h_z\nu\) as the positive-open homotopy produces supported lifts with literally zero \(p_A\)-column. One common homotopy converts both displayed lifts to those zero-unit representatives:

\[
V(p_A)=(0,0,\xi k/z),
\]

with other values zero. Its differential is the difference between each displayed lift and its zero-unit representative. Hence it leaves \(\widehat\nu_E-\widehat\nu_R\) unchanged. The denominator occurs only in the already localized positive target, never on the source or globally.

## 5. Independent complete Hom calculation

At reduced regulator-normal grade one, the full homogeneous Hom complex into \(\mathscr C_Z(T)\) has dimensions

\[
0,\ 9,\ 66,\ 151
\]

in map homological degrees \(2,1,0,-1\). The differentials entering and leaving degree zero have ranks nine and fifty-five. The kernel has rank eleven, and the nine boundary columns together with \(\widehat\nu_E,\widehat\nu_R\) have determinant \(-1\) in its integral coordinate basis.

Thus its degree-zero cohomology is \(\mathbb Z^2\), with no integer torsion. Grade two gives the identical matrices. All higher regulator grades are obtained by multiplying coefficients by \(\beta\), so the two classes form the same free \(\mathbb Z[\beta]\)-module as before, with the retained orientation grade restored at the end.

The calculation includes all permitted Laurent monomials in each fine degree. Those exponents are fixed by the nine occurrence weights; no Laurent or polynomial cutoff is used. The additional finite pole controls check the implemented coefficient rules, not the completeness theorem.

There is an independent conceptual verification. The conductor source \(A[2]\) is supported on \(Z\). Local-cohomology adjunction gives

\[
R\operatorname{Hom}_R(A[2],R\Gamma_ZT)
\simeq R\operatorname{Hom}_R(A[2],T).
\]

The counit matrix on the two displayed class bases is the identity. Performing this coefficient-support localization introduces no additional derived mapping-space ambiguity over a fixed map, although strict choices of localized primitives can differ.

## 6. The relation-only class moves between the two localized terms

Retain the ambient homotopy

\[
U(e_{35})=-\xi k.
\]

Its difference formula is

\[
\nu_E-\nu_R-\delta U=\kappa,
\qquad
\kappa(m_{n,35})=X_n\xi k\quad(n\in\{02,04,24\}).
\]

The relation-only map vanishes on the positive open. On the negative open its homotopy is

\[
H_\kappa^-(e_{35})=\xi k.
\]

Here \(z=0\), so \(d(\xi k)=0\); the source mixed-relation term gives \(X_n\xi k\). Consequently

\[
\widehat\kappa=(\kappa,H_\kappa^-,0)
\]

is closed, and the complete supported equation is

\[
\widehat\nu_E-\widehat\nu_R-\delta(U,0,0)=\widehat\kappa.
\]

The independent integral detectors give \([\widehat\kappa]=(1,-1)\). Both localized comparison terms are therefore required. Forgetting them would lose the chain-level relation between the two excess traces.

## 7. Endpoint and Cartier compatibilities

The target still contains \(h_{25},p_{25}\) and their occurrence partners. Applying the support construction to the opposite-endpoint support sequence gives the actual connecting map with the sign reversed on the localized Čech components. Each supported trace satisfies

\[
d_{25}\widehat F_{25}+\kappa_{25}\widehat F_{\mathrm{rel}}
=\widehat F_{25}d_{P_A}.
\]

The original physical endpoints and the full generic \(Q\)-components stay zero. Neither the localization nor the pairing changes a spatial face label.

The \(X_{03}\)-Cartier Hom construction commutes with this coefficient-support construction. Both orders have sixty target module summands. The explicit interchange is diagonal: it is \(-1\) exactly on a localized Čech component that is also in the shifted Cartier component, and \(+1\) elsewhere. It commutes with every differential and squares to the identity.

The checker applies that interchange to both supported trace maps and to the complete Cartier source. Under purity, the source is still

\[
A/(X_{03})[1]\otimes\mathfrak n_{03}^{\vee},
\]

with the same dual conormal factor on the target side. The local-cohomology construction is not substituted for Cartier purity, and the zero-divisor pair \((y,z)\) is not declared a regular sequence.

## 8. A canonical conductor class and the nodal residue test

The scalar coefficient Čech complex has

\[
\omega_c=[(0,1)]\in\operatorname{coker}(R\to R_y\oplus R_z).
\]

The branches are ordered as negative, positive. For a positive-sheet variable \(X_i\), \(X_i\omega_c\) is the boundary of the global positive-sheet element \(X_i\). Negative-sheet variables kill the representative itself. Thus \(I\omega_c=0\).

Conversely, if \(r\omega_c\) is a diagonal boundary, its negative localized component forces the negative branch of that boundary element to vanish. The two polynomial branch localizations are injective, so its common conductor coefficient is zero. Equality of the positive components then forces the common conductor coefficient of \(r\) to vanish. Therefore

\[
\operatorname{Ann}_R(\omega_c)=I.
\]

Exchanging the two branches sends \((0,1)\) to \((1,0)\); their sum is the diagonal boundary of one. The class is polarity-odd without division by two.

There is a direct explanation of why the mixed Laurent residue is not simply lost in a support-valued construction. On the valid slice setting the other four short variables to zero, put

\[
S=\mathbb Z[\beta,X_{03},X_{14},X_{25},y,z],\qquad R_0=S/(yz).
\]

In the smooth ambient ring, \(H^2_{(y,z)}(S)\) has basis \(y^{-i}z^{-j}\), \(i,j\ge1\). Multiplication by \(yz\) is surjective and has kernel spanned by those basis elements with \(i=1\) or \(j=1\). The exact sequence for \(0\to S\xrightarrow{yz}S\to R_0\to0\) gives

\[
H^1_{(y,z)}(R_0)
\xrightarrow{\sim}
\operatorname{Ann}_{H^2_{(y,z)}(S)}(yz).
\]

With Čech differential \((a,b)\mapsto b-a\), its explicit formulas are

\[
[(0,1)]\longmapsto[1/(yz)],
\]

\[
[(y^{-n},0)]\longmapsto-[1/(y^{n+1}z)],\qquad
[(0,z^{-n})]\longmapsto[1/(yz^{n+1})].
\]

The class moves from Čech degree two to one through the retained hypersurface \(\operatorname{Tor}_1\). Choosing the relation \(yz\) frames its conormal generator; rescaling that relation rescales the displayed fraction inversely. This is not an inversion of \(yz\) inside \(R_0\).

This two-variable slice does not identify the full nine-relation normalization immersion with a hypersurface. Nor is \(\omega_c\) claimed to be the scalar value of either excess trace. The trace output still contains the interval and occurrence complexes.

## 9. Scope and consequence

The attempted direct occurrence-Laurent continuation gives the zero ring. The supported coefficient construction instead retains the separate localized targets and both resolved-source comparison homotopies. It preserves the original two independent excess traces, including the relation-only difference, and commutes with the preceding native pairing and correctly shifted Cartier operation.

What remains is a geometric tangential/relative-dualizing evaluation from this retained support complex, with its spatial endpoint conditions. No scalar counit, physical generic \(Q\)-leg, or identification with \(\Delta_J\) has been inferred from the existence of the two coefficient-supported classes.

## Verification and sources

Run:

```sh
python branch_a_w03_cech_support_and_trace_descent_checker.py --output branch_a_w03_cech_support_and_trace_descent_certificate.json
```

The checker is standalone and uses only the Python standard library. It reconstructs the 430-state differential, the forty-state opposite edge, the conductor resolution, both traces, the localized module arithmetic, the thirty- and 120-summand support complexes, the complete homogeneous Hom matrices, the relative endpoint equations, and the sixty-state Cartier interchange. It performs 24,450 counted exact checks. The nodal all-degree statement and exact scalar annihilator have the independent proofs above; finite coefficient controls are not substituted for those proofs.

Semantic certificate SHA-256:

```text
19245bf354e51de54e0968ca1088b84cfb279bc06c468921239deb6f1d5c0a9f
```

Source data, repository `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- Entry 93, `Alternating Fusion Normalization-Conductor Square`: coefficient ring, sheet restrictions, and conductor.
- Entry 97, `Reciprocal-Twist D03 Bivariant Road Trace`: the normal pairing and the separate occurrence-Laurent scope of its tangential trace.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: signed radial/native differential.
- The immediately preceding standalone `branch_a_w03_reciprocal_pairing_and_excess_trace_checker.py`: the reconstructed local source and trace formulas. The new checker embeds the necessary definitions and does not import that file at runtime.

Mathematical references: Stacks Project 0952, especially Lemmas 47.9.1 and 47.9.3 (Čech local cohomology, right adjoint, and derived base change); 0A8H (Hom signs and tensor–Hom); 0117 (connecting homomorphisms); 0B4B (Cartier duality and normal line); 00H9 (flatness/localization).
