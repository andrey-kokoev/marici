# Second audit of the RH interaction net against the live source mathematics

## Scope

This packet audits Aspect's live contract
`research/aspect/contracts/theta-rh-interaction-net-state.v1.json` against the
source mathematics through Nima's event 10136. It refines the earlier audit;
it does not alter the SCC implementation and does not claim RH.

## Verdict

The outer dependency topology remains sound. The exact frontier antichain is
still Adams type-fiber composition, endpoint attachment, and the archimedean
determinant-to-operator lift. The defect is resolution: the contract still
records `type_fiber_adams_composition` as one undifferentiated open formal
slot, although its source side now contains several constructed interaction
cells and one sharply isolated missing incidence.

The Adams box should therefore become a typed subnet, not be marked
constructed.

## Constructed internal cells

The following witnesses now have source formulas.

1. The local adjacent-window carrier is

   \[
   D_p=M_{W_{2\log p}-W_{\log p}},
   \qquad \|D_p\|\le 1.
   \]

2. The coefficient-valued comparison map is

   \[
   J_p^{\mathrm{cell}}e_{p,k}=[W_{k\log p}],
   \qquad k=1,2.
   \]

   Its oriented endpoint difference represents (D_p), retains the
   coefficient wall, and preserves the prime label.

3. Finite prime diagonality is exact on the labelled valuation/Fock carrier.
   At completion its correct certificate is unconditional convergence of
   coordinate truncations on a fixed authorized rigging, not merely bounded
   individual prime projections.

4. The bilateral theta packet supplies a source-native reciprocal doublet:

   \[
   v_0=m(1,1)^T,
   \qquad
   v_1=\frac m2(1,-1)^T.
   \]

   It is rank two when (m\ne0).

5. Mellin half-density transport supplies its exact moving metric:

   \[
   T_L=\operatorname{diag}(e^{L/2},e^{-L/2}),
   \qquad
   G_L=\operatorname{diag}(e^{-L},e^L),
   \]

   with

   \[
   T_{L\to M}^{*}G_MT_{L\to M}=G_L.
   \]

   Consequently the transported frame Gram is independent of (L). This is
   an object-indexed isometric bundle, not a single uniformly equivalent
   Euclidean Hilbert space.

These are inhabitants of the source half of the Adams interaction net. They
do not yet inhabit the completed Adams edge.

## First open cell

The earliest missing constructor is now the metric- and label-preserving
incidence

\[
\mathcal I_{p,L}:
(\operatorname{span}\{v_0(L),v_1(L)\},G_L)
\longrightarrow
\mathcal A_{\mathrm{hist},p,L},
\]

where the target is the causal-history auxiliary block. It must simultaneously
produce independently typed endpoint lifts and the relative Green/Stokes form

\[
L_{P,p},\qquad L_{Q,p},\qquad
b_p=L_{Q,p}D_pL_{P,p}^{*}.
\]

The required laws are:

- preservation of prime idempotents;
- preservation of the Mellin transported metric;
- exponential primitive and tempered square target riggings;
- radical annihilation and closability;
- reciprocal reversal (b_p\mapsto b_p^{*});
- a source-derived odd history compression matching the Euler odd current;
- growth below the global summability threshold.

This incidence, rather than trace rank or local window propagation, is the
first unresolved arrow.

## Authority correction

The Fourier quarter-turn must not label the source of the tail skew phase.
For the normalized theta source, Fourier is fixed up to dilation reversal and
does not create the needed relative quadrature. The presently authorized
candidate is causal-history reflection,

\[
T_{\mathrm{hist}}=\frac{H_+-H_+^{*}}2,
\qquad
T_{\mathrm{hist}}^{*}=-T_{\mathrm{hist}}.
\]

Even this remains a candidate until it has a common closed domain, preserves
prime labels, descends through radicals, and compresses to the arithmetic odd
coordinate. The Schur formulas derived from an abstract skew carrier remain
conditional templates.

## Correct placement of later gates

Once the incidence exists, the local auxiliary cell still has distinct gates:

- auxiliary contraction;
- endpoint-loading contraction;
- absolute scale bounds;
- triangular shear control;
- positivity of the assembled endpoint Gram.

These are internal Adams-constructor admissibility gates. They are not the
global five Green margins and should not be counted as additional global
margins.

The connected Euler tail of grades (k\ge3) belongs to enlarged-cell or
reciprocal-sewing data. It cannot be silently compressed into the grade-one to
grade-two cell.

## Interaction-net refinement

The coarse node should be expanded as follows:

```text
labelled coefficient wall
  -> adjacent-window history and D_p
  -> coefficient cell map J_p^cell
  -> bilateral even/odd theta trace frame
  -> Mellin moving-metric transport
  -?> metric-preserving incidence into causal history
  -?> typed endpoint lifts L_P,p and L_Q,p
  -?> Green/Stokes mixed block b_p
  -?> history-odd Euler compression
  -?> nested Schur admissibility and endpoint positivity
  -?> typed Adams edge and grade-six filler
```

The question marks identify open construction cells. All arrows before the
first question mark are source-inhabited, subject to their stated completion
typing.

## Falsifiers for the refined SCC subnet

The refinement should reject:

1. promoting the Adams edge merely because the reciprocal trace frame is rank
   two;
2. using one fixed Euclidean metric instead of the object-indexed (G_L);
3. attributing the tail phase to a Fourier quarter-turn;
4. fitting (b_p) from its scalar Euler shadow rather than deriving the two
   endpoint lifts;
5. preserving local prime labels but smearing them under completion or sewing;
6. importing the full Euler odd tail into the two-grade cell without an
   authorized enlarged-cell compression;
7. treating local Schur contractions as the global five-margin theorem;
8. marking the typed grade-six filler constructed while its four typed edge
   maps remain absent.

## Exact status after the audit

- Outer Aspect topology: retained.
- Coarse Adams status: correctly open, but under-resolved.
- Newly constructed internal source cells: bilateral rank-two trace and exact
  Mellin moving-metric transport, in addition to the earlier history and label
  cells.
- First missing interaction cell: metric-preserving, prime-preserving incidence
  from the bilateral trace bundle into the causal-history auxiliary block.
- Endpoint and archimedean frontier cells: still independently open.
- RH terminal: open.

