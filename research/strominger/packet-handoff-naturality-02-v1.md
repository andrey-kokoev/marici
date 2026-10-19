# Packet handoff ground naturality — iteration 2/10

Owner: `marici.Strominger`. **Iteration complete; objective in progress.**

[Live conjecture net](contracts/packet-handoff-naturality-conjecture-net.v1.json) · [iteration contract](contracts/packet-handoff-naturality-02.v1.json) · [exact checker](checkers/check_packet_handoff_naturality_02.py) · [receipt](results/packet-handoff-naturality-02-v1.json).

## Ground-level construction: actual ports, not another tag automaton

I tested a source-neutral role convention: **M is the smaller full stage-image channel space; C is the larger**. Both spaces retain their induced metric. This is not an identification with physical main space/codimension, not a division of the active payload into two sectors, and not a claim of uniqueness. Equal-capacity pairs are outside this convention.

| Actual source | L image | G image | Active return | M | C |
|---|---:|---:|---:|---|---|
| Proton | 12 | 3 | 1 | 3 alignment channels | 12 local mode lines |
| Neutron | 3 | 12 | 1 | 3 intrinsic sectors | 12 alignment channels |
| Electron | 4 | 2 | 2 | full logical doublet | 4 native face lines |

These are **native channel dimensions**, not the old 12-chart electron sector dictionary. Primitive support components, with their internal ranks, are reconstructed: proton L has twelve rank-one triples and G three rank-one twelves; neutron reverses those dimensions; electron L has four rank-one spin pairs but G has **one connected eight-slot block of rank two**. Two coherent logical dimensions are not two disconnected geometric ports.

Native geometry is retained. Ports are transported with source/frame isomorphisms; arbitrarily mixing coordinates and counting the new nonzeros does not redefine physical ports.

## 1. The baryons really have opposite tensor preparations

For proton, use the **actual twelve geometric transport rotations**, not an invented chart change. In their body frames:

    raw = C^12 tensor M^3
    L = I_C tensor P_M
    G = P_C tensor I_M
    N = P_C tensor P_M.

Both P's are rank-one metric projections. The three alignment families are transported body axes, not three fixed global x/y/z labels.

For neutron, the actual intrinsic sector/plane embedding and repeated metric give:

    raw = M^3 tensor C^12
    L = I_M tensor P_C
    G = P_M tensor I_C
    N = P_M tensor P_C.

Thus the baryon difference is not merely relabelling a scalar return: their **local constraint prepares opposite tensor factors**. This does not identify their full geometric sources; their source operation groups still differ.

Electron cannot have this complementary-factor preparation, even after a frame change. Such a pair must satisfy

    rank(L) rank(G) = dim(raw) rank(N).

Baryons give 36=36. Electron gives **8 != 16**. Its nesting is structurally different, not a tensor-factor swap.

## 2. One exact metric partial-isometry interface

Let K_X,D_X encode/decode the full stage-image space X, with K_X D_X its source projector and D_X K_X=I. The native cross maps give

    B: M -> C
    R: C -> M = metric-adjoint(B)
    R B = Q_M
    B R = Q_C
    B R B = B,  R B R = R.

Q_M and Q_C are the same active return represented in their respective channel spaces. Full projected raw-reader squares are checked, not only one selected state.

* Baryons: Q_M has rank1 in dimension3; Q_C has rank1 in dimension12. Transport is a partial isometry, not a reversible map on the full ambient channels.
* Electron: **Q_M=I_2**. B is a lossless encoding of the whole logical doublet into a rank-two code inside four face channels.

Both source-bound proton generators, the neutron generator and **all 24 native electron spin/face operations** intertwine these maps. A nonmonomial raw-frame shear, with transported metric and primitive ports, preserves the construction.

## 3. Electron C is a concrete tetrahedral face code

The actual stack of four native face projectors K, and its native decoder D=K*/2, factor through the four local face lines. The four logical face effects are

    E_f = D (raw face-slot projector f) K = P_f/2.

They obey

    sum E_f = I,
    tr E_f = 1/2,
    tr(E_f^2) = 1/4,
    tr(E_f E_g) = 1/12  for f != g.

Their matrix span has dimension **4**, and they do not commute. This is the native tetrahedral informationally complete qubit measurement frame, retained coherently by B. It is not a classical choice between two M/C payload labels or an imported twelve-sector chart.

## 4. The proposed three words have conditional native realizations—but entry matters

The native L,G,N phase ledger has a raw N output. To compare its endpoint with the next local interface, I **explicitly apply the lossless L-image readout adapter D_L N**. This is an endpoint representation, not a claim that N's primitive raw target has become a local arrow target.

Under that declared adapter:

| Source | Phase window | Role word |
|---|---|---|
| Proton | L,G,N | C,M,C |
| Neutron | L,G,N | M,C,M |
| Electron | G,N,L(next copy) | M,C,C |

The desired paths are therefore **source-bound typed realizations without an extra handoff bit**. But the electron window starts one phase later. Under this role convention proton and electron share the same complete role cycle L:G:N = **C:M:C**. Proton also admits the M:C:C window; electron also admits C:M:C. A cyclic window alone is not a species law.

There is a second exact ambiguity for electron. From the same complete M input, encode then persist at C, or encode then decode back to M:

    M -> C -> C     versus     M -> C -> M.

With the explicit B adapter between terminal M and the encoded C **code**, both yield the same projected raw state and every raw endpoint reader, with the native action squares preserved. They differ in public format/phase/history, not their payload endpoint.

This does **not** identify full C preparation with M. A nonzero witness in I_C-Q_C has zero decoded M and zero return, but a nonzero retained C/raw reader. Electron has two such defect dimensions; each baryon C has eleven. Any full-preparation equivalence that discards these readers is false.

## 5. What remains to ground

The mathematical common interface is constructed. The physical meaning of M/C and a **source-selected entry/continuation rule** are not.

Iteration3 is executable from existing sources: `cycle-origin-and-primitive-history`. Inspect the actual primitive arrow endpoint/phase constructors and retained histories—not only their coefficient matrices. Does the source canonically pick L entry for baryons and G entry for electron, with the declared N-to-local readout? Is electron persistence a licensed primitive continuation rather than a freely chosen export format? Or is the claimed third recurrence a cyclic-window/adapter choice?

This is sharper than adding more fitted predicates: it targets the exact additional structure the candidate diagrams need.

## Verification and limits

**21 exact check groups pass**, followed by a passing frozen challenge at

`research/strominger/scc-freezes/packet-handoff-naturality-02-v1.65f0e11236e323e4.json`.

The contract was declared before the first check; a syntax error in the new checker was corrected before its successful scientific execution. The freeze precedes the subsequent challenge, not the exploratory run. The challenge is a replay of the frozen checker, not an independent peer proof.

```text
python research/aspect/scc/scc.py check packet-handoff-naturality-02-v1
python research/aspect/scc/scc.py check packet-handoff-naturality-net-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

No native producer, proof-assistant recompilation, other-owner/shared-fixture edit, commit, push, deployment or physical particle/clock identification is claimed.
