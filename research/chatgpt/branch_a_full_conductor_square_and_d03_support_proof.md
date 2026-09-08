# Branch A — full conductor square and marked D03 support

Date: 2026-09-07.

## Results

All nine coherent conductor-ideal extensions from the preceding calculation admit an explicit completion over the four-corner normalization–conductor diagram. The fixed-reflection sublattice still has rank three. Restoring the single lower conductor therefore imposes no additional equation on this already constructed family.

The spatial support test has a different answer. None of the nine extensions, including its recorded restriction homotopy, is supported on the actual two-edge marked D03 gallery. Allowing the whole short facet 35 leaves a rank-two lattice. Both directions contain unavoidable D25-labelled terms and are odd under the existing reflection action. Hence that larger support still contains no invariant member of the three-dimensional family.

These results are computations for the existing coefficient target, source placement, and frame. The four-corner target below is the square canonically built from the already specified inclusion N -> K and quotient K/N. It is not identified here with a geometric six-functor realization of the normalization square. The support exclusion concerns ordinary containment in the published marked gallery. It is not a nonexistence theorem for larger or extraordinary correspondences.

## 1. Coefficients and fixed target

Work over

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]/
(X_aX_b:a\in\{02,04,24\},\ b\in\{13,15,35\}).
\]

Let

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad
I=I_-\oplus I_+,\qquad A=R/I.
\]

The normalization is

\[
\widetilde R=R_+\oplus R_-,\qquad R_+=R/I_-,\quad R_-=R/I_+.
\]

These are the actual two-sheet modules of Marici Entry 93. In particular, the source square is

\[
\begin{matrix}
R&\xrightarrow{\nu}&\widetilde R\\
\downarrow&&\downarrow\\
A&\xrightarrow{\Delta}&A\oplus A,
\end{matrix}
\qquad \Delta(a)=(a,a).
\]

The diagonal here is not the difference map in the separate exact sequence
\(0\to R\to\widetilde R\to A\to0\).

The target is the full 430-state corrected complex C_beta. A basis state is [F,H,e], where F is a noncrossing dissection, H is its native-circle subset, and e=0,1 records the distinct occurrence-35 factor. Its homological degree is 3-|F|+|H|+e. Its differential contains the signed radial coefficient X_d, native coefficient beta X_d, and auxiliary occurrence coefficient X_35. No coefficient inverse is used.

The target frame is unchanged:

\[
K_n=\{c\in C_{\beta,n}:q(c)=0,\ v(c)=0,\ v(dc)=0\},
\qquad N=K\cap IC_\beta,
\qquad L=K/N.
\]

Here q is the genuine fourteen-state Q-quotient and v is the graded projection onto both complete endpoint packets. The condition on v(dc) is essential: v itself is not being asserted to be a chain map. K and N are actual subcomplexes. L embeds in C_beta/I C_beta by coefficient reduction, since the kernel of that reduction on K is exactly N.

The computation uses source modules placed in homological degree three, occurrence-map degree zero, and regulator-normal output grade three. These are the comparison degrees of the preceding audit, not newly derived geometric Gysin shifts. All source differential signs are specified by the exported matrices.

## 2. Reconstruct the nine extensions independently

Let P resolve I. Its displayed ranks are 6,24,92. Its first differential includes the same-sheet Koszul relations and the mixed-sheet annihilation relations. The next differential includes their complete 92 compatibility relations. Exactness in the degrees needed here follows from the decomposition of a coefficient into a constant, a positive-sheet polynomial, and a negative-sheet polynomial. On either sheet the internal syzygies are polynomial Koszul syzygies; the opposite sheet supplies the annihilator summand. Higher free terms can be appended without changing any equation in this audit.

Let P_nu resolve the normalization. It has ranks 2,6,24,92 in degrees zero through three. The first generator a_i resolves the annihilator of the opposite sheet unit:

\[
d_{P_\nu}a_i=X_i b_{\mathrm{opposite}(i)}.
\]

The later terms reuse P with one degree shift.

A possible ambient restriction homotopy H:P[3] -> K has 33 coefficient coordinates. Its Hom differential is injective on this homogeneous space. Requiring delta H to have coefficients in I imposes 24 independent equations, each eliminated with a signed unit. Thus there are nine independent H, with

\[
f=\delta H:P[3]\longrightarrow N.
\]

The checker verifies all source relations for every f and all endpoint/Q equations for both f and H. Every H is supported only on the source generator a_35 and has conductor-constant polynomial coefficients. The nine f are independent.

The normalization-source and node-source degree-zero mapping systems into K have only the zero solution in this grading. Their degree-one cochain slots vanish. Thus the top maps in the completion below are zero. This is not an omission of a nonzero sheet-unit map.

## 3. Construct the resolved diagonal, including its homotopy correction

There are two source inclusions

\[
k:P\longrightarrow R,
\qquad
j:P\longrightarrow P_\nu.
\]

On generators,

\[
k(a_i)=X_i,\qquad
j(a_i)=X_i b_{\mathrm{sheet}(i)},\qquad
\nu(1)=b_++b_-.
\]

