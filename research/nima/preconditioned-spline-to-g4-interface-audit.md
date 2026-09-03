# Preconditioned-spline to radial–G4 interface audit

## Question

Which typed arrows connect the frozen completed-zeta spline theorem to the current radial–G4 interface, and where does composition first fail?

## Source objects

The source theorem now provides:

1. an even compact log-coordinate test `f` and spectral transform `h`;
2. labelled prime powers `(p,m)` with grade `log(p^m)` and weight `log(p)/sqrt(p^m)`;
3. reciprocal pole modes `2` and `1/2`, annihilated by the unique positive coefficient ray;
4. the completed-zeta archimedean distribution with kernel `n+1/4`;
5. a certified positive scalar interval for the pole-deleted explicit form.

## Available G4-side interface

`research/nima/contracts/g4-radial-interface-candidate.v1.json` names a radial carrier, source map, feature map, codiagonal, recovery, Green form, and Green radical. Its labels include prime, grade, shell, ordered pair, and theta label. The companion packet `minimal-g4-radial-interface-delta-required-after-the-cycle-and-balance-kernel-audits.md` states the laws required for retained labels, common-history quotienting, endpoint–Wronskian balance, state recovery, cycle observation, metric typing, and radical quotienting.

These names define a conformance test shape, not a scientific comparison: the contract status is `test_fixture_only` and its claim boundary explicitly denies an authoritative G4 declaration or radial identification.

## First missing arrow

The first unavailable typed arrow is an authoritative radial source map

\[
R_{\zeta}:\{(p,m),\log(p^m),\text{reciprocal pole labels}\}
\longrightarrow U_{G4},
\]

where `U_G4` is a declared G4 projective oriented-edge source. The map must preserve prime and grade labels, construct shell and ordered-pair labels, type reciprocal pairing, and identify how the continuous log-coordinate test acts on the source. The fixture’s field called `radial_source_map` is not this arrow because fixture transport grants no G4 authority and no derivation from the completed-zeta objects is supplied.

Without `R_zeta`, the proposed feature map cannot receive the spline source; the codiagonal cannot be compared with the arithmetic coefficient or pole-annihilating multiplier; recovery cannot transport the completed-zeta state; and the positive scalar cannot be identified with a Green-form value. Label-name overlap and equal signs do not construct these maps.

## Acceptance test

An owner-authorized G4 declaration must provide the domain and codomain of `R_zeta`, images of `(p,m)` and reciprocal pole generators, preservation laws for grade and pairing, and a commuting square from source evaluation to the declared radial feature map. Only then can downstream codiagonal, metric, and radical comparisons be tested.

## Disposition

The source theorem is interface-ready, but radial–G4 composition is undefined at `R_zeta`. This is an ownership/authority blocker, not evidence against the source theorem or for a G4 identification.
