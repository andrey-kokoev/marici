# Helium-4: retained-core probe with unselected reader alternatives

Target: **2 P, 2 N, 2 e**. This probe specifically tests adding a neutron while
preserving the complete [helium-3 trial](helium3-shared-neutron-trial-v1.md).
It does not assume that every possible helium-4 construction must preserve that
layout. A fresh construction with different electron ports is not ruled out.

The separate [three-turn viewer trial](helium4-window-trial-v1.md) now explicitly
selects the retained-active-face/reference-context hypothesis. This unselected
probe still records all four alternatives; the new convention is not a physical
derivation and does not turn N2's ordinary NE continuations into old exits.

## A unique geometric addition

Each retained proton has one unused MCM face. Reading either of these as a P→N
interface gives the same positive lattice primitive: **cell 7**. Its four
vertices are the already bound `M0, M1, C0, C3`. No new point or displaced vertex
is needed. All existing five carriers remain unchanged; the six carrier IDs are
`0, 13, 16, 24, 14, 7`.

The four nuclear cells share the M0–M1 edge. Their four internal faces close a
nuclear ring, with eight external triangular faces forming a convex, six-vertex
core. The base-lattice positivity/non-overlap checks cover all six carriers.
This supplies the isotope census and geometry, not physical stability.

## The new reader comparison is not selected by geometry

For a retained proton window `Ca Mx Cb [My]`, both of these frames reach its
unused MCM face:

```
Cb Mx Ca [My]     reverse the C order on the current active face
Cb My Ca [Mx]     reverse the C order and use the other middle M
```

There are therefore four combinations for the two protons. No reader frame is
assigned to the new neutron in the candidate: its four possible marked readers
are recorded explicitly.

As a **conditional reference experiment**, compare the proton frames by fixing
the shared C identities, exchanging M identities only when necessary, and
matching the outside context slot. In local five-slot order
`C0,M0,C1,M1,C2`, this comparison is Q = (0 2). The context identification is a
new hypothesis; the original P→N→E protocol does not establish it.

Traverse:

```
P1 → N1 (change N reader) → P2
   → alternate P2 reader → N2 (change N reader)
   → alternate P1 reader → P1
```

The native PN steps use their actual forward/inverse reference operators.
Shared-N comparisons fix the common M identities and exchange the C identities.
The resulting whole-carrier permutations are:

| Other-middle-M choice at P1 / P2 | Output slot order | Operator order |
| --- | --- | --- |
| no / no | 1, 2, 0, 3, 4 | 3 |
| no / yes | 1, 0, 2, 3, 4 | 2 |
| yes / no | 1, 0, 2, 3, 4 | 2 |
| yes / yes | 1, 2, 0, 3, 4 | 3 |

Every inverse loop restores all five coefficients. No listed operator is the
identity after one turn. The common character hides the distinction, while
positive/negative characters detect it. For the order-three cases the active
triple acquires an omega factor, but the two complement coefficients do not:
with nonzero complement this is **not** a global scalar on the full packet.

Nontrivial holonomy is not inherently inconsistent with a fibration. It means
that the return is a different full reader state; an appropriate phase/branch
cover could retain it. Neither selecting a proton-reader rule nor identifying
these return states is justified by a successful geometric count or inverse
round trip alone. The probe therefore records the alternatives instead of
silently requiring flatness, discarding the complement, or choosing a frame.

## Remaining construction gate

The new neutron's ordinary NE continuations reach cells **6 or 8**, neither
of the retained electrons (16 and 14). Completing those packets would add
electrons. Reaching the old exits instead needs an admitted reader/transport
extension; no ordinary E→P step is invented here.

The **legacy layout** menu entry remains separate and is not evidence of
window compatibility. The new **3-turn reference trial** uses the explicit
conditional extension documented above; it does not establish its uniqueness
as a physical rule.

## Reproduction

- Model: `demos/particle-overlap-tetrahedron/helium4-core-probe.mjs`
- Check: `node research/strominger/checkers/check_helium4_core.mjs`
- Candidate: `results/helium4-core/candidate.json`
- Evidence: `results/helium4-core/verification.json`

The checker exercises four frame combinations, all nine character/phase inputs,
nonzero complement coefficients, basis-vector inverse tests, retained geometry,
convex nuclear closure and unavailable forward electron exits. Passing means the diagnostic findings are verified,
**not** that a physical helium-4 transport law has been established. The
separate viewer checker verifies only its explicitly declared reference rule.
