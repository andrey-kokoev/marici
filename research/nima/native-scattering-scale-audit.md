# Native scattering: doublet discrimination requires independent relative scale

## Result

Continued the existing native-pair/orbital scattering branch without identifying it with Strominger's coefficient Hamiltonian. The earlier two native-doublet predictions are distinct at the SAME declared scale, but an unknown relative native/orbital scale produces an exact rival with identical selected-encounter responses.

The scale was not fitted or adopted physically. It is a counterexample to identifying a doublet from flux while leaving that nuisance free.

## Retained source and fresh checks

[Contract](contracts/native-scattering-scale-audit.v1.json); [checker](checkers/check_native_scattering_scale_audit.py); [result](results/native-scattering-scale-audit.json).

Active SCC obligation: readout identifiability under relative-scale nuisance. Loaded and verified direct source pins of the existing Slater real-axis, endpoint dispersion, orbital density and native-pair adapter receipts. Rechecked both chiralities' exact pair-energy formulas. The original E4 interval predictions were reproduced **exactly**, including rational endpoints, with no midpoint substitution. Fixed scales1/2,1,2 for each doublet were then propagated through the same interval formulas. Every resulting probability enclosure is bounded and its optical sum contains one.

No source-owner main, continuum integration, new source Hamiltonian or physical experiment was executed. The imported real-axis certificates remain the basis of the interval calculations; this is not a new independent proof of their integrals.

## Exact scale rival

The two retained pair energies are

    e0=11-2sqrt(6)-sqrt(5),
    e1=11-2sqrt(6)+sqrt(5).

Introduce the relative scale s already acknowledged as supplied in the source model. The encounter core is s e_i I4. Its scalar/vector resolvent denominators depend on that core only through delta=s e_i:

    E-delta-2a_pair-a_Slater+i(2b_pair+b_Slater),
    E-delta-a_pair-a_vector+i(b_pair+b_vector).

Therefore option0 at s0=1 and option1 at

    s1=e0/e1=0.46358540402604537...,

have exactly the same denominators and, with the same declared vertices/couplings, the same encounter optical amplitudes. Symbolic substitution verifies the identity before probabilities are formed.

At E4 they share the original option0 probability enclosures: two outputs approximately[0.16916,0.18451], three outputs[0.55997,0.58403], survival[0.23776,0.26597]. This does not contradict the earlier source result: it compared BOTH options at scale1.

Where the same channel laws apply, the alias holds at every energy, not just E4. More energy samples or more precise Slater integration cannot by themselves resolve this exact parameter redundancy. The continua, couplings and orbital energy coordinate are held fixed; this is a change of the relative native scale, not a common change of all units.

## What would exclude this rival

Suppose an INDEPENDENT calibration constrains the same relative scale around1, with either rival restricted to[1-d,1+d]. Their possible core energies are disjoint if

    e0(1+d)<e1(1-d),
    d<(e1-e0)/(e1+e0)=sqrt(5)/(11-2sqrt(6))
      =0.3665072051814537... .

The checker verifies the boundary exactly: a25% halfwidth excludes core equality, a50% halfwidth does not. At equality the core ranges touch. This excludes this particular equal-core alias, not every possible intensity, coupling or preparation degeneracy. It is not an uncertainty budget for an actual experiment.

An independently sourced doublet/output-action selection or a native-state-sensitive observable could also distinguish the rivals. Equal selected encounter amplitudes do not identify their full100-state native embeddings or physical output representations; the96-state complement and native cycle information remain retained.

## Decision and continuation

Before using the existing flux difference to infer a native doublet, obtain independent relative-scale information or a source-selection measurement. Do not set the scale by the same flux to be explained. A useful next bounded search/test is whether existing preparations give access to both doublets under ONE common scale, or to their native-cycle response. Such a record would add information absent from the single selected scalar-energy encounter.

Physical partner/species, coupling and detector calibration remain open. This result does not change the independent high-energy strained-model numerical frontier or prove physical scattering.

## Reproduce

```text
uv run --with sympy python research/nima/checkers/check_native_scattering_scale_audit.py
uv run --with sympy python research/aspect/scc/scc.py check native-scattering-scale-audit-v1
```

Use structured-command. Outputs are owner-local; original source files/receipts remain unchanged. No commit/push authorized.
