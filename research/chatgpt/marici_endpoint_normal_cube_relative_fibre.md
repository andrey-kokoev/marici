# Endpoint-sensitive normal continuation and the exact relative moduli space

Date: 2026-09-07  
Repository: `andrey-kokoev/marici`  
Pinned input commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result

The order-two ambiguity found in the three-long-normal degree is a property of a specific relative comparison problem, not a coefficient-independent physical parity. Its continuation through all six short-normal directions can now be computed with the complete endpoint complexes retained.

The calculation gives three main results.

First, the deformation complex of the target-side endpoint/Q restriction is the **actual short-boundary complex shifted by one**, rather than a detached node/norm detector. Second, the entire 64-vertex short-normal multiplication cube reduces equivariantly to restriction of cochains on induced subcomplexes of the six-short-diagonal compatibility complex. Third, multiplying by all six short normals makes the relative fibre contractible, but it also kills both primitive endpoint homology classes. This identifies the earlier two choices; it does not select a preferred one.

The normalized comparison over one complete endpoint branch has one component and an integer loop group under its correct order-three stabilizer. It is not rigid. Reflection exchanges the two branch degrees and is never falsely treated as an automorphism of just one of them.

These are target-side theorems. No identification of the external exceptional Tor state with an internal normal multiple is assumed or proved. The normalization-sheet mixed-variance map and its framed endpoint connector 2-cells remain separate source data.

## 1. Fixed target, notation, and coefficient range

Use the established 215-generator loaded target. Let the short diagonal labels be

\[
x_i=(i,i+2)\pmod6,\qquad 0\leq i\leq5,
\]

and the long labels be D03, D14, D25. In words: the symbols x-i in this note label diagonals; they are not the two branch-function coordinates of the earlier node ring.

Every diagonal a has independent occurrence and normal variables X-a and u-a. The coefficient ring and generator stalks are

\[
R=\mathbb Z[X_a,u_a:a\in\mathcal D],\qquad
R[u_a^{-1}:a\in S\setminus H]\,[S,H].
\]

In words: only an unmarked normal appearing in the face admits its inverse. No integer, occurrence parameter, or external Rees parameter is inverted.

The homological degree is three minus face size plus number of marks. Radial differentials add a compatible diagonal with coefficient X-a/u-a and the lexicographic incidence sign. Normal-removal differentials have the prescribed signed localization-inclusion coefficient one. These are the exact source rules, not replacement maps between globally localized modules.

Retain

\[
V=F_V,\quad B=F_B,\quad K=F_K,\quad
E=K/V,\quad W=B/V,\quad Q=K/B.
\]

In words: V is the two-endpoint subcomplex, B the short-boundary subcomplex, and K the whole loaded target. W is a quotient complex and must not be confused with the monomials below.

Put

\[
U=u_{D03}u_{D14}u_{D25},\qquad
\gamma=\deg U,\qquad
\Delta=\prod_{i=0}^{5}u_{x_i}.
\]

In words: U is the old long-normal multiplier and Delta is the product of the six short normals.

For a subset P of the six short labels, let

\[
m_P=\prod_{a\in P}u_a,\qquad \lambda_P=\gamma+\deg m_P.
\]

In words: start at the previously computed marked-long-normal degree and add the indicated short-normal degrees. All generators and differentials in this slice retain their actual coefficient monomials.

At degree lambda-P, a loaded cell has the unique possible weight

\[
Um_P\prod_{a\in S}\frac{X_a}{u_a}.
\]

In words: it is legal precisely when every marked diagonal is either long or belongs to P. Higher positive exponents do not change this criterion. The 64 binary supports therefore cover all nonnegative short-normal degrees above gamma, up to their explicit common monomial factors. Other fine degrees, especially negative fine-degree localization sectors, are not classified by this cube.

## 2. Derive the relative complex with the full endpoints retained

Let

\[
r:E[-1]\longrightarrow V\oplus Q[-1]
\]

be the pair consisting of the endpoint connecting map and the generic quotient map. In words: a degree-one interior cycle is a marking; its full endpoint boundary and its actual Q restriction are prescribed, including comparison homotopies. This is a map of the target-side complexes, not the still-unconstructed normalization-sheet restriction.

