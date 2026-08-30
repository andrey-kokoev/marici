# The odd prime incidence is an exact Köthe automorphism despite its compact Hilbert realization

## Diagonal odd incidence

On prime-labelled coordinates, let

\[
D_{\mathrm{odd}}e_p
=
a_pe_p,
\qquad
a_p
=
2\sin\left(\frac{2\pi}{p}\right)
\]

for odd primes.

Every coefficient is nonzero. On the unweighted prime Hilbert space, \(D_{\mathrm{odd}}\) is Hilbert–Schmidt, compact, and not bounded below.

That is not its source-topological status.

## Two-sided coefficient estimate

For \(p\ge5\),

\[
0<\frac{2\pi}{p}\le\frac{\pi}{2}.
\]

Using

\[
\frac{2x}{\pi}\le\sin x\le x
\]

on this interval gives

\[
\frac8p
\le
a_p
\le
\frac{4\pi}{p}.
\]

The exceptional prime \(p=3\) contributes one fixed nonzero coefficient. Hence there are constants \(c,C>0\) such that

\[
\frac cp
\le
|a_p|
\le
\frac Cp
\]

for every odd prime.

Therefore

\[
|a_p^{-1}|
\le
C' p.
\]

## Projective exponential source

Let

\[
\mathcal A_{\exp}^{\mathrm{odd}}
=
\bigcap_{\delta>0}
\ell^1(\mathbb P_{\mathrm{odd}},p^\delta),
\qquad
q_\delta(c)=\sum_p|c_p|p^\delta.
\]

Then

\[
q_\delta(D_{\mathrm{odd}}c)
\le
Cq_\delta(c),
\]

while

\[
q_\delta(D_{\mathrm{odd}}^{-1}c)
\le
C'q_{\delta+1}(c).
\]

Thus

\[
D_{\mathrm{odd}}:
\mathcal A_{\exp}^{\mathrm{odd}}
\longrightarrow
\mathcal A_{\exp}^{\mathrm{odd}}
\]

is a continuous linear automorphism.

The inverse loses one polynomial order, but every such order is already present in the projective source topology.

## Euler-loaded incidence

After primitive half-density loading,

\[
D_{\mathrm{Euler,odd}}e_p
=
b_pe_p,
\qquad
b_p=p^{-1/2}a_p.
\]

The coefficient comparison becomes

\[
c p^{-3/2}
\le
|b_p|
\le
C p^{-3/2}.
\]

Hence

\[
q_\delta(D_{\mathrm{Euler,odd}}c)
\le
Cq_\delta(c)
\]

and

\[
q_\delta(D_{\mathrm{Euler,odd}}^{-1}c)
\le
C'q_{\delta+3/2}(c).
\]

Therefore the trace-class Hilbert realization is also an exact automorphism of the projective exponential source.

## Three simultaneous truths

The odd incidence now has three distinct, compatible classifications.

### Source topology

\[
D_{\mathrm{odd}},
D_{\mathrm{Euler,odd}}
\in
\operatorname{Aut}(\mathcal A_{\exp}^{\mathrm{odd}}).
\]

There is no source kernel, range defect, or lost prime label.

### Hilbert determinant topology

\[
D_{\mathrm{odd}}\in\mathcal S_2\setminus\mathcal S_1,
\qquad
D_{\mathrm{Euler,odd}}\in\mathcal S_1.
\]

The Euler-loaded map is suitable for determinant construction.

### Hilbert Green topology

Both operators are compact and have minimum modulus zero. Neither is coercive on the full prime Hilbert carrier.

No one classification may be substituted for another.

## Consequence for passive dilation

The open valuation–Fock passive-dilation slot must declare its ambient category.

If it asks for source-level reversible transport, the odd incidence passes on the Köthe carrier.

If it asks for a determinant-class crossing, the Euler-loaded incidence passes.

If it asks for Hilbert-space losslessness or a uniform Green lower margin, the same incidence fails.

Thus “passive dilation exists” is ill-typed until its source, determinant, and energy geometries are separated.

## Completion naturality

Prime cutoffs commute with the diagonal incidence:

\[
P_XD_{\mathrm{odd}}
=
D_{\mathrm{odd}}P_X.
\]

Since finite packets are dense in every Köthe seminorm,

\[
P_XD_{\mathrm{odd}}c
\longrightarrow
D_{\mathrm{odd}}c,
\]

and similarly for the inverse on each fixed source vector.

The completion is exact in the projective topology even though inverse norms on finite Hilbert cutoffs diverge.

## Dyadic attachment

The prime \(2\) requires a deeper-conductor odd pair. Once one nonzero dyadic coefficient is fixed by the local source convention, it contributes only a finite-dimensional direct summand.

It does not change the all-prime topology or ideal thresholds.

## Hostiles

1. Infer source noninvertibility from Hilbert compactness.
2. Infer Hilbert coercivity from Köthe invertibility.
3. Infer an ordinary determinant from source automorphism alone.
4. Treat the one-order or \(3/2\)-order inverse shift as an unbounded source operation.
5. State passive dilation without naming its ambient topology and energy form.

## Verdict

The canonical odd prime incidence is not lost at completion. It is an exact automorphism of the projective exponential source, and its Euler-loaded realization is trace class.

What fails is specifically Hilbert coercivity on the full labelled carrier. This sharpens the remaining passive-dilation problem from existence to compatibility among the source automorphism, determinant ideal, and Green energy geometries.
