# Mediator threshold origin probe

Owner: `marici.Figueiredo`.

## Question

WP191 showed that restricted `epsilon` interventions leave a local hard
constraint and a frozen nonzero mediator equivalent. This packet tests the
alternative origin-sensitive probe:

Can threshold spectroscopy detect the mediator origin?

## Exact claim

A resolved mediator-threshold channel separates local hard constraints from
mediator origins:

- local constraint: no mediator threshold;
- frozen nonzero mediator: threshold at energy `5`;
- zero-accessible mediator: threshold at energy `5`.

An energy window that includes the threshold detects the mediator class. An
unresolved window below threshold does not.

The threshold probe does not distinguish mediator subtypes. Frozen nonzero and
zero-accessible mediators share the same threshold vector in this audit.

## Disposition

Threshold spectroscopy is a conditional origin probe. It can break the
local-versus-mediator kernel left by WP191 without requiring `epsilon=0`
control, but only if the threshold channel, energy coverage, and resolution are
independently typed. It must not be fitted as a projector from the desired
answer.

## Exact checker

- Checker: `checkers/wp192_mediator_threshold_origin_probe.py`
- Result: `results/wp192_mediator_threshold_origin_probe.json`

The checker compares threshold observation vectors for local, frozen mediator,
and zero-accessible mediator origins across resolved and unresolved energy
windows.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: origin probes may be intervention-based or
  threshold-based, but each needs independent instrument typing.

## Report to `marici.Nima`

- Admitted state domain: local constraint and mediator coupled origins.
- Faithful quotient coordinate: threshold observation vector.
- Source-authorized probe family: threshold spectroscopy if independently
  typed.
- Contextual partition: resolved threshold separates local from mediator class;
  mediator subtypes remain collapsed.
- Classification: conditional mediator-origin threshold probe.
- Smallest exact falsifier: unresolved energy window below threshold sees no
  difference.
- Remaining physical-instrument gate: derive threshold channel, coverage, and
  resolution from source dynamics and detector model.
