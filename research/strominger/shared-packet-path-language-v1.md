# Shared packet language: native grammar, enlarged spin paths, source frames

## Question and disposition

Operator instruction: “add to conjecture net, and resolve.” The question has three different strengths:

1. **One source-bound packet grammar:** constructed on all three native sources.
2. **One signed spin-path language:** constructed for the electron and the explicit proton/neutron tensor-doublet candidates, including source-derived coordinate-frame adapters.
3. **The same nonabelian spin action already on the original baryon return lines:** rejected by a nonzero native-action residual.

This resolves the mathematical shared-language gates, not the original physical spin/coupling selection gate. The live [integration net](contracts/packet-assembly-bridge-conjecture-net.v1.json) also records the subsequently resolved [source spin-lift splitting proposition](source-spin-lift-splitting-v1.md); consult its `frontier` and `recommended_start` for current execution state.

SCC obligations are source attachment, explicit frame transport and phase-corrected route compatibility. No geometric square-filling homotopy or primitive-cost interpretation is imported.

## The common native grammar

Each model supplies a source $S$, metric $M$, encoder $K$, decoder $D$, operation dictionary $\mathcal O$, reader family $\mathcal R$ and retained word $w$:

\[
\mathcal P=(S,M,K,D,\mathcal O,\mathcal R,w),
\qquad DK=I,\quad KD=N.
\]

Here the identities are at the declared return-image scope. The actual native ranks are proton/neutron/electron $1/1/2$. The baryon stage letters L/G/N act identically on their respective lines; the electron additionally admits its 24 spinor operations. The common grammar does not identify their dictionaries, raw coordinates or metrics.

The checker instantiates source-bound word types and checks source, operation and enlargement guards. A proton word cannot be consumed as a neutron word; an original baryon line refuses a spin-mixing token. An inverse word and an empty word can have equal endpoint matrices while remaining different retained records.

## Why the strongest native identification fails

For each original baryon source, the actual encoder $K_1$ obeys

\[
LGK_1=GLK_1=K_1.
\]

The requested electron-style anticommutation equation would require their negatives to agree. Its residual is

\[
LGK_1+GLK_1=2K_1\ne0.
\]

The receipt exports this column for each source. More generally, every complex-linear endomorphism of a complex line is scalar. In characteristic zero, two invertible scalars cannot anticommute. This excludes the same full nonabelian spin action on these unextended returns; it does not describe physical proton/neutron spin states or refute the weaker common grammar.

## Conditional common path language

Reuse the explicit tensor candidates:

\[
\widetilde K=K_1\otimes I_2,\qquad
\widetilde D=D_1\otimes I_2,\qquad
S_U=I_{36}\otimes U.
\]

For the **same** 24 matrices and normal-form tokens used by the electron,

\[
S_U\widetilde K=\widetilde K U,\qquad
\widetilde D S_U=U\widetilde D.
\]

The original source metric becomes $M\otimes I_2$; its exact squared-normalizer tag is retained. Coordinates change from 36 to 72, return rank from 1 to 2, and chosen stage support from 1836 to 3672. None is a mere relabelling.

The inherited symbolic normalizer has all 576 multiplication results verified in the common exact field. Each enlarged baryon source transports all 12 signed sector comparisons, 36 situated encounters, 8 signed triple critical-pair joins and 48 permutation routes. Across the two sources these give 24 sectors, 72 encounters, 144 placement equations, 16 joins and 96 permutation routes.

Actual geometric actions remain attached as

\[
T_g=P_g\otimes(\pm U_g),
\]

with the nonidentity $P_g$ derived from the original source, not replaced by identity. Both mixed orders with every common spin operation are checked; no commutation is assumed.

## A real failure: the retained Cholesky frames do not close

The first prospective experiment measured the actual old-frame conjugations rather than assuming a common dictionary:

| Source generator | Shared operations still in the dictionary under conjugation |
|---|---:|
| Proton 0 | 4 of 24 |
| Proton 1 | 2 of 24 |
| Neutron 0 | 4 of 24 |

These counts hold for both lift signs. None of the old-frame generator lifts itself belongs to the 24-element dictionary. The receipt exports an outside conjugated matrix for each case.

