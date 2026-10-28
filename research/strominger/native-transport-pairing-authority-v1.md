# Can native transports select the pairing?

## Conjecture C3

Perhaps the existing native triangle equivalences ABC and ADB, together with their query-composition theorem, already force the left-invariant pairing used in the repaired exchange model.

## Source audit

`research/nima/agda/NativeSeedTransitionProbe.agda` supplies equivalences on Vertex, their marked-package attachments, native query agreement, retained-query agreement, and composition. Its triangle functions are extracted directly by the new checker, rather than assumed to match the earlier numerical generators.

These declarations do not specify a real amplitude carrier, measure, quadratic budget, or isometry of a pairing. An equivalence of finite types is not an isometry of every independently attached metric. This is a bounded audit of this module, not a repository-wide impossibility theorem.

## Falsifier

Reuse the positive conjugation-invariant alternative pairing from the preceding counterexample: double transpositions have weight two, other elements weight one, with the common feature normalization divisor four.

For the native transition function f_AB(g)=[g(A)=B], let the supplied ADB transport act by left pullback:

    (L_h f)(g)=f(h^-1 g).

Because h(B)=A, L_h f_AB=f_AA. Direct exact calculation gives

    ||f_AB||^2=1,
    ||L_ADB f_AB||^2=||f_AA||^2=3/4.

All native Boolean transition and composition identities still hold. The checker verifies the full 2,304-entry group/query composition table. Nevertheless, the independently attached pairing is not preserved.

The diagonal query f_AA is an allowed query of the native module, not an added primitive seed edge. No AA exchange port or new path is introduced by this test.

Thus C3 is false as a consequence of the inspected native interface. Composition preserves the semantics of evaluation, not the norm of an attached response carrier.

## Sharper repair C4

Within the declared carrier R^G with a positive diagonal measure pairing, require only the left actions of the TWO actual triangle generators to be isometries. This is sufficient; one need not separately postulate invariance under every group element.

On coordinate indicators delta_g, isometry says

    mu(hg)=mu(g),  h in {ABC,ADB}.

These generators connect all twelve group elements. Therefore every weight is equal. The constraint graph is connected, its equality constraints have rank eleven, and the remaining common scale cancels under feature normalization. The previous conditional exchange-uniqueness theorem then applies.

This is a smaller operational premise, not a derivation of that premise. It assumes both that the native transports are realized by these left actions on the amplitude carrier and that those actions preserve the chosen budget. Neither claim follows from their being vertex equivalences.

A transported metric could make the same maps isometric between different metric presentations. That is NOT preservation of the one fixed physical pairing required here and would not select its initial value.

## Decision

The immediate missing interface is now explicit:

    native triangle transport
       -> specified action on the prepared amplitude carrier
       -> preservation of ONE fixed pairing.

An independently supplied apparatus or source construction proving this interface would close the finite pairing selector. Merely declaring uniform counting, or calling native equivalences unitary, would assume the conclusion. This audit does not supply that apparatus, an autonomous preparation, a reset cycle, or a physical energy interpretation.

## Verification

    python research/strominger/checkers/check_native_transport_pairing_authority.py

The checker reruns the preceding exact pairing counterexample, binds both generators to the current Agda source text, checks group/query composition, the connected weight-constraint graph, and the 1 versus 3/4 norm witness. General uniqueness follows by the written connectedness argument above. No new Agda compilation was run.

Receipt: `results/native-query-pairing-selection/transport-authority.json`.
