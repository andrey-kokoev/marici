# Full target framing and the intrinsic conductor tower

Date: 2026-09-07  
Lane: Branch B — normalization descent and target-side comparison  
Coefficient provenance: `andrey-kokoev/marici`, pinned commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The full target-framed automorphism space of the previously constructed source is contractible, even when preservation of the target map means preservation up to coherent homotopy rather than pointwise equality. This statement is global on the existing test open and uses its actual top-cycle map; it does not select an independently defined native source.

After intrinsic occurrence-conductor restriction, that rigidity is lost. The derived source has the previously computed unbounded Tor groups, while the bounded-flat target has no homotopy in the corresponding positive degrees. At the reduced conductor the ordinary source fibre has rank 43, the target top kernel has rank 18, and their comparison has image rank one, kernel rank 42, and cokernel rank 17. Both endpoint cycles are retained in the target.

The main new result computes the full target-framed marking fibre at every occurrence-conductor thickness and its actual transition maps. Each finite thickness has infinitely many nonzero higher homotopy groups. Nevertheless, every one-step transition is zero on every based homotopy group, including the group of components. The homotopy limit of these target-framed marking spaces is therefore contractible. No infinite sequence of nonzero finite-order classes survives as a compatible target-framed choice.

The completion here is along the **occurrence conductor**, on its already existing common chart. It is not the opposite-normal completion in the preceding note. The global endpoint attaching class is not erased: its distinction lives in gluing this chart to the occurrence charts. No theorem about native physical states, a logarithmic Gysin identification, or an RH criterion follows merely from this completion calculation.

## 1. Fixed input and grading

Keep the two occurrence sheets and the six short Rees parameters from the previous construction. On the common chart, define

\[
C=\mathbb Z[X_\ell,u_\ell:\ell\in L]
 [t_s^{\pm1}:s\in S_+\cup S_-],
\qquad
B=C[x_1,x_2,x_3,y_1,y_2,y_3]/(x_i y_j).
\]

In words: C retains all independent long occurrences and long normals; only the short Rees parameters already invertible on the common chart are inverted. The x coordinates name the positive occurrences (13,15,35), and the y coordinates name the negative occurrences (02,04,24).

Set

\[
I_+=(x_1,x_2,x_3),\qquad I_-=(y_1,y_2,y_3),
\qquad I=I_+\oplus I_-,\qquad A_r=B/I^r\quad(r\ge1).
\]

In words: A-r is the r-th occurrence-conductor thickening, with A-one equal to C. The mixed-sheet monomials remain zero. No normal is set equal to one or identified with another normal.

The already constructed source and its full target map restrict to

\[
M=\mathcal S_{14}|_{D(T)}
 \cong B\oplus I_+^{\oplus7}\oplus I_-^{\oplus7},
\qquad
\Phi:M[3]\longrightarrow F_K|_{D(T)}.
\]

In words: one generic coefficient and fourteen conductor-vanishing channels are retained. The final channel on each sheet is the actual endpoint. This splitting is on the common chart only. Globally the source remains the previously specified normalization pullback.

All degrees below are homological unless explicitly stated otherwise. Thus M[3] has M in homological degree three. The actual target has 215 generators in degrees zero through three and has no degree-four term. Its absolute version is finite free over B. Its prescribed PC version is bounded flat, with the actual localization modules attached to each cell. These facts permit termwise computation of derived coefficient change in the target [M2]; they do not permit termwise coefficient change in the nonflat source ideals.

The channel map in the local splitting is

\[
\Phi(b,(f_{\sigma,N}))
 =b\ell_0+\sum_{\sigma,N}f_{\sigma,N}\Gamma_{\sigma,N}.
\]

In words: the map is the actual generic lift plus its fourteen labelled full target cycles. The formula includes both fully marked endpoint cycles. Their coefficients are not scalar readouts.

## 2. Full target framing is homotopically rigid before coefficient change

Globally, the preceding construction proved

\[
\mathcal S_{14}\cong\mathcal H_3(F_K)|_V.
\]

In words: the normalization pullback identifies with the target's top kernel sheaf, not with its entire complex.

For any sheaf A on V, truncation and the ordinary t-structure give

\[
\operatorname{Map}_{D(\mathcal O_V)}(A[3],F_K)
 \simeq
\operatorname{Hom}_{\mathcal O_V}
 (A,\mathcal H_3(F_K))_{\mathrm{disc}}.
\]

In words: maps from a degree-three sheaf into this target form a discrete space and are determined exactly by their top-homology map. There are no higher homotopies of such maps. The degree separation is the general Ext vanishing of [M1], not a deduction from a single chosen cellular presentation. In cohomological indexing the source is in degree minus three and the target has no terms below minus three.

