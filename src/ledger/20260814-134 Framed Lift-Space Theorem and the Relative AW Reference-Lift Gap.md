# Framed Lift-Space Theorem and the Relative AW Reference-Lift Gap

## Record

Date: 2026-08-14

Status: proved formal typing theorem and exact carrier specialization; loaded
lift space unconstructed.

Entry 133 correctly ablated ordinary coefficientwise Hom, but its replacement
objective was still one categorical level too linear.  The missing
specialization datum is not canonically an element of an
\(\operatorname{Ext}^1\) group.  It is a comparison between two fixed
two-extensions.  Consequently it is naturally a point of a lift/path space.
Only after choosing one point does \(\operatorname{Ext}^1\) become a group of
differences between choices.

This correction changes the order and interpretation of the next tests.

## The lift-space theorem

Let \(\mathscr D\) be a stable \(R\)-linear category, and let
\[
e_0,e_1:A\longrightarrow B[2]
\]
be two fixed maps.  Define
\[
\mathcal L(e_0,e_1)
=
\operatorname{Path}_{\operatorname{Map}_{\mathscr D}(A,B[2])}
(e_0,e_1)
\simeq
\operatorname{Null}(e_0-e_1).
\]

Then:

1. \(\mathcal L(e_0,e_1)\) is nonempty exactly when
   \[
   \omega=e_0-e_1=0
   \quad\text{in}\quad
   \operatorname{Ext}^2_{\mathscr D}(A,B).
   \]
2. If it is nonempty, its connected components form a torsor under
   \[
   \pi_1\operatorname{Map}_{\mathscr D}(A,B[2])
   =
   \operatorname{Ext}^1_{\mathscr D}(A,B).
   \]
3. There is no canonical zero in this torsor without an independently
   constructed reference path.

The proof is the standard loop-space action on the path space between two
points of a mapping space.  It is integral and uses no splitting.

This yields an important correction to the entry-133 rank trichotomy:

- \(\operatorname{Ext}^1=0\) does **not** falsify the synthesis.  If
  \(\omega=0\), it gives a unique connected component of lifts.
- \(\operatorname{Ext}^1\simeq R\) does **not** give a unique lift up to
  orientation.  It gives an affine \(R\)-torsor of lifts until geometry or
  boundary conditions select a point.
- higher rank or torsion measures ambiguity among lifts only after the
  \(\operatorname{Ext}^2\) obstruction has vanished.

Thus existence belongs to degree two; ambiguity belongs to degree one.

## Application to the scalar specialization objective

Once the loaded support category is constructed, the two intended
two-extensions should be
\[
e_{\rm supp}^{!,{\rm PC}}
=
\rho_{\rm PL}^{!,{\rm PC}}(e_F),
\qquad
e_{\rm Tate}^{!,{\rm PC}}
=
\Phi_{\rm nc}(\beta_\triangle)
\]
in one mapping space.  The correct candidate object is
\[
\boxed{
\mathcal L_{\rm sp}
=
\operatorname{Path}
\left(
e_{\rm supp}^{!,{\rm PC}},
e_{\rm Tate}^{!,{\rm PC}}
\right).
}
\]

The first formula objective is therefore
\[
\boxed{
\omega_{\rm sp}
=
e_{\rm supp}^{!,{\rm PC}}
-
e_{\rm Tate}^{!,{\rm PC}}
=0
\quad\text{in}\quad
\operatorname{Ext}^2_{\mathscr D_{\rm PC,F}^{D_3}(R)}(A,B).
}
\]

Only after this equation is proved may one ask for a geometric point
\[
\ell_{\rm sp}\in\pi_0\mathcal L_{\rm sp}.
\]
The induced scalar specialization map is then an evaluation of this chosen
comparison,
\[
G_{03}^{\rm Cousin}
\stackrel{\rm aspirational}{=}
\operatorname{Real}_{03}(\ell_{\rm sp}),
\]
and only afterward should one test
\[
\operatorname{gr}_{\mathfrak c}^1G_{03}
=K_{\rm alt}\otimes L_{\rm pol},
\qquad
\operatorname{gr}_Q(\rho_{\ell_{\rm sp}})(N_{\rm road})
=+[q_\Sigma],
\qquad
\operatorname{Res}_{x_3}G_{03}
=\operatorname{pur}_{x_3,\partial}^{\rm PC}.
\]

These values may select a point of an already constructed torsor.  They must
not be used to define its mapping space or its reference point.

## Exact carrier specialization

At carrier level, entries 114--115 already place the two extensions in the
same \(D_3\)-equivariant derived category and prove
\[
\omega_{\rm car}
=
\rho_{\rm PL}^{\rm car}(e_F)-\beta_\triangle
=0
\quad\text{in}\quad
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or}).
\]

Therefore
\[
\operatorname{Lift}_{\rm car}(e_F,\beta_\triangle)
\]
is nonempty, and its connected components form a torsor under
\[
\operatorname{Ext}^1_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})
\simeq\mathbb Z/2.
\]

This is not a remaining obstruction to existence.  It is the unresolved
parity of the comparison path.

The fixed base vertex, facet labels, orientations, saturated connector, and
the homology-level matrix \(1-r\) do not select a point of this torsor.  The
existing exact checker proves the carrier incidence and separately computes
the \(\mathbb Z/2\) group.  It does not construct a relative
Alexander--Whitney diagonal, a chain-level cap, or a comparison homotopy
between the two two-extensions.  Entry 103's explicit contraction is
non-equivariant and is not such a reference lift.

## Correct interpretation of the ablations

The two entry-133 ablations must also be retyped.  A forgetful functor acts on
the path object:
\[
\operatorname{Forget}(\mathcal L_{\rm sp})
\longrightarrow
\mathcal L_{\rm forgotten}.
\]

