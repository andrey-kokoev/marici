# The top coherencer is a syntax–behavior distributive law

**Owner:** marici.Kitaev  
**Status:** bounded cross-sector synthesis  
**Inputs:** Nima’s source/observation separation and Strominger’s mixed-cell audit

## 1. Convergence

The emerging top-level architecture has two independently closed sides.

- A **source coherencer** says how primitive constructors compose, substitute, tensor, and acquire successor authority.
- A **behavior coherencer** says how states evolve, expose observations, retain memory, and become behaviorally equivalent.

The top cell does not merely compare their final scalar outputs. It compares their closure operations.

Let \(T\) encode source syntax and let \(B\) encode behavior. The candidate mixed coherencer is a natural transformation

\[
\lambda:T B\Longrightarrow B T.
\]

Its meaning is:

> Construct behavior-bearing components and then expose the composite behavior, or first expose component behaviors and then construct from those behaviors; the results agree through the typed comparison cell.

## 2. Exact compatibility equation

Let

\[
a:T X\to X
\]

be a source-algebra structure and

\[
b:X\to B X
\]

a behavior-coalgebra structure. Compatibility requires

\[
b\circ a
=
B(a)\circ\lambda_X\circ T(b).
\]

The left route constructs in the source and then observes behavior.

The right route observes the ingredients, transports syntax across behavior using \(\lambda\), and then constructs the behavioral result.

The residual

\[
\rho_X
=
b a-B(a)\lambda_XT(b)
\]

is the exact top-level coherence defect.

This gives Nima’s quantitative \(\rho\) a categorical home: \(\rho=0\) is an exact distributive law on the represented object; controlled nonzero \(\rho\) is a lax law only when its typing, composition, resource accumulation, and repair semantics are supplied.

## 3. Laws required of the mixed cell

If \(T\) is a monad with unit \(\eta\) and multiplication \(\mu\), \(\lambda\) must respect primitive insertion and substitution:

\[
\lambda\circ\eta_B=B\eta,
\]

and

\[
\lambda\circ\mu_B
=
B\mu\circ\lambda_T\circ T\lambda.
\]

Naturality is also mandatory.

If behavior carries comonadic structure, corresponding counit and comultiplication laws must be tested. If \(B\) is only an endofunctor, SCC must not pretend those extra laws exist.

Nodewise commuting squares do not imply the multiplication law. A triple-composition hostile can pass every primitive and pairwise comparison while failing substitution coherence.

## 4. What each side contributes

### Source side

The source coherencer determines:

- legal constructor expressions;
- unit and substitution;
- tensor or parallel composition;
- typing and domains;
- authority succession;
- resource and waste annotations;
- fault factorization.

### Behavior side

The behavior coherencer determines:

- transitions and outputs;
- memory and reset;
- observational equivalence or bisimulation;
- context separation;
- viability and invariant closure;
- completion of observable traces.

### Mixed top cell

The distributive cell determines whether source equivalence is a congruence for behavior and behavioral equivalence is respected by source construction.

It is therefore the compiler from constructor semantics to behavioral semantics.

## 5. Strominger’s exact warning

Strominger’s current finite valuation packet separates three layers:

1. a source congruence jet creates three classes;
2. a nested readout converts those classes into a content jump;
3. a final Smith or snake-index cell identifies the classes again.

Thus a final behavior quotient can erase a valid source distinction.

The valuation failure proves a mixed-interface failure. It does not prove that either the source coherencer or behavior coherencer is internally defective.

This is exactly why the three certificates must remain separate:

- source coherence;
- behavior coherence;
- mixed distributive coherence.

## 6. Why this is higher than scalar coherence

A scalar comparison can commute on selected objects while substitution fails.

The distributive law must be stable under:

- naturality;
- unit insertion;
- multiplication or substitution;
- tensoring and parallel construction;
- context extension;
- reset and repeated use;
- resource and waste propagation;
- fault-model transport;
- successor-authority transport;
- completion where claimed.

Therefore the top cell governs a net of objects, not isolated nodes. It says which local coherent objects may be composed without changing their behavioral meaning.

## 7. Exact, partial, and lax forms

### Exact

All mixed laws commute. Source construction lifts functorially to behavior-bearing objects.

### Partial

The cell is defined only on a typed subcategory or domain. Closure claims must remain within that domain.

### Lax

A nonzero residual is admitted with an explicit target object and composition law. The residual must be:

- natural;
- typed;
- compositional under substitution;
- resource-accounted;
- bounded or assigned an authorized repair.

An unexplained scalar error tolerance is not a lax distributive law.

## 8. Hostile fixtures

1. **Nodewise hostile:** primitive squares commute, but triple substitution fails the multiplication law.
2. **Authority hostile:** outputs match while the two routes assign different successor authority.
3. **Waste hostile:** outputs match while one factorization discards an unrecorded resource.
4. **Fault hostile:** nominal behavior matches while fault propagation differs.
5. **Reset hostile:** one-use squares commute but reset changes the second-use behavior.
6. **Quotient hostile:** final behavioral readout erases a source distinction required by later construction.
7. **Completion hostile:** every finite mixed square commutes but residual norms escape in the limit.
8. **Unauthorized repair:** a comparison cell exists only after adding a constructor absent from source syntax.

## 9. Relation to the tower picture

The architecture is better written as two terminal towers plus one mixed cell:

[
egin{array}{ccc}
	ext{source syntax} & \xrightarrow{T}& 	ext{source closure}\
&&\downarrow\lambda\
	ext{behavior data} & \xrightarrow{B}& 	ext{behavior closure}.
end{array}
]

This is not a linear rung stacked above both. It is a distributive square that makes the two closure engines jointly compositional.

The user’s “top coherencer comparing final coherencers” is correct if “compare” means enforce this route equality. It is misleading if it means compare only their final scalar summaries.

## 10. SCC consequence

SCC should record three independent results:

```json
{
  "source_coherence": {
    "syntax_fingerprint": "...",
    "unit": "...",
    "substitution": "...",
    "authority_and_resource_laws": "..."
  },
  "behavior_coherence": {
    "behavior_signature": "...",
    "equivalence": "...",
    "context_separator": "...",
    "reuse_and_completion_scope": "..."
  },
  "mixed_coherence": {
    "lambda_constructor": "...",
    "authority": "...",
    "naturality": "...",
    "unit_law": "...",
    "multiplication_law": "...",
    "resource_waste_fault_transport": "...",
    "residual": "zero | typed lax residual | obstruction"
  }
}
```

Compiled operational closure requires all three. Source and behavior closure with only nodewise matching remains casewise operational.

## 11. Present conclusion

The top-level explanation is:

> Source coherence determines what constructions mean. Behavior coherence determines what executions mean. The distributive cell determines whether constructing preserves execution meaning under arbitrary admitted composition.

That cell is where network semantics lives.
