# Endpoint restriction and residual connector class for the D03 coefficient candidate

Date: 2026-09-06. Source inputs are pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Result and scope

The previously supplied endpoint-Koszul/local-collar candidate admits a completely explicit boundary restriction on its derived mapping complexes. Both Boolean endpoint branches and their common augmentation are retained. For the candidate sending the top generator to the unit collar generator, its known ambient nullhomotopy restricts to zero on the endpoint subcomplex. With connector homotopies retained, the residual class is determined by the principal-part expression

\[
[x_1h_0-x_5h_2]\in(x_1,x_5)W,
\qquad W=R[U^{-1}]/\bigl(R+(X/U)R\bigr).
\]

In words: the difference of the two weighted connector coefficients is taken modulo the two kinds of allowed regular upper-term boundaries. Every connector pair regular in U gives zero. Other legal lower-term Laurent coefficients can give nonzero classes.

This is an exact calculation for the stated coefficient candidate, not an identification with the entire source-filtered physical category. The physical endpoints v-plus and v-minus are not the Boolean endpoints q-zero and q-two. The retrieved source records supply their constructible connector boundaries but not their images as cochains in this Hom complex. Therefore a unique *physical* value of h-r(s) is not determined here. It would be incorrect to set those missing cochains equal to zero or to r(s) and report that as a calculation.

The preceding target-category note defined a general framework. It did not specify all the objects, geometric comparison maps, and connector cochains needed to instantiate the full physical restriction. The restriction computed below is a concrete, explicitly delimited part of that task.

## 1. The two complexes and the endpoint subcomplex

Let

\[
R=\mathbb Z[x_1,x_5,X,U],\qquad L=R[U^{-1}],\qquad y=X/U\in L.
\]

In words: x-one and x-five are the independent endpoint occurrence variables, X is the long occurrence variable, and U is the long normal equation. Only the indicated target summand is localized. Extra independent polynomial spectator variables can be retained throughout.

Use homological degrees for the input complexes. The source's endpoint hull is

\[
P_2=Re,\qquad P_1=Rq_0\oplus Rq_2,\qquad P_0=Ra,
\]

\[
\partial e=-x_1q_0+x_5q_2,\qquad
\partial q_0=x_5a,\qquad \partial q_2=x_1a.
\]

In words: this is the source's two-variable Koszul resolution before adding its final quotient module. It retains the augmentation cell that makes the two branches close. Its positive homology vanishes and its degree-zero homology is R/(x-one,x-five). [S1]

The lower endpoint subcomplex is

\[
B=(Rq_0\oplus Rq_2\xrightarrow{(x_5,x_1)}Ra)\subset P.
\]

In words: the inclusion is an actual subcomplex, not a replacement of two nonclosed endpoint generators by a discrete pair.

The previously studied local collar is

\[
C_3=Rk\oplus Rn,\qquad C_2=Lp,\qquad
\partial k=yp,\qquad \partial n=p.
\]

In words: the two upper terms have regular coefficients; the lower target term has the permitted inverse U. This is the branch-local row obtained after the source's peripheral collar completion and quotient. It is not the entire seven-generator Q diagram or the full endpoint-relative target. [S2, S3]

In particular, a homotopy from an endpoint generator to p may use a negative power of U because its *target* is Lp. A homotopy to k or n may not use that inverse. No negative power of an occurrence variable is permitted anywhere.

## 2. The actual restriction for these complexes

Put

\[
M=\operatorname{Hom}^{\bullet}_R(P,C),\qquad
N=\operatorname{Hom}^{\bullet}_R(B,C),\qquad
r(f)=f|_B.
\]

In words: restrict the comparison and every higher comparison to both endpoint branches and their common augmentation. Since P and B are bounded finite free complexes, these Hom complexes compute their derived mapping complexes, including the non-free localized target term. [M1]

The cochain degree convention is

\[
\operatorname{Hom}^j(P,C)=\prod_i\operatorname{Hom}_R(P_i,C_{i-j}),
\qquad \delta f=\partial_Cf-(-1)^jf\partial_P.
\]

In words: degree minus one is an ordinary chain homotopy, raising homological degree by one.

The complete module table is

| Cochain degree | M | N | r |
|---|---|---|---|
| -3 | R² | R² | identity |
| -2 | R⁴ ⊕ L | R⁴ ⊕ L | identity |
| -1 | R² ⊕ L² | L² | projection to L² |
| 0 | L | 0 | zero |

