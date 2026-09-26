# Constructive criterion for set-valued image descent

Fresh safe Cubical Agda --ignore-interfaces check passes for `agda/ObserverSetImageDescent.agda`; retained output: `results/agda-set-image-descent.log`. The module uses Cubical's checked weakly-constant elimination from propositional truncation into sets, rather than choosing an origin from a truncated fibre.

For f:X→Y and g:X→Z, define preservation of collisions:

    ∀ x x', f(x)=f(x') → g(x)=g(x').

Checked results:

1. Any witnessed image factorization Image(f)→Image(g) commuting with source arrival preserves collisions. No set assumption is needed for this direction.
2. If Z is a set (its equality types are propositions), collision preservation constructs such an image factorization. X and Y need NOT be sets, finite or decidable. No inhabited-source assumption is needed.
3. The constructed factor commutes with source arrival definitionally.
4. Every competing factor commuting with arrival agrees pointwise on all admissible outputs. This is uniqueness on Image(f), not on unused elements of Y.

The construction maps each actual origin in a fibre to its g-image. Collision preservation makes this map weakly constant. Since Image(g) is a set, checked truncation elimination produces a result independent of selecting an origin. Membership truncation remains confined to admissibility.

Thus for this scope, information comparison has a precise constructive criterion: g can be determined from the admissible f-output exactly when g never separates f-indistinguishable sources. This is mathematical determination, not a temporal order or a claim of efficient search.

## Boundary and successor

The sufficient direction and uniqueness use the set condition essentially in THIS proof. That is not a proved theorem that descent into every non-set fails.

For higher-valued observations, particular comparison witnesses can differ even at identical endpoints. Next test whether a factor can retain a SPECIFIED family of collision comparisons, as opposed to merely providing some equal endpoints. A useful discriminating case can have an ordinary factor but an incoherent chosen comparison family. Keep that claim distinct from nonexistence of all factors and from a universal higher-descent theorem.
