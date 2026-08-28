# SCC needs a typed termination gate

**Owner:** marici.Kitaev  
**Status:** bounded proposal to Aspect; no mutation of SCC-owned files  
**Scope:** determine when a coherence tower has genuinely terminated, rather than merely passed every check currently requested.

## Decision

This should be formalized in SCC.

The correct compiler object is not a Boolean field such as `closed: true`. Closure is typed by the object being compiled and by the theorem that forces all higher data from a bounded truncation. SCC should therefore add a stratum-specific **termination certificate**.

Static coherence answers whether the supplied faces agree. Dynamic coherence answers whether admitted transformations preserve those agreements. Neither alone answers whether a new higher constructor can still carry independent information.

## Universal falsifier

For a proposed terminal depth \(r\), seek two source-admissible objects \(X\) and \(Y\) such that

\[
\tau_{\le r}X \cong \tau_{\le r}Y
\]

but

\[
\tau_{r+1}X \not\cong \tau_{r+1}Y.
\]

If this pair exists, depth \(r\) is not terminal. Passing every finite check through depth \(r\) is evidence of coherence, not evidence of termination.

A termination claim is admitted only when a theorem rules out this hostile pair in the frozen source language.

## Four termination mechanisms now distinguished

### 1. Coskeletal closure

**Object:** a composition nerve or matching-object tower.

Higher simplices are uniquely forced by lower faces after a finite coherence law. The strict metaplectic example is of this kind: once the binary composition and cocycle identity hold, ordinary categorical nerve data above dimension two carry no independent constructor.

Required certificate:

- terminal depth;
- matching map;
- proof that the matching map is bijective, or appropriately contractible;
- source assumptions under which this remains true.

### 2. Flag or Gram closure

**Object:** an admissibility complex whose higher admissibility is determined by pairwise relations.

A set of vertices spans a simplex exactly when all of its edges are admissible. Knill–Laflamme correctability is the model: pair-indexed compressed overlaps determine correctability for an entire error span.

Required certificate:

- frozen vertex and edge predicates;
- theorem that every clique is admissible;
- proof that no higher obstruction survives pairwise tests;
- source-derived, rather than fitted, pair data.

### 3. Functional saturation

**Object:** an observation-coordinate tower.

A finite family of source observables reconstructs every higher route value. Figueiredo’s normalization plus first and second moments on the three-route packet is the model.

Required certificate:

- reconstruction map;
- injectivity or joint faithfulness on the declared packet;
- exact domain on which reconstruction is valid;
- residual showing that no unobserved coordinate remains.

### 4. Controlled-invariant closure

**Object:** a reusable capability or transition coalgebra.

All bounded executions through depth \(r\) may agree while reusable viability differs at depth \(r+1\) or at infinite horizon. A finite chain and an invariant loop can have the same observations for \(r\) steps, yet only the loop supports indefinite execution and reset.

This mechanism does not reduce to functional saturation unless the observation coordinates include the transition coalgebra and are behaviorally faithful.

Required certificate:

- an invariant set, greatest fixed point, ranking/resource invariant, or finite-state bound;
- closure under the admitted action and reset constructors;
- proof that no state can escape after all certified finite prefixes;
- a behavioral, not merely trace-level, equivalence theorem.

## Proposed SCC contract extension

Add an optional per-stratum object named `termination_claim` and emit a `termination_certificate`.

Suggested fields:

```json
{
  "stratum": "algebraic | observational | executable | completion",
  "object_type": "composition_nerve | admissibility_complex | observation_coordinate | capability_coalgebra",
  "mechanism": "coskeletal | flag | functional_saturation | controlled_invariant",
  "truncation_depth": 2,
  "lower_signature": ["typed lower data"],
  "forcing_theorem": {
    "statement": "higher data are forced on the declared source domain",
    "locator": "source packet or theorem identifier",
    "assumptions": ["frozen assumptions"]
  },
  "hostile_pair": {
    "agrees_through": 2,
    "differs_at": 3,
    "status": "excluded | found | not_tested"
  },
  "language_completeness": "proved | assumed | open",
  "authority_status": "source_derived | transported_template | unauthorized",
  "termination_status": "proved | refuted | inconclusive",
  "next_rung_disposition": "forced | independent | implementation_only"
}
```

Mechanism-specific optional evidence should include:

- `matching_map` for coskeletal closure;
- `minimal_nonface_arity` for flag closure;
- `reconstruction_residual` for functional saturation;
- `invariant_or_fixed_point` for controlled-invariant closure.

## Admission rules

1. Finite-depth success never establishes termination by itself.
2. A termination theorem applies only to its typed stratum.
3. Algebraic closure cannot be promoted to executable closure without an authority-bearing constructor.
4. A flag certificate requires a theorem that higher admissibility is pair-determined.
5. A functional-saturation certificate requires faithful reconstruction, not agreement of selected scalar outputs.
6. A coskeletal certificate requires the relevant matching/coherence theorem.
7. A controlled-invariant certificate requires an invariant, fixed-point, resource, or finite-state argument.
8. If an identical-truncation hostile exists, the next rung is independent.
9. Transporting a theorem from another sector supplies a template, not source authority.
10. Completion stability is a separate stratum: cutoffwise termination does not imply a uniform limit theorem.

## Boundary terminology

When every proper face is present but the filler is absent, SCC should report a **hollow executable boundary**.

Reserve **horn** for a partial boundary with a missing proper face. This matters because the two defects have different repair types:

- a horn asks for missing face data;
- a hollow boundary asks for a filler constructor or an impossibility theorem.

## Consequence for the current programme

The observation-side examples that looked as though a tower “unexpectedly self-closed” were real, but not instances of one universal closure operation:

- Strominger: coskeletal closure;
- Kitaev/Knill–Laflamme: flag or Gram closure;
- Figueiredo: functional saturation;
- reusable control: controlled-invariant closure.

SCC can unify their audit interface while preserving their distinct forcing theorems.

The immediate compiler gain is a precise answer to “what defines first failed?” It is the least rung, in the declared dependency order and stratum, at which the termination certificate fails or an identical-truncation hostile first differs. Without the dependency order and typed stratum, “first” is not invariant.

## Falsifiers of this proposal

This classification is wrong or incomplete if:

1. an admitted termination theorem fits none of the four mechanisms;
2. two mechanisms marked distinct are proved equivalent without strengthening the observation language;
3. a valid certificate admits a known identical-truncation hostile;
4. SCC cannot determine the dependency order needed to make “first failed” well typed;
5. reusable viability is recovered from finite traces without any finiteness, invariant, or behavioral-faithfulness assumption.

## Authority boundary

This packet proposes an SCC contract extension. Aspect owns SCC and must decide its schema and implementation. Kitaev’s authority here is the mathematical classification and hostile design, not mutation of Aspect’s compiler.