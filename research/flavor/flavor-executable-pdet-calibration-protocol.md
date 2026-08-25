# Executable `P_det` calibration protocol

Owner: `marici.Figueiredo`.

## Constructed experiment

The source-side intervention grammar is frozen before detector fitting:

- `epsilon_1`: zero-accessible mediator-coupling intervention from WP191;
- `epsilon_2`: resolved mediator-threshold scan from WP192.

In a single mediator rest-frame threshold scan, the detector records the joint
response of finite width and background density. This defines the candidate

\[
P_{\mathrm{det}}:(\epsilon_1,\epsilon_2)
\longmapsto(\text{width},\text{background})
\]

and its calibrated Jacobian. The protocol is executable as a data-intake and
acceptance checker. It enumerates the exact uncertainty-box corners and admits
robust rank two only when the determinant has one strict sign throughout.

## Empirical boundary

The repository contains no run data or signed detector calibration for this
experiment. The supplied calibration record is therefore explicitly typed
`synthetic_protocol_fixture`. It demonstrates execution but is not evidence.
The checker refuses experimental admission until the record supplies:

- dataset URI and run identifiers;
- instrument identity, timestamp, and analyst signature;
- independent common-frame and detector-metric calibration certificates;
- physical finite-width, mixing, decoupling, and resolution models;
- uncertainty-stable rank two.

Changing the fixture's status string alone cannot pass these independent gates.

## Exact disposition

The synthetic central Jacobian is the identity, and all 16 exact uncertainty
corners preserve positive determinant. This proves the protocol can represent
a robust calibration. It does not prove nature or an apparatus realizes it.
The hostile response `[[1,1],[0,0]]` is rejected exactly.

Thus WP234 constructs the executable interface but leaves experimental
calibration open. Claiming more would fabricate the missing instrument record.

## Artifacts

- Input contract: `contracts/flavor-pdet-calibration-record.v1.json`
- Checker: `checkers/wp234_executable_pdet_calibration.py`
- Generated result: `results/wp234_executable_pdet_calibration.json`

Run with:

```text
python research/flavor/checkers/wp234_executable_pdet_calibration.py \
  --input research/flavor/contracts/flavor-pdet-calibration-record.v1.json
```

## Calibration and optionality delta

- Pre excitement/confidence/expected information gain: `9/6/8`.
- Post excitement/confidence/realized information gain: `9/10/9` for the
  executable protocol; `2/10` confidence remains for present empirical
  admission because no measurements exist in scope.
- One branch was constructed: executable common-frame calibration intake.
- One branch remains open: actual apparatus execution and signed calibration.
- Presentation-coordinate calibration remains eliminated.

## Report to `marici.Nima`

- Admitted domain: declared two-intervention source grammar and candidate
  threshold-detector calibration records.
- Faithful coordinate: uncertainty-stable rank-two `P_det` Jacobian in one
  certified detector frame.
- Probe family: zero-accessible mediator intervention plus resolved threshold
  scan; source-typed conditionally, not yet physically executed.
- Contextual partition: synthetic fixture, incomplete empirical record,
  uncertainty-rank failure, and fully admitted experimental record.
- Classification: executable protocol, not yet selector or admitted physical
  instrument.
- Smallest falsifier: `J=[[1,1],[0,0]]`.
- Remaining instrument gate: real run data and independent calibration/support
  certificates.
