# The punctured target differential and the exact obstruction to jet-only comparison

Date: 2026-09-07  
Lane: Branch B — coefficient reconstruction and source-to-target comparisons  
Baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The previous formal-punctured gluing theorem reconstructed the fourteen-channel source, but warned that 128 nonzero PC coefficient summands vanish in every finite occurrence jet. Here that warning is turned into an exact map-level calculation.

Those summands form an actual subcomplex. Removing them produces a 72-term quotient with eighteen independent top cycles. Exactly which of these cycles lift to the full target is controlled by a surjective, explicitly computed seventeen-channel module map. Its target is three copies of the alternating ring and seven copies of each normalization branch. Both endpoint channels occur in this obstruction module. A single endpoint unit is a compatible cycle in every finite jet and nevertheless has no lift to the flat-completed target.

The intrinsic conductor fibre of this obstruction module has ranks 17, 42, 168, 644, 2478, and onward. The earlier singular source-to-target rank discrepancy is its Tor exact sequence, not an independent phenomenon.

Finally, applying derived Hom to the actual formal-punctured target reconstruction gives the complete mapping-space gluing formula. It applies to the nonperfect coefficient source by adjunction; no unjustified tensor–Hom base-change equivalence is used. In the top-degree source placement, map gluing is a discrete compatibility problem, and the computed row obstruction supplies its central-chart closure test.

These are results about the existing PC coefficient target and the previously constructed, target-selected source. They do not identify a native physical source, convert a supported or contravariant operation into a covariant map, create endpoint connector cells, or justify new physical inverses.

## 1. Fixed rings, grading, and the two different target comparisons

Use the original labels

\[
S_+=\{13,15,35\},\qquad S_-=\{02,04,24\},\qquad L=\{03,14,25\}.
\]

In words: the positive and negative occurrence sheets each have three short labels, while the long occurrence and normal labels stay independent.

On the existing common chart define

\[
C=\mathbb Z[X_l,u_l:l\in L][t_s^{\pm1}:s\in S_+\cup S_-],
\]

\[
B=C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,\ m\in S_-),
\quad I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-).
\]

In words: only the short Rees parameters already invertible on the common chart are units. No long normal or long occurrence is inverted globally. Opposite-sheet occurrences multiply to zero.

Put

\[
I=I_++I_-,\qquad B_+=B/I_-,\qquad B_-=B/I_+,
\qquad \widehat B=\varprojlim_n B/I^n.
\]

In words: the branch quotients are polynomial rings over C; the completion is along the occurrence conductor. Its branch quotients are denoted by \(\widehat B_\pm\).

Let F be the original 215-state PC complex restricted to this chart, in homological degrees zero through three. A generator is a noncrossing face and a subset of marked labels, written \([A,H]\). Its coefficient module is

\[
B[u_a^{-1}:a\in A\setminus H],\qquad u_s=t_sX_s\quad(s\in S_+\cup S_-).
\]

In words: the short-normal localization also localizes its occurrence coordinate, because its Rees parameter is already a unit here. The long-normal localizations remain cell-specific.

The supplied differential is

\[
d[A,H]=\sum_{a\ {\rm addable}}\epsilon(A,a)\frac{X_a}{u_a}[A+a,H]
+(-1)^{3-|A|}\sum_{h\in H}(-1)^{\operatorname{pos}_H(h)}[A,H-h].
\]

In words: retain the occurrence/normal ratio on radial arrows and the signed localization on mark-removal arrows. The apparent cancellation \(X_s/u_s=t_s^{-1}\) on a radial short arrow is only inside that arrow's localized target module.

If both polarities are localized, the coefficient module is zero: an opposite-sheet product would be both zero and invertible. There are fifteen such states. The other two classes of summands are the following.

| Coefficient summands | Count | Homological degree counts |
|---|---:|---|
| At least one short occurrence inverted, only one polarity | 128 | 8, 54, 66 in degrees 0, 1, 2 |
| No short occurrence inverted | 72 | 27, 45 in degrees 2, 3 |

The localized set can only increase along a differential arrow. Consequently the first class is a subcomplex P, not a freely chosen collection of discarded cells. Define the quotient F0 by

\[
0\longrightarrow P\longrightarrow F\xrightarrow{q}F_0\longrightarrow0.
\]

In words: the 72-term complex is the quotient by the actual punctured coefficient subcomplex. This exact sequence is termwise split as modules, but is not asserted split as complexes.

Every term is flat over B. If a short occurrence is invertible in a term of P, then tensoring with B modulo any positive power of I gives zero. Thus

