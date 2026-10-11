# Both storage routes advanced: interaction complexity versus battery shaping

## A. Changed error-sector hold: exact interaction audit

The recovery-frame construction is error transparent, but what operator would
have to be implemented? Expand its actual physical X_ET, Y_ET and Z_ET in the
Pauli basis of the owning five-qubit code.

For a signed logical/stabilizer coset term P of weight w, the coefficient is

    (1/16)*sum_(correctable E) sign(E,P) = 1-w/4.

Each extended logical operator has ten weight-three terms with relative
coefficient 1/4 and six weight-five terms with coefficient -1/4. These signed
coset coefficients include the owning logical and stabilizer phases.
All sixteen correctable error-sector responses equal one exactly.

The pair pulse Q_ET consequently has **769 Pauli terms**:

| Physical body weight | Terms |
|---:|---:|
| 0 | 1 |
| 6 | 300 |
| 8 | 360 |
| 10 | 108 |

The identity coefficient is 1/4; every other term has magnitude 1/64. The hold
extension has one identity term, twenty weight-three terms and twelve weight-five
terms.

Pauli-basis uniqueness rules out implementing this exact operator directly with
only one- and two-body terms on those same qubits. This does not exclude an
ancillary mediator, an approximate gadget or a different encoding.

A favorable truncation control retains only the weight-three component terms
and rescales them to preserve the correct on-code action. It fails transparency
in **all fifteen nonzero single-error sectors** for each logical operator. An
explicit first response is 1/5 instead of one. Matching the clean code is not
enough to justify dropping the higher-body terms.

**Branch A now has a concrete implementation target and a verified simplification
failure**, rather than an unspecified claim that the direct Hamiltonian is hard.
No microscopic coupling providing these terms has been admitted.

## B. Unchanged hold: optimize the finite ready packet

The uniform work packet was not optimal for the tested midpoint-fault transfer.
For amplitudes a_k on the same M interior work levels,

    F_mid = (1 + Re(sum conjugate(a_k)*a_(k+1))/sum |a_k|^2)/2.

The path adjacency matrix with off-diagonal entries 1/2 has eigenvalues
cos(j*pi/(M+1)). Its largest eigenvector is the sine profile, so

    a_k proportional to sin(k*pi/(M+1)),
    F_mid,opt = (1+cos(pi/(M+1)))/2.

The checker verifies the sine eigenvector recurrences, distinct eigenvalues,
normalizations and actual pulse outputs using the existing exact cyclotomic
arithmetic. The ordering of the real eigenvalues supplies the variational proof.
This is optimal only for this specified midpoint-input objective at fixed M.

Both packets use the same ladder size, maximum ready energy and mean ready
energy (M+1)/4, because both profiles are symmetric about the ladder midpoint.
No energy gap or measured particle value is fitted.

| M | Uniform midpoint fidelity | Sine midpoint fidelity |
|---:|---:|---:|
| 1 | 0.5 | 0.5 |
| 2 | 0.75 | 0.75 |
| 4 | 0.875 | 0.90450850 |
| 8 | 0.9375 | 0.96984631 |
| 16 | 0.96875 | 0.99148655 |

Decimal entries are illustrations of the exact cyclotomic results. Preparation
of the sine profile is still an explicit coherent resource, not free apparatus.

## Other-input and free-phase controls

Optimization does not imply uniform improvement over every fault history. At
M=4, the preexisting-fault even-superposition fidelity **decreases** from 0.75
to 0.72360680 with the sine profile. At M=16 it increases from 0.9375 to
0.96822223. A worst-case or channel-wide objective has not been optimized here.

The prior packet formulas describe the pulse benchmark. This audit additionally
includes the free hold/work phases for a declared total duration 8*pi and pulse
strength 1/8, with the fault halfway through. Quarter-integer energies make each
half-step's free phases exact signs; the complete result differs from the pulse
benchmark only by a common sign for the tested midpoint input. The displayed
fidelities therefore also hold for that explicit full schedule.

This commensurate schedule is not a source-derived physical clock. Arbitrary
fault times, phase-reference drift and the work of the actual fault/recovery
interaction remain additional tests. Conservation of pulse energy does not
supply a microscopic bath model.

## Verification and comparison

    python research/voevodsky/checkers/check_storage_branch_comparison.py

Fresh final execution passed. Receipt: `results/storage_branch_comparison.json`.
It binds both preceding branch receipts and the owning code, records exact
coefficients, the truncation witnesses and both packet objectives.

The branches now expose different concrete resource demands:

- **Changed hold:** exact logical protection, but a large, explicit many-body
  interaction and a new physical energy assignment off the code.
- **Finite work battery:** unchanged old hold and improved finite-resource
  fidelity, but state preparation, residual logical/work correlations and
  objective-dependent performance.

Neither branch is promoted to a local autonomous device, a physical noise
threshold, a mass prediction or an isotope-stability explanation.