Thus the initial conditional construction supplies a shared spin-word **sublanguage**, but not closure under all actual geometric operations in those retained coordinates. This failure is preserved. A second prospective contract tests a declared source-frame transport rather than retroactively asserting old-frame closure.

## Source-derived frame transport resolves the coordinate obstruction

The earlier actual coefficient binding already supplies native Cartesian source adapters $V$: the proton's source tetrahedron is mapped to its retained native tetrahedron, and the neutron's source coordinates to its retained Cartesian cyclic action. Their metric equations determine the scaling needed for an orthonormal frame $F$.

Let $B$ be the earlier Cholesky frame. Set

\[
O=FB^{-1},\qquad O^TO=I.
\]

If its determinant is negative, negate $F$ and $O$ together. This preserves the conjugated source rotations and gives a proper frame map. No rotation is fitted to a desired spin matrix.

Solve the three Clifford intertwining equations

\[
CE_j=E(Oe_j)C,\qquad j=1,2,3.
\]

For both sources the exact solution space is a one-complex-dimensional line. The exported representative is invertible and satisfies

\[
C^*C=rI,\qquad r\ne0.
\]

The scalar $r$ is retained exactly; no approximate square root is introduced. The representative's scalar freedom is coordinate freedom, not a selected physical spin phase.

Transport the encoder and decoder explicitly:

\[
K'=\widetilde K C^{-1},\qquad D'=C\widetilde D.
\]

Then

\[
D'K'=I,\qquad K'D'=\widetilde N,
\qquad K'^*(M\otimes I_2)K'=\frac{\rho}{r}I.
\]

The raw return projector is unchanged. The squared-normalizer becomes $\rho/r$; retaining the old normalizer fails. At the unnormalized coordinate level $K'(C\psi)=\widetilde K\psi$, so raw readers are preserved by the coordinate transport, not inferred from an endpoint count.

Both signs of all three source lifts now satisfy

\[
CU_gC^{-1}\in\mathcal G_{24}.
\]

Each transported lift normalizes **all 24** common operations. The unchanged actual raw action has the correct new square:

\[
T_gK'=K'(C(\pm U_g)C^{-1}),\qquad
D'T_g=(C(\pm U_g)C^{-1})D'.
\]

All common actions, signed sectors, encounters and triple joins pass with these new encoders. Keeping the old encoder while changing only the logical source action produces an exported nonzero residual.

The coordinate-frame obstruction is therefore resolved on the explicit doublets. It has not become a source-derived physical preparation or a choice between the two lift signs.

## Verification and remaining boundary

Two new exact suites pass:

- **12 check groups:** `checkers/check_shared_packet_path_language.py`, receipt `results/shared-packet-path-language-v1.json`.
- **10 check groups:** `checkers/check_shared_packet_frame_adapter.py`, receipt `results/shared-packet-frame-adapter-v1.json`.

The first suite's stdout initially contained two JSON objects. Its framing was corrected and a new SCC freeze was made; scientific tests and their frozen contract were unchanged. The authoritative corrected shared-language freeze is `b6433af337e1c949a28a21babb63aa4f15b28f4943471be07d00e4facf22f8f7`. The frame-adapter freeze is `a5fc7cc4ca3ebf718e24db390cb494eb2fc48bb347b98c2d9aff573f639bf3ef`.

Reproduce selected SCC checks:

```text
python research/aspect/scc/scc.py check shared-packet-path-language-v1
python research/aspect/scc/scc.py check shared-packet-frame-adapter-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

Both scientific suites validate inherited source hashes and retain deliberate failures. They use the existing exact number field and standard-library arithmetic; native producers and proof compilers are not executed. The registration audit checks the current dependency graph and scoped receipts, not a new physical bridge proof; the source splitting proposition has its own separate exact checker.

What remains missing is the independent source selection of the doublet, physical frame/lift and charge/magnetic/internal interaction/resource laws. The original coupling gate and root remain open. No minimum witness count, J-stage correspondence, physical mass relation or universal higher-path calculus follows from the common conditional language.
