# Signed-certificate availability is a causal observer obligation

## Result

The resolved Grothendieck signed-pairing certificate can be placed in an exact finite observer schedule without introducing a common commit boundary.

The test uses the already generated frozen source-task artifacts, not a new source experiment:

- the unchanged raw source-task intervals;
- the unchanged source family and prior;
- the signed-pairing calibration that resolves the former middle gate;
- the existing exact source-task checker.

For the `lower_threshold` and `upper_threshold` frozen worlds, the signed calibration respectively returns `CERTIFIED_FEASIBLE` and `CERTIFIED_INFEASIBLE`. The earlier theta-only calibration remains `UNRESOLVED` for each. Thus the signed certificate is genuinely decision-relevant information, not merely a duplicate display of an already local conclusion.

## Schedule

Observer A completes the common coarse record—vacuum and crossed rows—at time one. The distinguishing positive source row is retained by B in its full frozen-task package. B validates and issues the hash-bound signed-pairing task certificate at time four.

With one unit B-to-A delivery:

- B certifies at four;
- A validates the same certificate at five;
- both meet the deadline five;
- neither waits for an acknowledgement or simultaneous readiness.

A scheduled fixed commit at five also succeeds. The result does **not** claim that all commit protocols fail. A particular mutual-ready acknowledgement convention would complete at eight in this schedule, but that is only a property of that convention.

## Why the delayed case is an impossibility, not a failed heuristic

With B-to-A delay six, B still has and issues its certificate at four, while A receives it only at ten. Through deadline five, A receives precisely the same coarse transcript in the lower and upper frozen worlds:

    vacuum = 1/100,
    crossed = 0.

The omitted positive row differs. The correct definite outputs are opposite: feasible in one world and infeasible in the other. Therefore no causal rule using A's deadline transcript can issue a sound definite answer in both worlds. Abstention is the only safe behavior for A under this information contract.

A shared clock, a commit marker, or an acknowledgement cannot recover the missing positive row or its signed-pairing consequence. Faster delivery, a direct delivery of that row/certificate, a later deadline, or an explicitly changed task contract can.

## Scope

This is a conditional reliable-message schedule over mathematical artifacts. It establishes neither a physical acquisition time nor the physical occurrence of any synthetic source task. It does not cover message loss, Byzantine parties, consensus, irreversible simultaneous action, or arbitrary source families.

It also does not transfer the word-cut reversal theorem to the assembled noncommutative observer. The result instead supplies the immediately useful causal interface: a local decision is justified only after the observer possesses a compatible evidence package and the calibration certificate on which its task proof depends.

## Verification

    uv run --with python-flint python research/voevodsky/checkers/check_signed_certificate_deadline.py

Artifact:

- `research/voevodsky/results/signed-certificate-deadline.json`

The checker hash-binds the calibration, frozen inputs, refinement report and two portable signed-pairing chains; replays both task outcomes; verifies the theta-only unresolved baseline; and checks exact equality of A's delayed transcripts.
