# Branch B: native bar action, forward quotient test, and the uninstantiated physical collar

Date: 2026-09-08

## 0. Result and source boundary

The physical control complex requested in the task cannot yet be instantiated from the retrieved materials. This is not a computed nonexistence result for the modified physical collar. The complete Branch C framed endpoint matrices, Branch A's three new marked target models, and the cross-branch comparison maps were not recovered. The retrieved Branch C continuation brief explicitly leaves its bivariant map `b_*` to be constructed.

The retained Branch B operation-interface bundle is present and executable. Its checker was rerun and passed 179,709 assertions. The new calculation below constructs native bar-cochain operations without replacing the bar source by its cohomology, lists all 56 canonical seed images on each ideal endpoint, separates the branch module from the ideal endpoint module, tests the forward quotient, and verifies the graded control differential and full abstract dihedral bimodule action. Its certificate leaves physical seed images and physical control cohomology unset.

Two kinds of missing data must be separated. The groups of the requested control complex require actual assignments of the square's objects, the maps `a,p`, and their operation structures. The affine obstruction to filling that square additionally requires `b,c` and the specified homotopy between their boundary composites. Knowing a previously obstructed point `(1,1)` does not determine either collection of matrices for a new comparison target.

### Input inventory

| Input | Status in this calculation |
|---|---|
| Branch B operation-collar interface and three coefficient checkers | Available; read and rerun |
| Native alternating coefficient algebra and its 49 relative generators | Explicit; retained |
| Branch C's 128/1024 state counts and reported primitive endpoint obstruction | Reported in task/continuation brief; not substituted for matrices |
| Complete 128/1024-state differential, frame dictionary, endpoint maps and comparison homotopies | Not recovered |
| Older Branch A full normalization and scalar tangential proofs | Retrieved from repository commit `538594ab137c4459e11a5ee9d8e0bf6e1dfd1bf0` |
| Marked target D35, six-state compensating target, and mixed-product cofiber with their current structural maps | Named in task; full models not recovered |
| Cross-branch physical comparison and its operation intertwining matrices | Not supplied by the inspected material |

The successful older scalar pairing is not substituted for any of these missing physical maps.

## 1. The native bar complex and its coefficient operations

Use the established augmented ring

\[
B=C[X_{13},X_{15},X_{35},X_{02},X_{04},X_{24}]/(I_+I_-),
\qquad I_+=(X_{13},X_{15},X_{35}),\quad I_-=(X_{02},X_{04},X_{24}).
\]

The spectator ring C retains its existing parameters. The bookkeeping parameter lambda may be adjoined to C; it is not identified with a normal coordinate or with beta.

For a coefficient module N equal to C, either normalization branch B_sigma, or either ideal I_sigma, use the normalized relative bar resolution

\[
\mathsf P_n(N)=B\otimes_C\overline B^{\otimes_C n}\otimes_C N.
\]

These are free B-modules, since the indicated modules have their single-sheet monomial C-bases. The differential is

\[
\begin{aligned}
d(b_0[b_1|\cdots|b_n]m)
={}&b_0b_1[b_2|\cdots|b_n]m\\
&+\sum_{i=1}^{n-1}(-1)^i b_0[b_1|\cdots|b_ib_{i+1}|\cdots|b_n]m\\
&+(-1)^n b_0[b_1|\cdots|b_{n-1}](b_nm).
\end{aligned}
\]

In words: multiply adjacent factors, including the last module action. Opposite-sheet products are zero in the actual coefficient algebra. Polynomial products are not truncated in the checker.

On the associated bar cochains, use the usual cohomological bar convention `delta f=f d`; this is related to the standard internal-Hom convention by the usual degreewise sign rephasing. The concatenation cup action on

\[
\mathsf C^*(N)=\operatorname{Hom}_B(\mathsf P_*(N),C)
\]

satisfies

\[
\delta(\alpha\smile f)=\delta\alpha\smile f+(-1)^{|\alpha|}\alpha\smile\delta f.
\]

For each occurrence label i, let alpha_i be the one-bar cochain extracting the coefficient of X_i. It is closed, of cohomological degree one and internal occurrence weight minus the i-th unit vector.

Within one sheet there are explicit bar homotopies. Let b_ij extract minus the coefficient of X_i X_j. Then

