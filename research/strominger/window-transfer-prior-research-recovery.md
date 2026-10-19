# Recovered window transfer: electron attachment is not a centerline choice

Searched the October 15–16, 2026 research and its retained implementation.
The previous claim that no window-transfer rule had been specified overlooked
these sources. No viewer geometry is changed by this recovery audit.

## Sources, in order of correction

1. `cmc-mcm-marked-tetrahedron.md` (October 15): full marked occurrence order,
   shared global identities, and an archived history are required. C/M type
   labels or an opposite vertex alone do not retain the directed window.
2. `cmc-mcm-identity-attachment.md` (October 15 local time; receipt recorded
   `2026-10-16T02:52:29Z`): original walk
   `C0 → M0 → C1 → M1 → C1 → C2`; overlap-fixing transport and the N/E reversal.
3. `cmc-mcm-carrier-binding-v2.md` (October 16): corrected volumetric carriers
   `P = C0 M0 C1 [M1]`, `N = M0 C1 M1 [C2]`. This supersedes the earlier
   common-tetrahedron P/N labeling; N's fourth vertex is C2, not C0.
4. `electron-M2-carrier-trial-v1.md` (October 16):
   `E = M1 C1 C2 [M2]`, attached on the N face opposite M0.
5. `vacuum-space-lattice-cells-v7.md` (October 16): preserves this same
   four-vertex incidence in a three-tetrahedron prism on actual lattice nodes.
   It supersedes the detached similarity overlay, not the ordered windows.

## Definitive attachment at the marked-carrier scope

| Carrier | Ordered window | Fourth/context vertex |
|---|---|---|
| P | C0 → M0 → C1 | M1 |
| N | M0 → C1 → M1 | C2 |
| E | M1 → C1 → C2 | M2 |

P/N share **M0,C1,M1**. N/E share **M1,C1,C2**, the face opposite **M0**.
Their attachment faces retain the **C1,M1 edge**. The electron traverses that
edge in the reverse direction: N has C1→M1; E starts M1→C1. It is not a plain
sliding triple. With these ordered global marks retained, the outgoing N face
is fixed; no centerline, nearest-cell, or coordinate-order selector is needed.

The declared full-state frame comparisons swap C0/M1 for P→N, then M0/C2 for
N→E, fixing shared and uninvolved identities. The checked spectral adapter gives
`P+ → ω N+` and `N+ → ω² E−`. N/E intertwines the inverse target cycle, not the
same forward cycle. A pointer consisting only of `{id:'id'}` plus a chart bit
omits this window, occurrence-history, and branch information.

`carrier.mjs` still exports these exact windows and `electronFace`.
The historical spectral receipt has 53 true checks; all eight pinned source
hashes still match in the fresh recovery audit. Its frame rule and closing seams
remain declared adapters, not independently derived physical dynamics.

## Current implementation mismatch, measured

Fresh checker: `node research/strominger/checkers/check_window_attachment_recovery.mjs`.
Evidence: `results/window-attachment-recovery/verification.json`.

For each current Pb chain, compare its P/N and N/E attachment triangles:

- Required by the recovered incidence: exactly two common vertices, C1 and M1.
- Current layout: 17 chains share no vertex; 65 share only one.
- **0 of 82 chains satisfies even this necessary retained-edge condition.**

Thus the current outward/centerline heuristics do not implement the recovered
window protocol. Successful volume, non-overlap, counts and face-adjacency tests
must not be interpreted as window-transfer verification.

## Implementation consequence

Use the ordered window, fourth context mark, global vertex bindings, retained
history and frame/branch transport as construction state. Select an electron
attachment by matching the transported **ordered M1,C1,C2 interface**, preserving
its C1/M1 edge and adding a distinct M2 on the other side. Reject incompatible
lattice embeddings instead of choosing another arbitrary adjacent face.

The recovered rule fixes the interface in a marked carrier. It does not by
itself provide those markings on the current octahedral/composite neutron gap
volumes. The earlier reflected regular-tetrahedron trial must not be imported
as a space-filling integer-lattice construction. That lattice binding is the
remaining implementation task, rather than another search for an unmarked
outgoing-face rule.
