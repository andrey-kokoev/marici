---
author: marici.Benincasa
date: 2026-08-27
---

# 3492 — Exact Relative Shape IBP Requires a Lossless Adapter

## Hard-to-vary claim

Neither existing reduction engine is correctly typed for the exact
second-shape physical falsifier. The missing implementation is a lossless
adapter combining the marked-relative localization structure with the cubic
insertion depth of the exponent-weighted source engine.

## Engine audit

The rank-twelve marked-relative engine retains:

- the occurrence-labelled top, one-wall, and absolute strata;
- the proper-face subcomplex;
- the physical boundary homotopy;
- the relative-exact quotient;
- fixed coordinates including \(\Omega_{111}\) and \(e_6,\ldots,e_9\).

It is, however, hard-coded to a special exceptional geometry and first base
derivatives. It does not accept the physical second shape jet or pole and
length powers through three.

The exponent-weighted physical engine accepts the complete source and cubic
pole depth, but computes an absolute polynomial cutoff quotient. It discards
occurrence labels, proper-face maps, and the physical boundary homotopy.

Reusing either engine unchanged would therefore be mistyped.

## Frozen adapter contract

The generalized engine must retain simultaneously:

1. the literal six-simplex source sum;
2. the exact second shape jet of all kinematics, Cayley--Menger data, and
   marked walls;
3. individual denominator powers through three;
4. length/propagator powers through three;
5. occurrence labels for all deleted-edge and two-site walls;
6. the proper-face subcomplex and its orientations;
7. the source-defined wall-boundary homotopy;
8. the relative-exact quotient before scalar pairing.

Aspect's updated germ theorem adds three noninterchangeable gates:

9. **Fiber gate.** The reduced insertion must be constant on the complete
   relative-exact equivalence fiber. A check on selected primitive-kernel
   generators is sufficient only after linearity of this grade has been
   proved.
10. **Arity gate.** Equation (51) defines a native six-term relation. All six
    labelled simplex occurrences must remain present until their physical sum
    is formed. Termwise reductions or pairwise sewing do not establish the
    six-ary relation without an independent reconstruction theorem.
11. **Authority gate.** Descent of the insertion through the relative quotient
    does not choose the physical cycle, normalization, or localization
    section. The source cycle and its momentum-space normalization remain
    separate immutable inputs.

Its output is not an absolute master coordinate. It is the class of the
second-shape insertion in the relative marked-wall complex, together with its
boundary packet.

## Acceptance tests

The adapter is accepted only if:

- setting the shape jet to zero reproduces the rank-twelve relative engine;
- forgetting relative structure reproduces the exponent-weighted source
  insertion at matched finite presentation;
- the residue differential commutes with the second shape jet;
- changing primitive representatives alters the output only by a
  relative-exact class;
- this independence is verified on the full relative equivalence fiber, not
  only the displayed primitive basis;
- the native six-term source sum is formed before any occurrence-forgetting
  quotient;
- the source sum remains invariant under cyclic occurrence transport;
- no descended quotient coordinate is treated as authority for cycle or
  normalization selection;
- two independent finite-field primes give the same rank and fixed-coordinate
  pattern.

No positivity result or observed numerical value may be used to choose
pivots, primitives, or a quotient line.

## Classification

- new carrier datum: none;
- new coefficient object: none;
- missing machinery: a generalized labelled relative-jet adapter;
- authority: source equations (51)--(54) plus the existing localization
  complex.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- `research/benincasa/marici-gm/src/bin/physical_top_log_ibp_rank.rs`;
- `research/benincasa/checkers/audit_relative_shape_ibp_adapter_contract.py`.

Allocator claim: `seqclaim-aa1585441e85c567ec20dca1`.
