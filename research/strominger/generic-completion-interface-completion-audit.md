# Generic completion interface: requirement audit

## 1. Topology-bearing completion

Status: proved and mechanically typed.

Evidence:

- `contracts/generic-completion-interface.v1.schema.json` requires source and
  completed spaces, target spaces, topology, dense embedding, completion map,
  both operators, a canonical extension proof, and a commuting square.
- `generic_completion_interface.py` rejects ordinary-base-change typing,
  missing density, nonunique extensions, untyped unbounded domains, and
  noncommuting squares.
- Magnetic and theta contracts exercise respectively a unique locally convex
  continuous extension and a closed-form Friedrichs extension.

## 2. Finite linear observation fiber

Status: proved and mechanically typed.

Evidence:

- The magnetic fiber declares a 21-dimensional kernel, 21 independently
  authorized ports, a sparse exact identity matrix, rank 21, faithfulness, and
  all 21 row-deletion ranks.
- The validator computes exact rational rank rather than trusting declarations.
- A separate valid 22-port redundant fiber has rank 21 but is not minimal,
  proving that port count and kernel dimension are distinct fields.

## 3. Hostile distinctions

Status: all required distinctions have deliberate failing packets.

- completion versus base change:
  `completion_as_ordinary_base_change`;
- completion-only ordinary kernel versus completion defect:
  `completion_defect_dimension_mismatch` and
  `derived_completion_obstruction_untyped`;
- characteristic support versus kernel support:
  `characteristic_support_is_not_kernel_support`;
- kernel dimension versus port count:
  `kernel_dimension_port_count_conflation` plus the valid redundant fiber;
- unavailable versus zero-valued port:
  `unavailable_port_is_not_zero_port`, while an available port evaluating to
  zero on the zero state remains valid.

## 4. Completion-kernel comparison square

Status: proved as a typed comparison theorem.

The validator checks the induced kernel map, injectivity/rank, commutativity,
the dimension partition, graph-limit witnesses for ordinary completion-only
classes, and actual Tor references for derived obstruction classes. The
neutral fixture exercises all three classifications in one valid packet.

## 5. Magnetic reproduction

Status: reproduced with bounded upstream evidence replay.

The magnetic contract gives source-kernel rank zero on finite signed atomic
measures and completed-kernel blocks of dimensions 5, 7, and 9. Therefore

\[
\ker\widehat{\mathcal A}_3
=\mathcal H_2\oplus\mathcal H_3\oplus\mathcal H_4,
\qquad\dim=21.
\]

The aggregate evidence replay verifies 91 constituent gates and its artifact
digest. All 21 ports are faithful; every one-port deletion has rank 20.

## 6. Grothendieck export

Status: reusable scoped packet produced.

`contracts/grothendieck-theta-completion-test.v1.json` types the weighted
Hilbert completion, `A_Phi` as the closed Friedrichs generator, its ordinary
constant ground kernel, compact-resolvent projections `E_N`, and strong
spectral exhaustion. The packet explicitly sets `rh_bearing_kernel_claim` to
false, and the hostile checker rejects changing it to true.

## Final answer

Completion reveals an ordinary kernel without manufacturing it exactly when:

1. the source embeds densely into a declared Hausdorff completion;
2. the target embedding is explicit;
3. the source operator has a unique, independently proved continuous,
   graph-closed, or Friedrichs extension;
4. the operator-extension square commutes;
5. new ordinary zero modes possess graph-limit witnesses;
6. derived obstruction claims carry separate Tor evidence;
7. observation ports have independent execution authority and exact rank
   certificates.

If any of conditions 1--5 fails, a purported new ordinary kernel may have been
manufactured by an arbitrary extension choice. Support and dimension alone
never supply the missing authority.
