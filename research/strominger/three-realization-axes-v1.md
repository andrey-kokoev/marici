# Three signed realization axes; face navigation retired

## Question

Operator instruction: drop the face-crossing interpretation and implement realization axes. The current space page must show three discrete realization directions, retaining signed M/C axes, the 60-degree frame increment and node-bound carrier selectors.

## Construction and boundary

The active space has integer address (r1,r2,r3), with three equivalent unit generators:

    b1 = (1,0,0)
    b2 = (1/2,sqrt(3)/2,0)
    b3 = (1/2,sqrt(3)/6,sqrt(2/3)).

Their pairwise inner products are 1/2 and their determinant is 1/sqrt(2). This is an explicit face-centered-cubic lattice layout, chosen to give three equivalent noncoplanar generators and a unit regular tetrahedral seed. Its metric is a declared candidate input, not a physically derived realization law. No axis is designated vertical R.

The differences b2-b3, b3-b1, b1-b2 are unit, coplanar and mutually 120 degrees apart. They carry the two M / one C signed axes or the reference XOR alternative. The local frame rotates by 60(r1+r2+r3) degrees around its derived normal and exchanges M/C on odd grade. A signed step on any R axis changes its own integer coordinate, the frame angle by signed 60 degrees, and the role parity. The grade is derived from the three coordinates, not an additional realization axis.

Carrier cells use only lattice addresses. Relative to the selected address, their bindings are C0=(0,0,0), M0=(1,0,0), C1=(0,1,0), M1=(0,0,1), C2=(1,1,0), M2=(0,1,1). P/N/E incidence labels and five selectors remain; each point is a reference to the actual node table. The unit proton seed is regular; a physical particle/type operator law is not inferred.

## Disposition

`vacuum.html` is now the three-axis view at the existing URL. All face menus and controls are removed. The obsolete `face-space.html` redirects to this view. The face prototype SCC manifest is archived with a `.retired` extension; its earlier geometric overlap result remains historical, not an active UI. The former planar version is retained only at `planes.html`.

New sources: `realization-model.mjs`, `realization-app.js`, `realization.css`, and the rewritten `vacuum.html`, all under the owned experiment directory. The publisher mirrors them to both public roots and preserves the previous planar snapshot once.

Fresh checks cover three independent equivalent generators, unit lattice edges, coplanar signed typed directions, signed 60-degree steps on every R axis, all six realization labels visible on desktop/mobile, exact rendered carrier-node bindings, five selection modes and removal/redirect of face navigation. Results and visually inspected screenshots are in `research/strominger/results/three-realization-axes/`.

No physical time, global carrier dynamics or mass/energy law is asserted. Changes remain uncommitted and not deployed.