We use homological shifts: C[-1] has term C at degree n+1 and differential minus d. The mapping-cone convention is recorded explicitly below, so there is no grading inference from names.

The labelled support splitting writes a chain of K as a triple in V, W, Q, with differential

\[
d_K=
\begin{pmatrix}
d_V&a&0\\
0&d_W&b\\
0&0&d_Q
\end{pmatrix}.
\]

In words: a is the actual short-support-to-endpoint incidence and b the actual generic-to-short-support incidence. There is no direct generic-to-endpoint incidence: every generic face is empty or contains a long diagonal, and a single differential cannot land at either all-short endpoint. Square-zero gives a times b equal to zero.

After first fixing the endpoint data, differences between lifts lie in

\[
\operatorname{fib}(E[-1]\longrightarrow V)\cong K[-1].
\]

In words: retaining the endpoint comparison homotopy restores the full endpoint summand; it does not replace it by two scalar equalities. Prescribing Q as well therefore leaves

\[
\operatorname{fib}(r)\simeq B[-1].
\]

In words: the full short-boundary complex is precisely the relative deformation complex.

Here is an explicit integral contraction, also checked in every grade. The mapping fibre has variables (w,q,v,h), with w in W at degree n+1, q in Q at n+1, v in V at n+1, and h in Q at n+2. Its differential is

\[
D(w,q,v,h)=
(-d_Ww-bq,-d_Qq,-d_Vv-aw,d_Qh-q).
\]

In words: keep both comparison variables and all off-diagonal incidences. Projection, inclusion, and homotopy are

\[
p(w,q,v,h)=(v,w-bh),\qquad
i(v,w)=(w,0,v,0),\qquad
H(w,q,v,h)=(0,-h,0,0).
\]

They satisfy

\[
pi=1,\qquad DH+HD=1-ip.
\]

In words: the extra generic mapping-cone pair contracts with coefficient one. No support denominator is changed, no endpoint term is dropped, and no averaging is used.

For compatible data a basepoint is supplied by the previous labelled coherent corridor and its existing facet/chamber transport witnesses. The checker reconstructs those witnesses and verifies their multiplication into each grade. The resulting matching fibre is a torsor for the Dold-Kan mapping space of the displayed relative complex; after selecting that inherited basepoint, its homotopy groups are groups in the usual sense. Incompatible prescribed data can instead give an empty fibre; the table below concerns the inherited matching data.

## 3. Equivariant reduction to the remaining short faces

Let N be the union of P and all three long labels. Project B at degree lambda-P onto the unmarked faces disjoint from N. They are exactly the nonempty compatible subsets of the remaining short labels.

This projection is an actual chain map. A discarded face contains a member of N forever: radial arrows only add diagonals and normal arrows leave the face unchanged. The kernel is thus a strict subcomplex.

For each kernel face S, choose the least member c of S intersect N. On its mark complex, insert c when it is absent, with the inverse normal sign. Explicitly,

