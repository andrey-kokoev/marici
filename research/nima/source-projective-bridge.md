# The source has a projective invariant, but the interval record does not determine it

## Result

The source-origin audit in `source-projective-bridge-protocol.md` completed with three scoped conclusions:

- **Constructed:** four source-defined points on the actual twistor line (56) reproduce the transported history6 boundary coefficient as a projective cross-ratio.
- **Rejected:** that coefficient factors through the undecorated interval/compiler record alone. Three admitted kinematic inputs with the same record give distinct values.
- **Rejected:** every actual selected-prefix transport acts as an invertible projective symmetry. Nine of eighteen tested selected-prefix matrices have rank one and collapse the four-point packet.

This supplies a specific projective object in the enriched source, not the desired real endpoint PSL(2,R) action or AdS/dS geometry. The applicable SCC obligations are source-to-line forward realization and readout descent; descent to the bare record fails.

## Four source-defined points, not four fitted endpoints

Let A=Z5, B=Z6. Restrict the plane covectors

    phi(V)=<V812>, psi(V)=<V123>

to the line spanned by A,B. The actual incidence constructors give

    W=phi(B) A-phi(A) B = (56) intersect (812),
    Q=psi(B) A-psi(A) B = (56) intersect (123).

In the line basis (A,B), their coordinates are A=(1,0), B=(0,1), W=(phi(B),-phi(A)), Q=(psi(B),-psi(A)). For the determinant bracket [P,Q] in this two-dimensional line, define

    chi(A,B,W,Q)=[A,B][W,Q]/([A,W][B,Q]).

Then, wherever the original source and denominator are defined,

    chi = 1-phi(B)psi(A)/(phi(A)psi(B))
        = 1-<6812><5123>/(<5812><6123>)
        = c6.

Benincasa's existing symbolic incidence proof identifies the last expression with the actual transported endpoint ratio A0*St/(At*S0). That function was freshly called without executing its artifact-writing main routine. The three frozen fixtures also pass the original generalized-R localization guards. Projecting line (56) to its two spinor components is invertible in these fixtures, and gives the same four-point determinant ratio.

Every common invertible line-frame change multiplies each determinant by the same determinant factor, which cancels; rescaling individual point representatives also cancels. A common four-dimensional projective frame has balanced four-bracket weights. These are identities, backed by fresh exact frame/representative checks, not a fit of four endpoint coordinates to the desired result.

## Why the bare interval record is insufficient for this observable

The actual selected record is history index 6 at n=8:

    outer_pair=(2,6), inner_pair=(3,6), inner_prefix=(6,2),
    boundary_updates=(upper replacement (2,6)).

It maps to interval [2,2]. Across the existing kinematic fixtures, the same full combinatorial record gives

| Fixture shift | c6 |
|---|---|
| 0 | 20088/137611 |
| 1 | 28561/186493 |
| 2 | 7812/49555 |

Thus no function of that record alone equals c6 on these admitted inputs. Formally, if q forgets kinematics and retains the compiler record, there is no f with c6=f composed with q on this fixture family. This does not refute every possible intrinsic invariant of the record, nor a projective realization of a richer source.

Ledger 4328 recovers **compiler records**, not the external twistor/spinor coefficients. Its faithful finite process encoding is unchanged. To preserve this additional observable, an extension must retain more source data rather than reconstruct it from the interval label.

The [2,2] record is a diagonal algebraic boundary object. It is excluded from the metric chart u<v. The four points A,B,W,Q live on a separate source-defined twistor line; they are **not four distinct endpoints of the m=3 interval chart**. This discovery does not remove the four-endpoint requirement for testing real interval cross-ratios.

## Actual transports expose the group/correspondence distinction

For all six selected n=8 histories in each of the three fixtures, the checker constructs the existing prefix matrix from alternating x-interval matrices and adjugates. These act on row spinor covectors. Test their action on the four projected line representatives; do not assert this is already the full native evolution law of the twistor packet.

- Nine matrices have rank two and preserve chi exactly.
- Nine have rank one. Every pair determinant of the output representatives vanishes; some representatives may additionally vanish. The cross-ratio API rejects these outputs as undefined, rather than assigning a canceled value to 0/0.

An invertible matrix multiplies both numerator and denominator by det(M)^2; that argument does not extend to det(M)=0. A rank-one image cannot recover the input cross-ratio without retained input or other auxiliary data.

These are actual source matrices in the frozen fixtures, but this test is a candidate common row-action comparison, not an assertion that the source evolves every point in (A,B,W,Q) by the same matrix. It rules out treating the entire tested prefix family as a group of projective automorphisms. It does not rule out a rank-stratified correspondence category, or an independently justified invertible lift.

## Consequence for the geometric premise

The earlier phrase 'projective structure is merely supplied' needs refinement: **a nontrivial projective coefficient is already derived from enriched source incidence**. What is not derived is its identification with the real ordered endpoint projective structure used by the interval metric theorem.

A successful bridge must now specify:

1. the retained kinematic/line packet beyond the interval record;
2. a real ordered endpoint comparison on a valid nonsingular domain, including how boundary records are treated;
3. transport compatible with the rank-one cases, or an explicit retained-data lift—not silent restriction to group elements;
4. how that comparison sources the smooth projective chart used in the metric classification.

This is a more concrete obstruction than a generic request for geometry. The conditional dual-shadow transport audit remains valid at its declared source level, but cannot alone discharge these enriched-source obligations. No coefficient-to-curvature or continuum theorem follows from this audit.

## Reproduction

    python research/nima/checkers/check_source_projective_bridge.py

Receipt: `results/source-projective-bridge.json`. Fresh exact execution passes the symbolic source identity, three four-point constructions, frame/representative comparisons, source localization and eighteen rank-stratified action tests. Source files are hash-checked before and after execution; Benincasa's main routines and output artifacts were not run or rewritten.

Sources: `research/benincasa/history6-twistor-cross-ratio-2026-10-13.md`, its checker and projection/incidence dependencies; `research/nima/nnmhv_coherence_paths.py`; `research/nima/dual_spinor_kinematics.py`; `research/nima/momentum_twistor_constructors.py`. All numerical fixtures are model data, not observations; hardware is excluded.