All higher values of k and j are zero. The resolved maps nu k and j are not equal: their difference on a_i is X_i times the opposite sheet unit.

The normalization resolution supplies the homotopy

\[
t_n:P_n\longrightarrow(P_\nu)_{n+1},
\qquad t_n=(-1)^n\operatorname{id},
\]

under the displayed identification of the shifted generators. Its exact equation is

\[
d_{P_\nu}t+t d_P=\nu k-j.
\]

Define standard homological cones

\[
D=\operatorname{Cone}(k),\qquad
E=\operatorname{Cone}(j),
\]

with

\[
d_D(r,p)=(d_Rr+kp,-d_Pp),\qquad
 d_E(q,p)=(d_{P_\nu}q+jp,-d_Pp).
\]

They resolve A and A⊕A respectively. The displayed pieces have 123 and 246 generators. The resolved lower-conductor diagonal is

\[
\Delta_P(r,p)=(\nu r+t p,p).
\]

The homotopy equation proves d_E Delta_P = Delta_P d_D, and the checker verifies every column. The formula omitting t fails on exactly six primitive relation columns. Those errors are present before any regulator specialization.

The two-sheet decomposition is also explicit. Every generator of P has a terminal ideal sheet preserved by its differential. The P summand of E goes to that same conductor copy. A shifted P generator in the P_nu summand goes, with sign (-1)^n, to the opposite conductor copy. This is an integral chain isomorphism

\[
E\cong D\oplus D.
\]

Under this isomorphism Delta_P is the diagonal on every resolution generator, not just on the two degree-zero units.

The complete Mayer–Vietoris sequence of these resolutions is degreewise split exact:

\[
0\longrightarrow R
\xrightarrow{(\nu,\iota_R)}P_\nu\oplus D
\xrightarrow{\iota_\nu-\Delta_P}E
\longrightarrow0.
\]

The certificate exports a graded section and retraction and verifies exactness at every degree. A graded section is not misidentified with a chain section. Cone functoriality for a homotopy-commutative square gives exactly the t correction; see Stacks, Section 13.9, especially Lemma 13.9.2 (tag 014D).

## 4. Complete each of the nine comparisons over all four corners

For a recorded pair (f,H) with delta H=f, define cofiber maps into Cone(N -> K) by

\[
D[3]\longrightarrow\operatorname{Cone}(N\to K),
\qquad (r,p)\longmapsto(-H(p),f(p)),
\]

\[
E[3]\longrightarrow\operatorname{Cone}(N\to K),
\qquad (q,p)\longmapsto(-H(p),f(p)).
\]

The top source maps R[3] -> K and P_nu[3] -> K are zero. The complete cofiber chain equations follow from delta H=f and are verified before quotienting target coefficients.

Projecting the target cone to L gives

\[
\psi_D(r,p)=-\overline{H(p)},\qquad
\psi_E(q,p)=-\overline{H(p)}.
\]

The minus signs are determined by the displayed cone convention. Since Delta_P preserves its P component,

\[
\psi_E\Delta_P=\psi_D.
\]

The two vertical squares commute as well: psi_D is zero on R, and psi_E is zero on P_nu. Thus each existing comparison completes to a map from the resolved source square to

\[
\begin{matrix}
K&\xrightarrow{1}&K\\
\downarrow&&\downarrow\\
L&\xrightarrow{1}&L.
\end{matrix}
\]

This target square uses only the frame quotient already present in the preceding calculation. No physical geometric identification of this square is added.

All nine lower-conductor maps are independent. They vanish on the source unit but have nonzero values on its first relation generator a_35. There is no homotopy removing such a value in this grading: a unit homotopy would require L_4 at occurrence weight zero, which is absent, and a relation homotopy would require target degree five or higher. The projective resolution makes this a derived-map assertion for this nine-dimensional image.

After identifying E with D⊕D, the upper-conductor map is (psi_D,0) in the fixed occurrence-35 model. Its active component is the positive conductor copy because 35 is a positive-sheet generator. Pullback along the resolved diagonal therefore gives psi_D, without averaging or division by two. This tracks source provenance through the relations rather than inferring it from a target coefficient.

The four-corner equations impose no new constraint on the nine constructed families. Their reflection-invariant sublattice still has rank three. This is not a classification of arbitrary extra maps one could independently add on the conductor corners.

## 5. Test the actual marked D03 gallery

Entry 106 specifies the two-edge gallery with faces

\[
\{13,35\},\quad\{03,35\},\quad
\{13,15,35\},\quad\{03,13,35\},\quad\{02,03,35\}.
\]

Keeping every native mark and both values of the occurrence partner gives a 64-state subcomplex of C_beta. No artificial support rule is fitted to the nine candidates.

The audit requires both the ideal-map values f and its recorded normalization homotopy H to have support in the chosen carrier. It checks all source-generator and source-relation columns. The results are

