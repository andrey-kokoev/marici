# G4 radial-interface fixture test-completeness audit

## Question

Do the current fixture checkers cover every field, law, and hostile case required by the proposed minimal radial-interface delta?

## Requirement-to-test matrix

Status `shape+hostile` means the field shape is accepted and a targeted malformed fixture is rejected. Status `shape-only` means syntax is checked but the mathematical law is not executed. `external` marks a declared but absent witness.

| Requirement | Status | Existing executable evidence | Residual |
|---|---|---|---|
| carrier placement | shape+hostile | `check_g4_radial_interface_conformance.py` | no G4 carrier declaration |
| source synthesis `U:C→X` | shape+hostile | interface checker; `check_synthetic_zeta_g4_source_map.py` | no authoritative domain, codomain, or source derivation |
| directed six-coordinate feature packet | shape+hostile | interface checker | coordinate names only; no complete source maps |
| codiagonal coefficients `(1,1,-1/2,-1/2)` | shape+hostile | interface checker | no proof that this fixture map is G4 radial balance |
| state recovery | shape+hostile | interface checker; `check_synthetic_g4_recovery_radical.py` | identity-on-range and continuity are declarations, not evaluated witnesses |
| exclusive cycle policy | shape+hostile | interface checker; recovery/radical checker | no constructed quotient or observer |
| Green form, variance, metric, feature stage | shape+hostile | interface checker; `check_synthetic_zeta_g4_codiagonal_green.py` | matrix is absent |
| Green radical and quotient | shape+hostile | interface checker; recovery/radical checker | radical kernel and quotient map are absent |
| return placement | shape+hostile | interface checker; recovery/radical checker | no executable return map |
| source typing law | shape-only | literal `laws.source_typing=declared` | typed proof of `U` absent |
| reciprocal covariance | shape-only | required symbol list | no commuting equations evaluated |
| exact kernel sequence | shape-only | required formula string | kernels and exactness maps not computed |
| recovery law | shape-only | declaration and hostile readout test | no `QP(x)=x` evaluation on `ran(U)` |
| Green range nondegeneracy | external | placeholder `required_external_witness` | full metric rank witness absent |
| quotient projection compatibility | shape-only | required projection-name list | no commuting projection squares |
| projective continuity | shape-only | literal `declared` | topology-level witness absent |

All nine hostile fixtures required by the delta are rejected by `check_g4_radial_interface_conformance.py`. The three source-comparison failures and seven downstream failures added in the synthetic checkers improve localization but do not upgrade the shape-only laws.

## First false-positive path

A candidate can retain every required literal, pass all current hostile fixtures, and still replace every proof-bearing law by the strings already present: `declared`, `required_external_witness`, and the printed kernel-sequence formula. Therefore `baseline_errors=[]` is only schema conformance. The earliest unchecked mathematical edge remains typed source synthesis `U:C→X`; conditional on a supplied `U`, the first unchecked internal law is reciprocal covariance, followed by exactness of the kernel sequence.

## Acceptance test

A proof-bearing checker must replace literals by exact finite data: typed basis and maps for `U`, `D`, quotient, recovery, and return; matrices for the Green form; and executable equations for covariance, exactness, recovery, quotient projections, rank/nondegeneracy, and continuity on a declared finite projective diagram. Each law requires a deliberate noncommuting or rank-deficient fixture.

## Disposition

Field coverage and required hostile-case coverage are complete. Mathematical-law coverage is not: five laws are shape-only and Green nondegeneracy is externally blocked. The fixture remains useful for rejecting architectural conflations but cannot return scientific radial–G4 conformance.