Consequently composition with Phi identifies the endomorphism mapping space of S14 with its target-map space. In particular

\[
\operatorname{hofib}_{\Phi}
 \bigl(\operatorname{Aut}(\mathcal S_{14})
       \xrightarrow{U\mapsto\Phi U}\operatorname{Map}(\mathcal S_{14}[3],F_K)\bigr)
 \simeq *.
\]

In words: an automorphism preserving the full comparison up to homotopy is the identity, and the preserving homotopy has no extra choices. Restricting to the triangular endpoint automorphisms from the preceding note gives the same answer. Coherent duality gives the equivalent statement for the entire reversed diagram; this does not split its nonzero endpoint extension.

This is stronger than fixing the generic coefficient, the endpoint extension class, or a filtration symbol. It is also intentionally conditional on the **already constructed** Phi. It is not evidence that an independently defined physical source admits Phi.

## 3. The intrinsic conductor change is not top-exact

Define the actual derived comparison

\[
K_r=A_r\otimes_B^L M,\qquad
T_r=(A_r\otimes_B^L F_K)[-3],\qquad
\alpha_r:K_r\longrightarrow T_r.
\]

In words: change coefficients in the source and full target together, then move their former degree-three marking to degree zero. The target T-r has homological degrees at most zero, whereas K-r can have arbitrarily high positive homology.

At r=1 the ordinary source fibre is

\[
H_0(K_1)\cong C\oplus (I_+/I_+^2)^{\oplus7}
                    \oplus (I_-/I_-^2)^{\oplus7}
 \cong C^{43}.
\]

In words: each of the fourteen ideal channels supplies its three first occurrence symbols. These forty-two symbols are nonzero in the source fibre.

The actual map sends a singleton source generator to an occurrence times its target cycle. Hence

\[
H_0(\alpha_1)(1)=\overline\ell_0,
\qquad
H_0(\alpha_1)([x_i]\Gamma_{+,N})=0,
\qquad
H_0(\alpha_1)([y_i]\Gamma_{-,N})=0.
\]

In words: the generic unit is retained, but all forty-two occurrence-symbol directions become zero in the target after setting the occurrence conductor to zero. This is the intrinsic derived pullback of the existing comparison; no supported principal-line dual is being substituted for it.

### Compute the entire reduced target top kernel

Let N range over the noncrossing subsets of the six short diagonals, including the empty subset, and let

\[
L_N=\{\ell\in L:\operatorname{NC}(N\cup\{\ell\})\}.
\]

In words: NC means that the displayed set is noncrossing; L-N records the actual compatible long labels. There are eighteen such short supports, with cardinality counts 1,6,9,2.

For each one define

\[
\Omega_N=
\left(\prod_{\ell\in L_N}u_\ell\right)[N,N]
+(-1)^{|N|+1}
 \sum_{\ell\in L_N}X_\ell
 \left(\prod_{k\in L_N\setminus\{\ell\}}u_k\right)
 [N\cup\{\ell\},N\cup\{\ell\}].
\]

In words: retain the fully marked short face and all its compatible marked-long corrections. Each expression is a closed target cycle on the conductor.

At this coefficient change, every short radial or normal coefficient in the absolute target is zero. Thus its top-to-next-degree differential separates into eighteen blocks. A block has one base top generator and one marked generator per compatible long diagonal; its row equations are the source's signed X-long/u-long equations. Since the long normals are independent, any solution's base coefficient is divisible by their product, and every solution is a unique multiple of Omega-N. There are 45 top generators and 27 such rows.

In the PC target, any cell inverting a short occurrence has zero derived conductor fibre. This follows because its localization is flat and that occurrence is nilpotent in every A-r. The remaining top block has row coefficients X-long/u-long and one, with the exact prescribed long localization. The same divisibility argument gives the same top kernel. No coefficient denominator has been discarded or globally added.

Therefore

\[
H_0(T_1)\cong\bigoplus_N C\Omega_N\cong C^{18}.
\]

In words: both endpoint cycles are among these eighteen classes. The reduced target itself has not forgotten them.

The image of alpha-one has rank one and is a direct summand because the empty-short-support coefficient of the generic cycle is one in this basis. More explicitly,

\[
\overline\ell_0
=\sum_N(-1)^{|N|(|N|+1)/2}
 \frac{\prod_{\ell\in L\setminus L_N}u_\ell}
      {\prod_{s\in N}t_s}\,\Omega_N.
\]

