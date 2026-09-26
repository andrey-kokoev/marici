# A factor can exist while a chosen comparison family cannot descend

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverHigherWitnessDescent.agda`; log: `results/agda-higher-witness-descent.log`. It rebuilds the set-valued criterion and imported circle-cover material.

## Concrete higher-valued test

There is one source value (Unit). Its first observation is Unit. Its second observation is a fixed point of the higher index type used by the circle-cover example. An ordinary image factor exists explicitly: send the first admissible output to that fixed point's admissible image.

Now choose the output equality for EVERY source collision to be the nontrivial index loop. This supplies every endpoint equality requested by the earlier Preserves predicate, including the reflexive collision.

Agda proves that any actual factor induces the reflexive comparison on that reflexive collision. This holds even if the factor's source-arrival equality witness is nontrivial: its forward and inverse contributions cancel. The chosen loop cannot equal that induced identity comparison. Therefore NO factor retains the specified chosen comparison family, despite an ordinary factor existing.

This is a checked unit-coherence obstruction. It is NOT a counterexample to existence of all higher-valued factors, nor a proof that every higher-valued observation fails descent. It shows that endpoint-level existence and retention of supplied witnesses are different problems. The previous set-valued theorem avoids this distinction because equality witnesses in its target are propositions.

## Consequence

A proposed observational foundation must distinguish:

- an output is determined;
- output comparison endpoints can be connected;
- specified comparison witnesses are induced coherently by the determination.

The third cannot be replaced by the first two without losing mathematical content. This remains a direction-free requirement: preserving identity and composition is not introducing a clock.

## Next

Consolidate a fresh programme-wide proof/source audit and claim ledger. The chain now includes support, observation, gluing, information loss, records, admissible images, set descent and a higher-witness obstruction. A single checkpoint should make clear which statements are checked, which require additional coherence, and which remain interpretations of the user's execution-as-observation proposal.

A further mathematical branch remains: formulate a coherent higher-valued image-descent interface, with unit/composition and higher comparison laws rather than only Preserves. The present counterexample identifies a necessary missing law; it supplies neither a complete higher-descent criterion nor a physical observer model.
