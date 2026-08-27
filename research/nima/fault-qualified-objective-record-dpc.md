# Fault-qualified objective record formation

## Question

When may distributed physical records be treated as one objective classical
fact without identifying that fact with the complete physical state?

## Claim boundary

Let (S) be a global state space, let (r_i:S\to R_i) be record channels
derived from declared physical interactions, and let (F) be a declared fault
model. The candidate objective-record object is the quotient

\[
O=S/{\sim_O},
\qquad
s\sim_Os' \Longleftrightarrow
r_i(s)\simeq_F r_i(s')
\]

for every admitted fault-surviving observer family.

The partial constructor

\[
\mu_{\rm obj}:
(S,\{r_i\},F)\rightharpoonup O
\]

is defined only after source derivation, readability, agreement, fault
survival, witness independence, nondisturbance, descent existence, causal
provenance, and completion stability have been established. Descent uniqueness
is asserted only in (O). It is not a claim that the record family reconstructs
(S).

The exact separation gate is joint faithfulness:

\[
\bigcap_i\ker r_i=0.
\]

When this fails, the quotient may still exist and be objective while retaining
unobserved global distinctions.

## Finite hostile witnesses

### Proper-fragment GHZ witness

The states

\[
|\mathrm{GHZ}_{\pm}\rangle=
\frac{|000\rangle\pm|111\rangle}{\sqrt2}
\]

have identical one- and two-qubit reduced density matrices. Their difference
is nonzero globally and lies in the joint kernel of all proper partial traces.
Thus local descent exists but is not separated.

### Correlated-witness witness

Three agreeing observers do not constitute three independent witnesses when
one admissible common-cause fault controls all three. Raw redundancy passes;
fault-qualified quorum authority fails.

### Quorum-overlap witness

For (n) witnesses and quorum size (q), the minimum overlap is

\[
I_{\min}=\max(0,2q-n).
\]

Under Byzantine bound (f), overlap authority requires (I_{\min}>f).
The checker distinguishes unsafe (n=3,q=2,f=1) from safe
(n=4,q=3,f=1).

### Completion-collapse witness

The observation maps

\[
J_N=\operatorname{diag}(1,N^{-1})
\]

are injective at every finite cutoff, but their lower observability bound is
(N^{-2}), which tends to zero. Cutoffwise separation therefore does not imply
completion-stable observability.

## Decisive problem contract

The construction has three admissible dispositions:

1. The gates pass and a fault-qualified objective quotient exists.
2. Records exist, but at least one readability, independence, fault, causal,
   nondisturbance, or completion gate fails.
3. The quotient exists, but a nonzero global relational direction remains in
   the joint kernel of the admitted observer cover.

The third disposition is not a defect. It prohibits promotion from objective
record agreement to unique global-state reconstruction.

## Disposition

The finite DPC is closed and mechanically checked. It establishes the logical
separation between objective-record formation and reconstruction of the global
state. It does not establish that any particular natural environment satisfies
all constructor gates, solve the measurement problem, or identify the quotient
with complete physical reality.

Verification is provided by
`research/nima/checkers/check_fault_qualified_objective_record_dpc.py` and
`research/nima/results/fault-qualified-objective-record-dpc.json`.
