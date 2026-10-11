# Gram interference and Bell readout: source-bound comparison

## Frozen explanatory question

Do the legacy interference/Bell evidence paths actually test their declared
source-to-readout maps, or do their successful-looking outputs insert a
normalization, state or probability rule independently of the computed Gram?

Active SCC obligation: forward realization and typed state/effect comparison,
then readout dependence. Preserve the ENTIRE five-filler implementation:
ordered Bool-pair input labels, its explicit integer output encoding, all five
four-component vectors, their pairing and phases. Do not replace it by two
abstract amplitudes. Preserve the Bell script's actual four-by-four states,
analyzers and printed formulas too.

**Conjecture:** the interference formula is a valid conditional quadratic norm,
but its recorded pair expectations differ by a factor of two and are not checked.
The Bell script's correct Bell value is disconnected from its constructed state;
its product-state correlation is wrong. These defects do not defeat the richer
existing state/effect and sequential-instrument constructions.

**Strongest predecessors:** reuse Aspect's complete
`check_combined_bell_instrument.py`, not just a static correlation table. Its
joint continuations, trace map, no-signalling and sequential tests already
exist. Retain the external photon Bell source packet and the completed
conjugate-doubling/record-descent distinctions. No new Born-rule framework is
needed; those positive conditional results and negative boundaries stay closed.
The full filler functions also retain their permutation actions, not merely
their image-vector encoding. A source-preservation control compares the actual
twist action with the already implemented X-projector continuation; a failure
of one marker-preparation family must not become a failure of that richer route.

**Rivals:** the old numerical outputs already depend on the stated sources;
a rescaled raw norm is already a normalized detector probability; a Gram of
rank greater than one is outside quantum mechanics; the original Bell value
proves a source-selected state and probability law; the legacy defects show
that no conditional quantum comparison is available.

**Risky tests and closure:** replay complete legacy computations without old
receipt writes, expose the unchecked normalization residual, and change the
constructed Bell state while retaining the old readout. Construct a balanced
path/record comparison using all five original vectors and distinguish its raw
norm, click probability and conditioned record state. Compare the latter with
the existing instrument, transporting the Bell/singlet convention explicitly.
A state-sensitive repair must return the correct product-state correlations,
retain the Bell result, and distinguish a separable mixture from a single tensor
product. Test whether the fixed equal-path phase family actually supplies the
Bell state used by the legacy script rather than quietly granting arbitrary
amplitude control.

**Boundary:** complex linear preparation, trace/Born pairing, local analyzers
and a physical record assignment are supplied by the conditional quantum
protocol, not inferred from Gram factorization. Ordered Bool labels retain a
mathematical two-factor structure; they do not supply two laboratory wings.
No experiment, general quantum no-go, continuum limit or interpretation of
measurement is inferred. A changed preparation law is a new question, not a
retry of this one.

## Reproduced evidence defects

Both complete legacy programs were replayed with their receipt deletion/write
operations suppressed. All ten zero-phase pair rows disagree with their own
recorded expected values; none was asserted. For the identity/swap pair,
gamma=13/14. The raw norm is 27/7, while the old row says 27/14.

The Bell code constructs a four-by-four state but calculates its correlations
from a state-independent cosine formula. Replacing its constructed Bell matrix
by its constructed product matrix leaves its reported S unchanged. Its separate
product-state function returns 1 at every setting, including two X analyzers
on |00>, where the correct correlation is zero. These are dependency and
normalization defects, not failures of the Bell-state theorem.

## Full-vector norm versus a detector probability

Retain the five normalized record columns v_i in V, using the exact old integer
encoding and Euclidean pairing. V is four-by-five, has rank four, and
G=V-dagger V. We use G_ij=v_i-dagger v_j consistently; the old reversed bra/ket
notation is indistinguishable on real fixtures but not on complex ones.
An exact complex control checks that variance rather than silently swapping it.

For q_i=exp(i theta_i), the old quadratic expression is

\[
I=q^\dagger Gq=\left\|\sum_i q_i v_i\right\|^2.
\]

It is a valid coherent norm conditional on the declared linearization. Writing
it as a Gram form does not remove its equivalence to an amplitude sum or derive
a probability interpretation. The old V-squared+D-squared identity remains an
algebraic identity under its definition of D, not an independent measurement
test of distinguishability.

A typed conditional realization keeps an orthogonal path register:

\[
W|i\rangle=|i\rangle\otimes v_i,\qquad W^\dagger W=I_5.
\]

Prepare the normalized path vector q/sqrt(5), and choose the balanced path port
K=(1,1,1,1,1)/sqrt(5) tensor I4. Its effect K-dagger K and its complement are
orthogonal projectors summing to the identity. The selected record amplitude
is Vq/5, so the GIVEN Born trace rule gives p_click=I/25. For two paths the
corresponding factors are:

| Quantity at the identity/swap zero-phase fixture | Value |
|---|---:|
| Raw norm | 27/7 |
| Norm after dividing the coefficient vector by sqrt(2) | 27/14 |
| Balanced-port click probability | 27/28 |

The middle number is still greater than one. Correcting a factor of two is
not sufficient to turn an unnormalized intensity into a probability.

At zero phase, all five paths give p_click=118/175. Tracing out the records
instead gives the rank-four path density G-transpose/5. It is positive,
trace-one and obeys the same Born state/effect rule. Conditioning the selected
record yields a rank-one density. Thus Gram rank, reduced-state rank and
conditioned-state rank are different quantities: quantum mechanics is NOT
restricted to rank-one kernels, and higher-rank quantum states do not require
a new theory beyond the Born rule.

## Reuse the full existing instrument, not a cosine table