\[
\delta b_{ij}=\alpha_i\alpha_j+\alpha_j\alpha_i\quad(i\ne j),
\qquad
\delta b_{ii}=\alpha_i^2.
\]

The six linear bar cochains therefore do not satisfy the exterior relations strictly. The bar differential is retained, rather than replaced by the exterior cohomology algebra.

The relative algebra is free on the prescribed 49 nested commutators. Sending each generator to the same nested graded commutator in the closed alpha_i gives a genuine dg-algebra map

\[
T_C(V)\longrightarrow\mathsf C^*(C).
\]

Consequently cup product defines a chain-level relative-operation action on every displayed native coefficient-Hom complex. No formality theorem is needed for this map: the domain is free and its chosen generators map to cocycles. This does not assign an action to the raw 128-state, 1024-state, or 215-state physical complexes.

### The eighteen quadratic tests

For each positive i and negative j,

\[
\widetilde r_{ij}=\alpha_i\alpha_j+\alpha_j\alpha_i.
\]

For the positive branch unit, `[X_i|X_j]1` is a cycle after conductor tensor; the positive first product and the opposite-sheet module product vanish. The cochain tilde-r evaluates to one. On the negative branch use `[X_j|X_i]1`. Thus all nine mixed operations act nontrivially on the unit of each branch coefficient-Hom module.

For the 56-seed ideal modules, fix the seeds m35 and m04. The analogous cycles are `[X_i|X_j]X35` and `[X_j|X_i]X04`. Again each evaluation is one. The nine weights on each endpoint are distinct, so these are eighteen independent primitive coefficient classes. Their full native-word images are recorded, not only their evaluations.

This is a coefficient action. Identifying these marked coefficient vectors with Branch C's framed nu_plus and nu_minus requires the missing physical frame/comparison map.

## 2. The branch bar source and the 56-seed module are not the same module

Write E for the native Yoneda algebra and J_sigma for its left ideal of words ending in a nonempty sigma-sheet exterior block. The established normalization action gives

\[
\operatorname{Ext}_B^*(B_\sigma,C)=E/J_\sigma.
\]

As a relative-operation module, this has eight opposite-sheet exterior seeds:

\[
E/J_\sigma\cong\mathcal R\otimes_C\Lambda_C(C^3_{-\sigma}).
\]

The 56-seed module requested in the task is instead

\[
M_\sigma^q=\operatorname{Ext}_B^q(I_\sigma,C)=J_\sigma^{q+1},
\qquad
M_\sigma\cong\mathcal R\otimes_C W_\sigma.
\]

Its seeds are

\[
W_\sigma=\Lambda_C(C^3_{-\sigma})\otimes_C\Lambda_C^{>0}(C^3_\sigma),
\qquad |w_{O,P}|=|O|+|P|-1.
\]

In words: take any opposite-sheet subset O followed by a nonempty own-sheet subset P. There are 56 possibilities. Their degree counts are 3,12,19,15,6,1. Their occurrence weights are minus the six-coordinate multiplicity vectors.

This distinction is supplied by the actual coefficient sequence

\[
0\longrightarrow I_\sigma\longrightarrow B_\sigma\longrightarrow C\longrightarrow0.
\]

The bare bar formula with a normalization-branch final factor resolves B_sigma. Recovering the 56-seed module therefore requires retaining this augmentation fibre or an explicitly equivalent supported construction. The meaning of the native supported final factor must be checked against the actual Branch C source, not inferred from the bar shape alone. The three-normal and product-Cartier factors cannot be assumed to perform that identification merely from their ranks. No assertion is made that Branch C's unretrieved full source omits the fibre; its actual comparison must be read.

The new checker independently verifies the eight-seed quotient factorization by integral unit pivots through degree five. The retained predecessor verifies the full 56-seed factorization through degree six; the supplied algebraic factorization proves its all-degree form.

## 3. All 56 forward quotient images and the endpoint obstruction

For every one of the 56 seeds, the canonical permitted quotient has exactly the image

\[
\pi_\sigma(r\otimes w)=\epsilon(r)w.
\]

Thus its kernel is

\[
\ker\pi_\sigma=\mathcal R^+\otimes_CW_\sigma.
\]

