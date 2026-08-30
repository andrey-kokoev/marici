# Charged-cycle physical16 surjectivity

## Bounded question

Does the WP635-WP642 charged extension select a proper subset of the complete
stored 1,210-sheet fitted `physical16` domain, or does it attach an independent
probe fiber to every fitted sheet?

## Admitted domain and matching boundary

The faithful flavor coordinate is

\[
X_{16}=(m_u,m_c,m_t,m_d,m_s,m_b,
|V_{ij}|,J),
\]

with six ordered masses, nine CKM moduli, and signed Jarlskog coordinate,
modulo the full weak-basis group. The bounded state domain is the complete
stored 1,210-sheet fitted ensemble used by the earlier selector disposition.

The charged carrier obeys \(\langle\chi\rangle=0\). At the tree-level matching
order admitted in WP635-WP642, its two cross-couplings therefore contribute to
charged transition and contact amplitudes but not to the neutral quark mass
matrices. No loop backreaction, threshold correction to the neutral Yukawas,
or source equation correlating charged couplings with `physical16` is admitted.

## Product-extension theorem

Let \(F_{1210}\) be the fitted sheet set and let \(C\) be any nonempty admitted
charged context set. Under the stated zero-vev tree-level assumptions, the
extended domain is

\[
E=F_{1210}\times C,
\]

and the flavor readout is the projection

\[
p:E\longrightarrow F_{1210}.
\]

For every sheet \(x\), choosing any \(c\in C\) gives \(p(x,c)=x\). Hence \(p\)
is surjective and the charged extension selects no proper fitted flavor
family. Its response partitions the carrier fiber over each sheet; it does not
reduce the base.

The exact checker uses four hostile carrier contexts: relative signs plus and
minus at \(m_\chi=1\), and the same signs at \(m_\chi=2\). The product contains
4,840 extended states and projects onto all 1,210 fitted sheets, with fiber
size four on every sheet.

## Descent and classification

The charged responses are weak-basis invariant when expressed through matched
currents and masses, but descent is not selection. The operation is a
source-derived probe extension and, where a chart is chosen, may rigidify its
charged presentation. It is not a selector on `physical16`.

The smallest exact falsifier to selector status is any one fitted sheet with
both constructive and destructive carrier contexts: the flavor point is
unchanged while the added response changes. The ensemble-wide statement is
stronger: every stored sheet has the same four-context fiber.

## Reopening gate

This branch can reopen selector authority only if a source-derived equation or
backreaction is added that:

1. descends under the full weak-basis group;
2. correlates charged parameters with a proper subset of `physical16`;
3. has normalization fixed independently of the fitted answer;
4. survives all 1,210 sheets where its domain applies;
5. has a calibrated physical instrument.

A loop correction could in principle violate the product form, but it must be
computed and renormalized; its mere availability is not a selector.

## Reproduction

Run:

    python research/flavor/checkers/wp643_charged_cycle_physical16_surjectivity.py

The generated result is
`research/flavor/results/wp643_charged_cycle_physical16_surjectivity.json`.
