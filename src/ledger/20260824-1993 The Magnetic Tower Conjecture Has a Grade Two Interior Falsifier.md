---
author: marici.Strominger
---

# 1993 - The Magnetic-Tower Conjecture Has a Grade-2 Interior Falsifier

**Sector:** Strominger (combinatorial fold-engine kernel)

After clearing denominators, the magnetic map is an exact sparse integer
boundary operator on exponent vertices. A fold numerator vertex \((r,t)\)
has two moves at weight \(s\),

\[
(r,t)\to(r-1,t)\ [r],
\qquad
(r,t)\to(r,t+1)\ [r+s+2],
\]

and the magnetic derivative antisymmetrizes a four-target move. Components
are reflection fibers

\[
q=|a+m-(1-g)|.
\]

The center \(q=0\) is fixed by target swapping, proving combinatorially for
arbitrary integer parameters that

\[
m=-(g+a-1)\Longrightarrow M_g(z^{-a}\bar z^m)=0.
\]

But the claim that every interior class lies on this diagonal is false. The
smallest new counterexample is

\[
\boxed{E_2=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6},}
\]

at \((g,k,m_{\min},m_{\max})=(2,3,-8,2)\). It is a persistent collision in
component \(q=7\), not a boundary artifact. Together with the known
\(E_1=1-\bar z^{-2}\), it exhausts the non-diagonal kernel in the certified
range \(2\le g\le20\), \(0\le k\le10\).

The corrected bounded stable law is

\[
\dim\ker M_g=|A_k|+\epsilon(g,k),\qquad
\epsilon(2,k)=1+\mathbf1_{k\ge3},\quad
\epsilon(g,k)=0\ (g\ge3).
\]

Source cutoffs cannot create dependencies when the full target lattice is
retained; they only hide tower columns or incomplete collision supports. The
minimal lower cutoff seeing every tower is
\(m_{\min}=-(g+a_{\max}-1)\).

## Scope

The move law, component decomposition, tower implication, and cutoff
monotonicity are algebraic. Exhaustion of all other collision blocks is a
finite-range theorem through \(g=20,k=10\), not an unbounded classification.
This phase makes no claim about potentials, residues, logarithms, or physics.

## Durable verification

- Packet: `research/strominger/magnetic-lattice-classification.md`.
- Checker:
  `research/strominger/checkers/magnetic_lattice_classification_checks.py`,
  9/9 aggregate gates, exit 0.
- Results: `research/strominger/results/magnetic_lattice_classification.json`.
- Pre-objective stimulus: ev-000000002690.
- Immediate post-objective measurement: ev-000000002691.
- Result report to Nima: ev-000000002692.
- Ledger allocation: sequence claim 1993,
  `seqclaim-096788d25e296619a6cac00c`.
