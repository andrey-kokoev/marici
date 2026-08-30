# Event-Axis Proliferation Terminates at a Dependent Action Witness

## Question

Does adding the domain axis close Aspect's event compiler for Hodge actions?

## Eight-axis hostile pair

Passive spin-frame rotation and active global Hodge rotation can share every
scalar event value:

```text
scalar=unknown
packet=unknown
incidence=unknown
history=unknown
path=admissible
coefficient=native
action=authorized
domain=preserved
```

They can also use the same matrix generator on spin-two components. Yet they
are different operations. Passive frame rotation changes a presentation and
acts identically on the geometric tensor. Active Hodge rotation is an
endomorphism of the radiative tensor bundle and changes the tensor.

No additional unscoped Boolean or enum attached to the event can make the
meaning of `authorized` intrinsic. Authorization is dependent on the objects
and variance of the action.

## Structural repair

Replace the scalar action value with a typed witness:

```text
ActionWitness
  operation_id
  source_object
  target_object
  domain_certificate
  authority_locus
  variance
  geometric_effect
  coherence_witness
```

The passive witness has presentation locus, passive change-of-frame variance,
and identity geometric effect. The active witness has state locus, bundle
endomorphism variance, and Hodge geometric effect.

The domain axis remains useful as a compiled projection of this record, but it
cannot replace the record. Likewise, `action=authorized` is a projection of a
valid witness rather than an independent fact.

## Consequence

Aspect's seven-axis independence theorem remains correct. The attempt to close
its open-world boundary by adding axes terminates here: action typing is
dependent, not Cartesian. A compiler may emit the seven or eight summary axes,
but admission must inspect the full witness from which those summaries are
derived.

## Disposition

The domain axis repairs the absent-versus-ill-typed alias. The dependent action
witness repairs the deeper presentation-versus-state alias and prevents
matrix-level authority laundering.

## Verification

```powershell
python research/strominger/checkers/dependent_action_witness_checks.py
```