| Allowed carrier | States | Extension lattice rank | Fixed-reflection rank |
| --- | ---: | ---: | ---: |
| Complete target | 430 | 9 | 3 |
| Whole short facet 35 | 124 | 2 | 0 |
| Whole long facet 03 | 100 | 0 | 0 |
| Marked D03 two-edge gallery | 64 | 0 | 0 |
| Union of the 03 and 35 facets | 184 | 2 | 0 |

Each support is checked to be an actual subcomplex under the complete differential. Restriction equations are solved by integral unit pivots. Requiring f and H simultaneously gives the same kernels as requiring H alone; the certificate verifies both systems rather than relying only on that implication.

In particular no member of the current nine-dimensional coherent-extension family gives an ordinary map supported on the marked gallery. This is a statement about the current source degree and common target. A support-changing Gysin operation is a different map and is not ruled out by this calculation.

## 6. Why the larger 35 facet still fails the D03 locality test

A geometric basis of the rank-two 35-facet space is

\[
\begin{aligned}
U_a={}&[\{02,03,35\},\{02,03,35\},1]
+[\{02,25,35\},\{02,25,35\},1]\\
&-\beta[\{02,35\},\{02,35\},1],
\end{aligned}
\]

\[
\begin{aligned}
U_b={}&\beta^2[\{35\},\{35\},1]
+\beta[\{03,35\},\{03,35\},1]\\
&+\beta[\{25,35\},\{25,35\},1].
\end{aligned}
\]

Both define coherent extensions by H(a_35)=U and f=delta H. Their full boundaries and all relation values remain in N.

For c U_a+d U_b, the coefficient of the fully marked {02,25,35} state is c. The coefficient of beta times the fully marked {25,35} state is d. Thus the two D25 readouts are the identity matrix on the two lattice coordinates. No nonzero combination removes the D25 terms. It is not necessary to invert beta to read its known homogeneous coefficient.

The fixed source action is s(v)=2-v mod 6, with the published top-cell and ordered-normal signs. It fixes occurrence 35 and exchanges long labels 03 and 25. Direct computation gives

\[
sU_a=-U_a,\qquad sU_b=-U_b.
\]

There is no invariant integral vector in this two-dimensional lattice. A separate sign twist of the source would change this parity conclusion; none has been introduced. The zero result on the marked gallery is independent of that optional twist.

All three occurrence labels 35,15,13 were reconstructed. Rotation and reflection commute with the complete differential, and the three invariant comparisons transport with their full endpoint and Q equations intact.

## 7. Interpretation and remaining physical requirement

The normalization–conductor square is now present at the resolution level, including its single lower conductor, doubled upper conductor, and the comparison on source relations. It does not select one of the three remaining equivariant coefficient comparisons. Evaluating the lower-conductor unit cannot do so: all three maps vanish on that unit.

The independent marked-support test is stronger. Those comparisons are not realizations on the actual D03 gallery. Even the two non-equivariant comparisons supported on its containing 35 facet necessarily involve the other long label D25.

A physical identification must therefore construct an actual support-changing operation or a source-defined larger correspondence. It cannot be obtained by choosing scalar coordinates in this coefficient family and declaring the result local to D03. No value of H_cond or Delta_J is assigned.

## Verification and reproducibility

The standalone checker reconstructs all coefficients, source resolutions, cone maps, boundary kernels, coherent extensions, symmetry actions, and support matrices. It reads no prior certificate or companion module and requires only Python's standard library.

Run:

```sh
python branch_a_full_conductor_square_and_d03_support_checker.py
```

This execution verified 116,416 exact identities. A separate directory containing only the checker was executed with PYTHONHASHSEED=8731; its certificate agreed byte-for-byte.

Mathematical data SHA-256:

```
448633cd86f879068f32890935a8ddad88ff4fedf16c395a99aa87beaab51b7f
```

Checker SHA-256:

```
e03145674e6bc2b2fc638e0020f5e4e76241c2e6fda0eb2a206e1970f680451c
```

The asserted ranks concern exact integer kernels with fixed multidegrees, not a coefficient-degree sampling or a prime-only rank test. The source resolution is used through all degrees capable of entering a map, a chain equation, or a homotopy into the bounded target.

## Sources

Repository: andrey-kokoev/marici, commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61.

- Entry 93, *Alternating Fusion Normalization-Conductor Square*. Blob 840258522d45e450e4f1e8bb927d9aae58c75566.
- Entry 106, *Marked Log Gallery Secondary Class and the Global Yoneda Gap*. Blob d9ac9420e7360013ff6acde34df51a4941b34101.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`. Blob b967151cb0ee822e2361b9334a4ab26082c12682.
- Shared arithmetic and target routines are retained from `branch_a_normalization_sheet_extension_obstructions_checker.py`; its certificate is not read at runtime.
- Stacks Project tag 014D: cones, their homotopy corrections, and termwise split sequences. https://stacks.math.columbia.edu/tag/014D
- Stacks Project tag 0A8H: Hom differentials and cochain homotopies. https://stacks.math.columbia.edu/tag/0A8H
- Stacks Project tag 064B: projective-source computation of derived maps. https://stacks.math.columbia.edu/tag/064B