In words: all denominators are the short t units already available on the common chart. The empty-support coefficient is one. Hence

\[
\ker H_0(\alpha_1)\cong C^{42},\qquad
\operatorname{coker}H_0(\alpha_1)\cong C^{17}.
\]

In words: the comparison loses forty-two source coordinates and misses seventeen independent top-target directions. The rank-43 intrinsic source fibre is not the rank-18 top kernel obtained by specializing the target first. Truncation and this nonflat coefficient change do not commute.

## 4. A concrete endpoint automorphism is exposed at the next thickness

The preceding global transformation

\[
h=u_{14}a-t_{02}t_{35}z_{+,\{02\}}
\]

has local expression h equal to minus t02 t35 times that channel's conductor-vanishing coordinate. In words: substituting the actual singleton residue cancels the generic coefficient, leaving a map from one positive ideal channel into the positive endpoint ideal.

On a source input whose old channel equals X13, its change in the full target is

\[
\delta\Phi=-t_{02}t_{35}X_{13}\Gamma_{+,S_-}.
\]

In words: this is a nonzero multiple of the actual fully marked negative endpoint. It is closed, but cannot be a boundary in the unchanged degree-three target.

At the reduced occurrence conductor this expression is zero. At the next occurrence thickening it is nonzero:

\[
\delta\Phi\otimes_B A_1=0,\qquad
\delta\Phi\otimes_B A_2\ne0.
\]

In words: an endpoint shear invisible at the singular fibre fails the full-target test already modulo the square of the conductor ideal.

On the intrinsic conductor resolution, this shear is still nontrivial: it sends an old-channel word to the same word in the endpoint channel, multiplied by the nonzero spectator unit. Thus the invisibility is in the **comparison to the target**, not the disappearance of the source automorphism. A correction congruent to this unit modulo I cannot restore full target framing at A-two: its effect on the first occurrence symbols still has the displayed nonzero coefficient. Map-space degree separation prevents a higher target homotopy from changing that test.

This particular test does not claim that every choice at one finite thickness comes from a global automorphism. The next sections instead compute all target-framed **markings**, a different precisely specified space.

## 5. Define the target-framed marking tower

The local generic lift supplies compatible base markings. Let

\[
\mathscr F_r=
\operatorname{hofib}_{\ell_r}
 \left(\operatorname{Map}_{D(A_r)}(A_r,K_r)
       \xrightarrow{\alpha_r}
       \operatorname{Map}_{D(A_r)}(A_r,T_r)\right).
\]

In words: a point is a derived source marking together with a comparison of its image to the fixed full target marking. The local source marking with generic coefficient one and all ideal coordinates zero supplies the basepoint in every F-r.

The target mapping space is discrete because T-r has no positive homological degrees. For n at least one,

\[
\pi_n(\mathscr F_r)\cong\operatorname{Tor}_n^B(A_r,M).
\]

In words: every higher source Tor group is invisible to the bounded target at this finite thickness and remains as a higher comparison in the framed fibre. This follows directly from the mapping-complex convention and the homotopy-fibre sequence [M3].

The group of components is the kernel of the actual ordinary comparison. Here

\[
H_0(K_r)\cong A_r\oplus
 (I_+/I_+^{r+1})^{\oplus7}\oplus
 (I_-/I_-^{r+1})^{\oplus7}.
\]

In words: tensoring an ideal with B/I-r leaves one more ideal power than evaluating its inclusion into B/I-r. The extra layer must not be set to zero in the source.

A top-face pivot proves that the generic coefficient is detected by the independent product of the three long normals. After the generic part is fixed, each channel has a unique pure-short-face pivot not shared by any other channel. Its coefficient is a product of short t units and independent long normals, hence a non-zero-divisor even over A-r. Therefore the only kernel is the last ideal layer in each channel:

\[
\pi_0(\mathscr F_r)\cong
 (I_+^r/I_+^{r+1})^{\oplus7}
 \oplus (I_-^r/I_-^{r+1})^{\oplus7}
 \cong C^{\,14\binom{r+2}{2}}.
\]

In words: the component coordinates count exactly the degree-r monomials in three variables on each of the fourteen channels. These identifications use the chosen compatible base marking; without it the components form the corresponding torsor.

## 6. Compute the higher groups at every thickness

Use the established integral resolution of I-plus or I-minus. Its homological degree-n generators are alternating exterior-block words of total word degree n+1 ending on the chosen sheet. Write q-n for their number:

\[
q_0=3,\qquad q_1=12,\qquad q_2=46,
\qquad q_n=3q_{n-1}+3q_{n-2}+q_{n-3}\quad(n\ge3).
\]

