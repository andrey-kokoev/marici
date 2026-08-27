# Charged-cycle threshold-support fiber

## Bounded question

Does WP636's rephasing-invariant interference probe also determine whether its
charged heavy transition is physically open?

## Independent coordinate split

The cycle invariant and its two path amplitudes depend on

\[
Y_S^u,Y_S^d,C_A,C_B,Z_B^u,Z_A^d,\sigma.
\]

The candidate decay support

\[
A^u\longrightarrow B^d+\chi
\]

instead requires

\[
M_{A^u}>M_{B^d}+m_\chi,
\]

and therefore depends on \(Z_A^u,Z_B^d,m_\chi,\sigma\). The parent mass and
charged-scalar mass are absent from \(\mathcal I_\chi\).

## Exact hostile pair

Freeze every cycle coordinate to one, take \(M_{B^d}=m_\chi=1\), and compare

\[
M_{A^u}=3
\]

with

\[
M_{A^u}=3/2.
\]

Both points have \(\mathcal I_\chi=1\) and the same formal constructive
two-path rate factor four. For the first point the Källén polynomial is

\[
\lambda(9,1,1)=45>0,
\]

so the two-body channel is open. For the second,

\[
\lambda(9/4,1,1)=-63/16<0,
\]

so the channel is closed. The two points differ only in a positive source
coefficient not seen by the cycle invariant.

## Disposition

The charged cycle selects neither kinematic support nor a physical instrument.
WP636's response exists as a source amplitude, but the observable on-shell
partition has a nontrivial fiber over the same cycle record. Write \(C\) for
the cycle coordinate, \(A\) for the amplitude, \(T\) for threshold support,
and \(D\) for the detector record. The pipeline is

\[
C\longrightarrow A\longrightarrow T\longrightarrow D.
\]

The first nonfaithful arrow for on-shell accessibility is amplitude to
threshold support. A progressive source must derive a strict positive
threshold margin together with the cycle, or else construct an off-shell
observable whose sensitivity is quantified after propagator suppression.
Finite widths and detector calibration remain subsequent gates.

## Reproduction

Run:

    python research/flavor/checkers/wp637_charged_cycle_threshold_support_fiber.py

The generated result is
`research/flavor/results/wp637_charged_cycle_threshold_support_fiber.json`.
