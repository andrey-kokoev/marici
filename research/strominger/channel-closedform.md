# The all-\(n\) channel theorem: every V-tower channel in closed form — Lah-number coefficients, the support law and fold law for all orders

Companion to `checkers/channel_closedform_checks.py` (groups K, U, P, C,
X, V; results in `results/channel_closedform.json`). This packet upgrades
`rung4-foldrule.md` from "certified through tower order 4" to a **theorem
for all tower orders** — and, along the way, hands the tower its
coefficients explicitly: they are (twice) a binomial transform of
**unsigned Lah numbers**.

**Epistemic discipline (as in the fold-rule packet).** The universal-form
match and the support law are certified **unreduced**; the induction
engine is symbolic and order-independent; the recursion and closed-form
checks are exact integer arithmetic. What is machine-certified vs
hand-derived is stated per claim below.

## 1. The theorem

For every tower order \(n\ge1\) and every surviving channel
\(\alpha=(a,b)\in S_n\),

\[
A[n][(a,b)]
= k(n;a,b)\;\frac{2^{(n-2)/2}\,\omega^n\,E_k^{\,b}\,(z-z_k)^{n+a}\,
(1+z\bar z_k)^{b}}{(1+u)^{n}\,(1+z_k\bar z_k)^{b}},
\]

with the **explicit coefficient**

\[
k(n;a,b)=(-1)^{a+b}\,\frac{2\,n!}{a!\,b!}\binom{n-b-1}{a-1}
\quad(a\ge1),
\qquad
k(n;0,n)=2(-1)^n ,
\]

and the surviving channels are **exactly**

\[
S_n=\{(a,b):a\ge1,\ a+b\le n\}\cup\{(0,n)\},
\qquad |S_n|=\frac{n(n+1)}2+1 .
\]

Every channel coefficient is a single factored term times a nonzero
integer — no sums, no cancellations, no fitted constants.

**The Lah factorization.** With \(j=(-1)^{a+b}k>0\),

\[
j(n;a,b)=2\binom{n}{b}\,L(n-b,\,a),
\qquad
L(m,r)=\binom{m-1}{r-1}\frac{m!}{r!}
\]

the **unsigned Lah numbers** — \(L(m,r)\) counts partitions of
\(\{1,\dots,m\}\) into \(r\) ordered lists. The tower coefficients are
twice a binomial transform of Lah numbers. Edge columns:
\(j(n;0,n)=2\), \(j(n;1,b)=2\,n!/b!\), and
\(j(n;a,0)=2L(n,a)\). A combinatorial reading of the V-operator (each
tower step inserting an element into an ordered-list structure) is
suggested but **not pursued here** — recorded as an open question.

Sample \(j\)-table (machine-extracted from the tower, orders 1–5):

| n | \((a,b)\) → \(j\) |
|---|---|
| 1 | (0,1):2, (1,0):2 |
| 2 | (0,2):2, (1,0):4, (1,1):4, (2,0):2 |
| 3 | (0,3):2, (1,0):12, (1,1):12, (1,2):6, (2,0):12, (2,1):6, (3,0):2 |
| 4 | (1,0):48, (1,3):8, (2,0):72, (3,0):24, (4,0):2, … |
| 5 | (1,0):240, (2,0):480, (2,1):360, (5,0):2, … |

## 2. The proof

**Base (\(n=1\)).** The two order-1 channels are the \(c\)-factors
themselves, \(c_{z_k}=k(1;1,0)\cdot\text{shape}(1;1,0)\) and
\(c_{E_k}=k(1;0,1)\cdot\text{shape}(1;0,1)\) — machine-certified
(checker group U, order 1; reconfirmed on all 40 channels through
order 5, unreduced).

**Induction step** — two order-independent symbolic identities
(checker groups K and P):

*Engine.* For an on-shape monomial \(M\) with \((z-z_k)\)-power \(q\),
\(E_k\)-power \(b\) (and any \((1+u)\)-pole),

\[
V(M)=(q-b)\,\frac{\sqrt2\,\omega\,(z-z_k)}{1+u}\;M,
\]

because the off-shape pieces cancel via
\(\bar z_k(z-z_k)-(1+z\bar z_k)=-(1+z_k\bar z_k)\) — the same
cancellation that sends \((0,1)\) to extinction. Applied to the
universal shape:

\[
V\bigl(\text{shape}(n;a,b)\bigr)=(n+a-b)\,\text{shape}(n+1;a,b),
\]