\[
P\otimes_B^L B/I^n=0,\qquad
F\otimes_B^L B/I^n\simeq F_0\otimes_B^L B/I^n\quad(n\ge1).
\]

In words: every finite jet erases exactly this subcomplex. This does not imply that P vanishes after flat completed base change. Write \(\widehat F=F\otimes_B\widehat B\), and similarly for P and F0. Noetherian completion is flat [M2], so the displayed exact sequence survives, with 128 nonzero localized summands in \(\widehat P\).

F0 is an intermediate quotient, not a synonym for derived completion. In particular, its long-localization modules can still have different flat-basechanged and inverse-limit completions. No identification of these operations is used below.

## 2. Solve the seventy-two-term quotient's complete top kernel

Let N run over the noncrossing subsets of short labels. There are eighteen:

\[
1+6+9+2=18.
\]

In words: one empty support, six singletons, nine pairs, and two endpoint triples. Fourteen nonempty supports lie entirely on one sheet. The other three are

\[
\{02,35\},\qquad\{04,13\},\qquad\{15,24\}.
\]

In words: the mixed short edges form a matching between the two triangles.

Define

\[
L_N=\{l\in L:N\cup\{l\}\text{ is noncrossing}\},\qquad
U_N=\prod_{l\in L_N}u_l,\qquad
s_n=(-1)^{n(n+1)/2}.
\]

In words: retain the exact compatible long labels and the inherited orientation. The empty product is one.

The eighteen top cycles in F0 are

\[
\Omega_N=s_{|N|}U_N[N,N]
+s_{|N|+1}\sum_{l\in L_N}X_l
 \left(\prod_{k\in L_N\setminus\{l\}}u_k\right)[N+l,N+l].
\]

In words: each fully marked short support carries its required long-normal corrections. This formula uses products, not division by a long normal.

For completeness, write the coefficient of a fully marked face A as \(s_{|A|}v_A\). A row that removes a marked long label l forces

\[
u_l v_{N+l}=X_l v_N.
\]

In words: long normalization and radial attachment must agree. The long parameters remain independent; \(X_l\) is a nonzerodivisor modulo \(u_l\). Therefore \(u_l\) divides \(v_N\). Applying this to every compatible long label gives

\[
v_N=U_Nb_N,\qquad
v_{N+l}=X_l\left(\prod_{k\in L_N\setminus\{l\}}u_k\right)b_N.
\]

In words: there is exactly one coefficient \(b_N\in B\) for each support. Long diagonals cross pairwise, so these equations exhaust the top long rows. There are no degree-four boundaries. Hence

\[
H_3(F_0)=\bigoplus_N B\Omega_N\cong B^{18}.
\]

This holds before completion. Flatness gives the corresponding statement with \(\widehat B\). The checker independently solves the actual 45-column top matrix in 5,184 homogeneous coefficient degrees, including negative long-normal exponents only where their localization modules permit them. It never infers these equations from a count of cells.

## 3. Restore the omitted rows: an exact seventeen-channel obstruction

Write \(U_L=\prod_{l\in L}u_l\), and set

\[
r_N=\left(\prod_{l\in L\setminus L_N}u_l\right)
          \left(\prod_{s\in N}t_s^{-1}\right),\qquad
\ell_0=\sum_Nr_N\Omega_N.
\]

In words: this is the existing coupled generic lift on the common chart. Its generic block coefficient is one. All denominators are the already permitted short Rees units. Direct calculation gives \(d\ell_0=0\) in the full F, not merely its quotient.

For an arbitrary core cycle \(z=\sum_N b_N\Omega_N\), remove that generic part:

\[
a=b_\varnothing,\qquad w_N=b_N-a r_N\quad(N\ne\varnothing).
\]

In words: the remaining coordinates have zero generic projection. The omitted short rows now determine whether they are actual full cycles.

For a short label s added to a short face N, the row is equivalent to

\[
t_s b_{N+s}-
 \left(\prod_{l\in L_N\setminus L_{N+s}}u_l\right)b_N
\in I_{\mathrm{opp}(s)}.
\]

In words: the coefficient discrepancy must vanish upon localizing the occurrence s. The kernel of that localization is exactly the opposite occurrence ideal. This is a statement about the existing coefficient map, not about setting s to zero.

After subtracting the coupled generic lift, induction on pure supports gives

\[
w_N\in I_-\quad(\varnothing\ne N\subseteq S_+),\qquad
w_N\in I_+\quad(\varnothing\ne N\subseteq S_-).
\]

In words: a pure short block can vary independently only with a coefficient from the opposite occurrence ideal.

