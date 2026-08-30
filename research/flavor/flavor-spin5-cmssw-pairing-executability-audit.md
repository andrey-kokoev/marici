# Spin(5) CMSSW pairing executability audit (WP903)

## Question

Does the existing CMS software stack instantiate the common-random-number
coupling assumed by WP902 when the scalar width is changed?

## Typed distinction

Five claims must not be conflated:

1. a job has a configured seed;
2. CMSSW can save and restore a module's random-engine state;
3. two jobs receive the same random sequence at each named module;
4. corresponding physical latent draws retain the same meaning after the
   width change;
5. the complete paired experiment emits stable event identifiers and a typed
   null when selection fails.

The CMS `RandomNumberGeneratorService` establishes a mechanism for claim 2.
Its replay documentation says that exact reproduction additionally requires
all random draws to use the service, event processing not to depend on prior
events, and the relevant calculation and products to remain reproducible. It
also warns that a changed logical decision can alter the number of draws and
throw subsequent draws out of synchronization. A different width can change
generator rejection and decay paths, so claims 3 and 4 do not follow from a
shared seed or restored engine state. WP905 corrects the original audit
boundary: semantic draw alignment is not required for a mathematically valid
coupling. A shared reproducible seed still defines a joint law if each arm has
the declared marginal. Desynchronization can destroy variance reduction
without destroying coupling validity.

Primary implementation evidence is the CMSSW
[`RandomNumberGeneratorService` documentation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDMRandomNumberGeneratorService),
the official
[`ConfigBuilder.py`](https://github.com/cms-sw/cmssw/blob/master/Configuration/Applications/python/ConfigBuilder.py)
restore-state wiring, and the official
[`testRandomService2_cfg.py`](https://github.com/cms-sw/cmssw-framework/blob/master/IOMC/RandomEngine/test/testRandomService2_cfg.py)
unit-test configuration. They demonstrate replay infrastructure, not a
cross-width physical coupling.

## Capability audit

| Capability | Present evidence | Status |
|---|---|---|
| module-labelled engine-state save and restore | CMSSW service and unit test | available |
| identical source latent uniforms across widths | no source wrapper or inverse-transform contract | absent |
| generator draw-call alignment across widths | no trace-equivalence certificate | absent |
| shower, pile-up, and detector replay | possible per unchanged module, not executed end to end here | unverified |
| stable pair identifier through the full chain | specified by WP902, no produced paired record | absent |
| seven-symbol output including selection null | analysis schema specified, no produced paired record | design only |
| independent seed families and pair-independence test | no generated ensemble | absent |
| calibrated two-pole acceptance floor | `389/14688` is only a pilot design value | absent |

The local environment has neither `cmsRun`, `cmsDriver.py`, a CMS container
runtime, Pythia, nor MadGraph. Thus no executable full-chain pairing test was
performed.

## Exact disposition

WP902 remains a correct statistical implication conditional on a coupling.
The current CMS evidence supplies replay infrastructure but no executed paired
sample. The smallest validity falsifier is instead a replay failure or an arm
whose shared-seed execution does not have its declared marginal. A branch that
changes later draw meanings is only a falsifier of semantic alignment and of
the hoped-for high agreement rate.

An admissible repair must freeze a source-level coupling independently of the
desired stability result, preferably by storing a typed base-event packet or
by an explicit latent-uniform transform. It must then record module engine
states, pair identifiers, all selection failures, software/container hashes,
and nuisance support through generator, shower, pile-up, detector simulation,
and reconstruction. A deterministic replay equality test must pass before the
55,712-pair WP902 budget has authority.

Until that constructor exists and executes, WP901's independent four-cell
test is the authorized fallback. Neither route is a flavor selector: both are
simulation instruments for checking detector-response stability.

Run:

~~~text
uv run python research/flavor/checkers/wp903_spin5_cmssw_pairing_executability_audit.py
~~~
