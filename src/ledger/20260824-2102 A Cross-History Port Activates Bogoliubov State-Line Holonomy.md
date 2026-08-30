# 2102 — A Cross-History Port Activates Bogoliubov State-Line Holonomy

## Question

Entry 2101 found nontrivial squeezed-vacuum state-line holonomy but correctly
left it physically unclassified: an isolated global phase is not observable.
Test it with a source-defined relative-history pairing.

## Frozen protocol

Introduce a labelled two-history control:

\[
\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes|\psi\rangle.
\]

- On history \(0\), hold the quadratic source at the base point.
- On history \(1\), execute the closed squeezed-phase loop of Entry 2101.
- Remove the common dynamical phase by the declared balanced protocol.
- Recombine the control histories in the Hadamard basis.

The system state returns projectively to the same ray on both histories.  The
control therefore retains only their relative geometric phase.

## Exact relative transport

Entry 2101 gives

\[
\gamma=-\frac{16\pi}{9}.
\]

Since \(-16/9\) is not an even integer,

\[
e^{i\gamma}=e^{-16\pi i/9}\ne1.
\]

The endpoint state is

\[
\frac{|0\rangle+e^{i\gamma}|1\rangle}{\sqrt2}
\otimes|\psi\rangle.
\]

Hence the control readout probabilities are

\[
P_+=\frac{1+\cos(16\pi/9)}2,
\qquad
P_-=\frac{1-\cos(16\pi/9)}2.
\]

They differ from the trivial-loop output \((1,0)\), while visibility remains
one.

## Narrow result

\[
\boxed{
\text{the Bogoliubov state-line holonomy becomes physical when paired through
a labelled cross-history interference port.}
}
\]

The covariance lens remains blind because it forgets state phase.  The
relative-history readout does not.  Thus observability is not a property of
the loop alone:

\[
\text{Carrier loop}
+\text{coefficient line}
+\text{physical pairing}
\longrightarrow
\text{observable phase}.
\]

No new incidence stratum was introduced.  The additional datum is a
source-defined labelled cross-history port—the same general kind of
relational readout that appears in the double-slit sector.

## Limitation and next falsifier

The balanced protocol explicitly cancels common dynamical phase.  A genuine
cosmological application must derive the two histories and their relative
normalization from the physical contour or in-in doubling, rather than append
an abstract laboratory control.  The next test is whether the native
Schwinger--Keldysh/Bunch--Davies occurrence structure supplies this cross-history
port and whether its trace preserves or cancels the geometric phase.

## Durable evidence

- `research/benincasa/checkers/squeezed_vacuum_controlled_interference.py`
- `research/benincasa/checkers/results/squeezed-vacuum-controlled-interference.json`
- Ledger allocation: `seqclaim-e413d09d928c3a2f277afdce`

