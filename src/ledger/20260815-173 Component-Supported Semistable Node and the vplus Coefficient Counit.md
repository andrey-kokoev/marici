# Component-Supported Semistable Node and the (v_+) Coefficient Counit

## Record

Date: 2026-08-15

Status: two scoped coefficient theorems proved. The selected semistable-node
component has a canonical principal support line and two primitive conductor
Tor grades; on the (v_+) branch this line carries a unique normalized
Cartier/occurrence counit. Literal identification with the entry-143 spatial
endpoint, global polarity and generic-(Q) compatibility, the framed mapping
fiber, and parity remain unconstructed. No graph admission is claimed.

## The semistable node and its normalization row

Let

\[
D=V(tx)=X\cup T,
\qquad
X=V(x),
\qquad
T=V(t),
\qquad
C=X\cap T.
\]

Over a coefficient field or the corresponding polynomial base, the node ring
is

\[
\mathcal O_D=k[x,t]/(xt).
\]

Its normalization is the disjoint pair

\[
\mathcal O_X\oplus\mathcal O_T
=k[t]\oplus k[x].
\]

A pair descends to \(D\) exactly when its two conductor values agree. Hence
the normalization--conductor row is

\[
\boxed{
0\longrightarrow\mathcal O_D
\longrightarrow\mathcal O_X\oplus\mathcal O_T
\xrightarrow{\varepsilon_X-\varepsilon_T}
\mathcal O_C
\longrightarrow0.
}
\]

The difference map is surjective. This is the local coefficient form of the
normalization/conductor cdh row, with no averaging and no inversion.

## Selected-component support object

Select the physical component \(X=V(x)\) by its admitted label. Its reduced
component-support object is

\[
J_X
:=operatorname{Cone}
(\mathcal O_X\longrightarrow\mathcal O_C)[-1].
\]

Since \(\mathcal O_X=k[t]\) and \(C=V(t)\subset X\),

\[
\boxed{
J_X=(t)\subset k[t].
}
\]

Thus component support is a principal conductor ideal. It is not the entire
two-branch node and is not obtained by taking a scalar difference of endpoint
values.

The opposite component has the analogous ideal \((x)\), but selecting
\(X\) retains the conormal label \([t]\). The selection is geometric input:
the coefficient theorem does not derive which component is physical from an
unlabelled node.

## Derived conductor fibre and the two Tor grades

On \(X\), the conductor Cartier resolution is

\[
k[t]\xrightarrow{\ t\ }k[t].
\]

Derived restriction to \(C=k[t]/(t)\) sets this differential to zero.
Therefore

\[
\boxed{
\operatorname{Tor}_0^{k[t]}(k,k)=k,
\qquad
\operatorname{Tor}_1^{k[t]}(k,k)=k,
}
\]

and there are no higher terms. Both grades are primitive rank-one lines.
The filtered connecting/Bockstein symbol is the retained conormal

\[
[t].
\]

The distinction is essential:

- \(J_X=(t)\) is the component-support ideal; while
- \(\operatorname{Tor}_0\oplus\operatorname{Tor}_1\) is its two-grade
  derived self-intersection on the conductor.

Neither grade may be contracted away merely because \(J_X\) is principal.

## (D_3) conormal signs

For the three rotated nodes, order the selected conormal labels as

\[
(t_1,t_3,t_5).
\]

The physical three-cycle permutes this ordered triple with determinant
\(+1\), while reflection reverses its determinant orientation and acts by
\(-1\). Thus

\[
\det(R)=+1,
\qquad
\det(S)=-1.
\]

This proves the local coefficient sign representation. It does not construct
the global polarity-conjugate endpoint counit or its reflection square.

## Selected corner in the completed weighted graph

Use the weighted occurrence-normal closure from entry 172. At \(t=0\), with
the long comparison parameter \(t_D\) a unit in its named completed scope,
the strict selected \(X\)-direction has nonzero \(H\). The graph equation
then forces

\[
P=0.
\]

Hence the selected \(X\) component has a unique normal corner. The opposite
direction retains an exceptional \(\mathbb P^1\) ambiguity.

This uniqueness is completion-scoped. If \(t_D\) also vanishes, the graph
equation can vanish identically and the deeper fibre again becomes
ambiguous. No universal inversion of \(t_D\) is asserted, and the result does
not clean the full unlocalized graph.

## The (v_+) coefficient node

Specialize to the positive endpoint node

\[
u_5=t_5x_5.
\]

The selected component-support line is

\[
J_{v_+}=(t_5)
=\operatorname{Cone}
(\mathcal O_X\longrightarrow\mathcal O_C)[-1].
\]

Use the reciprocal/original one-normal packet

\[
D_5=K(u_5^\vee)\otimes K(u_5),
\qquad
u_5^\vee=-q_5^{-1}u_5.
\]

Its primitive oriented middle generator is