In words: these are the minimal ideal-resolution ranks, one-half of the conductor-resolution rank one degree higher. The differential multiplies a coefficient by one occurrence and deletes that label from the first word block.

For r,n at least one, set

\[
a_{r,n}=q_n\binom{r+1}{2}
 +(3q_n-q_{n+1})\binom r2
 +q_{n-1}\binom{r-1}{2}.
\]

In words: the binomial coefficients count monomials at the allowed occurrence degrees; a binomial coefficient with upper index smaller than two is zero. The exact answer is

\[
\operatorname{Tor}_n^B(A_r,I_\sigma)\cong C^{a_{r,n}},
\qquad
\pi_n(\mathscr F_r)\cong C^{14a_{r,n}}.
\]

In words: fourteen channels retain their individual labels and grading shifts. Both endpoints contribute one channel throughout. No integer torsion is present.

### All-degree proof, not an extrapolation

A word in ideal-resolution degree n has occurrence degree n+1. A coefficient has degree d, with zero at degree r in A-r. The old spectator-linear contraction removes one existing coefficient factor and puts it into the first word block. It preserves total internal degree and uses no integer or variable inverse.

In an untruncated ideal-resolution strand the augmented complex is split exact over C. Truncating coefficient degree at r removes a bottom segment of that strand. In positive homological degree, the only possible remaining homology lies at its new bottom, with coefficient degree r-1. Equivalently it has total internal degree r+n. The integral contraction makes the resulting homology free; it identifies it with a direct-summand image of a differential in the original split-exact strand.

Let h-d be the rank of the degree-d part of B over C. Then

\[
h_0=1,\qquad h_d=2\binom{d+2}{2}\quad(d\ge1),
\qquad
 a_{r,n}=\sum_{j=0}^{r-1}(-1)^j h_{r-1-j}q_{n+j}.
\]

In words: this is the finite alternating dimension sum of that complete strand. Multiplying the Hilbert series of B by the alternating tail of the q sequence gives the three-binomial formula above. The recurrence proves it for every r and n, not only the tested bounds.

The first ranks are:

| Occurrence thickness r | Components | First homotopy | Second homotopy | Third homotopy |
|---|---:|---:|---:|---:|
| 1 | 42 | 168 | 644 | 2478 |
| 2 | 84 | 364 | 1386 | 5334 |
| 3 | 140 | 630 | 2394 | 9212 |
| 4 | 210 | 966 | 3668 | 14112 |

Each entry is a rank over C. Every finite thickness has nonzero higher groups in arbitrarily high degree. This does not yet say anything about their compatibility as thickness changes.

## 7. Construct the actual transition homotopies

Let p-r lower the coefficient quotient from A-r-plus-one to A-r. If h is the explicit spectator-linear word contraction before truncation, define

\[
K_r=p_r h.
\]

In words: apply the existing polynomial contraction and then reduce to the lower thickness. It is spectator-linear, not asserted B-linear or strictly dihedral-equivariant.

In every positive ideal-resolution degree,

\[
p_r=dK_r+K_rd.
\]

In words: the one-step coefficient reduction is explicitly nullhomotopic on positive homology. The formula is well-defined despite truncation: a discarded coefficient of degree r+1 becomes degree r under h, which p-r still kills. All other terms are exactly the untruncated contraction identity. This proves the statement in every degree and at every thickness.

The coefficient quotient and original target maps themselves remain equivariant. A non-equivariant contracting homotopy is sufficient to prove that their equivariant induced map on homology is zero; no averaging is used or asserted.

For components, the transition sends a class of degree r+1 in a branch ideal to its image modulo the same ideal power, hence zero. Thus

\[
(p_r)_*:\pi_n(\mathscr F_{r+1})\longrightarrow\pi_n(\mathscr F_r),
\qquad (p_r)_*=0\quad(r\ge1,\ n\ge0).
\]

In words: every nonzero finite-order component or higher class fails to continue to the next thickness as a target-framed compatible class. The increasing numerical ranks in the table do not form an increasing system of persistent classes.

## 8. The completed target-framed marking space is contractible

Define

\[
\mathscr F_{\mathrm{formal}}=\operatorname*{holim}_{r\ge1}\mathscr F_r.
\]

In words: retain compatible markings and all their comparison homotopies through every occurrence thickness.

The compatible base marking identifies the fibres with the connective spaces of additive mapping fibres. The Milnor derived-limit sequences therefore apply [M4]. Every homotopy-group inverse system is already zero after a single transition. Both its limit and its first derived limit vanish. Consequently