For a mixed edge \(\{p,m\}\), where p is positive and m negative, the compatible long sets of the pair and its two vertices agree. Its remaining two rows give

\[
w_{\{p,m\}}=t_p^{-1}w_{\{m\}}+t_m^{-1}w_{\{p\}}.
\]

In words: each mixed block must be the sum of its two prescribed adjacent contributions. The proof uses \(I_+\cap I_-=0\). Rows on faces also containing a long label are the displayed equations multiplied by their already solved long coefficients, so they add no unexamined condition.

Define the map \(\mathfrak o\) by taking the fourteen pure coordinates modulo the indicated ideals, together with the three mixed discrepancies:

\[
\mathfrak o(b)=\left(
(w_N\bmod I_-)_{N\subseteq S_+},\
(w_N\bmod I_+)_{N\subseteq S_-},\
\left(w_{pm}-t_p^{-1}w_m-t_m^{-1}w_p\right)_{\{p,m\}}
\right).
\]

In words: the first fourteen outputs are functions on the respective occurrence sheets; the final three remain functions on the full alternating ring. All pure-support indices in this formula are nonempty.

This map is B-linear and surjective. One can choose representatives of any desired pure branch coefficients and then choose the mixed coordinates to realize their remaining prescribed errors. Its kernel is precisely the full target top kernel. Consequently

\[
0\longrightarrow M\longrightarrow B^{18}
 \xrightarrow{\mathfrak o}\mathcal O_{\rm top}\longrightarrow0,
\qquad
\mathcal O_{\rm top}=B_+^{\oplus7}\oplus B_-^{\oplus7}\oplus B^{\oplus3},
\]

\[
M\cong B\oplus I_+^{\oplus7}\oplus I_-^{\oplus7}.
\]

In words: this is a complete module presentation of the closure obstruction, with the previously constructed common-chart source as its kernel. The apparent free factors carry their inherited homogeneous support shifts; ranks alone are not a replacement for those labels.

The exact sequence and formula remain valid under flat completion. In particular,

\[
\widehat{\mathcal O}_{\rm top}
\cong\widehat B_+^{\oplus7}\oplus\widehat B_-^{\oplus7}\oplus\widehat B^{\oplus3}.
\]

The connecting morphism from the actual short exact sequence identifies

\[
\mathcal O_{\rm top}\cong
\operatorname{im}\bigl(H_3(F_0)\longrightarrow H_2(P)\bigr).
\]

In words: the seventeen-channel module is the part of punctured-target homology detected by failed top lifts. It is not asserted to be the whole of \(H_2(P)\), and no decomposition of the entire target complex into these factors is claimed.

## 4. Explicit endpoint counterexamples to every finite-jet test

The two fully marked endpoints are

\[
e_-=[S_-,S_-],\qquad e_+=[S_+,S_+].
\]

In words: both have degree three and require no long correction. They are cycles in F0.

For \(S_-=(02,04,24)\), the full differential is

\[
de_-=[S_-,\{04,24\}]-[S_-,\{02,24\}]+[S_-,\{02,04\}].
\]

In words: the three terms live in the actual modules localizing \(X_{02}\), \(X_{04}\), and \(X_{24}\), respectively. Their coefficients are one, minus one, one. They do not vanish over B or \(\widehat B\).

Each summand disappears after every finite occurrence-jet base change. Thus e-minus defines a compatible closed target element at all finite orders. But

\[
\mathfrak o(e_-)\ne0,\qquad
\operatorname{Ann}_B[de_-]=I_+,
\qquad
\operatorname{Ann}_B[de_+]=I_-.
\]

In words: neither endpoint unit lifts to a closed element of the full flat-completed target with that same core value. Only multiplication by the opposite occurrence ideal makes that isolated endpoint direction closed.

There is no hidden chain homotopy that repairs this particular problem: P has no degree-three term, so a core top chain has only one underlying top preimage, and P has no boundaries entering degree two. The displayed nonzero connecting cycle is therefore a direct obstruction, not a choice-dependent representative.

The same example can preserve the generic coefficient. Both \(\ell_0\) and \(\ell_0+e_-\) project to the same genuine generic-Q coefficient. The latter is a cycle in every finite jet, yet is not a full completed cycle. Hence even all-order generic normalization plus finite-jet closure misses a concrete endpoint equation.

This does not contradict the earlier contractibility of the target-framed *source-marking* limit. That calculation fixed a particular target marking and required its image from the derived source. The present example is a different target marking with no such full comparison.

## 5. The derived obstruction fibre explains the old singular rank defect