All eighteen quadratic classes, every positive relative-operation descendant, and all decomposable reflection products lie in this kernel. Every nonzero pure seed remains nonzero in the quotient. The certificate enumerates all 112 seed records with degrees, labels, bar representatives, and quotient images.

The requested physical seed images are a different set of data. They are explicitly `null` in the certificate, with a reason, rather than filled with zero or assigned the canonical quotient images.

This yields an immediate test for the proposed comparison kernel. If the identified physical endpoint class has nonzero seed projection, then

\[
\pi_\sigma[\nu_\sigma]\ne0.
\]

The canonical quotient alone then cannot place that endpoint in the comparison fibre. It kills the operation descendants, but not their generating endpoint. In particular it cannot by itself change a nonzero seed-level endpoint pair to the coefficient-null pair.

More generally, any operation-linear map to an augmentation target is determined by a seed map ell:

\[
f=\ell\pi_\sigma.
\]

An endpoint class can enter its kernel only if ell kills its seed projection. Killing all descendants is not sufficient. Once a relative kernel contains a class m and is an operation submodule, it must also contain the entire submodule R m. For a chosen free seed, its quotient can be written explicitly, but no such further quotient is admitted as the physical comparison without a support-defined map.

## 4. Ordered products are not relative generators

Put a=eta04 and b=eta35. Their coproducts satisfy

\[
\Delta(ab)=ab\otimes1+a\otimes b-b\otimes a+1\otimes ab,
\]

\[
\Delta(ab+ba)=(ab+ba)\otimes1+1\otimes(ab+ba).
\]

The ordered class has nonzero exterior image. Its sum with the reverse order is primitive and has zero exterior image. Both statements are checked in the actual native Hopf algebra.

The ordered class and the relative anticommutator are independent over C, with integral unit pivots in their two-dimensional mixed quadratic word lattice. Multiplying by beta squared does not identify them. After beta inversion both remain nonzero; beta=0 kills those particular beta-squared multiples, not the unscaled relative generator or the nonsplit dualizing object.

A nullhomotopy for beta-squared ab does not give a nullhomotopy for beta-squared (ab+ba). The missing term is the reverse product. As an algebraic negative control, modulo the left ideal generated by ab, the relative generator is represented by the nonzero word ba. This is not a computation of Branch A's geometric mixed-product cofiber.

For a defined map phi:X->Y between dg operation modules, a cofiber action requires its generator intertwiners. In cohomological conventions an operator of degree k can be represented on the cofiber by

\[
\rho_{\operatorname{Cone}\phi}(g)=
\begin{pmatrix}
\rho_Y(g)&(-1)^k h_g\\
0&(-1)^k\rho_X(g)
\end{pmatrix},
\qquad
\partial h_g=\rho_Y(g)\phi-\phi\rho_X(g).
\]

This gives the exact matrix test for the cofiber candidate once the actual modules, map and line shifts are present. Attaching a cofiber in the coefficient category alone does not supply these additional action matrices on a separately specified physical target.

## 5. Symmetry on bar representatives and on the obstruction resolution

The supplied six labelled dihedral permutations act strictly on the native coefficient ring and its bar resolution. The 49 chosen cohomology generators transform by the full supplied relative-algebra formulas, including products.

Their chosen bar representatives need not obey these formulas strictly, because same-sheet exterior relations hold there through the b_ij homotopies. For each of the 294 transported generators the checker constructs an explicit cochain H satisfying

\[
\delta H_{s,g}=s(\widetilde g)-\widetilde{s(g)}.
\]

The algorithm repeatedly replaces an out-of-order same-sheet adjacent pair using its b_ij boundary; repeated adjacent labels use b_ii. It terminates by the finite inversion count, and supplies an integral homotopy with one quadratic-extraction cochain in each term. Every differential identity is checked before passing to cohomology.

These are first comparison homotopies for the native bar representatives. They do not by themselves assert all higher physical group/action coherences. The abstract relative algebra and its bimodule resolution, however, carry the complete strict labelled group action already specified by the source.

For the free-algebra bimodule resolution,

\[
0\longrightarrow\mathcal R\otimes V\otimes\mathcal R
\xrightarrow{\partial}\mathcal R\otimes\mathcal R
\longrightarrow\mathcal R\longrightarrow0,
\]

