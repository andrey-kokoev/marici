# Branch C: D35/D04 strict input gate

Date: 2026-09-08

## Status

The requested D35/D04 spatial comparison has **not been tested**. This is an input-access stop, not a new mathematical no-go and not a completed Decision 4 under the task's requirement to consume every listed input first.

The attached follow-up names 18 unconditional inputs: the three binding native-pullback files and 15 further source/checker/adapter files. Nine are present as uploaded files in the active runtime. Nine are absent. The three Q-manifold/P24-conditional inputs were not read.

The connected GitHub default branch was resolved to commit `bea7339e69931b479e395d147c5f5a7fcb0dce8b`. The exact nine missing paths returned 404 in the connector. File Library searches returned task references and summaries, not their bodies. Commit-history queries for the primitive-conormal note and first-jet JSON returned empty lists on that branch. These observations do not establish that the files do not exist in the user's local working tree or another unpublished branch.

The inventory script parses available Python/JSON for syntax and records content hashes. It does not execute prior checkers, certify a new spatial matrix, or count inherited assertions as new work.

## Binding results retained

The follow-up's statements are retained as supplied results:

- the native derived-pullback candidate is ruled out by its mixed Tor-coherence obstruction;
- the complete physical endpoint has the stated primitive normalized conormal-column map;
- the full physical source contributes the stated ambiguity ideal, including the three endpoint Rees parameters;
- the nine native mixed actions are nonzero;
- the relative conormal orbit is injective;
- the graded antipode is required for the stated variance mate;
- the algebraic mate does not itself provide the missing spatial/frame comparison;
- reflection exchanges the D35 and D04 targets.

None is downgraded because an implementation file was unavailable. Equally, a theorem summary is not treated as the missing ordered matrix or line dictionary.

## 1. The strict pullback calculation can be reduced without choosing omega

Use the notation

\[
W=\omega[2],\qquad E_k=E_{\beta,k}\otimes\Pi^\vee[3],
\qquad T=C\otimes\Pi^\vee[3],\qquad k\in\{35,04\}.
\]

In words: these are the three complete complexes in the specified pullback. No complex is replaced by its cohomology. Here T names the pullback base complex only; it is not a channel subset.

For actual strict chain maps q and pi, the prescribed model is

\[
D_k^n=W^n\oplus E_k^n\oplus T^{n-1},
\qquad
d_{D_k}^n=
\begin{pmatrix}
d_W^n&0&0\\
0&d_{E_k}^n&0\\
q^n&-\pi_k^n&-d_T^{n-1}
\end{pmatrix}.
\]

In words: the third summand retains the comparison homotopy, with the stated negative differential. The shifts are already included in the displayed component differentials.

Multiplying consecutive differential blocks gives

\[
d_{D_k}^{n+1}d_{D_k}^n=
\begin{pmatrix}
d_W^{n+1}d_W^n&0&0\\
0&d_{E_k}^{n+1}d_{E_k}^n&0\\
q^{n+1}d_W^n-d_T^nq^n&
 d_T^n\pi_k^n-\pi_k^{n+1}d_{E_k}^n&
 d_T^nd_T^{n-1}
\end{pmatrix}.
\]

In words: square-zero requires the three complex equations and the two chain-map equations. This identity is a formal calculation, not verification of any unavailable block.

For a strict native B-action, the diagonal action on this pullback commutes with its differential exactly when the component actions commute with their differentials and q and pi are B-linear. A merely homotopy-linear representative would require its actual additional action components. None is supplied here by setting them to zero.

## 2. The kernel-valued route has no additional q equation

Let

\[
N_k=\ker(\pi_k),\qquad j_k:N_k\hookrightarrow E_k.
\]

In words: this is the actual kernel subcomplex, not a replacement of E_k or omega by their cohomology.

Suppose the existing normalized primitive column has been realized as a native, fully line-valued chain map

\[
\kappa_{\sigma,T}:G^{\mathrm{native}}_{\sigma,T}\longrightarrow N_{k_\sigma},
\qquad k_+=35,\quad k_-=04.
\]

The subscript T again denotes the prescribed channel. The hypothesis includes the actual physical source, not a conductor resolution substituted for it.

Then there is a strict pullback map

\[
b_{\sigma,T}(x)=(0,j_{k_\sigma}\kappa_{\sigma,T}(x),0).
\]

Its complete chain defect is

\[
d_{D_k}b-bd_G=
\left(0,
 j_k(d_{N_k}\kappa-\kappa d_G),
 -\pi_kj_k\kappa\right).
\]

In words: once the supplied source-to-kernel map is a correctly framed native chain map, both terms vanish. The omega and q components are identically absent from this particular image because the omega component of b is zero; they have not been set to zero in the target.

Likewise the native-linearity defect is

\[
b\rho_G(a)-\rho_{D_k}(a)b
=
\left(0,j_k(\kappa\rho_G(a)-\rho_{N_k}(a)\kappa),0\right).
\]

