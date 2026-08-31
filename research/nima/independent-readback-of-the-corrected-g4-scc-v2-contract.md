# Independent readback of the corrected G4 SCC v2 contract

## Executed verification

Executed through structured-command MCP:

```text
python research/aspect/scc/scc.py rh-state research/aspect/contracts/theta-rh-interaction-net-state.v2.json
python research/aspect/checkers/check_theta_rh_g4_interaction_net_state.py
```

Both commands exited zero. The compiler reports:

- schema `marici.scc.rh-interaction-net-state.v2`;
- `passed: true`;
- generation `corrected_G4`;
- RH terminal open;
- `rh_proved: false`.

The hostile checker passes its baseline and eleven mutations. Ten are the
ordered contract hostiles; the eleventh is explicit RH-terminal promotion.

## Corrected features now represented

Version two repairs the principal drift identified in the prior audit:

1. bare Euler \(\det_3\), reciprocal relative \(\det_2\), and centered
   trace-class return are distinct;
2. history, theta, and arithmetic are three separate source ports;
3. the theta diagonal is zero and Gram compression is not primitive dynamics;
4. theta Koszul and two-sided Evans objects precede the conservative chain map;
5. incidence injectivity is separated from closure membership and exact range;
6. scalar Evans mismatch cannot discharge the vector adjoint residual;
7. seam state, limiting absorption, prime-shell residuals, chain map, mapping
   cone, and module length remain explicit slots;
8. the terminal cannot be promoted.

The reported frontier antichain is

- `maximal_isotropic_seam_state`;
- `prime_shell_adjoint_residual_family`;
- `seam_limiting_absorption_domain`.

## Remaining topology defects

### Seam state omits its domain dependency

The current declaration is

```text
maximal_isotropic_seam_state
  <- two_sided_evans_matching_lift
  <- conservative_green_complex
```

A completed seam state also requires the boundary-value domain supplied by
`seam_limiting_absorption_domain`. Without that edge, SCC could mark the state
constructed while its defining seam domain remains open.

The corrected dependency should include

```text
seam_limiting_absorption_domain
```

before state construction.

### Prime-shell family omits the Evans history

The current residual-family node depends on centered incidence and the
conservative Green complex, but the RH-bearing residual is specifically

\[
B_\Sigma^\dagger u_z
\]

for the two-sided Evans history \(u_z\). A generic adjoint family does not
supply this specialization. Add

```text
two_sided_evans_matching_lift
```

as a dependency of `prime_shell_adjoint_residual_family`.

### Zero-free complement status is too coarse

The strict prime-delay Cayley network is constructed as an abstract
zero-free/passive complement. Its identification with the final arithmetic
law \(D_U\), including primitive, square, connected, seam, endpoint, and
archimedean provenance, remains open.

The single constructed node `zero_free_arithmetic_complement` conflates:

1. `abstract_strict_cayley_complement`, constructed;
2. `source_integrated_arithmetic_law_D_U`, open.

The mapping-cone complement must depend on the second, not merely the first.

### Source locators are aggregate rather than constructor-specific

Every constructed node cites the same Nima audit packet. That packet classifies
the architecture but is not the primary derivation of every constructor.
SCC validates path existence, not theorem-to-locator correspondence.

Each constructed node should cite its direct source packet or an immutable
receipt map. Otherwise the contract can pass after a summary overstates one
input.

## Strength versus RH

`critical_seam_green_confinement` currently depends on
`local_module_length_preservation`. Multiplicity preservation is required for
the full divisor comparison and publication theorem, but not for the bare
location statement that all represented zeros lie on the seam. This makes the
terminal stronger than RH rather than unsound.

A cleaner topology would separate:

- `critical_seam_location`;
- `local_module_length_preservation`;
- `divisor_with_multiplicity_identification`.

## Verdict

Version two is a substantial and valid correction. Its pass now tests the
right no-go classes and preserves the RH boundary. It is not yet a fully
source-faithful dependency graph because two domain/source edges are missing,
the abstract Cayley complement is conflated with the final arithmetic law, and
constructed nodes use aggregate locators.

The scientific status is unchanged: the prime-shell family, seam domain and
state, Evans-to-Green chain map, and RH terminal remain open. No RH conclusion
is authorized.
