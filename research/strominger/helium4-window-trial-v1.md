# Helium-4: retained-face reference algebra (phase admission withheld)

**Historical model, not the current viewer:** the older reader windows fail
necessary phase checks; three-turn coefficient closure did not establish phase
discipline. The corrected viewer uses
[phase-first assemblies v2](phase-first-assembly-v2.md), retaining absolute origins,
full histories, and all three face modes. The transport controls described below
remain removed. Only **Previous item / Next item** remain for assembly display.

This is a **conditional reader model**, not a derivation of a helium nucleus or
its stability. The viewer explicitly selects
`retain-active-face/reference-context-hypothesis`. The geometry-only probe
continues to retain the other reader choices; those alternatives have not been
refuted by this implementation.

## Construction

Select **Helium-4 · 3-turn reference trial** in `vacuum.html`, then use **Next
element** five times. The ordered carrier cells are **0, 13, 16, 24, 14, 7**:
P1, N1, E1, P2, E2, N2. Every click commits one new carrier. The first five
carriers and their bindings are the retained He-3 construction. Adding N2 uses
an unused proton MCM face and adds **no new geometric vertices**. The result
has 2P/2N/2e, with a convex four-carrier nuclear core; no tubes are created.

The last commit reads back through existing E2/N1/P2, compares P2 with its
reversed-C reader, and performs PN to construct N2. It does not construct a
second copy of N1 or either electron. Geometry, construction history, and the
particle identity remain unchanged during subsequent reader motion.

## Explicit additional rule

At each proton, retain the set of its three active face vertices and reverse
the two C positions. Of the two probe readers at that proton, this selects
`exchangeMiddleM = false`. In native coordinates
`[C0,M0,C1,M1,C2]`, the comparison exchanges slots 0 and 2 and retains the other
three coefficients. The outside C2 context is identified with the other
packet's context **by hypothesis**, not by coincident geometric identity.
The shared-neutron comparisons use the same conditional full-context rule as
He-3. Neither comparison discards the fifth coefficient.

The forward nuclear reader circuit is:

| Carrier | Active ordered window |
| --- | --- |
| P1 | C0 M0 C1 |
| N1, first reader | M0 C1 M1 |
| N1, second reader | M1 C2 M0 |
| P2, original reader | C3 M1 C2 |
| P2, reversed-C reader | C2 M1 C3 |
| N2, P2-side reader | M1 C3 M0 |
| N2, P1-side reader | M0 C0 M1 |
| P1, reversed-C reader | C1 M0 C0 |

The next step returns to P1's first reader. The eight transitions are PN,
shared-N comparison, inverse PN, proton comparison, PN, shared-N comparison,
inverse PN, and proton comparison. These are reader operations; only the last
PN of the construction commits new geometry.

At the first P1 reader, one circuit acts on the **whole** native carrier as

```
(a,b,c,d,e) → (b,c,a,d,e).
```

Its operator order is three. Positive/negative characters advance their phase
by +1/−1 modulo three; the common character is fixed. With nonzero complementary
coefficients this is not an overall scalar phase of the five-slot packet.
The implementation transports actual coefficients at every step: no cached
endpoint restoration or phase reset closes the circuit.

## Clock sheets and retained exits

**Next window / Previous window** traverse individual reader transitions.
**Next turn / Previous turn** apply an entire eight-transition nuclear circuit,
retaining the current local reader and showing the circuit count modulo three.
The chronological passage log is retained separately from the reader state.

At either N1 reader, **Read electron** performs its original NE transition to
E1 or E2, respectively. These are terminal forward states; only the inverse NE
operation returns from an electron. There is no invented ordinary E→P edge.
N2's ordinary NE continuations still reach cells **6/8**, not the retained
16/14 exits. The declared nuclear circuit instead returns through an existing
proton and N1 before taking an existing electron branch.

There are eight nuclear reader charts and two electron charts. For either
non-common character, the phase-resolved graph contains **30** distinct reader
states; the common sector has **10** (its packet is fixed after one circuit).
Charts carry ordered windows, reference aliases, all five coefficients, the
retained construction history, global bindings, and the particle identity.
They are not merged merely because they read the same geometric cell.
All admitted states are reachable from the entry and can reach a retained
terminal electron. This is **6/6 local carrier coverage**, only **6/343** of the
ambient primitive space, and conditional on the declared comparisons.

## Verification

- `node research/strominger/checkers/check_helium4_window.mjs`: nine character/
  phase cases with nonzero complementary coefficients; 24 requested seed
  markings × three characters (8 markings admitted, 16 rejected by the fixed
  subdivision); inverse steps, both exits, one/three-turn distinctions,
  full-state coverage, immutable geometry/bindings/history, and identity.
- `node research/strominger/checkers/check_fiber_space.mjs`: integrated model,
  desktop and mobile viewer checks, including all 30 default reader states,
  both terminal branches, reused carrier meshes, and absence of tubes.
- Receipts: `results/helium4-window/verification.json` and
  `results/fiber-space/verification.json`; screenshots in the latter directory.

Verification correction from the [Li-6 growth audit](lithium6-growth-probe-v1.md):
the earlier marking sweep passed `bindings` through He-4, but He-3 ignored that
option and repeatedly used the default seed marking. The constructor now
forwards it, and the check asserts the actual initial bindings. The former
claim of successful construction under all 24 markings was not supported.

See [the geometry-only probe](helium4-core-probe-v1.md) for the unresolved
alternative framings. The new trial admits one explicitly labelled reference
rule; it does not establish that nature selects that rule.
