# Coherent memory, quantum combs, and tester kernels

## Bounded question

What replaces a classical instrument record when feedback remains coherent,
and what can final scalar probes actually determine about the resulting ordered
process?

## Coherent control memory

Let \(S\) be a system and \(M\) an accessible memory. A first authorized
interaction correlates them, an intermediate constructor may act on either or
both, and a later interaction can convert the retained correlation into a
system output.

No measurement outcome need exist. The usable carrier is the operator algebra
of \(M\), not a classical outcome set.

A classical record is the special case in which every admitted memory state,
readout, and continuation is diagonal in one fixed decomposition

\[
M=\bigoplus_a M_a.
\]

The corresponding accessible algebra is commutative. Coherent memory retains
off-diagonal operators between those sectors and permits continuations that
interfere them.

## Minimal coherent-memory witness

Initialize two qubits as

\[
|+\rangle_S|0\rangle_M.
\]

Apply a controlled-not from \(S\) to \(M\). The joint state becomes

\[
|\Phi^+\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]

Apply the same controlled-not again. The state returns to

\[
|+\rangle_S|0\rangle_M,
\]

so a final \(|+\rangle\) test on \(S\) succeeds with probability one.

Now insert complete dephasing of \(M\) in the computational basis between the
two gates. The Bell coherence is replaced by

\[
\frac12|00\rangle\langle00|
+
\frac12|11\rangle\langle11|.
\]

After the second gate, the reduced system state is maximally mixed, and the
same final test succeeds with probability one half.

The memory population record is identical in both cases. The lost resource is
the off-diagonal memory-system correlation. No classical outcome label can
represent it without changing the experiment.

## Ordered process representation

A finite multi-time quantum process with open intervention slots is represented
by a process tensor or quantum comb \(W\). Its Choi operator is positive and
satisfies causal partial-trace constraints. An admissible tester \(T\) fills
the slots with a causally ordered sequence of instruments, channels, memories,
and a final outcome.

The resulting scalar probability has the linear form

\[
p(T|W)=\operatorname{Tr}(WT),
\]

up to the fixed transpose/link-product convention chosen for the Choi
representation.

The convention must be frozen, but the architectural fact is invariant:
the process is an ordered positive multilinear object, while a completed tester
produces one scalar contraction.

## Tester-kernel theorem

Let \(\mathcal C\) be a declared affine class of causally valid combs, and let
\(\mathcal T\) be the source-authorized tester family. Two processes \(W_1,W_2\)
are indistinguishable by every admitted experiment exactly when

\[
\operatorname{Tr}\bigl((W_1-W_2)T\bigr)=0
\]

for all \(T\in\mathcal T\).

Thus the invisible process directions are

\[
\operatorname{span}(\mathcal C-\mathcal C)
\cap
\operatorname{span}(\mathcal T)^\perp.
\]

The tester family is jointly faithful on \(\mathcal C\) exactly when this
intersection is zero.

This is the ordered-process instance of the kernel-reference theorem. A scalar
completed section is one row. Process reconstruction requires a jointly
faithful tester frame on the declared process class.

## Finite tester-frame consequence

If the admissible process-difference space has finite dimension \(d\) and the
full authorized tester family is jointly faithful, then a finite subfamily of
at most \(d\) linearly independent tester functionals is jointly faithful.

Choose testers greedily, each reducing the current common kernel dimension.
This proves finite algebraic tomography relative to the declared class. It does
not prove that the testers can be executed with bounded cost or stable
precision.

The associated frame operator on the real Hermitian difference space must have
a positive least singular value for robust reconstruction. Across a cutoff
system, completion stability requires that lower bound to remain uniform.

## Classicalization as an operator-algebra quotient

Let \(\Delta_M\) be dephasing onto the declared classical memory algebra. A
comb classicalizes through that port when inserting \(\Delta_M\) at the memory
cut changes no probability for any admitted continuation tester.

Equivalently, the coherent residual

\[
W-W^{\Delta}
\]

lies in the annihilator of the authorized tester span, where \(W^{\Delta}\) is
the comb with dephasing inserted at the chosen interface.

There are therefore two distinct reasons that memory coherence may appear
irrelevant:

1. the process never creates an off-diagonal memory component;
2. the process creates one, but the authorized continuation family cannot
   convert it into an observable difference.

Only the first is an intrinsic absence of coherent memory. The second is a
tester deficiency.

## Coherent continuation criterion

