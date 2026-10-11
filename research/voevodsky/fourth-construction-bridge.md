# Constructing the fourth return and one coherent comparison

## Question and claim boundary

Construct the conditional fourth route and test whether it preserves its required relationships to the other constructions, rather than only displaying a new shape.

The active obligation is **route/comparison compatibility**. The executable conjecture is that the electron return and the fourth return can encode the same complete two-component input, with an explicit lossless comparison between them. The stronger meta-tetrahedral interpretation requires comparisons with the original proton and neutron returns as well.

Rivals: two routes may agree while distorting the state; identical endpoint projectors may conceal a relative route phase; or a geometric comparison may be mistaken for a lossless state comparison.

## Explicit encoders and bridge

Let A_e be the vertical stack of the four retained electron face projectors. Let A_x be the stack of the six signed belt projectors. Their frame operators are

\[
A_e^\dagger A_e=2I,
\qquad A_x^\dagger A_x=S.
\]

The electron encoder is J_e=A_e/sqrt(2). The fourth encoder is J_x=A_x S^(−1/2), with the positive inverse square root and the actual belt signs retained.

An explicit comparison is

\[
T=J_xJ_e^\dagger.
\]

The checker materializes this 12×8 matrix and verifies

\[
TJ_e=J_x,\qquad
T^\dagger T=N_e,\qquad
TT^\dagger=N_x.
\]

Consequently the direct route from a two-component input to the fourth return agrees with the route through the electron records, for every input. T is an isometry between the selected two-dimensional subspaces; it is not an isomorphism between the entire eight- and twelve-coordinate raw spaces.

This bridge is constructed using the retained common spinor coordinate frame. Its existence is not a derivation of that frame or of a common full construction state for all four endpoints.

## Exact normalization without numerical square roots

For the current belt, set

\[
a=\frac5{\sqrt{74}},\qquad
\delta=\frac{21}{\sqrt{74}},\qquad
B=(3+\delta)I+3a\sigma_y,\qquad
k=\delta^2(6+2\delta).
\]

Then B is positive Hermitian and B²=kS⁻¹. Store

\[
C=A_xB,\qquad F=CA_e^\dagger,
\]

with their positive normalization factors. The actual matrices are J_x=C/sqrt(k) and T=F/sqrt(2k).

All coefficient numerators and squared denominators lie in Q(sqrt(3),sqrt(74),i). Exact identities C†C=kI, C C†=kN_x, F†F=2kN_e, F F†=2kN_x and F A_e=2C verify the normalized statements without rounding.

The separate bridge is not counted among the fourth return's 312 core transfers.

## Two falsifiers

1. **Agreement without preservation.** Replacing J_x by A_x/sqrt(3) still permits the direct and through-electron routes to agree, but the resulting map is not an isometry. At +y and −y inputs its total weights are 1−5/sqrt(74) and 1+5/sqrt(74). At a +z input the total weight happens to be one, yet reconstruction still fails. Neither route equality nor unit weight on one sample suffices.
2. **Endpoint equality without rooted route equality.** T and −T have identical source and target projectors. Only T agrees with the retained direct-input encoder; −T changes its relative sign. The common input record and phase convention are therefore part of the comparison.

## What this does and does not complete

The electron/fourth edge now has an explicit lossless comparison and a checked common-input square.

The original proton and paired belt returns each select one complex mode. The electron and fourth returns each retain two components. Thus the existing selected-state spaces cannot all be identified losslessly. The fourth retains the neutron route's geometry and face signs, not an already established equivalence to its complete coefficient state.

This does not rule out the operator's proposed common construction record: a larger retained record or explicitly lossy views could have different output ranks. Those maps must be supplied. They are not constructed by the present square, and the other edges and faces of the proposed meta-tetrahedron remain unverified.

## Interactive construction

The generated standalone page is `papers/witness-generators/fourth-construction.html`; its site route is `/experiments/fourth-construction.html`.

It displays the four-face reference and signed six-face construction side by side. The stages expose the failed face-count normalization and its frame-correct replacement. Controls select the input state and either the direct or through-electron route. Live checks separately report total weight, route difference and recovered-state error.

The page embeds matrices decoded from the exact stored bridge; it does not fetch mutable coefficient files at runtime. The template and publisher are retained, and existing construction pages link to it. The fourth endpoint remains unnamed.

## Verification

```text
python research/voevodsky/checkers/check_fourth_construction_bridge.py
python research/voevodsky/checkers/prepare_fourth_construction_page.py
pnpm run build
node research/voevodsky/checkers/check_fourth_construction_page.mjs
```

The exact checker has eleven conditions, including the two falsifiers and input immutability. Artifacts:

- `results/fourth_construction_bridge.json`
- `results/fourth_construction_bridge_store.json`
- `results/fourth_construction_page.json`
- `results/fourth_construction_browser.json`

The browser test samples both routes, both normalizations, input-state changes and a narrow viewport. Its numerical checks supplement, rather than replace, the all-input matrix identities.
