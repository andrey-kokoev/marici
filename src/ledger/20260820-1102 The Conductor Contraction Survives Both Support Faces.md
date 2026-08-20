# 1102 — The Conductor Contraction Survives Both Support Faces

## Record

Entry 1101 showed that the generic anti-invariant conductor complex at the
second exceptional center is

\[
[R\xrightarrow{2}R].
\]

Its supported derived restrictions are now computed on the two degeneration
faces and their intersection.

Sequence claim: `seqclaim-f7fe65b2e7ee66f40bf53740`.

## Explicit contraction

Over characteristic zero, define

\[
h=\frac12.
\]

Then

\[
dh=1,
\qquad
hd=1.
\]

The contraction contains neither \(s\) nor \(B-1\).  It is therefore preserved
by ordinary and derived base change to

\[
s=0,
\qquad
B-1=0,
\qquad
s=B-1=0.
\]

The durable checker verifies the same chain homotopy on all three supported
restrictions.

## Consequence

The anti-invariant normalization/conductor complex has zero cohomology both
generically and on every support face selected by the first smoothing
coefficient:

\[
\boxed{
H^\bullet_-
\left(
L i^*[R\xrightarrow{2}R]
\right)=0.
}

Thus neither a face Tor class nor a codimension-two conductor extension
survives.

## Deutsch--Popperian verdict

The conjecture that the vanishing of \(U=-16s(B-1)\) might obstruct the
conductor contraction is falsified.  The conductor-descent mechanism closes
uniformly over both existing supports.

This does not eliminate vanishing-cycle data of the total family

\[
XY=ps(B-1).
\]

It types that data correctly: any residual belongs to the sector-specific
nearby/vanishing-cycle coefficient object, not to normalization descent and
not to a new carrier cell.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u2v0_conductor_complex.rs`;
- `research/benincasa/rank12-u2-v0-joint-newton.json`.

Epistemic graph admission:
`ev-000000000801-9c8d134f-8ad2-4540-b584-8884c01a5b94`.

## Next falsifier

Construct the iterated nearby-cycle object of the local node
\(XY=ps(B-1)\), preserving the three labelled factors \(p,s,B-1\).  Compare
its face maps with the already frozen parameter-exceptional, \(q=0\), and
\(L_1\) Gysin maps.  A residual mapping-cone class would be coefficient
excess; only failure to type those three factors on the existing incidence
carrier would challenge H2.
