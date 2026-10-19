# Iteration2: term-resolved routes and a retained RH query seam

## New construction

There is now an executable six-occurrence **evaluator ledger** for the fixed
three-Gaussian packet. It retains each arithmetic term, the original test,
independently reevaluated finite spectral atoms, and an unresolved full-divisor
remainder. It never promotes numerical agreement with the scout to a completed
RH comparison.

This is a declared source-query protocol assigned to the directed occurrence
names. It is **not** a claim that the old native arrows execute those evaluators.
That distinction is an explicit failed promotion in the receipt.

## 1. Exactly what is sent across the seam

Fix the freshly read source packet

    t=1/10, a=(0,14,21),
    g_i(u)=exp[-t(u-a_i)²/2].

For coefficients c define the entire polarized test

    h_c(u)=sum_ij conjugate(c_i)c_j g_i(u)g_j(u).

In this real-coefficient Gaussian family it can be encoded by six weights:

    |c0|², 2Re(conj(c0)c1), 2Re(conj(c0)c2),
    |c1|², 2Re(conj(c1)c2), |c2|².

The seam carries t, the labelled Gaussian family, c, these weights, source
normalization and route/remainder statuses. On the synchronized mirrored seed
restriction, the opposite triangle reads -c, and h_(-c)=h_c exactly. The two
original occurrences remain distinct records. This is not a declaration that
independent generic triangle updates synchronize.

The shared object is therefore the **same source query**, not an asserted
common scalar value. Equality of completed evaluations remains a separate gate.

## 2. Declared directed route roles

| Occurrence | Evaluator action | Retained output |
|---|---|---|
| AB | Transport query to arithmetic route | Test and coefficient provenance |
| BC | Apply endpoint/gamma/prime source evaluations | Three separately labelled contributions |
| CA | Sum the arithmetic contributions | Sum plus original test and all term records |
| BA | Transport mirrored query to spectral route | Same polarized test, distinct directed occurrence |
| AD | Evaluate supplied signed spectral atoms | Atom records plus an unresolved full-divisor remainder |
| DB | Return spectral comparison record | Finite sum and explicit remainder status |

These actions give concrete computational meanings **if this evaluator layer
is admitted**. The original triangle primitive instead cycles three amplitudes.
Its operator has not been replaced or relabelled as an integral/prime evaluator.
The occurrence labels alone do not authorize the new layer.

## 3. Arithmetic route: signed terms stay separate

Read the live analytic source certificate. Its six endpoint, gamma and prime
entry enclosures are parsed as exact rational intervals; interval multiplication
and summation use only rational arithmetic. No fresh Arb integration is claimed.
The gamma and prime records retain the previous certificate's infinite-tail
meaning, not just a finite quadrature/prime partial sum.

For c=(1,0,0), the three contributions are approximately

    endpoint: +1.0253151205244,
    gamma:    -0.8625096009156,
    prime:    -0.1628055175040.

Their positive residual is approximately 2.1048e-9. The ledger preserves the
large signed cancellation; it does not independently replace each term by a
positive norm.

All six coefficient controls have retained term-wise interval evaluations.
Their summed intervals are compatible with the separately reported total
source enclosures. The authority/normalization boundary on that source remains
unchanged.

## 4. Spectral route: independent finite atoms, not a manufactured full sum

For every query the checker reevaluates the 32 signed atoms from the stored
sixteen positive-ordinate numerical zero samples. It does not obtain them from
the arithmetic matrix or copy the old finite-zero matrix. Their numerical
reevaluation agrees with the prior scout, and each query's finite sum lies
numerically inside its arithmetic interval.

However AD also returns

    remainder = full signed divisor minus these32 sampled atoms,
    value = unresolved,
    certified = false.

DB retains that object. The full shared-edge equality gate rejects completion
for all six queries. No missing tail is assigned value zero.

