# Shared geometric seed: framed quadrilateral, full retained carrier required

Definition: `research/conjecture_net/contracts/shared-quadrilateral-geometric-seed.v1.json`.
Checker: `research/voevodsky/checkers/check_shared_quadrilateral_geometric_seed.py`.
Receipt: `research/voevodsky/results/shared-quadrilateral-geometric-seed-v1.json`.
Run: `uv run research/voevodsky/checkers/check_shared_quadrilateral_geometric_seed.py`.

## Constructor, not a dimension match

Supply a quadrilateral vertex frame with boundary order (A,D,B,C). This agrees with the existing twelve-arrow vertex permutation A->D->B->C->A; it is a declared compatible frame, not a claim that every external vertex convention agrees automatically. Its two diagonals are {A,B} and {C,D}. Each singleton diagonal is a genuine triangulation. Supply a mark j in this diagonal set and positive rational additive mesh h.

For either triangulation T the shared geometric constructor outputs:

- its canonical channel incidence vector v_T in Z^2 and atom delta_(v_T);
- a twelve-arrow state x_T, assigning weight 1/2 to each orientation of its diagonal, all other arrows zero;
- immutable vertex frame, triangulation, mark and lineage records.

The symmetric oriented-pair rule requires no diagonal orientation choice. It is an explicitly chosen geometric encoding into the existing carrier, not an assertion that the original Hamiltonian selected this preparation.

## Native geometric square and decoder

Let rho be the supplied polygon quarter rotation. It swaps the two diagonals. The actual C12 permutes both endpoints of each directed arrow, so

    x_(rho T)=C12 x_T.

The checker tests all four powers on both seeds, including mark/packet relabelling. Channel rotation is the corresponding permutation of incidence coordinates. This establishes a geometric rotation square on this seed image without replacing the native C12.

Decode a full carrier state by taking each diagonal's two oriented coefficients and adding them. Require that the result is a unit triangulation incidence vector and that re-encoding reproduces the input carrier state exactly. States outside this two-seed image are rejected rather than assigned invented geometry.

## Why the retained archive is essential

Both diagonal seeds lie outside the four selected boundary arrows in the existing reader K=JP. Each therefore has the SAME coarse readout: the cyclic vector (1/14,1/14,1/14,1/14). Their hidden components Nx differ. Given both Kx and Nx, reconstruct x=S Kx+Nx with S=E J^-1 and apply the validated seed decoder. This supplies actual executable geometric seed access from the full retained carrier at this scope. Kx alone cannot distinguish the two triangulations.

The decoded finite channel packet can now execute the queries and updates of `retained-history-source-access.v1`. The checker imports that implementation, evaluates a nonuniform Gaussian query on each decoded seed, transports its mark under rotation and preserves original geometric provenance under heat.

## Subsequent operations and boundaries

Once the seed is decoded, licensed channel packet shifts, modulation, heat, convolution, bonding and relabelling use the full packet and contribution lineage contract. Keep the original x_T and geometric seed immutable as provenance. Do not assert that those updates are native twelve-arrow controls or that every transformed packet is another triangulation.

The native geometric square is NOT a channel Fourier square. C12 has two established interpretations under different maps: polygon rotation on these geometric seeds and Fourier on the earlier analytic comb attachment K. The channel Fourier of an incidence atom is a character distribution, not the rotated incidence atom. Identifying these distinct operations would be precisely the silent native-tick replacement prohibited by the source-map gate.

Thus this result fills the bounded shared geometric SEED gap, including full retained-state decoding and packet-query access. It does not fill the full operation binding, general n-gon constructor, physical preparation, or parent source-map verdict. A general polygon has more diagonal data than this fixed twelve-arrow encoding supplies; additional geometric archives must be specified rather than inferred from the coarse reader.

Next gate: freeze the two-operation dictionary (geometric rotation versus analytic Fourier) on a declared retained-history extension, and review which added channel operations are accepted for the intended source task. Keep `rh:channel-carrier-source-map` open until that scope review is complete.
