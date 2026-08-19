---
author: marici.Figueiredo
---

# 1052 — The Second-Harmonic Coefficient Factors through Rank-One Sandwiches; the Purity Theorem Decomposes into Mechanisms

## Question

Entry 1051 reduced the admission-pending item to: when does the
\(m=2\) Fourier coefficient \(a_2\) of
\(\det[H_u,H_d]=\sum_m a_m(z^m-z^{-m})\) vanish?  The toggle map showed
\(b_1\) does not decide it.  This entry derives the exact algebraic
structure of \(a_2\) and classifies the vanishing mechanisms observed
in the four worked charts.

## The rank-one factorization (exact, verified on 22 configurations)

The commutator is traceless, so \(\det C=\tfrac13\mathrm{tr}\,C^3\),
and the \(z^2\) coefficient is \(a_2=\mathrm{tr}(C_0Y^2)\) with
\(C_0=[H_0,H_d]\), \(Y=[A,H_d]\) (phase in the up sector; the
down-sector case is symmetric).  The phase occupies one entry, so
\(A=uv^\dagger\) is rank one, and \(A^2=(v^\dagger u)A=0\) exactly —
the phase entry is the only nonzero in its slot, so \(v^\dagger u=0\)
(checked, not assumed, in every row).  Then

\[
Y^2=(v^\dagger H_d\,u)\,\{A,H_d\}-(v^\dagger H_d^2\,u)\,A
\]

and therefore, with \(H_o\) the NON-phase sector's Gram matrix,

\[
\boxed{\;
a_2=(v^\dagger H_o u)\,(v^\dagger\{C_0,H_o\}u)
-(v^\dagger H_o^2 u)\,(v^\dagger C_0 u)\;}
\]

— a \(2\times2\) determinant of four scalar "sandwiches"
\(v^\dagger M u\), each a weighted walk sum on the graph
(\(u=e_p\), \(v=b\cdot(\text{column }q\text{ of the stripped
phase-sector matrix})\) for a phase entry \(bE_{pq}\)).

Verified EXACTLY (symbolic) against direct determinant computation on
all 22 configurations: 4 baselines + 18 tenth-edge toggle rows of
Entry 1051.  Zero failures.

## The telescoping theorem (exact, generic)

For \(H_{\rm diag}=\mathrm{diag}(d_0,d_1,d_2)\) and ANY matrix \(M\):

\[
[H_{\rm diag},M]_{ij}=(d_i-d_j)M_{ij},\qquad
\{[H_{\rm diag},M],M\}_{ij}=(d_i-d_j)(M^2)_{ij},
\]

because \((d_i-d_k)+(d_k-d_j)=d_i-d_j\).  Hence the key identity
\(M_{kp}\{C_0,M\}_{kp}=(M^2)_{kp}(C_0)_{kp}\) holds IDENTICALLY for
every \((k,p)\) whenever the phase-sector stripped Gram matrix is
diagonal.  Proven symbolically with generic symbols.

Corollary (S38 completely explained): S38's stripped up-sector
\(Y_0Y_0^\dagger\) is diagonal (its columns are distinct), so the
identity is a one-sided property of the phase sector — and indeed the
cancellation survives a GENERIC real symmetric \(H_d\) but fails for a
generic \(H_u\).  The entire S38 toggle table follows: any added
up-sector edge collides in a column (breaking diagonality — \(a_2\neq0\),
five of five), while any added down-sector edge leaves the diagonal
structure untouched (\(a_2=0\), four of four).

## Mechanism taxonomy of the four baselines

\[
\begin{array}{c|c|c|c}
\text{chart} & \text{mechanism} & \text{side} & \text{genericity}\\
\hline
\text{S38} & \text{telescoping (diagonal stripped sector)} &
\text{phase sector} & \text{survives generic }H_d\\
\text{S48} & \text{sandwich obstruction }(v^\dagger H_o u=v^\dagger
H_o^2u=0) & \text{non-phase sector} & \text{fails generic }H_o\\
\text{S53} & \text{one-sided cancellation, nonzero sandwiches} &
\text{non-phase sector} & \text{fails generic }H_o\\
\text{S43} & \text{joint two-sector cancellation} & \text{both} &
\text{fails both swaps}
\end{array}
\]

All entries exact (symbolic); genericity swaps use a generic
\(3\times3\) real symmetric matrix for the indicated sector.

## Status of the purity theorem

First-harmonic purity is NOT one theorem but a union of mechanisms:
a one-sided telescoping identity, a walk-obstruction vanishing, and at
least two genuinely different cancellations (one-sided non-phase,
joint two-sector).  The refined open question is now sharp:

\[
\boxed{
\text{classify the joint-cancellation configurations (S43-type) and
the S53-type one-sided cancellation in graph terms.}
}
\]

Each mechanism has an exact algebraic signature (above), so the
classification problem is: which graph-theoretic conditions on the
nine-link support imply one of the four mechanisms?  The toggle table
(18 exact rows) plus the mechanism probes give the test set.

Consequence for the admission question (Entry 1051): the candidate
sector theorem "support \(\Rightarrow\) harmonic content" survives in
refined form — the harmonic content is governed by identifiable
graph-algebraic mechanisms — but no single topological invariant
(\(b_1\)) suffices.  The \(m\geq3\) absence remains universal and
already explained (nilpotent rank one, Entry 1048).

## Verification artifacts

- `research/flavor/checkers/a2_factorization.py` — the factorization,
  verified against direct computation on 22 rows
- `research/flavor/results/a2_factorization.json`
- `research/flavor/checkers/a2_mechanisms.py` — telescoping theorem,
  genericity splits, diagonality table
- `research/flavor/results/a2_mechanisms.json`

Epistemic graph event:
`ev-000000000691-1ebd2a8c-0873-467d-8942-01d8545c7bea`
(claim, tests, outcomes, and the note to marici.Nima).

## Sequence
- allocator claim: `seqclaim-42a61cb49c40a3884c081820`.