\[
\partial(a\otimes g\otimes b)=ag\otimes b-a\otimes gb.
\]

Symmetry is defined by the universal noncommutative derivative, not by a permutation of generator labels. For example, if s(g)=-g+[r21,r12],

\[
s(d_{\rm nc}g)=-d_{\rm nc}g+(d_{\rm nc}r21)r12+r21(d_{\rm nc}r12)
 -(d_{\rm nc}r12)r21-r12(d_{\rm nc}r21).
\]

Every derivative term is retained. The checker verifies all 294 matrices and all 1,764 ordered group compositions on them. It also checks group-bar d-squared on the whole 96-dimensional operation-degree-four coefficient module, which contains all quadratic products and the degree-four indecomposables. No averaging is used.

## 6. The exact control differential once the physical maps are supplied

All formulas in this section are cohomological. Let D=cofib(a) and F=fib(p), formed in the specified filtered coefficient diagram, with support and determinant lines retained. Choose cofibrant coefficient models when required; do not turn localized terms into their conductor images.

The standard models are

\[
D^n=X^n\oplus A^{n+1},\qquad
 d_D(x,u)=(d_Xx+a(u),-d_Au),
\]

\[
F^n=Y^n\oplus Z^{n-1},\qquad
 d_F(y,z)=(d_Yy,p(y)-d_Zz).
\]

Define

\[
C_0=R\operatorname{Hom}_{C[\lambda]}(D,F),\qquad
C_1=R\operatorname{Hom}_{C[\lambda]}(V\otimes_CD,F).
\]

Each Hom here is taken with the required internal weights, normal lines and allowed supports, and can itself be a diagram before normal/Čech totalization. For homogeneous f of degree n and a generator g of degree k,

\[
\delta(f)(g,m)=f(gm)-(-1)^{kn}g f(m).
\]

The operation control is

\[
L_{\rm op}=\operatorname{fib}(C_0\xrightarrow{\delta}C_1),
\quad
L_{\rm op}^n=C_0^n\oplus C_1^{n-1},
\quad
 d(f,h)=(\partial f,\delta(f)-\partial h).
\]

The checker tests the internal-Hom and intertwiner signs with nonzero source/target differentials and both odd and even operation degrees. These are sign tests, not synthetic substitutes for the physical complexes.

Normal and Čech directions are totalized with their Koszul signs. The row filtration remains encoded by lambda throughout; no contraction requiring a negative lambda degree is allowed. If strict action models are chosen, the group-cochain differential is

\[
\begin{aligned}
(\delta_Gc)(g_1,\ldots,g_{q+1})
={}&g_1c(g_2,\ldots,g_{q+1})\\
&+\sum_{i=1}^{q}(-1)^i c(g_1,\ldots,g_ig_{i+1},\ldots,g_{q+1})\\
&+(-1)^{q+1}c(g_1,\ldots,g_q).
\end{aligned}
\]

Thus the full requested complex is the product totalization of the normal/Čech diagram and these group cochains of L_op. With group degree first, its differential is delta-G plus (-1)^q times the internal differential. For homotopy-coherent physical actions, their higher structure maps must be included or a specified strict replacement supplied.

The resolution length one concerns only the relative-operation bimodule direction. It supplies no bound on the physical Hom, normal, Čech or group-cochain directions. A safe finite truncation for H1,H0,Hminus1 must follow from the actual grades and matrices, not from the freeness of R.

### Exact first missing entries

Even before the operation differential is evaluated, the following structural entries are absent from the retrieved data:

1. an assignment of the framed physical complexes to A,X,Y,Z and the actual maps a and p for each of the three target choices;
2. the common coefficient-base change and the identifications of the ordered source/frame lines;
3. the cross-branch b_sigma map on the complete framed endpoint source, beginning with the coefficient column representing its primitive endpoint point;
4. the image of each of the 56 ideal seeds in the actual comparison-Hom complex, including its prescribed degree, occurrence weight and support.

The first quadratic block that cannot currently be evaluated is

\[
\delta(f)_{r_{04,35}}
 =f\rho_D(r_{04,35})-\rho_F(r_{04,35})f
\]

for degree-zero f. It needs the actions on the chosen cone/fibre models and the intertwiner for p, not merely the already known native word r. Its operator degree is two, its intrinsic occurrence weight is minus e04 minus e35, and its bookkeeping-lambda degree is zero. The external determinant and normal grades must come from the unrecovered frame dictionary.

