# Proton/electron ratio: shared-state comparison hypothesis

## Proposed construction

The operator proposes interpreting 12^2+3^2 as a comparison of two full four-state carriers, each with twelve directed nonidentity relationships, relative to one identified shared state. The full carrier is called T0 in this proposal; this use refers to its available relational structure before fixing a relationship reference. It requires reconciliation with the earlier convention in which T0 retains identities and T1 witnessed relationships.

Let E_A and E_B each be the twelve ordered pairs of distinct carrier points. Let S_A and S_B each be the three state alternatives remaining after fixing the shared reference state. The comparison domain is the disjoint union

    D = (E_A x E_B) disjoint-union (S_A x S_B),
    |D| = 144 + 9 = 153.

The shared-state identification is input to this count. The nine slots test compatibility relative to it; counting alone does not establish that the identification is valid. Arrow pairs are comparison slots; composability and endpoint matching require additional comparison maps.

## Meaning of the outer twelve

A precise candidate for 12*153 is a family of one D-comparison for each outer directed relationship e in a carrier:

    F = disjoint-union over e in E of D_e,
    |F| = 12*153 = 1836.

This counts labelled comparison instances. They need not be dynamically independent. The mass interpretation would require an energy observable summing their contributions and a carrier identification of the proton with that full response and the electron with the normalization unit. The inspected sources do not construct these identifications.

## Symmetry test

S4 is transitive on all twelve directed relationships before a reference is fixed. Fixing a shared state reduces the symmetry to S3 and splits those relationships into three orbits:

- three directed outward from the reference;
- three directed inward to the reference;
- six directed between the other states.

For equal inner-slot normalization but outer weights w_out,w_in,w_internal, the total is

    153*(3*w_out + 3*w_in + 6*w_internal).

Unit weights yield 1836. Rooted symmetry alone allows different weights for the three orbits. Reversal symmetry could identify incoming and outgoing weights, while the internal orbit remains separate. A construction that moves the reference together with each relationship could have another orbit structure; it would need an explicit reference-selection rule.

## Source audit

research/nima/checkers/check_proton_electron.py computes 12*(12^2+3^2), identifying three with the miscounted SU(2) matter trace. It then calculates electron mass by dividing an observed proton mass by the proposed ratio. This supplies a numerical comparison, not independent particle energies.

research/nima/baryonic-matter-bridge.md uses the incorrect natural S4 permutation split 1+sign+2 already audited in the weak-angle work. It does not construct a proton bound state or its energy. Its particle assignments therefore cannot provide the missing mass interpretation for the new count.

## Direct Gram-energy test

Use the existing Gram with diagonal 12 and offdiagonal 1 as a positive metric. Represent a directed relationship i->j by e_j-e_i, and a state by e_i. Every relationship then has squared norm 12+12-2=22, including each of the three rooted edge orbits. Every state has squared norm 12.

This explicit energy choice gives equal outer-edge weights while retaining the original full-carrier metric. Fixing a reference does not itself require changing that metric. Thus the outer factor twelve has a concrete conditional support in this realization.

For tensor-product comparison slots, arrow-arrow squared norm is 22^2=484 and state-state squared norm is 12^2=144. Their total is 144*484+9*144=70992. Including the twelve outer arrows and dividing by the energy of one outer-arrow/arrow-pair channel gives

    12*(144+9*(12/22)^2) = 212976/121 = 1760.132231404959.

This conditional energy ratio differs from the slot count 1836. Separately normalizing every arrow and state primitive to unit norm restores 1836 by construction. Equivalently, raw state-pair energy needs relative multiplier 121/36 to match raw arrow-pair energy. A physical normalization rule would have to select that treatment. The denominator channel used here is an explicit reference choice, with no independently established electron identification.

There is also a coherent/incoherent distinction: opposite directed arrows become opposite vectors, and the coherent sum of all twelve vectors is zero. Their summed squared norms equal 264. The twelvefold energy interpretation therefore uses a sum over labelled channels (or another dynamics suppressing interference), not the squared norm of their coherent sum. Directed labels remain distinct in the bookkeeping even when their feature vectors differ only by sign.