No other degrees occur.

Write a degree-minus-one map as

\[
s(e)=Ak+Bn,\qquad s(q_0)=c_0p,\qquad s(q_2)=c_2p,\qquad s(a)=0,
\]

with A,B in R and c-zero,c-two in L. Then

\[
\delta_Ms=yA+B-x_1c_0+x_5c_2,\qquad
r^{-1}(A,B,c_0,c_2)=(c_0,c_2).
\]

In words: the boundary restriction retains the two endpoint homotopy values and discards the top-generator value. Here the superscript minus one denotes cochain degree, not the inverse of r.

For degree minus two, use coordinates

\[
t(q_0)=A_0k+B_0n,\qquad
 t(q_2)=A_2k+B_2n,\qquad t(a)=zp.
\]

Then

\[
\begin{aligned}
\delta_Mt={}&(x_1A_0-x_5A_2,\ x_1B_0-x_5B_2,\
&yA_0+B_0-x_5z,\ yA_2+B_2-x_1z),\\
\delta_Nt={}&(yA_0+B_0-x_5z,\ yA_2+B_2-x_1z).
\end{aligned}
\]

In words: the last two coordinates are the changes in endpoint connectors produced by higher homotopies. The z terms are forced by the retained augmentation a. Deleting a would incorrectly delete this indeterminacy.

For a degree-minus-three map with a sent to Ak+Bn,

\[
\delta_M(A,B)=\delta_N(A,B)
=(x_5A,x_5B,x_1A,x_1B,yA+B).
\]

In words: the same augmentation identities supply the next higher compatibility. The checker verifies both differentials square to zero and r commutes with them in every degree, respecting which slots are regular and which are localized.

## 3. Restrict the known nullhomotopy

Take the earlier candidate

\[
f(e)=p,\qquad f(q_0)=f(q_2)=f(a)=0.
\]

In words: this is precisely the ordinary unit attachment whose nontriviality required testing.

Its ambient primitive is

\[
s(e)=n,\qquad s(q_0)=s(q_2)=s(a)=0,
\qquad \delta_Ms=f.
\]

Therefore

\[
r(s)=(0,0).
\]

In words: this nullhomotopy already vanishes on the entire endpoint subcomplex. Merely fixing those endpoint *maps* does not exclude it.

After translating a prescribed comparison problem by a reference lift, the difference problem has zero boundary value. Retaining its two comparison homotopies means keeping

\[
h=(h_0,h_2)\in N^{-1}=L^2.
\]

In words: these are cochains, not the earlier scalar endpoint-map coefficients called a-zero and a-two. Here the endpoint restriction of every degree-zero map is zero, and N has no degree-zero term, so any such pair is a closed boundary homotopy. A physical source must choose it independently.

For this candidate,

\[
h-r(s)=(h_0,h_2).
\]

This equality of cochains still requires passage to the full higher-homotopy quotient below.

## 4. Compute the residual class, including every connector indeterminacy

Let

\[
K=R+yR\subset L,\qquad W=L/K.
\]

In words: K is an R-submodule, not an ideal of the localized ring L. Treating it as an L-ideal would contain one and incorrectly kill the whole calculation.

The displayed degree-minus-two differential gives

\[
H^{-1}(N)
\cong W^2/\{(x_5z,x_1z):z\in W\}.
\]

In words: regular k/n homotopies remove K from each endpoint coefficient; the a-cell identifies the displayed paired connector changes.

Define

\[
\psi:H^{-1}(N)\longrightarrow W,\qquad
\psi([(h_0,h_2)])=[x_1h_0-x_5h_2].
\]

In words: take the weighted difference dictated by the source's top boundary.

This map is injective and has image (x-one,x-five)W. To prove injectivity, note that W is a polynomial module in the independent variables x-one and x-five over its remaining coefficients. Thus the equation x-one times h-zero equals x-five times h-two forces h-zero=x-five z and h-two=x-one z in W. This is exactly the quotient relation already imposed. Equivalently, the two-variable Koszul syzygy is exact even though W has U- and X-torsion. [M2]

Now let s be any degree-minus-one cocycle of M. Its closedness says

\[
x_1c_0-x_5c_2=yA+B\in K.
\]

