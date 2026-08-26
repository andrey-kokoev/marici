# Cross-run optical witness-splicing test

## Result

An exact two-clock hostile passes every marginal validation while supporting a false source claim. It is rejected only by requiring the source certificate, optical record, calibration, decoder, and claim to admit one common execution, with either a common frame or a certified coherent frame transport.

This establishes a required composition invariant and falsification test. It does not establish that Marici lacks such a composition or needs a new primitive.

## Source and typed ports

The packet contains five independently well-formed objects:

- a source-band certificate claiming source 1 in run `e1`;
- the ordered optical record ((1,2)) captured in run `e2` at epoch 0;
- a valid epoch-1 calibration with modulo-5 phase displacement 1;
- the corresponding epoch-1 decoder;
- an authorized band-scoped claim for source 1.

Every value, residue, decoder version, and claim scope is locally valid.

## Constructor order and calibration frame

The physical record came from source 17 at epoch 0:

\[
d_0(1,2)=17.
\]

The spliced epoch-1 decoder instead computes

\[
d_1(1,2)=1.
\]

The latter calculation is mathematically correct in its own frame. It is not applicable to the record from run `e2`. Marginal validity therefore cannot substitute for the joint constructor.

## Joint witness

A valid measurement claim requires one common solution for:

\[
(\text{run id},\text{epoch},\text{port binding},\text{decoder version},\text{source claim}).
\]

The spliced packet contains run identifiers `e1` and `e2` and epochs 0 and 1, with no transport witness, so no such joint realization exists. An honest epoch-0 packet for source 17 passes both all marginal checks and the joint check.

A same-run epoch change is not rejected merely because its epoch labels differ. For a certified phase displacement \(\delta\), the record transport

\[
T_\delta(a,b)=(a,b-\delta\bmod5)
\]

maps the shifted record \((1,2)\) to \((1,1)\) in the epoch-0 frame. A packet carrying this source-derived transport passes the corrected joint check. Literal epoch equality is therefore sufficient but not necessary.

## Conserved information and detector kernel

Each local validator preserves only its own schema and relation. None sees the cross-object execution fiber. Even claimant authorization does not repair the missing physical join. The joint validator retains the correlations erased by marginal projection.

## Smallest hostile

Reuse the ambiguous record ((1,2)), keep every witness individually valid, and replace only its execution/frame incidence by evidence from another run. A system validating fields independently emits source 1 although the sampled source was 17.

## Prospective explanatory role

This is a constructor-level prediction: any adequate composition must reject witness splicing even though every marginal is valid. The test was frozen before inspecting a candidate Marici encoding. If an existing composition already enforces the common joint witness, the test passes and no architectural gap follows.

## Completion and authority boundary

The finite test does not claim a new Marici primitive, universal evidence model, physical band certificate, or stochastic clock theorem. It supplies one exact hostile against which existing compositions can be audited.

## Reproduction

Run:

    python research/aspect/checkers/cross_run_optical_witness_splicing.py
