# Phase-retaining optical geometry with detector memory

## Candidate and scope

Constructed the versioned **`passive-port-fock-memory.v1`** candidate for the frozen cavity/detector pair. The [contract](contracts/physics-geometric-candidate.v1.json) supplies a common conditional mathematical state space, explicit target maps, operation lifts and a bounded routed comparison. The model-level geometric binding is accepted by `contracts/physics-interface-geometry-admission.v1.json`; its physical and native-source comparisons remain separate tasks.

The source is bosonic Fock space `F_s(C^10)` tensored with the ready/dead memory space `C^2`. States are trace-one positive trace-class operators with finite mean photon number. Hilbert and trace-norm topologies are declared; finite mean number is a separate domain restriction, not a consequence of trace-norm convergence.

This is a new candidate built from imported passive optical and CP-instrument theory. It has no supplied identification with native Bool, exchange or marked137. Its geometry and target interpretations are conditional constructions; independent source-law selection remains the next task.

## Ports, geometry and retained time order

Slot 0 is the returning cavity mode. Round k, for k=0,1,2, uses fresh slots `1+3k`, `2+3k`, `3+3k` for `(u,v2,w)`. After the complete four-port operation, those slots retain reflected, transmitted and environmental outputs, and slot 0 carries the next returning field. Unused future input modes are untouched.

The nominal four-port map is embedded into a ten-mode unitary `W_k`, with explicit output rewiring. Open-loop input preparation takes place in the initial fresh slots; no hidden state reset is introduced. Operation/occurrence histories remain separate from the final matrix.

The field geometry is `C^10` with real metric `Re(z* w)` and symplectic form `Im(z* w)` in declared normalization. Passive unitary maps preserve both. Time-bin and port labels specify constructor order; a physical clock, phase reference and energy scale remain calibration inputs. No spacetime or causal-field geometry is derived here.

## Cavity embedding and exact recovery

For complex port amplitudes z, use the normalized coherent state

`|z> = exp(-||z||²/2) sum_n z^n/(n!) e_n`,

where `e_n = product_j (a_j†)^n_j |vac>` and `n! = product_j n_j!`.

The passive lift is creation-operator substitution

`a_j† -> sum_i W_ij a_i†`,

with vacuum fixed. Hence `Gamma(W)|z> = |Wz>`, `E[a_j]=z_j`, and `E[N]=sum_j |z_j|²`. These are exact identities of the supplied bosonic model. Complete port retention therefore recovers the cavity amplitude and resource equations at their stated normalization.

The construction is coherent across compositions: substitution gives `Gamma(VW)=Gamma(V)Gamma(W)`. Each fixed-number sector is the symmetric tensor power of the one-particle unitary, so it is unitary; the Hilbert direct sum extends the map to Fock space. These are written algebraic arguments using the imported Fock construction, not a new kernel proof.

The executable checker uses the unnormalized creation basis. Its Gram matrix is diagonal with entries `n!`, not the identity. Exact checks cover sectors N=0,1,2 of dimensions 1,10,55, and two ordered round trips. A Euclidean metric on this occupation basis fails the two-photon test.

These finite-sector tests do not approximate a general coherent state. Coherent recovery above uses the analytic all-sector identity; no finite-cutoff error certificate is supplied.

## Detector inclusion and its domain

At a named port, embed Aspect's vacuum/one-photon times ready/dead instrument. Each of its seven Kraus operators acts locally and is tensored with identity on all spectator modes. In particular, a vacuum/no-click branch preserves superpositions among spectator modes. Assigning a different environment label to each spectator occupation would incorrectly destroy this coherence.

The instrument's exact domain is density support on `n_port<=1` before the event. Its Kraus sum is the identity on that domain. This condition is checked before applying an outcome map: an invalid input is rejected, not projected and renormalized.

A coherent state with nonzero detected amplitude has positive probability outside this domain:

`P(n_port>=2)=1-exp(-lambda)*(1+lambda)>0` for `lambda=|z_port|²>0`.

Weak illumination alone is therefore not an exact inclusion into the finite detector. An approximate inclusion needs a stated error bound and protocol; a larger counting instrument needs a versioned constructor.

## A composed comparison on the shared single-photon domain

Prepare

`psi=(4/5)|1_u0>+(3/5)|1_x>`

with memory ready and all remaining modes vacuum. This is a normalized one-photon state. Apply round 0, detect its transmitted slot 2, retain every outcome and memory branch, apply round 1 with its fresh vacuum inputs, and detect transmitted slot 5.

The exact joint record distribution is:

| Word | Probability |
|---|---:|
| CC | 0 |
| CN | 81/625 |
| NC | 104976/9765625 |
| NN | 8395024/9765625 |

The probabilities sum to one. Independently, the second transmitted wave coefficient is `(3/5)*(3/5)*(12/25)=108/625`, so the NC probability is `(9/25)*(108/625)^2`, agreeing with the full routed instrument calculation. The first click consumes the only photon and sets memory dead, giving zero CC.

This is a conditional source-operation/instrument comparison on a specified preparation. It does not equate one-photon and coherent preparations. In the one-photon state, every field mean `<a_j>` is zero even when its wavefunction coefficient is nonzero. Their coefficients transform by the same passive W, while their observation maps differ.

Relative phase is retained: replacing the initial plus by a minus preserves initial occupations but changes the reflected wave coefficient from zero to `-24/25`. The occupation-only quotient cannot support this cavity interference event.

## Verification and residuals

[Checker](checkers/check_physics_geometric_candidate.py), [result](results/physics-geometric-candidate-v1.json):

- 9378 exact factorial-metric entries across three rounds and sectors N=0,1,2;
- 66 composition-column comparisons;
- normalized two-step routed instrument distribution and independent amplitude route;
- preserved spectator coherence;
- rejection/detection of wrong metric, erased phase, reversed rounds, silent multiphoton projection and wave-coefficient/field-mean conflation.

```
python research/nima/checkers/check_physics_geometric_candidate.py
python research/aspect/scc/scc.py check physics-geometric-candidate-v1
```

Physical preparation/routing/calibration and comparison with native relational sources remain open. The candidate does provide an explicit mathematical object and maps for the next dynamics test: determine which assumptions select `Gamma(W)` and the detector update, and which alternative number/metric-preserving laws remain observationally indistinguishable on the tested sector.
