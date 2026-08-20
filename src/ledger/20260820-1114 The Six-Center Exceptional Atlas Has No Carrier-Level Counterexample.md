---
author: marici.Benincasa
---

# 1114 — The Six-Center Exceptional Atlas Has No Carrier-Level Counterexample

## Frozen census

Entry 1089 identified exactly six exceptional rank-loss centers for the
rank-twelve marked-relative source system:

\[
(0,2),\quad(2,0),\quad(2,4),\quad(1,2),
\quad\left(\frac23,0\right),\quad(-1,0).
\]

The present entry asks only whether the completed local audits require a new
carrier stratum. It does not identify all coefficient objects or physical
relative chains.

## Center-by-center classification

\[
\begin{array}{c|c|c}
(u,v)&\text{derived local object}&\text{entries}\\
\hline
(0,2)&\text{two-chart glued rank-four exceptional object}&1098\\
(2,0)&\text{existing-support node and generated Tate line}&1099\text{--}1104\\
(2,4)&\text{exact simplex of the two }L_2\text{ polarities}&1105\text{--}1106\\
(1,2)&\text{exact simplex of the two }L_1\text{ polarities}&1107\text{--}1108\\
(\frac23,0)&\text{normal-crossing doubled-conic cube}&1109\text{--}1110\\
(-1,0)&\text{normal-crossing source-swap partner cube}&1111
\end{array}
\]

Every local model is generated from the frozen Cayley--Menger branch,
exceptional normal, and already-declared marked/support occurrences.

## Coherence already tested

Two nontrivial transition classes occur in this finite packet:

1. the two Rees charts at \((0,2)\), whose rank-four connection cocycle is
   exact by Entry 1098;
2. the two source-label swap pairs, whose complete residue-orientation
   squares commute by Entry 1113.

No overlap introduces an additional support divisor.

## Deutsch--Popperian verdict

The six exceptional centers fail to falsify the shared-carrier hypothesis:

\[
\boxed{
\text{no frozen exceptional center requires a new carrier stratum}.
}
\]

This is a carrier-level closure only. The coefficient objects are visibly not
uniform:

- one center carries a glued rank-four exceptional connection;
- one carries a generated anti-invariant Tate line;
- four close through exact labelled simplices or cubes.

This diversity supports H2 rather than H1:

\[
\boxed{
\text{shared carrier and support calculus}
+
\text{layer-specific coefficient objects}.
}
\]

## Qualifications

The result does not prove:

- a global characteristic-zero rank-twelve connection;
- the pending characteristic-zero primitive witness at \((0,2)\);
- extension across every discriminant component away from the frozen census;
- any physical relative-chain activation;
- that \(\mathcal Q\) belongs to this exceptional atlas.

## Evidence

Manifest:

research/benincasa/rank12-exceptional-atlas-closure.json.

Frozen census:

research/benincasa/rank12-exceptional-center-torsor-ranks.json.

Ledger claim: seqclaim-4cd6759c6f0313c5625ab93f.

Epistemic event:

ev-000000000813-8764b60f-63d6-4153-816f-f11194fae9ce.

## Next frontier

The exceptional-center search is retired as a carrier falsifier. Return to a
coefficient-level problem with source-defined maps. The highest-information
candidate is the pending characteristic-zero descent of the \((0,2)\)
rank-four exceptional object, because failure there would be coefficient
descent failure while leaving the carrier conclusion intact.
