# 2880 — Four Soft Compatibility Gates Do Not Determine the Readout

## Deutschian uniqueness conjecture

The completed soft construction satisfies:

1. full \(S_3\) chart descent;
2. compatibility with the moving physical \(a\)-cycle after pushforward;
3. invariance under source-normal regulator deformation;
4. source-oriented Leray monodromy.

A tempting stronger claim is that these four conditions uniquely determine
the pointed scalar readout.

## Hostile family

Let

\[
P(t)=\int_2^t I(s)\,ds
\]

be the source primitive and define

\[
P_c(t)=P(t)+c(t-2).
\]

For every constant \(c\):

- \(P_c(2)=0\);
- the correction is single valued and regular at \(t=0\);
- the logarithmic translation monodromy remains \(2\pi iL\);
- it transports through the chart atlas because \(t\) is the normalized
  invariant coordinate;
- it is added only after moving-fiber pushforward, so it does not revive the
  mistyped fixed-\(a\) construction.

Nevertheless,

\[
\operatorname{FP}(P_c)
=
\operatorname{FP}(P)-2c.
\]

The four-gate uniqueness claim is therefore false.

## Missing explanatory condition

The source does provide a stronger condition:

\[
dP=I(t)\,dt.
\]

If \(P+h\) obeys the same Gauss–Manin equation, then

\[
dh=0.
\]

The pointing condition \(h(2)=0\) then forces \(h=0\). Thus uniqueness
survives in the narrower and correctly typed form:

\[
\text{source-horizontal section}
+
\text{source endpoint pointing}
\Longrightarrow
\text{unique readout}.
\]

## Interpretation

Compatibility constrains the space of possible readouts but does not select
one. Selection comes from the dynamical transport law. No new carrier datum is
needed; the missing selector is the already existing sector-specific
Gauss–Manin connection.

## Durable artifacts

- `research/benincasa/check_soft_readout_uniqueness_falsifier.py`
- `research/benincasa/soft-readout-uniqueness-falsifier.json`

