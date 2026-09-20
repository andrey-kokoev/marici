# Two-polarity/four-presentation source patterns for determinant construction

## Question

Which prior constructions explain how rich (2,4)-shaped packets are actually realized, transported, and read out, rather than replaced by arbitrary finite matrices?

Operator direction: search the existing amplituhedron and related analytical realizations for the full polarity/phase structure, including the possibility that a scalar residual reflects an omitted component. This is a search direction, not evidence identifying the earlier -4/5 residual.

This is a bounded source audit, not a new verification run. Equations below are read from the cited packets or implementation. The large coverage ledger was inspected through its initial semantic-refinement audit; no claim is made to have exhaustively audited all its later revisions.

## 1. Amplituhedron construction retains cells, not just transports

Sources:

- `research/nima/coherent-construction-law.md`
- `research/nima/coherent-construction-bridge-atlas.md`
- `research/nima/nnmhv-positive-geometry-history-equivalence.md`

The construction starts from an oriented history-cell chain and its source map C -> CZ:

\[
\Omega_{n,2,4}=\sum_h\epsilon_h(\Phi_Z)_*\omega_{\mathcal C_h}.
\]

It requires degree-one coverage, cancellation of internal oriented facets, and residue-compatible pushforward. Composition of transport matrices alone does not establish any of those properties.

A concrete nonfaithfulness witness is already recorded: at seven points, three distinct certified cells have the same rank-one projective transport. The minimal tested remedy retains transport together with the history endpoint labels. A matrix-only determinant constructor can therefore lose the source even when all its path products cohere.

The selected scalar update has two retained contributions:

\[
\Delta S_n=J_n^{\rm ins}+J_n^{\rm ref}.
\]

The stored `results/phase-boundary-biconvolution-rule.json` separately records contravariant insertion and covariant reflow before augmentation. Its numerical examples show that a zero boundary-index shift still has both channels; it does not mean the contributions vanish. These are stored numerical results, not newly checked exact identities.

## 2. Four-component exterior composition is implemented, not inferred from dimension

Source: `research/nima/coherence_amplitude.py`.

A `CoherencePhase` carries a degree-four Grassmann weight. `CoherenceHistory` composes these by exterior multiplication. Its component evaluator uses four antisymmetrized determinants, one for each SU(4) component, multiplied by the phase normalizations and chart Jacobian. For depth d, each determinant is d by d; at depth two it is 2 by 2 and the resulting weight has degree eight. Branches are summed only after the same component has been extracted on each branch.

This gives an explicit analytical model of how a two-step/four-component object retains coupling and antisymmetry. It does not identify the four SU(4) component indices with four Fourier charts, nor the two Grassmann factors with reciprocal polarity. Those comparisons require maps; the common numbers are not the maps.

## 3. Four analytical charts change the product

Sources:

- `research/nima/four-chart-fourier-convolution-realization.md`
- `research/nima/four-charts-are-one-periodic-object-in-the-canonical-homeomorphism-groupoid.md`

The chart products alternate:

\[
\mu_0=*,\quad\mu_1=\cdot,\quad\mu_2=*,\quad\mu_3=\cdot.
\]

Fourier transport advances both the analytical presentation and the source channel labels. The recorded intertwining law is

\[
\mathcal F R_i(T)=R_{i+1}(qT).
\]

Thus one cannot keep a fixed multiplication while merely permuting four slots. Tagged Schwartz atoms retain channel provenance. Removing their tags requires an additional independence theorem.

On canonical Pontryagin charts, the atom orbit is

\[
\delta_v\to\chi_{-v}\to\delta_{-v}\to\chi_v\to\delta_v.
\]

The ordinary closure is q^4=I. In the stable graded version q^4=Sigma, so the full turn remembers a grade shift. The packet explicitly withholds native-topology equivalence of all historical semilocal charts.

## 4. Polarity is antiunitary and contravariant

Source: `research/nima/opposite-polarity-carriers-are-conjugate-homeomorphic-presentations.md`.

On the minimal source-generated feature carriers, source star constructs the opposite-sheet antiunitary D. It extends with the signed endpoint coordinates and obeys D^-D^+=I. Dagger reverses composition and exchanges left/right successors.

This supplies polarity transport rather than duplicating a matrix and assigning it a sign. Polarity remains recorded equivariant data even when the two carriers are conjugate-homeomorphic. Descent to a positive quotient remains a separate acceptance theorem.

## 5. There is a concrete source-derived four-port Fourier realization

Sources:

- `research/grothendieck/generic-rational-cosets-form-an-exact-four-port-fourier-orbit.md`
- `research/voevodsky/absolute-radial-mellin-collapses-the-fourier-orbit-but-oriented-radial-doubling-retains-it.md`

Shifted support combs P_r and character-weighted combs C_r have the orbit

\[
P_r\to C_{-r}\to P_{-r}\to C_r\to P_r.
\]

Generic rational labels require all four ports. Absolute radial Mellin evaluation identifies the reflected support pair and the conjugate character pair, erasing the plus/minus i sectors. The repair is explicit, not a fitted correction: retain both oriented half-lines. For a=r/q,

\[
\mathcal M_{\rm or}(P_a)=(\zeta(s,a),\zeta(s,1-a)).
\]

The character ports give the two conjugate periodic Dirichlet sections. Reflection swaps channels. The endpoint residue is retained as (1,1), not prematurely summed to 2. This is a directly relevant precedent for an analytical loss caused by suppressing polarity inside a four-phase orbit.

## 6. Full response includes cycle coordinates

Source: `research/voevodsky/completed-history-plus-cycle-observation-gives-an-algebraically-reversible-helical-presentation.md`.

On each fixed ratio block, the completed history observer has the cycle space as its kernel. A separately constructed cycle selector repairs it:

\[
\ker\widehat B_D\cap\ker\widehat Z_D=0.
\]

Hence (Bhat_D,Zhat_D) is injective and algebraically invertible onto its realized image. A scalar history output is not invertible. The topological inverse, cross-block bounds, seam preservation, and analytic phase rotation remain separate obligations.

The successor seam is particularly relevant to the operator's phrase 'first phase of the second connected full phase'. In `research/voevodsky/four-periodic-seam-upgrades-the-two-segal-baseline-to-a-twisted-successor-system.md`, the precise candidate is

\[
V_{4,k}\xrightarrow{R_k}V_{1,k+1},\qquad
S_k=R_kC_{14,k}.
\]

A full turn may be successor transport, not identity. The cited theorem is conditional on the supplied seam and its mixed coherence; it does not determine a numerical 4/5 coefficient. The phase label must retain the stage k as well as the within-stage index.

## 7. Other sectors test the lost channels directly

- `research/aspect/incidence-resolved-denominator-three-fourier-optics-control.md`: two sources have identical normalized scalar density and origin weight but different fractional-endpoint incidence. A second source probe detects the extra direction. Multiple scalar records of the common mode cannot replace that probe.
- `research/flavor/flavor-oriented-unitary-cycle-boundary-compression-constructor.md`: start from an oriented unitary four-cycle U and explicitly remove one return port. The open operator C=(I-P_0)U has C*C=I-P_3 and CC*=I-P_0. The defect P_0-P_3 is derived from the boundary operation; arbitrary normalization is not inserted afterward.
- `research/nima/the-Clark-codiagonal-preserves-colocation-so-the-chain-map-gate-reduces-to-the-four-port-source-pair.md`: a 2 by 4 projection can hide a nonzero four-port defect in its kernel. Test the unprojected defect and its projected image separately.

These are three distinct successful methods: active excitation of a lost coordinate, boundary compression with an exact defect identity, and comparison of full versus projected defects.

## Claim boundary and changed construction strategy

The earlier prefix-matrix experiments tested neither the full amplituhedron realization nor its two-polarity/four-presentation transport. Their numerical residuals cannot identify a phase, stage, or missing number of channels. In particular, -4/5 was determined by the chosen 1/5 diagonal.

The useful correction is architectural and executable: start with the existing labelled history packet, retain insertion/reflow and cycle ports, apply the actual chart-dependent products and dagger, and distinguish the fourth-phase seam from an identity closure. A component comparison must specify its projection and its source readout; a connected-stage comparison must also specify R_k.

For the determinant question, arbitrary flat frames F_m^-1 F_n force telescoping and erase any independent seam monodromy. Their coherence is therefore insufficient to test this fuller packet. The next source-based experiment should compare the full and projected response on the same labelled source and then track that difference through the fourth-to-first successor seam. No coefficient should be assigned until those maps are fixed.

The audited NNMHV packet verifies the history/cell bridge through n=7 and records further finite kernel analyses; it leaves the arbitrary-n cell compiler open. The separate correction `research/nima/correction-NNMHV-coherence-histories-and-RH-theta-histories-are-distinct-source-types.md` still requires an explicit bridge to the theta source. This audit enriches the constructor's available source operations; it does not declare that bridge or the full determinant comparison proved.
