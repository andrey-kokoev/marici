# Retained spinor dual-line trial

**Scope: exact test against the existing electron spinor source, not an admitted P/E/N wiring.** This follows the prior-research audit, without assigning internal rays from physical cell-centre directions or adding spatial monopoles.

## Actual source reused

The checker imports the existing `check_spinor_potential_link_bridge.py` functions without invoking producer entrypoints. It reads the bridge's declared electron projectors, potential atlas and source contract. It checks the actual electron encoder and L/G/N intertwiners. Source stores are hashed before and after; only a new Strominger-owned receipt may be written.

The prior bridge reconstructs a nonzero spinor z from retained potential/norm/link data, with a separate phase witness on the dark line. We exercise both its stored-ray and mode-based decoders and its serialization round trip. Moving the host within the declared source host domain leaves the internal state unchanged. No host coordinates are identified with the Hopf base.

## The complementary pair is already determined by one spinor

For z=(z0,z1), set

```
Jz = (-conjugate(z1), conjugate(z0))
F(z) = [ z , Jz ].
```

Then, exactly,

```
F(z)^dagger F(z) = ||z||^2 I
 det F(z) = ||z||^2
F(g z) = F(z) diag(g, conjugate(g))      (|g|=1).
```

Thus the normalized frame is SU(2), and its two line transitions have opposite weights and determinant one. The complementary column adds no independent payload: it is computed from z. This is a retained coordinate-frame calculation, not a deterministic antiunitary quantum gate or preparation of a second particle. The first column recovers z. In particular `F(-z)=-F(z)`; the retained spinorial sign has not disappeared.

This is NOT a way to encode two independently supplied P and E states into one spinor. It is also not a derivation of a baryon doublet from a rank-one source. Identifying these two lines with the operator's paired records remains a separate gate.

The exact checker verifies covariance `F(Uz)=U F(z)` for all 24 source binary tetrahedral rotations. It retains norm explicitly, so normalization requires no unjustified extension of the exact arithmetic field.

## Cancellation does not erase actual source holonomy

Use the four **stored** rank-one source projectors P_i, with complementary projectors Q_i=I-P_i. For every triangular face, calculate independently

```
B = Tr(P_i P_j P_k)
C = Tr(Q_i Q_j Q_k).
```

The actual source gives `C=conjugate(B)` and normalized phase `b=+i` or `-i`. The paired holonomy is

```
H = diag(b, conjugate(b)).
```

It has determinant one but is **not the identity**: its trace is zero. Replacing it by identity loses the source loop information. Giving both channels the same phase instead fails the determinant-one test.

For the continuous complementary line bundles, the standard identity `c1(L direct-sum L*)=0` expresses determinant cancellation. These finite source checks verify the corresponding paired transitions and actual triangular loop operations; they are not a new continuum Chern-class computation or proof of arbitrary non-Abelian coherence.

## Retention and negative controls

- Deleting the dark phase witness is rejected by the source decoder.
- Multiplying a dark state by i keeps its potential and zero link but changes its retained phase witness.
- A zero spinor is rejected rather than assigned a fictitious ray.
- Central minus one changes the retained frame even though it fixes its ray.
- Trivializing paired holonomy to identity fails the actual source-loop comparison.
- A determinant-one pair is not treated as an independently available neutral-output contraction.

## What this changes, and what it does not

There is now an exact **source-level** realization of the dual-line proposal using one already retained logical electron spinor. It does not need the 44 spatial monopoles from the earlier reference trial. That trial remains valid under its own extra assumptions; this is a different internal-state construction, not a gauge transformation of its flux.

The missing adapter is precise: map the operator's actual signed-pair records and N adjacent-face operands into this retained source frame, and intertwine their actual comparison maps with its SU(2) action. If those records are independent inputs, or their operators are not such intertwiners, the present frame cannot substitute for them. No four-port or 80-fibre identification is inferred from counts.

Consequently there is still no proved global native boundary law, routing, or filling of the vertex-star diagrams by this construction. No renderer or existing source artifact is changed.

## Replay

```sh
python research/strominger/checkers/check_retained_spinor_dual_line_trial.py --record
```

Receipt: `research/strominger/results/retained-spinor-dual-line-trial-v1/verification.json`.

The checker uses exact arithmetic in Q(sqrt(3),i), retaining actual Bargmann invariants, source hashes, and explicit `constructionAdmitted: false` / `nativePENBindingAdmitted: false` flags.
