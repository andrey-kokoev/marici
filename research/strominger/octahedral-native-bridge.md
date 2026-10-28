# Native bridge grown between the signed octahedral parents

## Question and explicit assumptions

Can native shared-face connectivity generate a middle complex, rather than importing the historical 34-cell belt?

The probe keeps the P/E-symmetric octahedral parent family but changes its placement to a common native lattice. It uses the declared E axis `v=(1,-1,-1,1)` and places parents of radius r at translations `+(r+1)v` and `−(r+1)v` about the neutral centre. These are the nearest integer translations along that axis with disjoint parents and a positive pole gap.

**Trial growth rule:** between the native N cells occupying the two facing E-labelled poles, retain **all shortest shared-face paths** through empty lattice cells. Other parent cells are blocked during the corridor search. Do not choose a particular path, use vertex-only links, impose the old belt shape, or target particle counts.

The axis labels, lattice registration/spacing, and shortest-path growth criterion are assumptions. This is a derived graph corridor under those assumptions, not a field-driven derivation of the signed construction.

## Result

For parent edge lengths 1, 3 and 5:

- shortest path length: **8 shared-face steps**;
- equally short paths: **576**, all retained;
- the union is **exactly the native edge-3 octahedral sector** (51 whole cells);
- its two polar N cells are already the two parent terminal cells;
- therefore it contributes **49 new cells: 16 P, 17 N, 16 E**;
- the new cells attach through **four complete native faces per parent**, eight total;
- each attachment has two P-oriented and two E-oriented triangles;
- no point-only links or duplicate terminal cells are required.

Growth-layer node counts, including the existing terminal cells:

| Distance from first terminal | P | N | E |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 |
| 1 | 2 | 0 | 2 |
| 2 | 0 | 4 | 0 |
| 3 | 6 | 0 | 6 |
| 4 | 0 | 9 | 0 |
| 5 | 6 | 0 | 6 |
| 6 | 0 | 4 | 0 |
| 7 | 2 | 0 | 2 |
| 8 | 0 | 1 | 0 |

P/E balance holds at every layer, not just in the total. The entire corridor is closed under native geometric P/E inversion.

At parent edge size 5, the full union contains **176 P, 187 N, 176 E = 539 cells**, with **1,224 shared-face links**. This is not a Pb-208 inventory.

## Shared terminal cells, not overlapping copies

The corridor and each parent share one **whole N cell**. They are represented once in the union. This is an explicit common-cell identification, not two independently rendered overlapping solids. Alternatively, ownership of those terminal N cells can be assigned to the middle octahedron while retaining the same union and connectivity. The latter convention would count a 51-cell middle and parents each lacking their one terminal N cell.

This also means the old viewer pose is not preserved: the new common-lattice placement moves the parents closer. The independently posed 34-cell belt remains available as its own reference process. The new **Octahedral pair — native grown bridge** dropdown process displays this common-lattice union separately.

## Viewer

Select **Octahedral pair — native grown bridge** (`native-octahedral-bridge`). Default parent edge size is 5; sizes 1 and 3 are also available. Geometry has the same thick white N-sector borders and native P/E face colours. Wiring has only shared-face links, with no point-contact edges.

The two shared terminal cells are drawn once. They remain visible whenever their parent **or** the bridge is visible. Hiding both parents therefore isolates the complete 51-cell middle octahedron; the table counts its 49 newly added cells separately to avoid double counting the terminals. Hidden parts expose their neighbouring cells' actual newly visible faces. The old belt process is unchanged.

## Verification

`tests/octahedral-native-bridge.test.mjs` checks:

- native lattice registration of both parents;
- all face-contact witnesses, unique terminal cells and connected full union;
- exact equality of the corridor with the independent edge-3 octahedral sector;
- P/E-balanced layers and attachment faces;
- closed boundary edge incidence and Euler characteristic 2;
- invariance under enlarging the ambient search sector by one shell.

Run:

```
node scripts/probe-octahedral-native-bridge.mjs
node --test tests/octahedral-native-bridge.test.mjs
```

The next unresolved gate is whether a signed-state evolution selects these paths and this registration without imposing the shortest-path criterion. The current result establishes a substantially more native geometric connection, not that dynamics.