In words: the relevant native action must already be retained by the framed primitive-column map.

This is a conditional factorization lemma. It does not establish a new physical map, its uniqueness, or its operation intertwiners. In particular, it would be incorrect to announce a new obstruction coming from q for a valid kernel-valued map. Conversely, using this formula with only a scalar coefficient detector does not establish the missing native/support/line hypothesis.

## 3. Exact data needed to instantiate the primitive column

The next unavailable export is the **native framed primitive-column adapter**:

\[
\left(G^{\mathrm{native}}_{\sigma,T},d_G,\rho_G,\kappa_{\sigma,T}\right)
\longrightarrow
\left(N_{k_\sigma},d_N,\rho_N\right),
\]

including its occurrence, Rees, regulator beta, long-normal, product-Cartier, endpoint determinant, Pi-dual, and two excess-label dictionary.

The follow-up reports that the normalized column succeeds. To compile it in the requested source model rather than silently substitute a different one, the export must contain its ordered D0, D35/D04, nu0 and nu35/nu04 blocks and the precise line/support maps used to place that column in N_k.

For the known first-jet presentation, write alpha and b for the two row components, avoiding confusion with the ambient ring and target labels. The equations to be instantiated are

\[
\alpha D_0=0,\qquad bD_0+\beta\alpha D_k=0,
\]
\[
\alpha\nu_0=0,\qquad b\nu_0+\beta\alpha\nu_k=1.
\]

In words: these are the primitive first-jet equations specified in the earlier Branch B task. The kernel specialization is alpha=0, leaving bD0=0 and b nu0=1. Their success is retained as an input; their actual entries have not been recovered in this session.

The complete strict target also needs the native omega/q model required in Part I. The conditional kernel lemma avoids dependence of the proposed image on q, but does not authorize replacing the full target by its kernel or marking all of Part I as verified.

## 4. Operation and physical Q gates are not reached

The stated antipode equation describes the algebraic mate. It is not enough to form

\[
\Phi_\sigma(r\smile\nu_\sigma)-j_{k_\sigma}(v)\circ S(r)
\]

as a difference of spatial cochains until both expressions have the same declared source, target, degree, support, and line frames. No nullhomotopy is inferred from equality of their cohomology orbit labels. No decomposable reflection term is dropped.

No assertion is made about the physical control complex, outer vector fields, a physical Q-manifold, its trace, or P24's deformation class. The old native-pullback no-go is neither retested nor transferred to D35.

## 5. Retrieval manifest

Available flat uploads, with exact hashes in the JSON audit:

- `marici_native_pullback_obstruction.md`
- `check_marici_native_pullback_obstruction.py`
- `marici_native_pullback_obstruction_certificate.json`
- `marici_physical_endpoint_pullback.md`
- `check_marici_physical_endpoint_pullback.py`
- `marici_comparison_fibre_adjunction_bar.md`
- `check_marici_comparison_fibre_adjunction_bar.py`
- `marici_physical_change_of_rings.md`
- `check_marici_physical_change_of_rings.py`

Unavailable exact inputs:

- `research/chatgpt/marici_primitive_conormal_column_20260908.md`
- `research/chatgpt/check_marici_primitive_conormal_column_20260908.py`
- `research/voevodsky/physical-conormal-first-jet-adapter.json`
- `research/voevodsky/endpoint-to-conormal-cohomology-mate.json`
- `research/voevodsky/native-endpoint-operation-action.json`
- `research/voevodsky/conormal-variance-antipode-mate.json`
- `research/voevodsky/check_conormal_variance_antipode_mate.py`
- `research/voevodsky/agda/DGPyramidRelativeOperationOrbitMate.agda`
- `research/voevodsky/agda/DGPyramidThreeLayerHigherHom.agda`

The exact local/repository mapping is recorded; availability is not confused with proof verification. Missing mathematical entries are null in the audit, never zero matrices.

## Reproduction

```sh
python check_marici_d35_input_gate.py --root /mnt/data \
  --output marici_d35_input_gate_certificate.json
```

A repository checkout can instead be passed with `--root /path/to/marici`. `--require-all` returns exit status 2 if any named unconditional input is missing or syntactically invalid. An all-present result would pass only the input gate; it would not by itself verify a mathematical comparison.

## Sources and status distinctions

The current task is `branch-c-followup-task.md`. Its successful primitive-column and antipode statements are used as supplied results. The earlier Branch B follow-up and first-jet task in the user's File Library corroborate that summary, but do not provide the missing implementations. The retained Branch C files define the existing physical source and prior tested comparisons. The two GitHub path-history queries and exact-path responses are availability observations, not mathematical obstructions.

**No new spatial chain calculation is certified by this note or its audit.** The nontrivial usable reduction is the conditional kernel-valued factorization above. Actual instantiation requires the missing native framed adapter data.
