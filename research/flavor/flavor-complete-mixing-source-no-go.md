# Complete-mixing source no-go: WP1120

## Question

Can current source dynamics produce the complete-mixing kernel \(J_6/6\)
required by WP1119?

## DPC resolution

- **Conjecture:** current UV boundary dynamics can produce the
  complete-mixing event kernel \(J_6/6\).
- **Rivals:** fully connected Markov relaxation; Krylov/history dilation; no
  source mixing dynamics.
- **Risky consequences:** Markov relaxation must supply rates and an
  event-time or coarse-graining limit with \(x=0\); Krylov history must become
  an irreversible six-state kernel despite three isometric slots.
- **Falsification attempt:** the exact calculation below gives nonuniform
  output for every \(x>0\), and the history dilation supplies no rates.
- **Residual:** a new UV boundary source could derive irreversible six-state
  mixing rates and a finite event-time limit.
- **Disposition:** reject the current-source complete-mixing conjecture;
  retain irreversible mixing as an open requirement.

## Markov obstruction

The fully connected Markov form is

\[
P(x)=\frac{J_6}{6}+x\left(I-\frac{J_6}{6}\right),
\qquad x=e^{-6\lambda t}.
\]

For branch weights \(q=(6,8,1,4,2,2)/23\),

\[
P(x)q=\Bigl(\frac16\Bigr)^6+x\left(q-\Bigl(\frac16\Bigr)^6\right).
\]

Uniformity requires \(x=0\), the infinite-time or coarse-grained limit. At
\(x=1/2\), for example, the output remains nonuniform. No source supplies the
mixing rates, irreversible coarse graining, or event-time limit.

## Krylov obstruction

The Krylov history dilation has three slots and is an isometry. It has no
six-state irreversible mixing limit.

## Classification

Negative gate. Long-time Markov algebra, Krylov history, or isometric
dilation cannot be promoted to \(J_6/6\) event production.

Checker: `research/flavor/checkers/wp1120_complete_mixing_source_no_go.py`

Result: `results/wp1120_complete_mixing_source_no_go.json`