\[
\mathscr F_{\mathrm{formal}}\simeq *.
\]

In words: the completed full-target-framed marking has no residual component choice or higher ambiguity, despite the unbounded homotopy at each finite thickness.

This is also consistent with exact completion on the finite coherent top-kernel module: derived completion recovers the completed sheaf, not a persistent copy of every Tor class in one fibre. The explicit transition proof is stronger for the present purpose because it identifies exactly why those particular classes do not persist.

The **stable** comparison fibre is not asserted acyclic. Lower target homology, in negative degrees after the regrading, lies outside these marking spaces and is not discarded. Nor is the completion of the whole target replaced by its top homology.

## 9. What this does not identify

The occurrence conductor inside the pre-existing test open V lies wholly in D(T). Every conductor thickening considered above has the same underlying topological support and is contained in this common chart. The nonzero global endpoint extension is already locally split there. Completion cannot reconstruct the missing gluing to the occurrence charts or show that the global attaching morphism vanishes.

The results therefore distinguish three problems:

1. Automorphisms of the existing coefficient source preserving its full target map: rigid, including coherent homotopies.
2. Derived markings after one finite occurrence-conductor restriction: highly non-rigid, with the displayed genuine unbounded homotopy groups.
3. Compatible such markings through every occurrence thickness with the full target fixed: contractible.

None is the yet-unidentified native physical source problem. In particular, the earlier contrary variance of a supported-dual comparison is not resolved by an ordinary completion. Native source maps with different degree placement or a target with additional derived degrees are not covered by the top-degree argument.

The useful new falsification test is explicit: an identification based on the isolated conductor groupoid must also preserve its all-thickness target comparison and transition maps. Matching its local Tor ranks, even in all degrees, would miss this distinction. The global conductor attachment and the independent generic-Q source still require their actual comparison maps.

## 10. Verification and reproducibility

Run:

```sh
python check_marici_target_framed_conductor_tower_20260907.py \
  --output marici_target_framed_conductor_tower_certificate_20260907.json
```

The standalone standard-library checker passes **187,315 exact assertions**. It reconstructs all 215 original target states, keeps both endpoint cubes and all fourteen source channels, checks the complete absolute and PC differentials, verifies the actual source ideal relations in the target, constructs all eighteen reduced top blocks, and checks the source comparison through four occurrence thicknesses.

It independently performs **2,983 complete integral homogeneous Tor calculations**, with no modular rank inference, and **62,980 explicit one-step transition-homotopy basis checks**. The fixed generic cycle and coefficient restriction maps are checked under all six labelled dihedral transports. The proof homotopy itself is not falsely asserted to be equivariant.

The preceding global-endpoint-transformations checker was independently rerun and passed **600,682 exact assertions**. Its new output hash and input file hashes are recorded in the certificate. No claim is made that its older prerequisites were rerun unless its replay output records them. No repository files were modified, no current-head audit was performed, and no geometric carrier cell was added. This is an algebraic proof with executable exact checks, not proof-assistant certification.

## Sources and conventions

Existing conversation artifacts read directly in this runtime:

- `marici_global_endpoint_transformations_20260907.md` and its checker: all global endpoint-triangle transformations, their full target-map caveat, and the original target matrices.
- `marici_normalization_endpoint_extension_20260907.md`: the fourteen-channel normalization source, actual full-cycle map Phi, and identification with the top kernel sheaf.
- `marici_intrinsic_conductor_resolution_20260907.md` and its checker: the all-degree alternating exterior-block resolution and explicit spectator-linear contraction.
- `marici_reverse_endpoint_gysin_20260907.md`: distinction between supported reverse lifts and preserving the unrestricted endpoint attachment.

Primary references:

[M1] Stacks Project, Lemma 13.27.3, tag `06XS`, Ext vanishing at the edge of the t-structure: https://stacks.math.columbia.edu/tag/06XS.

[M2] Stacks Project, *Derived tensor product*, tag `06XY`: https://stacks.math.columbia.edu/tag/06XY.

[M3] Stacks Project, *Hom complexes*, tag `0A8H`: https://stacks.math.columbia.edu/tag/0A8H.

[M4] Stacks Project, *Derived limits*, tag `0BKN`, Lemma 20.37.1; and tag `0919`: https://stacks.math.columbia.edu/tag/0BKN and https://stacks.math.columbia.edu/tag/0919.

The resolutions, finite-thickness ranks, target comparison, and vanishing transition maps are the computations of this note. These references supply the ambient derived-category conventions and the limit theorem; they are not citations claiming those numerical computations occur in the literature.