\[
h_0[S,H]=
(-1)^{3-|S|+\#\{a\in H:a<c\}}
[S,H\cup\{c\}]
\]

when c is not marked, and zero otherwise. In words: the chosen normal provides a signed-unit contraction of that fixed-face block. All its coefficients are legal in the current grade.

If A denotes the radial operator, the correction

\[
H=\sum_{j\geq0}(-h_0A)^j h_0
\]

terminates because each additional radial factor increases face size. In words: the kernel contracts integrally even with radial arrows retained. The executable checker independently performs signed-unit reductions, retaining complete projection, inclusion, and homotopy matrices, and checks the contraction identity on every kernel generator.

Let Lambda-P be the simplicial complex of nonempty noncrossing subsets of the remaining short labels. Then

\[
H_j(B_{\lambda_P})\cong H^{2-j}(\Lambda_P;\mathbb Z)
\]

nonequivariantly. In words: the actual loaded relative data reduce to ordinary, not reduced, cochains on this induced short-face complex, with the indicated degree reversal.

The projection is equivariant, even though the chosen contracting homotopy need not be. The coefficient orientation character satisfies chi of rotation equals one and chi of reflection equals minus one. On a simplex the action also includes its vertex-permutation orientation.

Crucially, normal multiplication has a simple and **strictly compatible** description: adding one label to P restricts cochains to the induced complex obtained by deleting that label. The projection squares commute on every actual generator and its monomial. Thus the whole reduction is natural over the 64-vertex cube, not a list of unrelated quasi-isomorphisms.

The checker verifies all 192 multiplication arrows, all 240 squares, and all six dihedral transports of every grade. Proper grades use the group that preserves their normal support:

\[
G_P=\{g\in D_3:gP=P\}.
\]

In words: the full dihedral group acts on the whole cube, but only the stabilizer acts within one vertex. Reflection exchanges the odd and even three-normal branch degrees.

## 4. Exact moduli formula and integral computation

Let R-P denote the matching relative comparison space at degree lambda-P, with its inherited basepoint. Applying derived invariants to the actual relative complex gives

\[
\pi_n(\mathcal R_P)
\cong H^{1-n}_{G_P}(\Lambda_P;\mathbb Z_\chi),\qquad n\geq0.
\]

In words: components are degree-one equivariant cohomology, loops are degree-zero equivariant cohomology, and higher homotopy vanishes. Here equivariant cohomology means the total complex of group cochains with coefficients in the oriented simplicial cochains, with the additional character chi. It is not invariants taken only after discarding the simplicial differential.

The homological minus sign from shifting B is removed by the harmless basis sign (-1) to the power of the simplex degree. The normalized group bar differential and the simplicial differential are then totalized with the usual sign depending on group degree. The checker writes every matrix needed for cohomology degrees zero and one, including the outgoing degree-two equations.

No higher bar column can affect these groups: the simplicial cochains start at degree zero, so an element of total cohomological degree zero or one has group degree at most one, and its boundary has group degree at most two. This is a complete low-degree calculation, not extrapolation from finitely many group identities.

Exact rational row reduction computes ranks. Integral row and column operations compute the Smith factors of the incoming differential. Every nonzero factor is one or two. This proves the torsion as well as the free ranks: the quotient by the cycle subgroup is the free image of the outgoing differential, so it contributes no additional torsion. An independent full Smith decomposition agrees in all 64 cases.

### Complete classification

The entries in the pi-zero column describe groups after the inherited basepoint is chosen. A zero pi-zero group means one connected component. All homotopy groups of degree at least two vanish.

| Positive short normals | Stabilizer order | Number of grades | pi-zero | pi-one |
|---:|---:|---:|---|---|
| 0 | 6 | 1 | Z/2 | 0 |
| 1 | 1 | 6 | Z | Z |
| 2 | 1 | 6 | 0 | Z |
| 2 | 2 | 9 | Z/2 | 0 |
| 3 | 1 | 12 | 0 | Z |
| 3 | 1 | 6 | 0 | Z squared |
| 3 | 3 | 2 | 0 | Z |
| 4 | 1 | 6 | 0 | Z |
| 4 | 2 | 6 | 0 | Z |
| 4 | 2 | 3 | Z/2 | 0 |
| 5 | 1 | 6 | 0 | Z |
| 6 | 6 | 1 | 0 | 0 |

The complete labelled records, stabilizers, matrix ranks, Smith factors, and available nullhomotopies are in the certificate. The count of grades sums to 64. All 13 torsion cases are accounted for by the transported original parity class; no additional independent order-two class appears in this cube.

At P empty, Lambda consists of two filled triangles, on the odd and even short labels, joined by the three compatible cross-edges. This recovers the earlier two contractible components.

At P equal to the odd triple, the remaining complex is the even filled triangle. Its stabilizer is the cyclic order-three group and the orientation character restricts trivially. The matching relative space is therefore

\[
\mathcal R_{\{x_1,x_3,x_5\}}\simeq K(\mathbb Z,1).
\]

In words: one component remains, but it has an integer group of comparison loops. The even-triple case is its reflected counterpart. This calculation does not assign the full dihedral action to either branch separately.

At P equal to all six short labels, the remaining complex is empty. Consequently

\[
\mathcal R_{\{x_0,x_1,x_2,x_3,x_4,x_5\}}\simeq *.
\]

In words: the matching relative fibre is contractible after full short-normal multiplication. The mechanism is given next.

## 5. Follow the actual parity class, not just group orders

The old marked-long generic class is

\[
\omega=UT-\sum_{i=0}^{2}X_{D_i}\frac{U}{u_{D_i}}M_i.
\]

In words: it is the corrected chamber using the three existing marked long normals. Its lift into E has an 18-term short-support boundary beta.

Projection to the residual short-face cochains sends beta to the sum of the remaining vertices. If eta is zero on rotations and one on reflections, the relative parity class is represented by eta times that sum. Its double is the bar boundary of minus the same vertex sum.

The finite nullhomotopy test in the checker is complete for this specific class. A prospective primitive is a function on vertices that must be constant on each connected component and invariant under rotations. On a reflection-related pair of components, the two values must sum to minus one. If reflection fixes a component orbit, this would require twice an integer to be minus one and is impossible. Otherwise, choose zero on one side and minus one on the other. Therefore checking these zero/minus-one assignments covers every possible integral solution, not merely a bounded search radius.

This class is nonzero exactly in the 13 torsion cases of the table. Some other grades have free component or loop groups, but those are not additional copies of the original parity.

## 6. The full lifting chain includes both endpoint corrections

The full 45-term polynomial top cycle is

\[
\Omega=
\sum_{S\in\mathcal F}
(-1)^{|S|(|S|+1)/2}
\left(U\Delta\prod_{a\in S}\frac{X_a}{u_a}\right)[S,S].
\]

In words: every noncrossing face contributes its fully marked state. Every coefficient is polynomial, because U times Delta contains all nine normal factors. No displayed quotient introduces an inverse into a marked stalk.

Direct calculation gives

\[
d_K\Omega=0,\qquad \pi_Q\Omega=\Delta\omega.
\]

In words: multiplication by Delta allows the corrected generic top cycle to lift to an actual closed top chain, including the endpoint terms.

There are 43 terms in its image in E and two fully marked endpoint terms in its V part. Writing those parts as Omega-E and Omega-V gives

\[
\delta\Omega_E=-d_V\Omega_V.
\]

In words: the endpoint restriction of the lifted loop is not silently set to zero; the two endpoint tops provide its explicit nullhomotopy.

There is a 39-term filler in B/V and, after restoring these endpoint corrections, a 41-term filler in B:

\[
t_E=\Delta\widetilde\omega-\Omega_E,\qquad
t_B=\Delta\widetilde\omega-\Omega=t_E-\Omega_V,
\]
\[
d_Et_E=\Delta\beta,\qquad d_Bt_B=\Delta\beta.
\]

In words: the same generic discrepancy becomes exact in the appropriate support complex, but the fully endpoint-framed equation uses two more terms than the endpoint quotient equation.

Both Omega and omega transform by the orientation character. Thus eta times Omega lifts the multiplied generic comparison loop, with eta times Omega-V retaining its endpoint nullhomotopy. Equivalently, the appropriate signed eta times t-B is a boundary witness for the multiplied relative parity class.

The exact all-polynomial top-cycle classification supplies a useful control. If a top chain has chamber coefficient c, the singleton-face equations force every u-a to divide c. All other coefficients are then forced by induction over face size. Hence

\[
H_3(K)=R\Omega,\qquad H_3(E)=R\Omega_E,\qquad
H_3(Q)=R\omega,
\]

and the top map into Q is multiplication by Delta. In words: this is an integral divisibility statement across the actual coefficient domains, not a choice of an attractive filler. In particular, the cyclic ordinary support class beta has annihilator the principal ideal generated by Delta. This is normal-parameter torsion, not integer torsion.

The new conclusion about parity is more precise than this ordinary annihilator statement: the full endpoint-framed deformation calculation and the bar cocycles show exactly how the old order-two relative class is identified under this multiplication, while the other intermediate grades can retain loops or discrete choices.

## 7. Why full multiplication is not a physical parity selection

The primitive endpoint classes themselves have smaller, branch-specific annihilator ideals. At the positive endpoint the topological label is the odd triple; at the negative endpoint it is the even triple. The corresponding degree-zero endpoint module is the last quotient of the three-normal Cech complex.

For the positive endpoint, suppressing its fixed generator line, this quotient is

\[
\frac{R[u_{x_1}^{-1},u_{x_3}^{-1},u_{x_5}^{-1}]}
{R[u_{x_3}^{-1},u_{x_5}^{-1}]+R[u_{x_1}^{-1},u_{x_5}^{-1}]+R[u_{x_1}^{-1},u_{x_3}^{-1}]}.
\]

In words: a Laurent monomial survives only when all three branch normals occur with negative exponent. The primitive class has exactly one inverse of each branch normal, multiplied by its nonzero occurrence factor and U.

It follows for arbitrary polynomials that

\[
\operatorname{Ann}_R[e_+]=(u_{x_1},u_{x_3},u_{x_5}),\qquad
\operatorname{Ann}_R[e_-]=(u_{x_0},u_{x_2},u_{x_4}).
\]

In words: multiplying by any normal at an endpoint makes that endpoint's primitive class a boundary. The converse follows from the independent Laurent monomial basis. No integer annihilates either primitive class.

The witness is already in the target. For a short normal a belonging to the endpoint, the allowed coefficient-weighted one-mark state has boundary u-a times the unmarked primitive endpoint. The checker verifies the entire endpoint normal-cube contraction, not just that one equation.

Consequently Delta kills both endpoint classes. The map from the two-component original fibre to the terminal contractible fibre **forgets their distinction**. It does not choose one of the original components. Nor does the resulting contractibility demonstrate preservation of a nonzero primitive endpoint normalization under this operation.

There is no contradiction with using derived endpoint data throughout: the multiplied endpoint chains are retained as specified, now exact, objects together with their homotopies. The statement is that their original homology classes no longer provide the same nonzero readout.

## 8. Consequence for the remaining physical construction

A proposed source-defined physical comparison now faces a sharper test. Its actual external Tor generator and its branch endpoint maps must determine which part of this normal diagram is relevant, and must specify the induced endpoint homotopies. Neither choosing a branch nor multiplying by all normals can be advertised as a canonical parity choice: the first retains integer loop freedom in the corresponding branch degree; the second identifies the old choices while killing both primitive endpoint classes.

This does not obstruct a genuinely extraordinary/logarithmic correspondence. It excludes using these particular coefficient operations as a substitute for deriving that correspondence. In particular, the occurrence ideals at the normalization branches, these normal annihilator ideals, and the external Cartier/Rees parameters remain distinct despite sharing diagonal labels.

The physical reflection parity remains unassigned. The full source map into this now-computed target-side relative restriction is still required.

## 9. Reproduction and provenance

Run:

```sh
python check_marici_endpoint_normal_cube_relative_fibre.py \
  --output marici_endpoint_normal_cube_relative_fibre_certificate.json
```

The self-contained Python 3.10+ checker uses only the standard library and passes **894,553 exact assertions**. These cover full mapping-fibre contractions, normal-kernel contractions, all 64 grades, all multiplication arrows and squares, actual group transports, integral bar and Smith computations, inherited coherent basepoints, the 18-term support class, and the full endpoint-corrected top filler. An independent SymPy full Smith decomposition was also run on all 64 small bar matrices and agreed with the standard-library result.

Assertion counts are not proofs of the unbounded statements. The support criterion, kernel-contraction argument, Laurent-monomial annihilator proof, and complete bar-degree bound establish the claims outside individual matrix entries. No proof assistant was used and no repository file was modified.

Repository inputs at the pinned commit:

- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: the target stalks, differential, and support filtration.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: endpoint labels, corridor, and endpoint-swapping reflection.
- `src/ledger/20260814-117 D03 Thom Endpoint Koszul Hull and the Missing Road Generizations.md`, blob `af6874dc6928614a824a14105fa8e4ba37d96306`: the distinction between independent external Thom/Tor data and actual endpoint maps.
- `research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs`, blob `592811b138855554c921dcf4269581632e8f0050`: the separate physical restriction problem.

Preceding local artifacts: `marked_normal_q_extension.md`, `check_marked_normal_q_extension.py`, and `actual_q_graded_restriction.md`. Their sector and physical-comparison qualifications remain in force. Common helper code is included in the new checker; those files are not runtime dependencies.

General conventions: Stacks Project, Group cohomology, tag `0A2H`; Hom complexes, tag `0A8H`; Cones and termwise split sequences, tag `014D`. The specific homotopy groups and comparison maps above are derived here, not attributed to these general references.