including \(V(\text{shape}(n;0,n))=0\) — the boundary survivor's
\(V\)-contribution vanishes (\(q-b=0\)), so it propagates only by
multiplication.

*Multiplication.*

\[
c_{z_k}\,\text{shape}(n;a{-}1,b)
=c_{E_k}\,\text{shape}(n;a,b{-}1)
=-\,\text{shape}(n+1;a,b).
\]

Hence if order \(n\) is on-form, the tower recursion
\(A[n{+}1][\alpha]=V(A[n][\alpha])+\sum_i c_i\,A[n][\alpha-e_i]\) puts
order \(n+1\) on-form with

\[
k(n{+}1;a,b)=(n+a-b)\,k(n;a,b)-k(n;a-1,b)-k(n;a,b-1)
\qquad(\textbf{K-recursion})
\]

(\(k=0\) off \(S_n\)). The closed form satisfies this recursion —
machine-verified orders 1–60 (checker group C), and a one-line binomial
identity by hand: with \(v(n;a,b)=k\cdot a!b!/(2n!)=\binom{n-b-1}{a-1}\)
the recursion reduces to
\((n{+}1-b)\binom{n-b}{a-1}=(n+a-b)\binom{n-b-1}{a-1}+a\binom{n-b-1}{a-2}\),
both sides \(=(n-b+1)!/((a-1)!(n-b-a+1)!)\).

**Extinction and survival are exact.** Off-set channels stay off:
\(c\)-factor predecessors of an off-set channel are off-set, and the
only survivor leaving \(S_{n+1}\) is \((0,n)\), whose engine
coefficient \(n+a-b=0\) kills its \(V\)-contribution (checker group X,
orders 1–200, plus the finite set argument). On \(S_n\),
\(\binom{n-b-1}{a-1}\ge1\), so \(k\) never vanishes — survival cannot
be lost to cancellation (group X, orders 1–60).

## 3. Corollaries

**Support law, all \(n\).** The universal form has \(x=1+u\) degree
exactly \(p=a+b\) — each factor contributes known \(x\)-degree with
nonzero edge coefficients — and \((1+u)\)-pole exactly \(n-1\). Hence

\[
\operatorname{supp} G=[-(n-1),\,p]\qquad\text{for ALL }n
\]

(certified unreduced on all 40 channels of orders 1–5, checker group X;
the edge-factor argument is order-independent).

**Fold law, all \(n\).** The diagonal-operator mechanism of
`rung4-foldrule.md` §2 is order-independent; its only order-dependent
input was the support law. Therefore, for every channel \((a,b)\) at
every tower order \(n\), \(p=a+b\):

\[
\text{closure at }(g,w_0)
\iff 2w_0+p\le0\ \ \text{and}\ \ g\ge n-2w_0,
\qquad
(\text{grade}_{\min},w_0^{\min})=\bigl(n+2\lceil p/2\rceil,-\lceil p/2\rceil\bigr).
\]

The rung ladder of `rung4-foldrule.md` §5 is now a theorem, not a
certified sample: rung \(n+1\) forces \((n+2\lceil n/2\rceil,-\lceil n/2\rceil)\).

**Census.** \(|S_n|=n(n+1)/2+1\): 2, 4, 7, 11, 16, 22, …

## 4. What is proved, and what is not

**Proved:** the universal form and explicit \(k\) for all \(n\) — base
and 40-channel reconfirmation machine-certified unreduced, induction
step symbolic and order-independent, recursion satisfaction
machine-verified to order 60 and hand-checked as a binomial identity;
the surviving set, extinction, and nonvanishing for all \(n\); the
support law and fold law for all \(n\); the Lah factorization (orders
1–60, integer-exact).

**Not proved (labeled):** the combinatorial interpretation of the Lah
factorization (what the ordered lists *are* in the tower) — open
question; the specialization-locus boundary — the form is certified in
the reduced ring with indeterminates, so its conclusions hold off the
loci \(\bar z=\bar z_k\), \(1+z_k\bar z=0\) (automatic generically; any
statement at special kinematics needs a separate argument); the rung-5
readout oscillation remains a *prediction* under the declared
fold-grade = readout-grade identification, as before.

## Verification

`uv run --with sympy python research/strominger/checkers/channel_closedform_checks.py`
— see `research/strominger/results/channel_closedform.json`.
