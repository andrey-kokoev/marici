# A fixed Newtonian tidal calculation retained in RRC

Successor: [two-route comparison](newtonian-two-route-comparison.md) now checks
an independently constructed potential jet against this geometric formula.
The reproduction runner below now checks both certificates and three compiler
negative controls, as well as independent polynomial calculations.

## Result and physical inputs

With G=1, retain the existing `sources_a` fixture from
`checkers/check_machian_newtonian_localization.py`: mass 2 at (3,0,0),
mass 1 at (0,4,0), observation point at the origin. The assumed Newtonian
potential is Phi=-sum m/|x-r|. Its assumed point-source Hessian formula is
m/r^3 (delta_ij-3 n_i n_j). The live evaluator and separate normalized-direction
calculation agree on

    E = diag(-229, 74, 155) / 1728.

For a unit x-directed separation the supplied relative-acceleration law
`delta a = -E delta x` gives (229,0,0)/1728. The formal certificate explicitly
checks its x component and all nine tensor components. Trace E is zero.
These are model calculations, not experimental observations or a derivation
of Newton's law from RRC.

## Formal calculation

- `agda/NewtonianTidalKernel.agda`: integer-scaled point-source tensor formula,
  second jets, affine-jet action, and relative-acceleration contraction.
- `agda/NewtonianTidalFixture.agda`: generated from the live Python fixture,
  including exported tensor and lower jet entries.
- `agda/NewtonianTidalCertificate.agda`: pins the sources, verifies radial
  directions are unit, and checks 3^3*64=4^3*27=1728 before checking the tensor.

For every integer-scaled second jet j, constant c, and vector b, Agda proves

    hessian (addAffine c b j) = hessian j.

This is a universal algebraic identity of the declared second-jet action.
It is not a formal derivation of differentiation on real-valued potentials,
not a construction of a quotient type, and not a theorem about arbitrary
coordinate transformations. Exported potential and gradient values are not
independently certified here; the tensor is. The common-denominator integer
encoding avoids floating-point arithmetic. The Python comparisons still
share Fraction and are not independent arithmetic-backend checks.

## Actual RRC connection

The certificate imports `WholePackageResolution.Generators` and
`WholePackageSigmaPi.Universe`; it does not invent a stand-in history type.
Four explicit seed constructors admit only the source package, evidence
package, computed tensor package, and shifted tensor package.

The existing `compare-rule` retains an identity equivalence of tensor types
and the proved agreement of their values. Existing `Pi-rule` applications
combine that comparison history with the source and evidence packages.
`reify-history` retains the whole derivation at the next universe level;
`retains-history` checks recovery of the same history.

The proof is constructed by Agda calculation first and admitted explicitly
as evidence. RRC retains and combines this evidence; the current bridge does
NOT show that RRC synthesizes the physics or the calculation from bare masses.
This is forward realization of a checked fixed calculation into RRC, not a
faithful translation of the complete Newtonian theory or the Python evaluator.

## Reproduction and controls

Run through shell, as directed by the operator:

```powershell
pwsh -NoProfile -File research/nima/checkers/check_newtonian_tidal_bridge.ps1
```

The runner executes the existing exact checker, exports and cross-checks the
fixture, and freshly compiles the certificate with Agda 2.8.0/Cubical 0.9
(`--safe --cubical --guardedness`, interfaces ignored by the positive runner).
The fresh positive closure check passed. Negative controls were rejected with
exit 42 and the intended `[UnequalTerms]` errors:

- numerator -230 instead of -229: `228 != 229` in negative-integer encoding;
- inverse-cube denominator 1729 instead of 1728: `1728 != 1729`.

Receipts:

- `results/newtonian-tidal-export.json`: live export consistency and source hashes;
- `results/agda-NewtonianTidalCertificate.json`: fresh compiler result;
- `results/newtonian-tidal-formal-audit.json`: aggregate positive/negative check.

No external-reference convention audit, continuum potential theorem,
arbitrary-source implementation proof, or gravitational emergence claim is
made by this certificate.
