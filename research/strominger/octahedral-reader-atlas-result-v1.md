# Prior-led fixed-root octahedral reader atlas

## Why this attempt, rather than a new species rule

Prior research supplied clues that narrow the task:

- `prior-assembly-clues-v1.md`: an N reader may reference an unoccupied P; that
  geometry is not an extra particle. Existing NN/reader continuations should be
  tested before introducing a larger-body law.
- `composite-neutron-binding-v1.md`: a native N component can embed in a whole
  octahedron with external PN/NE ports for some seed markings. The canonical
  root's direct exit is internal. Whether other native readers can solve that
  fixed-root problem was left open.
- `nuclear-electron-separation-audit-v1.md`: terminal E coverage is a supplied
  completion criterion, not a universal physical nucleus criterion.
- `cmc-mcm-carrier-semantics-audit.md`: geometric windows are not automatically
  the full36/8-dimensional native preparation objects.
- `generated-reader-classification-v1.md`: reader-image agreement can construct
  compatible fillers in its specific WG fragment. That theorem does not identify
  this neutron atlas with that fragment or supply its particle inventory.

The registered attempt in net revision28 therefore stays with the fixed marked
root and the existing N-only operations. It does not relax species admission,
occupy reference P bodies, change the subdivision or select a favorable marking.

## Atlas construction

Start with the actual PN target. Retain its original owner octahedron. Explore
NN-phase-advance and neutron reader-phase-advance, recording each representative
path, five-slot permutation, reference context and outgoing NE face.

A finite key contains the full geometric chart and five-slot permutation. Absolute
origins and operation histories are not equated: every quotient edge records its
actual target origin and the offset from its representative. Native source code
constructs the same geometry and permutation after a uniform origin shift; phase
witnesses translate all occurrence indices together. An offset replay checks this
implementation property. The following invariant, not a finite cutoff alone,
supplies the all-N-only-length statement.

## Exact invariant and geometric obstruction

In the canonical first N chart the unordered pair

    D = {C1,C2}

is a pair of opposite vertices of the whole octahedron. The actual four-component
subdivision uses D as its internal diagonal. No external triangular face contains
both endpoints of D.

Inspection of BOTH unchanged source N-only rules gives

    new C1 = old C2,
    new C2 = old C1.

Hence D is preserved inductively, regardless of the number of advances. A reader
advance stays in its component. An NN advance crosses a face containing D; such
a face is internal to this subdivision, so it stays in the same whole support.
Every NE exit also uses a triangle containing C1 and C2. Consequently every such
exit is internal to the original octahedron, not an exterior regular endpoint.

The checker verifies the diagonal, boundary and all atlas transitions directly.
It also checks valid representative retained paths, full permutations, translated
origins and reference-only P contexts. The two extra support vertices have not
been assigned invented coefficients.

## Fresh bounded results and additional recovered clues

The closed atlas has8 reader states,16 N-only transitions and8 NE ports. All8
ports are internal;7 representative readers use unoccupied reference-P geometry.
Nine checks pass. This strengthens the fixed-root direct-exit observation under
the registered N-only scope; it does not replace the broader prior constructions.

Further source reading prevents repeating already tested alternatives:

- `subdivision-dependence-v1.md` already reports that uniform diagonal01|23 makes
  the exact canonical root's NE port external, but suppresses NN growth in its
  tested universe. It is not a free fix preserving all old continuations.
- `mixed-subdivision-n14-v1.md` already implements globally consistent per-item
  subdivision choices. Its N-14 origin7 query remains UNKNOWN, including a600s
  retry. Do not describe mixed subdivisions as untried or turn timeout into UNSAT.
- `native-screw-patch-v1.md` already reports a genuinely growing retained native
  patch:24 occupied primitives,66 readers and repaired incidental contacts. Its
  eight-transfer macro uses inverse-PN and P-reader moves, precisely outside this
  N-only invariant. Its far E cap also blocks simultaneous NN occupation, retaining
  the same distinction between a capped finite patch and indefinite extension.

These three prior results were inspected, not freshly replayed here. The screw
patch is a more concrete next source to assess against an esd7 shared-interface
obligation than inventing a new reader/species rule. It is not yet a Pb model,
neutral isotope, complete four-branch channel or all-prefix coherence theorem.

## Disposition and boundary

**No external port under the fixed-root N-only rules.** This answers the narrow
registered question with a source-derived invariant, rather than an arbitrary
search-depth failure. It is not a no-go theorem for the original whole-body task.

Inverse-PN followed by P-reader operations, a changed support or an explicitly
transported alternative subdivision are outside this atlas. The earlier8/24
external markings per seed orientation remain valid prior local results; this
attempt does not authorize rebinding the fixed root to one of them. Nor does a
whole support containing several native readers thereby count as one neutron.

Before selecting a next attempt, compare those excluded routes against existing
source constructions. In particular, the registered predicate was an external
port of the ORIGINAL support: leaving it through a new P or another octahedron
would be a different candidate, not a hidden success here.

## Reproduce

```sh
node research/strominger/checkers/check_octahedral_reader_atlas.mjs
```

Contract: `contracts/pb208-octahedral-reader-atlas-attempt.v1.json`.
Pre-execution state: `contracts/persistent-seam-pe-conjecture-net.snapshot.rev28.json`.
Atlas, explicit histories/offsets and verification: `results/octahedral-reader-atlas/`.
No production constructor, other-owner source or viewer admission was changed.