For complex u the evaluator uses h_c(u), not |sum c_i g_i(u)|². A hypothetical
quartet u=+/-20pi+/-i/4 is evaluated through the same code: its Gaussian divisor
value is negative, while projection onto its real ordinates is positive. This
is not an assertion about actual zeta zeros. It protects the RH-bearing sign
question from a critical-line-only substitution.

## 5. Fixed Gaussian slot addresses fail the triangle cycle

The actual primitive cycle is C(c0,c1,c2)=(c1,c2,c0). With the Gaussian basis
labels fixed, preserving the same arithmetic form would require

    C^dagger G_arith C=G_arith.

The source's three diagonal intervals are pairwise disjoint, approximately

    2.1048e-9, 0.502706, 0.604607.

Every one of the six bijective assignments of the three Gaussian labels to
three fixed slots fails this requirement. This failure holds for the actual
source enclosures, not merely for one rounded midpoint. Individual phase
changes cannot repair the unequal diagonal norms.

This is a restricted same-query/static-address obstruction. If C is instead
intended to generate a different test at each step, changing the arithmetic
value is not a failure: both routes must evaluate that changed test. The audit
does not exclude that alternative, arbitrary feature mixing, a different
admitted test family or an enlarged carrier.

A retained three-valued basis frame repairs the **source-label bookkeeping**:

    c_k=C^k c, g_k=C^k g,
    G_term,k=C^k G_term (C^k)^dagger.

The test and every endpoint/gamma/prime readout remain unchanged. All three
frames are checked on six inputs. This is not yet a native W intertwiner, nor
proof that an actual neutron rotation transports these Gaussian features.

## 6. Same individual term forms survive in both native carriers

The iteration1 source/sink channels were freshly bound and rebuilt from the
proton and neutron coefficient stores. The neutron denominator metric remains
in place. For each of the three rational **midpoint** term matrices G_j, form

    B_j=X+Y D^-1 G_j.

Every term satisfies its exact weighted signed pullback in each carrier. The
midpoint matrices are finite representatives of reported enclosures; they are
not relabelled as exact transcendental source values or interval matrices.

A new composition control matters here. Naively adding the three lifts gives

    B_naive=3X+Y D^-1(G_endpoint+G_gamma+G_prime),
    B_naive^dagger F B_naive=3 G_total.

The common query source was included three times. The corrected composition is

    B_total=B_endpoint+B_gamma+B_prime-2X,
    B_total^dagger F B_total=G_total.

Both identities are verified in both structures. This is a property of the
explicit affine signed-attachment recipe, not a universal claim that every
geometric seam must be counted once.

Thus the source term labels and signed finite forms survive in both; native
operation-level computation of those terms remains unconstructed.

## 7. Verification, status and next step

    python research/voevodsky/checkers/check_rh_term_resolved_seam.py

Passed: six retained query histories, all source-term interval operations,
independent spectral reevaluation, mirrored-test identity, off-critical sign
control, all six static-label failures, all three moving frames, and both
native term-composition tests. Source-owner stores are read-only.

SCC fingerprint:
`44ac6df0f74f056ef6313a24f9437eb74e00c67b5c4cd41826aeab1f1af0608e`.

- Contract: `inputs/rh-term-resolved-seam-v1.json`.
- Receipt: `results/rh-term-resolved-seam-v1.json`.
- Model: `scc-models/rh-term-resolved-seam-v1.json`.

**Current answer:** the arithmetic triangle's proposed computation is a signed,
term-resolved source evaluation; the spectral triangle's proposed computation
is a full-divisor evaluation with an explicitly uncompleted remainder. Their
common edge identifies the query and conventions, not an assumed equality.
The finite term forms survive in both seed carriers, but the seed arrows have
not been shown to execute this new evaluator protocol.

**Nonredundant next step:** compare the retained evaluator ledger and its basis
frame against actual six-occurrence source operations in each structure.
Construct or reject an explicitly enlarged record-bank intertwiner. Its test
must preserve processing and intermediate records, not only the final form.