The obstruction module is nonperfect at the conductor. Its intrinsic derived restriction is computed without replacing either branch module by its coefficient image.

Let \(q_n=\operatorname{rank}_C\operatorname{Tor}_n^B(C,C)\). The earlier integral alternating-block resolution gives

\[
\sum_{n\ge0}q_nz^n=
\frac{(1+z)^3}{1-3z-3z^2-z^3},\qquad
(q_0,q_1,q_2,q_3,q_4)=(1,6,24,92,354).
\]

In words: these are free conductor-module ranks. They are not orders of integer torsion.

Splice the existing ideal resolution into

\[
0\longrightarrow I_-\longrightarrow B\longrightarrow B_+\longrightarrow0
\]

and its polarity conjugate. In words: this resolves each branch quotient by the actual opposite ideal. In alternating-word notation, keep precisely the words whose final block belongs to the killed branch; the differential still acts on the first exterior block. This is exact by the preceding ideal-resolution proof, not merely because its square vanishes.

For positive degrees, each branch quotient has rank \(q_n/2\) on the conductor. Therefore

\[
\operatorname{Tor}_0^B(C,\mathcal O_{\rm top})\cong C^{17},\qquad
\operatorname{Tor}_n^B(C,\mathcal O_{\rm top})\cong C^{7q_n}\quad(n\ge1).
\]

In words: the obstruction fibre has ranks 17, 42, 168, 644, 2478, 9534, and continues without a finite bound.

The exact sequence in Section 3 gives

\[
0\longrightarrow C^{42}\longrightarrow C\otimes_B M
\longrightarrow C^{18}\longrightarrow C^{17}\longrightarrow0.
\]

In words: the forty-two invisible source directions and seventeen missed target directions computed earlier are the exact connecting terms of this same obstruction module. The middle source has rank forty-three and its map has rank one.

Higher degrees satisfy

\[
\operatorname{Tor}_n^B(C,M)
\cong\operatorname{Tor}_{n+1}^B(C,\mathcal O_{\rm top})\quad(n\ge1).
\]

In words: the earlier unbounded source tower is linked to these concrete missing target equations by one degree of dimension shifting. This does not assert new homotopy groups of a physical moduli space.

## 6. Construct the full mapping-space gluing square

Return to the original open V. Let U be its occurrence complement, let \(f:\operatorname{Spec}\widehat B\to V\) be the flat completed central chart, and let W be its inverse image of U. For a fixed source A and the actual target F, use flat pullback on the completed factor.

The formal-gluing target triangle follows by applying the extended-Cech comparison on the central chart, then gluing with U [M1, M3]. Applying derived Hom to that triangle and using pullback–pushforward adjunction gives

\[
\begin{aligned}
R\operatorname{Hom}_V(A,F)\simeq\operatorname{fib}\bigl(&
R\operatorname{Hom}_U(A_U,F_U)\oplus
R\operatorname{Hom}_{\widehat B}(\widehat A,\widehat F)\
&\longrightarrow R\operatorname{Hom}_W(A_W,F_W)\bigr).
\end{aligned}
\]

In words: a global comparison consists of the two actual local comparisons and a homotopy between their restrictions on the completed puncture. The higher Cech intersections are inside the derived Hom terms, not omitted.

Equivalently,

\[
\operatorname{Map}_V(A,F)\simeq
\operatorname{Map}_U(A_U,F_U)
\times^h_{\operatorname{Map}_W(A_W,F_W)}
\operatorname{Map}_{\widehat B}(\widehat A,\widehat F).
\]

In words: this is an explicit mapping-space reconstruction for the fixed coefficient geometry. No assumption that A is perfect is used: adjunction, rather than a tensor–Hom base-change formula, moves each local mapping term into its correct category. The bounded-flat target permits the stated Cech reconstruction. This argument does not assert an unqualified equivalence of arbitrary unbounded derived categories.

A source-target diagram with endpoint inclusions, the support filtration, and generic quotient is reconstructed by applying the same formula to its component maps and taking the appropriate finite homotopy limits. Thus it retains specified connector homotopies; it does not create connector data that have not been supplied.

For the particular top source \(A=\mathcal S_{14}[3]\), the source is a sheaf in homological degree three and F has no terms above that degree. Derived degree separation [M4, M5] gives

\[
\operatorname{Map}(\mathcal S_{14}[3],F)
\simeq\operatorname{Hom}(\mathcal S_{14},\mathcal H_3(F))_{\rm disc}
\]