\[
\boxed{
\eta_5=(-q_5,-1).
}
\]

It is closed under the middle differential. After the standard \(q_5\)
normalization of the top generator \(z_{\rm norm}\), the chain identity is

\[
\boxed{
d z_{\rm norm}=x_5t_5\eta_5.
}
\]

This equality retains separately the occurrence factor \(x_5\), the
conductor conormal \(t_5\), and the reciprocal/BM excess vector \(\eta_5\).

## Cartier boundary and occurrence-dual compatibility

The Cartier connecting morphism along \(x_5=0\) removes the principal
occurrence factor and gives

\[
\boxed{
\beta_{x_5}(z_{\rm norm})=[t_5]\eta_5.
}
\]

No \(x_5^{-1}\) is adjoined to the base. This is a principal-line
extraordinary evaluation, not scalar division.

The first occurrence edge has

\[
de=X_Dm_+-x_5v_+.
\]

Its \(v_+\) coefficient is \(-x_5\). Evaluation by the positively oriented
principal ideal dual

\[
x_5^\vee(x_5)=1
\]

therefore produces endpoint coefficient \(-1\). Reversing the occurrence
orientation reverses this sign. Hence the occurrence counit and the
component-supported Cartier class have compatible, independently tracked
orientations.

## Uniqueness of the coefficient counit

The conductor line is principal, so

\[
\operatorname{Hom}_{k[t_5]}((t_5),k[t_5])
\]

is rank one. Among integral scalar multiples, primitive positive residue
normalization selects the scalar \(+1\) uniquely. Thus the local coefficient
counit

\[
\epsilon_{v_+}^{\rm coeff}:
J_{v_+}\otimes D_5
\longrightarrow\mathbf1
\]

is uniquely fixed by

\[
\epsilon_{v_+}^{\rm coeff}
\bigl([t_5]\eta_5\bigr)=+1
\]

with the declared orientation convention. The occurrence edge then carries
the forced \(-1\) boundary sign above.

The shared \(u_1,u_3\) packets remain external factors. Their tensoring does
not alter the uniqueness of the selected \((t_5)\) counit.

## Spatial and global boundary

The coefficient node and completed selected corner do not identify the
selected strict transform with the literal entry-143 endpoint costalk
\(E_{v_+}\). That spatial identification must construct a ringed functor

\[
\Phi_{v_+}^{\rm supp}:
(J_{v_+},D_5)
\longrightarrow
E_{v_+}^{\rm BM,\check C}
\]

and prove that the coefficient counit is its extraordinary endpoint
evaluation.

Still unconstructed are:

- the sheaf-level extraordinary counit on the selected strict transform;
- the literal entry-143 face/circle endpoint identification;
- the polarity-conjugate \(v_-\) component and the global reflection square;
- descent/pushforward to the full endpoint/\(Q\) target;
- the generic-to-special \(Q03\) leg and logarithmic Beck--Chevalley cell;
  and
- the endpoint-fixed mapping fiber.

Therefore global polarity compatibility and reflection parity are undefined.

## Anti-circularity controls

- Do not identify \(J_X=(t)\) with its two-grade derived conductor fibre.
- Do not choose the physical component from the desired endpoint sign; its
  label is independent input.
- Do not promote completion-scoped invertibility of \(t_D\) to the universal
  base.
- Do not infer a spatial endpoint from the unique coefficient corner.
- Do not replace the Cartier evaluation by inversion of \(x_5\).
- Do not infer the polarity conjugate, generic \(Q\), mapping fiber, parity,
  or graph admission from the coefficient counit.

## Falsifiers and scope

The node theorem would be falsified by failure of the normalization row,
nonsurjectivity of the conductor difference, a component-support object not
isomorphic to \((t)\), loss of either Tor grade, or incorrect \(D_3\)
determinant signs. The completed-corner theorem would be falsified by more
than one selected normal corner when \(t_D\) is a unit.

The \(v_+\) counit theorem would be falsified if \(\eta_5\) were not closed,
if \(dz_{\rm norm}\ne x_5t_5\eta_5\), if the Cartier boundary required
\(x_5^{-1}\), if the occurrence-dual sign disagreed, or if primitive positive
normalization failed to be unique.

The spatial boundary would be crossed by an independently constructed
ringed endpoint functor \(\Phi_{v_+}^{\rm supp}\), its polarity conjugate,
and a global pushforward retaining the generic \(Q\) leg. No no-go is claimed
for that construction.

## Provenance and exact certificates

The exact checkers are

- `research/voevodsky/check_d03_component_supported_semistable_node.rs`; and
- `research/voevodsky/check_d03_vplus_component_supported_counit.rs`.

Their SHA-256 hashes are, respectively,

- `54a99308ad6424f3707d714ba21095ade69f4c7dce762177276156478834a583`;
  and