Outcome: the Gram metric supports equal weights for the twelve outer relationships in this realization. It gives unequal weights for the two inner comparison blocks. The unweighted1836 mass hypothesis needs both a channel-sum rule and a relative block-normalization rule, in addition to proton/electron identification.

Exact checker: research/nima/checkers/check_proton_electron_gram_energy.py verifies all norms, totals, and the coherent cancellation with rational arithmetic.

## Path-resource correction to the displacement model

The operator specifies that arrows are traversed paths: reversing a path does not refund its traversal resource. The earlier vector displacement test loses this retained history. For path resources use C(p followed by q)=C(p)+C(q), with positive costs for nonempty traversals. A closed path may have zero endpoint displacement while retaining positive total resource. The vector cancellation result therefore does not evaluate the intended path-resource model.

The 1836-slot family can serve as the nominal unit-resource comparison programme. To interpret an excess over 1836, specify additional traversals or variation in traversal resource relative to an independently defined electron resource. A fractional mass-ratio excess does not require fractional path counts.

## First positive-resource closure trial

Declare three independent uniform routing selections: one outer relationship among 12, one arrow-comparison slot among 144, and one state-comparison slot among 9. One designated triple returns to its reference. There are 15552 labelled routing triples and the return fraction is p=1/15552. This is an explicitly chosen uniform-routing trial; the carrier has not selected its transitions or return set.

Let each of the 1836 base unit-resource channels repeat with this return probability, unchanged on subsequent rounds. Its expected resource obeys C_p=1836+p*C_p. With an uncorrected unit electron reference:

    m_p/m_e = 1836/(1-p) = 1836.118063147065.

The first repeated-channel contribution is 1836/15552=17/144=0.118055555556. Further returns add about 0.000007591509. The trial undershoots the rounded observed ratio 1836.152673 by 0.034609852936.

The stages above are routing-selection conditions, not an accounting of extra physical routing traversals. If implementing those selections requires additional paths, their positive resource must also be added. The expected value additionally assumes an ensemble or repeated-run interpretation; it does not explain a stable rest mass without a dynamical identification.

With electron return fraction p_e and proton return fraction p_p, the same renewal ansatz gives

    m_p/m_e = 1836*(1-p_e)/(1-p_p).

Equal return fractions cancel in the ratio. Positive electron closure at fixed p_p lowers the ratio further. Thus electron overhead alone cannot repair this trial's shortfall. For diagnosis, with p_e=0 the rounded target would require p_p about 0.0000831483145411; the trial uses about 0.0000643004115226. No coefficient is changed to that fitted value.

Outcome: an explicit positive path-resource model gives a tail of 0.118063. It fails the 0.152673 target. Its return set, transition weights, any separate routing-path costs, and electron resource remain to be supplied by actual carrier dynamics. The arithmetic and renewal identities are verified by research/nima/checkers/check_proton_electron_path_closure.py using exact fractions and full enumeration of the routing triples.

## Composable paths on the actual four-state graph

A topology-based test replaces the invented three-stage return selector with paths on the complete directed four-state graph without self edges. Root the graph at the shared state. Each step has three possible outgoing edges; each traversal has unit resource. Uniform choice among outgoing edges is an explicit dynamical assumption, while composability and return endpoints are enforced by the graph.

For paths of length n starting at the root, total paths number 3^n. Closed paths number [3^n+3*(-1)^n]/4. First-return paths for n>=2 number 3*2^(n-2), since the first departure has three choices, each intermediate nonroot step has two choices, and the final edge to the root is fixed. Their first-return probabilities are (1/3)*(2/3)^(n-2).

| Length | First-return paths | First-return probability | Resource per path |
|---:|---:|---:|---:|
| 2 | 3 | 1/3 | 2 |
| 3 | 6 | 2/9 | 3 |
| 4 | 12 | 4/27 | 4 |
| 5 | 24 | 8/81 | 5 |
| 6 | 48 | 16/243 | 6 |