The repaired `check_entanglement.py` evaluates each joint probability as the
trace of its ACTUAL joint continuation. That whole continuation, not just its
trace, agrees with Aspect's existing exact Q(sqrt(2)) implementation for the
Bell state, |00>, |01>, a classical mixture, and the five-filler conditioned
record. All four setting contexts and their four joint records per state are retained.

The predecessor's singlet convention is transported explicitly: I tensor
[[0,-1],[1,0]] sends Phi+ to the singlet, and the Bob analyzers are transported
with it. Dropping the analyzer transport would compare different experiments.
Its original no-signalling, deterministic-local-strategy and Z-Z versus Z-X-Z
continuation tests are rerun unchanged without touching its receipt.

For the original fixed CHSH analyzers, the corrected values are:

| Supplied density | CHSH S |
|---|---:|
| \(\Phi^+\) | \(2\sqrt{2}\) |
| \(\lvert00\rangle\) | \(\sqrt{2}\) |
| \(\lvert01\rangle\) (the original constructed product matrix) | \(-\sqrt{2}\) |
| \((\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert)/2\) | \(\sqrt{2}\) |

The last state is separable by its explicit convex decomposition but is NOT
a single tensor product. This repairs the old mixed-state conflation of
nonproduct form with entanglement. The Bell state's negative partial-transpose
eigenvalue and its conditional CHSH violation survive.

The external `photon-bell-source-packet.md` computation also survives in full.
The older `born-readout-variance-obstruction.md` and Aspect's already completed
pairing-versus-record-descent distinction remain boundaries, not open problems
to solve again by refactoring a norm. In particular, compatible state/effect
probabilities still do not establish a physical record map.

## Preserve the stronger route on the SAME filler source

The original twist FUNCTION is more than its encoded vector: after the already
declared C4 linearization its permutation action is CNOT on the ordered Bool
pair. Apply the existing Alice X+ instrument to |00>, condition on its
probability-1/2 branch, then apply that actual twist action. The resulting
state is exactly Phi+. This supplies a positive source/instrument comparison
without changing a filler, fitting amplitudes or inventing a preparation law.
The X-projector instrument and trace rule are existing conditional inputs,
not physical laws derived from the Boolean function.

Consequently the source is not deprived of conditional Bell preparation. The
next, narrower obstruction concerns ONLY the old image-vector encoding with
five equal-amplitude paths and phase control, not this richer action route.

## Exact boundary of the fixed equal-path marker preparation

For that marker route, its conditioned zero-phase state has
S=48 sqrt(2)/59, not the Bell-script value. No choice of its five phase factors
z_i, each of modulus one, produces Phi+ at the balanced port.

This is an all-phase certificate, not a grid search. Requiring the actual raw
synthesis V_raw z to be proportional to (1,0,0,1) gives three linear conditions:
its second and third components vanish and the last equals the first. A linear
combination of these conditions gives

\[
z_2+2z_3+3z_4=0.
\]

Equality in the triangle inequality forces z_2=z_3=-z_4. Substitution into the
other two equations then gives z_0=z_1=2z_4/3, contradicting unit modulus.
The opposite extremal CHSH eigenvector, the singlet, requires a zero first
component, but that component is 2z_3+3z_4 and has magnitude at least one.
These are the unique positive/negative extremal eigenspaces of the specified
CHSH operator. Thus this particular phase-only marker route cannot saturate
the bound in either sign with THESE analyzers.

Its success denominator does not hide a zero-state exception: the raw synthesis
has rank four and kernel generated by (3,-4,0,3,-2), which contains no vector
with all components of unit modulus. This comparison does not exclude
nonmaximal violations, other analyzers, different amplitude controls or the
explicit successful twist/instrument route above.

## Disposition and stopping boundary

**Constructed:** a comparison from the complete encoded filler family to a
conditional instrument readout, and a stronger conditional Bell preparation
using the actual filler action. **Repaired:** unchecked normalization, disconnected
state/readout data, product-state correlations and the separable-mixture error.
**Not derived:** the physical preparation, Born pairing or detector-record law
from Gram rank. The earlier source/probe and physical-selection closures are
unchanged. Repeating compatible Grams or scanning more phases cannot supply
those missing laws or evade the fixed marker-family obstruction.

The two live checkers now enforce their claims with exact arithmetic and write
NEW repaired receipts, never overwriting the two historical paths. False pair
expectations and invalid densities are rejected; changing the state changes the
computed correlations. Seven original inputs are byte-preserved in
`quarantine/20261007-quantum-readout-evidence/SHA256SUMS`. The two old receipts
were absent. Index, compendium, session and admission-request entry points
visibly supersede the unsupported probability/quantum-completion claims.

## Verification

Complete legacy replay: `checkers/collect_quantum_readout_diagnostics.py`, SciPy
profile, execution `e_38524_1791402418041543600_75`.
Exact consumer: `checkers/check_gram_bell_readout_comparison.py`, SymPy profile.
The initial comparison passed against freeze `e2d9933455139d64`; the stronger
same-source twist-action control was then added without changing its predicates.
Current freeze: `scc-freezes/nima-gram-bell-readout-comparison.d259c9d025783542.json`.
Challenge `e_38524_1791403442875251900_79` passes. Results are in
`results/gram-bell-readout-comparison.json` and `results/quantum-readout-transport.json`.
The external instrument/photon/record-map sources were run with their sole
receipt writes suppressed; their original assertions were not removed.

Fresh owner-model check `e_38524_1791404459056726200_84` passes:

```text
uv run --with sympy python research/aspect/scc/scc.py check nima-gram-bell-readout-comparison
```

Two preceding `scc.py run` invocations addressed the central check registry,
not the owner-model interface, and were rejected before executing a checker.
No scientific predicate was changed in response. Both repaired standalone
entry points also pass (`e_38524_1791403823604351200_80` and
`e_38524_1791403826228468100_81`).