In words: its restricted endpoint pair has zero image under the injective map psi, so its class in H-minus-one of N is zero. Consequently

\[
\operatorname{im}\bigl(H^{-1}(M)\to H^{-1}(N)\bigr)=0,
\]

\[
\operatorname{coker}\bigl(H^{-1}(M)\to H^{-1}(N)\bigr)
\cong(x_1,x_5)W.
\]

The requested secondary class, for the specified unit attachment, is therefore

\[
[h-r(s)]\ \longleftrightarrow\ [x_1h_0-x_5h_2]\in(x_1,x_5)W.
\]

In words: this is the complete answer as a function of the supplied connector cochains. It includes changes of ambient nullhomotopy and higher endpoint homotopies, not just the test r(s)=0 for one representative.

### A constructive zero test

Every Laurent polynomial has a unique decomposition

\[
f=w+ya+b,
\qquad a,b\in R,
\]

where w consists of all terms with U-exponent at most minus two, and the terms with U-exponent minus one and X-exponent zero. Thus

\[
W\cong
\mathbb Z[x_1,x_5]\,U^{-1}
\oplus\bigoplus_{j\ge2}\mathbb Z[x_1,x_5,X]\,U^{-j}
\]

as a module over Z[x-one,x-five,X]; on the first summand X acts as zero. The action of U shifts powers toward zero, using that quotient rule.

This is an all-degree proof of the normal form. There is no ordinary integer torsion. It is not a claim that W is free over R.

For an arbitrary degree-zero coefficient f and connector pair h, the complete framed mapping-fibre invariant is

\[
\mathcal I(f,h)=[f+x_1h_0-x_5h_2]\in W.
\]

In words: the top attachment and its two endpoint comparisons contribute to one residue in the quotient module.

If its normal form is zero, write f+x-one h-zero minus x-five h-two as yA+B. Then

\[
\widetilde s=(A,B,h_0,h_2)
\]

satisfies

\[
\delta_M\widetilde s=f,\qquad r(\widetilde s)=h.
\]

In words: the zero test constructs an admissible framed nullhomotopy; it is not just a dimension count. The executable implements this decomposition exactly.

### Controls

For h-zero=h-two=zero, the unit attachment is framed nullhomotopic.

For any h-zero and h-two in R, the result is again zero because the weighted difference is regular in U.

For

\[
h_0=U^{-1},\qquad h_2=0,
\]

one obtains

\[
[x_1/U]\ne0.
\]

In words: the same zero endpoint maps can carry different comparison homotopies and different framed classes. This example is allowed in the coefficient candidate's lower target slot, but is not assigned to the physical connector.

For

\[
h_0=x_5/U,\qquad h_2=x_1/U,
\]

the result is zero. The degree-minus-two cochain with z=-U-inverse on a is an explicit boundary witness. Omitting the augmentation would miss this cancellation.

## 5. The entire relative mapping complex

The map r is degreewise surjective. Hence its homotopy fibre is quasi-isomorphic to its strict kernel, not by declaring a strict kernel in general, but by this particular surjectivity. [M3]

\[
\operatorname{fib}(r)\simeq
[R^2\xrightarrow{(y,1)}L],
\]

in cochain degrees minus one and zero. Consequently

\[
H^0\operatorname{fib}(r)=W,\qquad
H^{-1}\operatorname{fib}(r)=R\langle(U,-X)\rangle,
\qquad H^j\operatorname{fib}(r)=0\quad(j\ne-1,0).
\]

In words: even a zero framed map can have a nontrivial family of nullhomotopies. The surviving degree-minus-one class is the regular upper cycle Uk-Xn. A zero secondary class is not a contractibility theorem for the whole extension space.

For the corresponding additive mapping space, connected components are indexed by W, the fundamental group at each component is the additive group of R, and higher homotopy groups vanish. Additional physical Q- or normal framings can change this mapping space and are not supplied by the local row.

## 6. What the actual physical endpoint-connector source supplies

The source's dP6 oriented-boundary construction has six local corridor intervals and six connector intervals. Reconstructing its fan, cone labels, and germ maps gives the following connector boundaries. Use the ordered target vertices

\[
(v_+,v_-,c_0,c_1,c_2).
\]

The c-labels here denote the three shifted road centers in that checker, not the Boolean endpoint generators in P.

For its cyclic connector order zero through five,