The retrieved Branch C brief calls the corresponding map b_* an unconstructed bivariant comparison. Its coefficient-null endpoint map is not a replacement for this missing map.

## 7. Comparison of the three Branch A target choices

| Target choice | Supported conclusion | Required additional data for this task |
|---|---|---|
| Unchanged marked D35 | The source reports the nonzero ordered mixed continuation class beta-squared eta04 eta35 for the specified rank-one-layer problem. This is not automatically the relative anticommutator obstruction. | Complete marked target/restriction matrices, framed endpoint comparison, and generator intertwiners |
| Reflection-closed six-state compensation | The current task names this enlargement. Its six-dimensional state count does not determine its differential or operation action. | Six occurrence-action matrices or equivalent resolved model, its inclusion/projection and determinant/frame dictionary |
| Mixed-product cofiber | A cofiber of the specified ordered map nullifies that map through its canonical cofiber homotopy. It does not automatically kill the reverse ordered product or all endpoint orbits. | Defining chain map, source/target actions and the h-g entries displayed above, plus physical restriction maps |

None of these three operation-equivariant physical squares was instantiated in this run. Their relative control groups are not reported as zero or identified with one another.

## 8. Six obstruction types remain separate

The available data give the following independent tasks, not a proved direct-sum decomposition of one computed H1:

- the coefficient comparison discrepancy `(1,1)` reported by Branch C;
- eighteen quadratic endpoint-operation classes, explicitly tested in the native bar models;
- Branch A's ordered beta-squared eta04 eta35 continuation class;
- the relative anticommutator r04,35 and its full operation orbits;
- the product terms in labelled reflection and their noncommutative derivatives;
- the lambda-torsion defect of the normalization/conductor row filtration.

The first three can occupy related ordinary degrees only after their respective source shifts are specified. The ordered class and anticommutator have the same intrinsic weight but different coproducts. The filtration defect uses a different parameter and cannot be absorbed by beta specialization or by applying the unfiltered normalization contraction.

## 9. Reported cohomology and exact execution scope

For the actual physical collar, H1, H0 and Hminus1 are all **not computed**. Its differential is not specified by the recovered inputs. This is different from an obstructed/empty completed square and different from a computed nonzero group. In particular, the known same-target `(1,1)` obstruction is not being repackaged as the full H1 of the new target choices.

The executable input gate rejects missing maps; it never replaces them with zero. All 112 physical seed-image slots are explicitly unset. The manifest states exactly which matrices, supports, actions and frame records are needed to continue.

The new run passes 32,493 exact assertions. It includes the free native bar differential, the quadratic bar primitives, all eighteen endpoint tests, the 112 seed records, the eight-seed branch-module factorization, all 294 bar transport homotopies, the full abstract noncommutative symmetry checks, group-cochain sign tests, and the graded Hom/control sign tests. The fresh inherited replay passes 179,709 assertions and is included separately.

No 128-state or 1024-state physical matrix was reconstructed from its rank, no proof assistant was used, and no repository file was modified.

## References and provenance

- Retained local input: `marici_operation_collar_interface_20260908.md` and its supplied checker bundle. All input hashes and the fresh replay are included.
- Retrieved Branch C continuation brief: *construct the comparison-fibre Hom complex and test the minimal bivariant endpoint map*, uploaded 2026-09-08 14:04:36 UTC. This is a task/status source, not the unrecovered matrix certificate.
- Retrieved Branch A continuation brief: *two-grade duality and obstructed conormal-extension leg of the physical-collar pullback*, uploaded 2026-09-08 13:17:00 UTC. The current task additionally names the three later target choices.
- Repository source inspected: `research/chatgpt/branch_a_full_normalization_duality_and_two_grade_trace_proof.md` and `branch_a_tangential_duality_scalar_pairing_proof.md`, commit `538594ab137c4459e11a5ee9d8e0bf6e1dfd1bf0`. Neither was used to supply unspecified physical endpoint columns.
- Stacks Project, tags `0A8H` (Hom complexes), `0FQ2` (dg-module Hom), and `0B6A` (global derived Hom), for the mapping-complex conventions.