The correct control is that a selected geometric lift maps to a specified
canonical trivialization in the forgotten theory.  It is not necessary for
the whole acting \(\operatorname{Ext}^1\) group to vanish.

At present:

- the fully ordinary joint ablation is defined and contractible by entry
  133;
- the individual support/\(Q\) and Tate-window forgetful maps are untyped,
  because their common framed source category and defect arrows have not
  been constructed.

Their ranks are therefore undefined, not zero.

## The simplification

It is unnecessary to axiomatize an entire six-functor category before the
next finite test.  A smaller noncircular construction suffices:

1. fix the existing barycentric/cellular model of
   \[
   (X;B,L)
   =
   (K_6;B_{\rm short},
   F_{14}\sqcup F_{03}\sqcup F_{25});
   \]
2. construct an explicit \(D_3\)-equivariant relative
   Alexander--Whitney diagonal
   \[
   \Delta^{\rm AW}_{(X;B,L)}
   \]
   with its front/back convention, relative quotients, and endpoint
   augmentations;
3. cap with the oriented relative fundamental chain and compare the
   resulting chain-level two-extension with the
   \(N/(1-r)/\epsilon\) Tate extension;
4. compute the reflection defect of that comparison modulo \(2\);
5. only then load the same finite comparison with the positive-support,
   occurrence, multi-Rees, reciprocal/Borel--Moore, and PC/Cousin data.

This concrete chain model is enough to define the obstruction, the lift
torsor, and both ablations.  A general formalism may be built afterward.

## Sharp blocker

The loaded maps
\[
\rho_{\rm PL}^{!,{\rm PC}}(e_F)
\quad\text{and}\quad
\Phi_{\rm nc}(\beta_\triangle)
\]
are not yet typed as two points of one mapping space.  The repository has no
\(D_3\)-equivariant ringed positive-support realization with:

- a based nonzero \(Q\)-leg;
- endpoint-relative extraordinary variance;
- the full Tate window;
- the independent multi-Rees conormal lines;
- the occurrence-loaded relative AW cap;
- the reciprocal/Borel--Moore and physical-orientation factors.

Consequently \(\omega_{\rm sp}\), \(\mathcal L_{\rm sp}\), its
\(\operatorname{Ext}^1\)-torsor, and the two separate ablations are currently
undefined.  Deleting the two entries of the ordinary contraction would
produce a basis-dependent kernel, not this object.

The first canonical map to construct is the relative AW/cap comparison at
carrier level and its loaded extraordinary lift.  It must be derived without
using \(K_{\rm alt}\), \(q_\Sigma\), or the entry-131 residue to select its
parity.

## Evidence

Exact inherited certificates:

- `research/voevodsky/check_multirees_cartier_pl_cap.rs`
  - SHA-256
    `3389c61357f1ac14503569dac448a15ac89efc294e8ec20e42d9ba118ba5db5e`;
  - proves \(\omega_{\rm car}=0\), the carrier \(1-r\), and the acting
    \(\mathbb Z/2\), but contains no chain-level relative AW cap.
- `research/voevodsky/check_scalar_common_ring_hom.rs`
  - SHA-256
    `a73a1209ba961acab656d5e949d6d7dca9b5433ac0570a965b29daa73ec2acb2`;
  - proves the fully ordinary joint ablation is acyclic.

Read-only independent audits:

- Ptolemy carrier-parity audit: no canonical parity is selected by current
  labelled cellular data; no files changed.
- MCP worker run
  `run-66cd440c8db945a79245998101e6b377`: the proposed support/Tate homotopy
  equalizer is untyped because both defect arrows are absent; admissible
  rank and individual ablations are undefined, while the ordinary joint
  ablation is zero.

## Outcome contract

~~~json
{
  "claim": "The scalar off-diagonal is correctly typed as a path between two fixed framed two-extensions, not canonically as an Ext1 element. Existence is controlled by their Ext2 difference; when it vanishes, choices form an Ext1 torsor. At carrier level the obstruction is zero and the choices form an unpointed Z/2 torsor. At loaded PC level even the two comparison maps are still unconstructed.",
  "status": "proved",
  "assumptions": [
    "The ambient category is stable and R-linear once constructed.",
    "The support/Yoneda and Tate classes are fixed two-extensions rather than output-fitted maps.",
    "All carrier labels, D3 actions, orientations, and the integral Tate window are frozen.",
    "No relative AW convention is treated as canonical before its chain-level comparison is constructed."
  ],
  "factorization_test": {
    "carrier_Ext2_obstruction": "zero",
    "carrier_lift_components": "nonempty Z/2 torsor",
    "carrier_reference_lift": "unconstructed",
    "loaded_comparison_maps": "untyped",
    "loaded_Ext2_obstruction": "undefined",
    "loaded_Ext1_torsor": "undefined",
    "ordinary_joint_ablation": "contractible",
    "individual_framed_ablations": "untyped"
  },
  "counterevidence": [
    "The existing checker derives 1-r only at carrier/homology level and separately computes Z/2; it has no relative AW cap.",
    "Entry 103's contraction is non-equivariant and cannot point the D3 lift torsor.",
    "The ordinary target contraction crosses the based Q filtration and endpoint support.",
    "A coordinate kernel obtained by deleting contracting components depends on the chosen splitting."
  ],
  "next_experiment": "Construct one explicit D3-equivariant relative Alexander-Whitney diagonal and cap for (K6; B_short, F14 disjoint-union F03 disjoint-union F25), compare its two-extension with the Tate window, and compute the mod-2 reflection defect. Then load that same comparison with the positive-support PC/Cousin coefficients and test the Ext2 obstruction before any K_alt, qSigma, or residue normalization."
}
~~~