\[
\partial_{\rm conn}=
\begin{pmatrix}
-1&0&-1&0&-1&0\\
 1&0& 1&0& 1&0\\
 0&1& 0&0& 0&-1\\
 0&-1&0&1&0&0\\
 0&0&0&-1&0&1
\end{pmatrix}.
\]

In words: connectors zero, two, and four join v-plus to v-minus; the other three join the centers cyclically. The connector-only matrix has rank three. Including the six corridor edges gives a five-by-twelve incidence matrix of rank four with a unit spanning-tree minor. The sum of its twelve oriented columns is zero. These are source-derived cellular boundary data, reconstructed here without choosing any Hom-cochain values. [S4]

The source explicitly stops short of a single mixed-variance coefficient kernel that identifies the disk filler and all its boundary edges with the literal endpoint/Q target in one Hom complex. Its later primitive-signature tests do not furnish the arbitrary-coefficient images required in this calculation.

Thus the displayed cellular columns do not determine h-zero or h-two. A cell's boundary and an image of that cell as a degree-minus-one coefficient map are different data. The same distinction applies to the Morse and conductor trivializations: their difference can be formed only after both are constructed in one mapping complex. [S5]

## 7. Decision for the current research task

Computed: the complete r for the supplied endpoint-hull/local-collar candidate; r(s) for its known unit nullhomotopy; the complete higher-connector indeterminacy; the formula and constructive zero test for h-r(s); and the actual constructible source connector-boundary matrix.

Not determined: the full physical mapping restriction from the normalization-provenanced source to the complete framed BM-Cech target, or the images of its endpoint connectors as h. In particular, no physical zero, nonzero class, or parity is inferred from the local calculation.

The precise missing input is an image cochain for each source endpoint connector, in the same coefficient/filtration complex as the ambient primitive, together with its comparison on the full Q diagram. Once such cochains are supplied, the formula above evaluates their contribution in this local candidate. A full physical calculation must also prove that this local candidate is the relevant restriction of that larger diagram.

## Verification

Run:

```sh
python check_endpoint_boundary_restriction.py --output endpoint_boundary_restriction_certificate.json
```

The checker completed 9,402 exact assertions. It checks the two full Hom differentials, the restriction in every degree, allowed coefficient rings, the unit nullhomotopy and its boundary restriction, relative-fibre invariance, constructive zero witnesses, nonzero principal-part examples, the augmentation cancellation, and the source dP6 connector matrices. Laurent test exponents run from minus four through plus four; the displayed algebraic normal-form and syzygy proofs establish the unbounded results. This is not proof-assistant verification. No source-repository files were modified.

## Sources

[S1] Marici entry 117, `src/ledger/20260814-117 D03 Thom Endpoint Koszul Hull and the Missing Road Generizations.md`, blob `af6874dc6928614a824a14105fa8e4ba37d96306`.

[S2] Marici entry 174, `src/ledger/20260815-174 Two-Edge Bivariant Trace and the Unlocalized Two-Flip Alignment Gate.md`, blob `ae5d4fc93fa135e7dc0ee6088928f9b8f8cad405`. The collar's symbolic/branch-local scope remains in force.

[S3] The earlier generated `branch_a_q2_completion.md`, Section 5, fixes the regular upper terms and localized lower term used here. It does not identify the local row with the full physical comparison.

[S4] Marici entry 249, `src/ledger/20260815-249 Oriented dP6 Boundary Connectors and the Six-Functor Lift Gate.md`, blob `9f759c9998cb0c33f5ccdb94f7c02f0eeef53445`; checker `research/voevodsky/check_dp6_oriented_boundary_connector_realization.rs`, blob `7b0bc2735e99d3075968e11da0ea6f9f0937ea38`.

[S5] Marici entry 109, `src/ledger/20260814-109 Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism.md`, secondary-trivialization specification; the earlier generated `framed_target_category.md` defines the mapping-fibre criterion but not a physical connector cochain.

[M1] Stacks Project, Hom complexes, tag `0A8H`, https://stacks.math.columbia.edu/tag/0A8H .

[M2] Stacks Project, Koszul regular sequences, tag `062D`, https://stacks.math.columbia.edu/tag/062D . The specific polynomial-module syzygy used here is proved in Section 4.

[M3] Stacks Project, Cones and termwise split sequences, tag `014D`, https://stacks.math.columbia.edu/tag/014D .
