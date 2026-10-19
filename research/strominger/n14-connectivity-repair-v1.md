# N-14 from N-15: targeted connectivity repair

## What was tested

Start from the two saved N-15-minus-one-neutron candidates that retain local
contact witnesses and exit reachability but fail rooted construction. The
removed neutron cells are 8 and 12 in the original saved witness; these IDs
are local to that source, not universal lattice names.

For each candidate, consider every generated reader on its retained body sites,
not only the original saved reader records. Check rooted reachability in the
complete uniform-subdivision universes at origins 4 and 10 and the complete
mixed-subdivision universe at origin 8. Then test relocating exactly one of its
seven remaining neutrons to each available neutron site, keeping every P/E
site and all other neutron sites fixed.

These are deliberately optimistic necessary-condition checks. Pairwise role
compatibility, incidental contacts and exit conditions are not imposed; the
mixed graph even allows mutually inconsistent diagonal choices across edges
and all three root charts. Every valid construction in this restricted family
would still appear in this larger graph. Thus failure excludes a valid witness
in the stated family/bound, but a graph success would require the full solver
and replay. No relaxed graph is admitted as a physical or viewer model.

## Findings

**Additional readers do not repair either fixed arrangement.** At uniform
origin 10 and mixed origin 8, the same bodies remain unreachable:

| Deleted neutron | Unreachable original body cells |
|---|---|
| 8 | proton 9, neutron 16, electron 30 |
| 12 | protons 13 and 14, neutron 17, electrons 34 and 42 |

The saved operation trace explains the immediate obstruction:

- Neutron 8 receives an NN advance from neutron 3 and supplies inverse-PN
  entry into proton 9. Its deletion cuts that rooted route.
- Neutron 12 receives NN advances from neutron 1 (and neutron 8), and supplies
  inverse-PN entry into protons 13 and 14 using different reader origins.

These cuts concern directed native construction operations, not merely
undirected physical contact. They explain why an exit-certified residual
configuration can nevertheless be inadmissible from the fixed root.

**Moving one remaining neutron also fails the optimistic connectivity test.**
Per candidate, tested relocation counts were:

| Geometry/universe | Relocations | Passing all-body root reachability |
|---|---:|---:|
| Uniform, origin 4 | 98 | 0 |
| Uniform, origin 10 | 686 | 0 |
| Mixed, origin 8 | 1,309 | 0 |

These counts include geometrically/role-incompatible alternatives because the
test intentionally overapproximates valid constructions. None even reaches all
required bodies. They are not 4,186 independently certified assembly searches.

## Implication

The two residual arrangements demonstrate that local 7P/7N/7e contact/exit
compatibility is attainable. Their missing ingredient is not repaired by extra
reader depth within these bounds, changing reference diagonals while keeping
occupied shapes fixed, or relocating just one remaining neutron with all P/E
sites fixed.

A next targeted family must change more: e.g. move an entire disconnected
P/N/E branch to an entry already reachable from the retained core, or move
multiple bodies jointly. The mixed test here is NOT a general search over all
occupied geometries under mixed diagonals. Larger origins and other arrangements
remain open. No new N-14 witness or viewer option was produced.

## Evidence

```sh
node research/strominger/checkers/probe_n14_connectivity_repair.mjs
```

`results/n14-connectivity-repair/verification.json` records the source witness
hash, full missing-body coordinates, relocation counts, and exact removed
operation links with origins. The precursor deletion audit is in
`results/n14-from-n15/verification.json`.
