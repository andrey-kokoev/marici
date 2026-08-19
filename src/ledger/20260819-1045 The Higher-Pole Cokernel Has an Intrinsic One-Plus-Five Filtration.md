# The Higher-Pole Cokernel Has an Intrinsic One-Plus-Five Filtration

## Intermediate map gate

Entry 1039 finds the cumulative exact-valuation ranks

\[
7\longrightarrow8\longrightarrow13
\]

as the higher-\(K\)-pole de Rham and principal strata are admitted.  Rank
growth alone does not exclude a transient class that is later killed and
replaced.  The two intermediate quotient maps were therefore computed
directly.

Each complete source exact-valuation basis was exported, embedded blockwise
into the next nested presentation, reduced by the target's valuation-zero
and valuation-one subspace, and expressed in the target exact-valuation-two
quotient.

## First transition

For

\[
E_2(F_0)\longrightarrow E_2(F_1),
\]

where \(F_1\) adds the \(k=2\) de Rham relations, the result is

\[
\operatorname{rank}=7,
\qquad
\dim\ker=0,
\qquad
\dim\operatorname{coker}=1.
\]

All seven source representatives have zero reduction remainder.

## Second transition

For

\[
E_2(F_1)\longrightarrow E_2(F_2),
\]

where \(F_2\) then adds the \(k=2\) principal relations, the result is

\[
\operatorname{rank}=8,
\qquad
\dim\ker=0,
\qquad
\dim\operatorname{coker}=5.
\]

Again every source representative has zero reduction remainder.

Thus the complete sequence is genuinely injective:

\[
\boxed{
E_2(F_0)\hookrightarrow E_2(F_1)\hookrightarrow E_2(F_2),
\qquad
7\hookrightarrow8\hookrightarrow13.
}
\]

## Intrinsic associated graded

Let

\[
Q_6=E_2(F_2)/E_2(F_0).
\]

The intermediate image defines a canonical filtration

\[
0\subset Q_1\subset Q_6
\]

with

\[
\boxed{
\dim Q_1=1,
\qquad
\dim(Q_6/Q_1)=5.
}
\]

Hence the higher-pole cokernel has intrinsic associated graded dimensions

\[
\boxed{1+5}.
\]

The one-dimensional de Rham class survives principal coherence; it is not a
transient rank artifact.  The temporary first-normal jump
\(5\to15\to7\) occurs in the lower valuation structure without killing this
exact-valuation-two class.

## Boundary and next test

No canonical splitting

\[
Q_6\simeq Q_1\oplus Q_5
\]

has been constructed.  The result is a filtered extension, not a direct-sum
decomposition.

The next typed question is how the canonical tangential connection acts on

\[
0\subset Q_1\subset Q_6.
\]

If \(Q_1\) is horizontal, the extension class lies in a rank-five quotient
connection.  If the connection mixes \(Q_1\) into the five-plane, then the
six directions form an indecomposable higher-pole coefficient block.  That
test must use Entry 1018's exact source derivative, not a projected finite
connection matrix.

## Durable verification

- staged exporter:
  `research/nima/export_triangle_wall_dual_rows.py`;
- transition-capable rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- result packet:
  `research/nima/triangle-wall-kdepth3-rank.json`;
- allocator claim: `seqclaim-eb1effe380e7fd94c33b90e2`.