- `c555c8105de0e8ae4320decc59b416847be957073dec3db728016d30f9c3e64a`.

The first verifies the normalization equalizer, surjective conductor
difference, \(J_X=(t)\), both primitive conductor Tor grades and \([t]\),
the \(D_3\) determinant signs, and the unique selected corner in completed
scope. The second verifies \(u_5=t_5x_5\), closure and primitivity of
\(\eta_5\), the normalized top identity, Cartier Bockstein, absence of
\(x_5\) inversion, occurrence-dual sign compatibility, and uniqueness of
the primitive positive counit.

## Next experiment

Construct the sheaf-level extraordinary endpoint counit from the selected
strict transform to the literal entry-143 \(v_+\) BM--Cech costalk, retaining
both conductor Tor grades and \([t_5]\). Then construct the polarity-conjugate
\(v_-\) component, verify the global reflection square, and glue both
endpoint maps to a normalization-provenanced source with a retained nonzero
\(Q03\) leg. Only afterward instantiate the framed mapping fiber or evaluate
parity.

## Outcome contract

~~~json
{
  "claim": "For the selected component X of the semistable node V(tx), the normalization-conductor row is exact, J_X=Cone(O_X->O_C)[-1]=(t), and the conductor fibre retains primitive Tor0 and Tor1 with symbol [t]; on the v_plus node u5=t5*x5, eta5=(-q5,-1) is closed, d(z_norm)=x5*t5*eta5, and beta_x5(z_norm)=[t5]*eta5 gives the unique primitive positive coefficient counit compatible with the occurrence ideal dual.",
  "status": "proved",
  "scope": "component-supported coefficient node, completed weighted-graph corner, and local v_plus coefficient counit only; no graph admission, literal entry143 endpoint identification, global Q map, mapping fiber, or parity",
  "assumptions": [
    "The physical component X=V(x) is selected by its admitted label.",
    "t_D is a unit only in the named completed D03 comparison.",
    "The ordered conormal labels are (t1,t3,t5).",
    "Occurrence principal duals and reciprocal normal lines retain separate orientations."
  ],
  "factorization": {
    "normalization_row": "0 -> O_D -> O_X+O_T -> O_C -> 0",
    "component_support": "J_X=(t)=Cone(O_X->O_C)[-1]",
    "conductor_Tor": {"Tor0": 1, "Tor1": 1, "higher": 0, "symbol": "[t]"},
    "D3_determinants": {"rotation": 1, "reflection": -1},
    "selected_X_corner": "unique when t_D is a unit",
    "opposite_corner": "exceptional P1 ambiguity",
    "deeper_fibre": "ambiguous if t_D also vanishes",
    "vplus_node": "u5=t5*x5",
    "vplus_component_line": "(t5)",
    "reciprocal_normal": "u5^vee=-q5^-1*u5",
    "eta5": "(-q5,-1), primitive and closed",
    "normalized_identity": "d(z_norm)=x5*t5*eta5",
    "Cartier_beta": "[t5]*eta5",
    "x5_base_inversion": false,
    "occurrence_edge": "de=X_D*m_plus-x5*v_plus",
    "positive_endpoint_evaluation": "x5^vee(x5)=1 gives coefficient -1",
    "coefficient_counit_uniqueness": "rank-one Hom and primitive positive scalar +1",
    "literal_entry143_vplus_identification": "unconstructed",
    "global_polarity_Q": "unconstructed",
    "mapping_fiber": "uninstantiated",
    "parity": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_component_supported_semistable_node.rs",
    "research/voevodsky/check_d03_vplus_component_supported_counit.rs",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260814-119 Endpoint-Relative Ablation and the Missing Unlocalized Road Costalk.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-167 First Central-Flip Line-Valued Counit and the Next-Flip Generic Gate.md",
    "src/ledger/20260815-172 Weighted Occurrence-Normal Graph and the Cartier Nearby-Cycle Gate.md"
  ],
  "checker_sha256": {
    "component_supported_semistable_node": "54a99308ad6424f3707d714ba21095ade69f4c7dce762177276156478834a583",
    "vplus_component_supported_counit": "c555c8105de0e8ae4320decc59b416847be957073dec3db728016d30f9c3e64a"
  },
  "counterevidence": [
    "The component-support ideal and its two-grade derived self-intersection are different objects.",
    "The selected corner is unique only while t_D is a unit in the named completion.",
    "The coefficient counit does not identify the selected node component with the literal entry143 endpoint.",
    "No polarity-conjugate endpoint or generic-Q pushforward has been constructed."
  ],
  "next_experiment": "Construct the sheaf-level extraordinary v_plus endpoint counit to the literal entry143 BM-Cech costalk retaining both Tor grades and [t5], then build its polarity conjugate and glue both to a normalization-provenanced source with a nonzero Q03 leg before forming the mapping fiber or parity."
}
~~~
