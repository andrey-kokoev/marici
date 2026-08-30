---
id: 20260827-3281
date: 2026-08-27
status: replicated-source-direct-modular-theorem
---

# 3281 — The Total-Energy Principal Part Is Canonical Modulo the e6 Logarithmic Row

## Question

Entry 3274 source-authorized the unique (u^{-2}) term of the reconstructed
rank-twelve marked extension.  Does the same complete Laurent recurrence fix
the twelve simple-pole coordinates at (u=0)?

Use the ordered target basis

\[
(e_6,e_7,e_8,e_9)
\]

and source basis

\[
(q_0,q_1,q_2).
\]

## Source-direct result

The calculation retains all three source right-hand sides against one common
372-coordinate primitive system.  Thus no separate primitive section is
chosen for any (q_i).

The complete second-order matrix is fixed:

\[
B_u^{(-2)}=
\begin{pmatrix}
-1/8&0&0\\
0&0&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]

At simple order, the source recurrence fixes exactly the final three rows:

\[
B_u^{(-1)}\bmod\langle e_6\rangle=
\begin{pmatrix}
\dfrac{(v-4)^2}{8(v-2)^2}&
-\dfrac{v-4}{4(v-2)}&
\dfrac{v-4}{4(v-2)}\\[3mm]
-\dfrac{v-4}{v(v-2)^2}&
\dfrac{2}{v(v-2)}&
-\dfrac{2}{v(v-2)}\\[3mm]
\dfrac{v-4}{v(v-2)^2}&
-\dfrac{2}{v(v-2)}&
\dfrac{2}{v(v-2)}
\end{pmatrix},
\]

where the displayed rows are (e_7,e_8,e_9).

Every displayed coordinate is fixed by the source recurrence and equals the
corresponding reconstructed-candidate coefficient.

The (e_6)-valued simple row is not fixed.  The candidate chooses

\[
\left(
\frac{9v+2}{16(v-2)},
\frac34,
\frac34
\right),
\]

but the complete source recurrence permits changing all three entries through
the residual primitive freedom.  These numbers are therefore not promoted to
source invariants.

## Replication

At (v=5), the fixed simple rows are

\[
\begin{pmatrix}
1/72&-1/12&1/12\\
-1/45&2/15&-2/15\\
1/45&-2/15&2/15
\end{pmatrix}.
\]

They replicate at both large field primes.  At the independent fiber (v=7),
they become

\[
\begin{pmatrix}
9/200&-3/20&3/20\\
-3/175&2/35&-2/35\\
3/175&-2/35&2/35
\end{pmatrix},
\]

again agreeing coefficientwise with the candidate.  Every recurrence has
rank 655.

## Sign audit of Entries 292--293

After substituting

\[
X_1=1,
\qquad
X_2=(v-2)/2
\]

at (u=0), the fixed (e_7,e_8,e_9) row for (q_0) is the negative of the
tail recorded in Entries 292--293, just as the fixed (e_6u^{-2}) coefficient
is the negative of their recorded value.

The discrepancy is therefore a uniform frame or connection sign, not an
isolated (e_6) accident.  The current source presentation and the current
candidate agree throughout the gauge-invariant principal part.  The earlier
entries remain valid for location, rank, Gysin kernel, and Rees order, but
their displayed coefficients require an explicit sign bridge before reuse.

## Structural classification

Let

\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle
\]

be the final-block algebraic plane.  The total-energy principal part now has
the following typing:

- its (u^{-2}e_6) term is source-canonical;
- its logarithmic image in
  \(\mathcal A_{--}/\langle e_6\rangle\) is source-canonical;
- its logarithmic lift back to \(\mathcal A_{--}\) is not canonical;
- the candidate's (e_6) row is a splitting choice;
- the elliptic quotient remains zero;
- no new carrier support is required.

Thus the marked extension is more canonical than a generic interpolated
matrix but less canonical than a fully framed connection.  The invariant
object at total energy is the filtered extension class modulo the existing
Kummer line, not the candidate's complete scalar matrix.

## Next falsifier

Determine whether the source-normalized Kummer connection and Entry 293's
Rees gauge select a unique (e_6) logarithmic lift in the current sign
convention.  If they do, compare that derived row with the candidate.  If they
do not, permanently classify the row as triangular-gauge presentation data
and proceed to the next support factor.

## Durable artifacts

- source recurrence checker:
  `research/benincasa/checkers/audit_marked_extension_source_laurent_lead.py`;
- candidate comparison and replication checker:
  `research/benincasa/checkers/audit_marked_extension_source_laurent_replication.py`;
- aggregate packet:
  `research/benincasa/results/marked_extension_source_laurent_lead.json`;
- allocator claim: `seqclaim-b19e4450ccad6b3f51259e81`.