After departure, the expected remaining resource h satisfies h=1+(2/3)h, hence h=3. The complete first-return cycle has expected resource 4. Return occurs with probability one. Opposite-edge traversal has positive resource throughout.

Outcome: the actual carrier graph has abundant short closure paths. It does not supply the earlier 1/15552 rare-return selector or the empirical required renewal fraction. In the graph model ordinary closure is part of executing a comparison. A small mass tail would have to concern exceptional extra work beyond that baseline, or a separately defined relative resource weighting. To compute it, the comparison protocol must identify which completed paths count as baseline, which leave a failed compatibility check requiring another traversal, and how the proton and electron protocols differ.

The graph alone contains no failure predicate or particle-specific programme. Introducing one is additional physical input. Uniform random walk return is not equivalent to comparison failure. This test therefore replaces a guessed routing interpretation with exact topology, without producing a mass prediction.

Checker: research/nima/checkers/check_four_state_return_paths.py enumerates composable paths through length six and checks the first-return counts and expected-resource equation. It writes no artifacts.

## Pairwise disturbance-settling prototype

The operator proposes that the fractional tail represents additional work settling pairwise disturbances created by the nominal comparisons. Test this mechanism with an explicit provisional update rule: on the three nonreference state values, comparison of i and j replaces both by their mean. Hold the shared fourth state fixed. Every comparison attempt consumes one unit of resource, even if its update is zero.

Starting from (1,0,0), comparing pair01 gives (1/2,1/2,0). Comparing pair12 next gives (1/2,1/4,1/4), reopening the first agreement by 1/4. Thus sequential pairwise updates can generate precisely the settling problem proposed.

Under the repeated schedule (01,12,20), absolute spread falls below 1/10 after four attempts, 1/100 after seven, and 1/1000 after ten. Exact consensus cannot occur after any finite sequence of these averaging updates from this input: all coordinates remain dyadic rationals, while conservation of their sum requires consensus value 1/3. Repeated complete cyclic averaging converges to that consensus, with indefinitely many positive-cost attempts for exact settling.

There are distinct possible resource observables. Let E=sum_i(x_i-mean(x))^2. Each update reduces E by (x_i-x_j)^2/2. The cumulative decrease tends to the initial E=2/3, while the count of unit-cost traversals diverges if exact consensus is required. The finite quadratic budget measures dissipated disagreement under the chosen model, not the whole traversal resource. Doubling initial disturbance multiplies this budget by four.

Outcome: an explicit update rule demonstrates pairwise disturbance and settling. It yields no universal 0.152673 correction: traversal resource depends on stopping precision and schedule, and quadratic disagreement resource depends on initial disturbance. A carrier mass interpretation needs its own update rule, initial disturbance created by the 1836-slot programme, stopping or steady-state condition, and electron reference normalization. The averaging example is a mechanism test, not the carrier's selected dynamics.

Exact checker: research/nima/checkers/check_pairwise_comparison_settling.py verifies reopening, nonnegative disagreement reduction, conservation, telescoping resource accounting, and dyadic coordinates over sixty scheduled updates. No target mass is used.

## Full 1836-attempt programme

Extend the mechanism test to the complete counted domain. Two four-state carriers share pinned state0, leaving six rational state potentials. Each arrow value is its directed endpoint potential difference. Comparing two arrows imposes equality of their values; comparing remaining states imposes equality of their potentials. Each update is Euclidean orthogonal projection onto that comparison's equality constraint. Every attempt costs one traversal-resource unit, including zero updates and reversed-arrow comparisons.

The programme visits all 144 arrow-pair constraints and nine state-pair constraints, then repeats this sweep once per outer directed label, for 1836 paid attempts. Repetition without an outer-label-dependent update is an explicit prototype choice; a physical programme must specify that dependence if present. These scalar potentials carry comparison data; the labelled traversal resource is kept separately so displacement cancellation never refunds work.

Exact results:

