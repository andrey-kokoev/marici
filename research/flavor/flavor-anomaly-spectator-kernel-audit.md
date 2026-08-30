# WP155 — anomaly spectator-kernel audit

## Bounded question

Does WP154's faithful \(\mathbb Z_4\) anomaly condition still select flavor
fixed-sector packets when the admitted UV source domain includes unresolved
spectator or counterterm contributions?

## Frozen extended source domain

Let

\[
f=(f_1,f_2,f_3)\in(\mathbb Z_4)^3
\]

be the flavor fixed-sector residue packet, and let

\[
s\in\mathbb Z_4
\]

be the net anomaly residue of an additional UV spectator sector or permitted
topological counterterm. The faithful total anomaly is

\[
\mathcal A_{\rm total}(f,s)
=f_1+f_2+f_3+s\pmod4.
\]

This is an abstract residue completion grammar, not yet a claim that every
value of \(s\) has a gauge-complete massive-fermion realization.

## Exact projection result

On the frozen spectator-free slice \(s=0\), anomaly freedom selects WP154's
16-packet kernel. On the extended domain, however, every one of the 64 flavor
packets has exactly one canceling spectator:

\[
s=-f_1-f_2-f_3\pmod4.
\]

Therefore the anomaly-free extended space has 64 elements and its projection
onto flavor is surjective:

\[
\pi_f\bigl(\ker\mathcal A_{\rm total}\bigr)
=(\mathbb Z_4)^3.
\]

The total anomaly remains a faithful constraint on the extended source, but it
selects no proper flavor subspace after unresolved spectator data are
forgotten.

The smallest hostile repair is WP153's packet

\[
f=(1,1,1).
\]

It is rejected when \(s=0\), yet

\[
1+1+1+1=0\pmod4,
\]

so spectator residue \(s=1\) restores it. This packet produces WP153's
inaccessible \(k=1\) branch.

## Restricted spectator domains

If only even residues \(s\in\{0,2\}\) are admitted, the projected flavor
domain has 32 packets rather than 16. This reproduces a partial, nonfaithful
selector. Thus selector strength is relative to the independently frozen UV
completion grammar.

## Typing

- **Admitted state domain:** extended anomaly packets \((f,s)\in(\mathbb
  Z_4)^4\).
- **Faithful quotient coordinate:** `physical16` downstream; the low-energy
  flavor map forgets \(s\) unless threshold-sensitive spectator observations
  are added.
- **Source-authorized probe family:** total anomaly residue only.
- **Contextual partition:** four total-anomaly fibers in the extended domain;
  the anomaly-free fiber projects onto all 64 flavor residues.
- **Separation:** total anomaly separates extended residue classes but does not
  identify the flavor contribution independently of \(s\).
- **Selection:** proper on the full extended space, absent on projected flavor;
  the WP154 flavor selector exists only on a frozen spectator-free domain.
- **Rigidification:** none.
- **Faithfulness versus selection:** on the anomaly-free graph, projection
  \((f,s)\mapsto f\) is actually bijective because \(s\) is fixed by \(f\).
  The failure is not a nonfaithful arrow: enlarging the legal source domain
  changes the anomaly-free subspace so that its flavor image expands from 16
  to 64. Faithful readout therefore does not imply selection.
- **Descent:** the total character is permutation invariant and the resulting
  flavor packets descend under full weak-basis equivalence.
- **Reference port:** a spectator-sensitive threshold port would define a new
  relational experiment.
- **Physical instrument:** absent.

## Selector disposition

WP154 is a valid mathematical selector only relative to a closed UV spectrum.
It cannot be promoted to open-world flavor selection until the mediator and
spectator grammar is frozen independently of the desired answer and all legal
anomaly-canceling completions are included.

## Smallest exact falsifier

\[
(f,s)=((1,1,1),1)
\]

is total-anomaly-free but projects to the flavor packet that WP154 intended to
exclude.

## Reopening condition

Derive a gauge-complete UV spectrum in which permitted heavy spectators and
counterterms have net residue \(s=0\), or provide physically typed
spectator-sensitive observations that retain source attribution. Finite
widths, threshold accessibility, decoupling, and detector resolution must be
included before such observations gain identification authority.

## Verification

```text
python research/flavor/checkers/wp155_anomaly_spectator_kernel.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10 that open spectators would
erase projected flavor selection, expected information gain 10/10. The
confound was that the residue completion is abstract rather than a constructed
gauge-complete spectator spectrum.

Frozen optionality snapshot: one 16-packet closed kernel, one 64-packet open
kernel, one 32-packet even-spectator branch, one hostile repaired packet, 12
checks, and no physical instrument.

Post-objective: excitement 9/10, confidence 10/10, realized information gain
10/10. Opening the spectator grammar expands the admitted flavor image from 16
to 64 packets; restricting to even spectators leaves 32. WP154's selector is
retained only as a closed-domain theorem. The exact source ambiguity is one
\(\mathbb Z_4\) compensation coordinate, and no gauge-complete realization or
spectator-sensitive instrument was constructed.