Fix a pre-continuation joint state \(X_{SM}\) and its classicalized version

\[
X_{SM}^{\Delta}=(I_S\otimes\Delta_M)(X_{SM}).
\]

For an authorized continuation channel \(C\) and final effect \(F\), the
coherent advantage is

\[
\operatorname{Tr}
\left[
F C\left(X_{SM}-X_{SM}^{\Delta}\right)
\right].
\]

It is nonzero exactly when the backward-propagated effect \(C^*(F)\) has
nonzero pairing with the off-diagonal residual. Hence coherent memory is usable
relative to the authorized continuation family precisely when that family does
not annihilate every retained off-diagonal correlation.

This supplies a finite witness:

- one source-generated coherent residual;
- one authorized continuation;
- one final effect;
- one nonzero exact pairing.

## Same scalar, different comb

Agreement on a chosen completed tester says only

\[
\operatorname{Tr}(W_1T_0)=\operatorname{Tr}(W_2T_0).
\]

It does not imply equality of the processes. Even agreement on every final
system measurement after one fixed intervention sequence determines only the
induced endpoint channel for that sequence. It leaves responses to alternative
intermediate interventions undetermined.

This is why a scalar analytic section can be a diagnostic shadow of an ordered
plant without being its realization. The plant is the rule assigning outputs
to all admitted intervention histories; the section is one contraction after
the history has already been chosen and closed.

## DPC: accessible-memory explanation of feedback

The sharpened conjecture is:

> Every reproducible feedback advantage over a memoryless coarse model is
> explained by an accessible memory degree of freedom that remains correlated
> with an earlier interaction and pairs nontrivially with at least one
> source-authorized later continuation. Classical feedback uses a commutative
> memory algebra; coherent feedback additionally uses off-diagonal memory
> operators.

The conjecture is falsified by an advantage that survives after replacing the
claimed memory with its coarse model for every authorized tester while holding
all other constructors fixed.

## Critic of the DPC

An apparent memory advantage can be simulated by enlarging the instantaneous
system state. Therefore “memory” is relative to a declared system-interface
factorization. The conjecture has content only when the system port, memory
port, allowed interventions, timing, and reset conditions are frozen
independently.

This is not a weakness to hide. It identifies the source typing needed to
distinguish a genuine temporal carrier from a relabelled larger state space.

## Required typing

A coherent-memory claim must state:

- the system and memory tensor factors;
- which joint states can be prepared;
- the ordered intervention slots;
- the admitted local and joint constructors;
- whether memory is reset between trials;
- the final tester family;
- the causal Choi/link-product convention;
- and the comparison dephasing or discard map.

Without this packet, “the environment remembers” is a metaphor rather than a
testable constructor claim.

## Exact falsifiers

- A scalar tester probability used to reconstruct a unique comb.
- A classical outcome alphabet used to represent off-diagonal memory operators.
- A coherent advantage claimed when every authorized continuation annihilates
  the coherent residual.
- A dephasing comparison that also changes an unrelated constructor.
- Process tomography claimed from a tester span with nontrivial annihilator.
- Finite-cutoff tester faithfulness promoted to stable completion without a
  uniform lower frame bound.
- An inaccessible environment degree of freedom presented as controller memory.
- A memory claim whose system-memory factorization changes after observing the
  desired advantage.

## Deutschian explanation

Coherent feedback works because a past interaction leaves an operator-valued
correlation in an accessible memory, and a later ordered constructor converts
that correlation into a present population difference. Dephasing removes the
off-diagonal carrier, not merely an observer's knowledge.

The explanation predicts the exact hostile operation that destroys the
advantage and the exact backward effect that witnesses the loss. It also says
why endpoint statistics are insufficient: closing the slots contracts away the
counterfactual responses to interventions that define the process as a plant.

## Claim boundary

This packet gives finite-dimensional algebraic comb and tester theorems plus a
minimal coherent-memory witness. It does not establish a particular physical
memory, derive infinite-dimensional process tensors, or prove stable process
tomography under completion.

## Process calibration

Pre-objective: excitement 10/10, confidence 8.5/10, expected information gain
10/10. The target was the noncommutative generalization of record-relative
closure.

Post-objective: excitement 10/10, confidence 9.5/10, realized information gain
10/10. Classical record fibres become a commutative memory algebra; coherent
feedback is detected by pairing an off-diagonal residual with a
backward-propagated authorized effect. The comb's tester annihilator is the
exact process-level blind sector.