- compatible zero input: 1836 paid attempts, zero final defect;
- one unit initial potential on carrier A: 1668 immediately preceding agreements reopened during the forward programme; final summed-square defect has log10 value -60.918234;
- reversed comparison order: 1664 immediately preceding agreements reopened; final summed-square defect has log10 value -60.127874;
- doubling the input doubles the final residual vector and multiplies its squared defect by four.

Each step exactly enforces its own equality and decreases potential norm by the squared comparison discrepancy divided by the constraint-vector norm squared. The accumulated decreases telescope, while paid attempt count remains 1836. These two resource/readout quantities remain distinct.

Outcome: the full comparison programme exhibits pairwise disturbance with retained positive traversal cost. It does not select a universal post-programme residue. The residual varies with input and order. Compatible inputs produce no disturbance under this equality-enforcing rule. A nonzero reproducible tail therefore requires carrier-selected initial data, a comparison back-action/source term, or another specified dynamical programme, together with a mass readout. The small final defect of this prototype has no established conversion to 0.152673 units of electron mass.

Checker: research/nima/checkers/check_full_mass_comparison_programme.py runs both full orders with exact fractions, checks all equality projections and the resource-accounting identity, and writes no artifacts. No measured mass is used.

## Back-action-supported settling floor

Add an explicit stochastic comparison back-action to the six-potential programme. For comparison row r, let P=I-r r^T/(r^T r) be its equality projector. Update x'=P x+eta, where eta is independent zero-mean noise with covariance q P/5. The rank-five normalization gives expected injected squared norm q per attempt. Noise stays inside the newly satisfied equality plane, so the current comparison remains valid while other agreements can be disturbed.

The covariance update is

    Sigma' = P Sigma P + q P/5.

Every comparison separately retains its unit traversal cost. The Euclidean squared norm is a second, explicitly chosen resource/readout. The expected squared disagreement removed by the projection is r^T Sigma r/(r^T r). The exact trace balance is

    Tr(Sigma') = Tr(Sigma) - r^T Sigma r/(r^T r) + q.

For the declared repeated 153-row schedule the numerical covariance converges to a periodic end-of-sweep state. With q=1, end-sweep trace is 14.845441092541 and the sum of comparison variances is 612.240649285455. The covariance iteration met its 1e-12 entrywise stopping threshold after four sweeps from zero. At stationarity each sweep removes 153 squared-resource units, matching injection. A twelve-sweep programme removes and receives 1836 q units. Halving q halves covariance and settling budget; q=0 restores zero floor for initially compatible data.

Outcome: comparison back-action can sustain a reproducible settling floor while every traversal keeps positive cost. The model predicts the response to a specified q; it does not select q from the carrier or convert squared potential into rest mass. A mass correction would require that conversion and the electron's own settling response. Substituting 0.152673 to determine q would calibrate the model to the target, not derive the tail.

The covariance computation does not add new comparison attempts beyond the scheduled programme. If the hypothesis specifically attributes the tail to extra traversals, an adaptive stopping/retry rule and its cost must also be specified. This prototype measures continual settling work inside the repeated programme.

Checker: research/nima/checkers/check_comparison_backaction_floor.py verifies current-constraint preservation, trace balance, zero-injection behaviour, and linear covariance scaling. It uses floating arithmetic with explicit tolerances, writes no artifacts, and uses no measured constants. Independent isotropic noise, its Euclidean metric, and the fixed comparison order are trial dynamics.

## Outcome and next object

The 153-slot domain and twelvefold 1836-slot family are exactly constructible. The mass ratio and the equal-energy weighting remain hypotheses. The next object is a carrier energy/readout rule that fixes the three rooted orbit weights and identifies the proton/electron sectors. A common change in energy units multiplies numerator and denominator equally and cancels in a mass ratio; a physical correction must distinguish the two responses.

Verification: research/nima/checkers/check_proton_electron_comparison_slots.py enumerates all slots and S4/S3 edge orbits and passes exact checks. It writes no artifacts and computes no masses.