on V and on all flat pieces. In words: once the actual top-map restrictions agree, there is no additional higher map obstruction in this placement. Representatives using resolutions may have comparison homotopies, but their spaces have the displayed zero-truncation. A differently shifted native or supported source must be tested in the full mapping complex, not silently reduced to this case.

## 7. A constructive coefficient-level identification test

A candidate central top comparison first determines eighteen functions \(b_N\) in the basis of Section 2. Apply \(\mathfrak o\). A nonzero result rules out closure in the actual target, even if every finite jet passed. If \(\mathfrak o=0\), the actual full chain is recovered as follows.

For a nonempty pure support N define

\[
G_N=\Omega_N+
\sum_{a\in S_{\mathrm{opp}(N)},\ N+a\text{ noncrossing}}t_a^{-1}\Omega_{N+a}.
\]

In words: a singleton has its one matching mixed-edge correction; doubletons and endpoints have none. For a coefficient in the opposite occurrence ideal, this is a full cycle after multiplication by that coefficient.

Then

\[
z=a\ell_0+\sum_{N\ {m pure},\ N\ne\varnothing}w_NG_N.
\]

In words: this gives an explicit source-coordinate reconstruction using only the allowed Rees units. Its equality with the original top coefficients follows from the three mixed equations. No target homotopy or carrier cell is adjoined.

Finally require the resulting formal comparison and the actual comparisons on both algebraic punctured sheets to agree through the mapping-space square of Section 6. In the present top placement this is a sufficient, not merely necessary, coefficient-map test. The global endpoint residues still constrain the source bridge. Neither \(\mathfrak o=0\) on one chart nor equality of generic readouts replaces those bridge conditions.

This distinguishes three levels: finite-jet closure, closure in the complete local PC target, and global realization with the actual normalization transitions. The computation supplies the exact missing test between the first two and the full derived reconstruction for the third.

## 8. Verification and provenance

Run:

```sh
python check_marici_punctured_target_obstruction_20260907.py \
  --output marici_punctured_target_obstruction_certificate_20260907.json
```

The standalone standard-library checker passes **68,561 exact assertions**. These include the original differential identities and coefficient domains, the 128-term subcomplex and 72-term quotient, all eighteen top-block representatives, the exact seventeen-channel criterion, explicit reconstructions, both endpoint three-term boundaries, labelled dihedral covariance, and the intrinsic branch-resolution differentials.

There are **5,184 independent integral homogeneous full-target top-kernel calculations**, retaining the original long parameters and their legal cellwise localizations. A separate 127-strand calculation checks the integral presentation after the explicitly verified unit changes of coordinates. The latter does not substitute a scalar specialization for the symbolic target proof.

The previous formal-punctured checker was independently rerun and passed **292,331 assertions**. Its replay hash and input-note hashes are recorded in the new certificate. The new checker does not run the predecessor silently.

All-polynomial and all-formal-series conclusions follow from the row elimination, flatness, and the established integral ideal resolutions. Mapping-space reconstruction follows from the cited gluing and adjunction argument, not numerical tests. This is not proof-assistant certification, and no repository files were modified.

## References

[M1] Stacks Project, *Formal glueing of module categories*, tag `05E5`, in particular the extended alternating Cech comparison and its exact gluing complex. `https://stacks.math.columbia.edu/tag/05E5`

[M2] Stacks Project, *Completion for Noetherian rings*, tag `0BNH`: flatness and exactness of completion on finite modules. `https://stacks.math.columbia.edu/tag/0BNH`

[M3] Stacks Project, *Local cohomology: Generalities*, tag `0DWQ`: open-complement triangles and Cech realization. `https://stacks.math.columbia.edu/tag/0DWQ`

[M4] Stacks Project, *Hom complexes*, tag `0A8H`: mapping differentials, composition, and tensor–Hom adjunction. `https://stacks.math.columbia.edu/tag/0A8H`

[M5] Stacks Project, Lemma 13.27.3, tag `06XS`: the relevant derived-category degree separation. `https://stacks.math.columbia.edu/tag/06XS`

Local proof inputs, available with the preceding conversation: `marici_formal_punctured_gluing_20260907.md`, `marici_target_framed_conductor_tower_20260907.md`, `marici_normalization_endpoint_extension_20260907.md`, and `marici_intrinsic_conductor_resolution_20260907.md`.

The target differential is the source-defined 215-state PC rule audited in `research/voevodsky/check_ringed_alexandrov_pc_target.py` at the pinned baseline. The new standalone checker reconstructs that rule and the required localization domains; no fresh repository fetch or claim about a changed repository revision is made in this step.
