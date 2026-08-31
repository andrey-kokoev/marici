# Reciprocal theta doubling is not yet adjoint completion

> **Status update.** The successor packet
> `the-retained-history-metric-now-constructs-the-adjoint-incidence-but-not-its-xi-characteristic.md`
> uses the retained half-density history and seam metrics to construct the
> bounded reverse incidence \(B^\dagger\). The obstruction below remains valid
> against obtaining it from reciprocal doubling alone. The current open gate
> is Xi-divisor compatibility of the paired pencil, not existence of the
> metric adjoint.

## Status

Exact typing and block-matrix obstruction. Two reciprocal forward-forced tail
systems do not become one symmetric system under a role-preserving sector
pairing. Adjoint completion requires an incidence-reversing duality with a
state-bearing reservoir.

## Two forward systems

The doubled tail equations have the form

\[
G_+'=-zG_+-B_+c_+
\]

and

\[
G_-'=\overline zG_--B_-c_-.
\]

Each sector therefore has a triangular operator

\[
A_+
=
\begin{pmatrix}
A_{0,+}&B_+\\
0&C_+
\end{pmatrix},
\qquad
A_-
=
\begin{pmatrix}
A_{0,-}&B_-\\
0&C_-
\end{pmatrix}.
\]

Reflection may relate \(A_{0,+}\) to \(A_{0,-}\) and \(B_+\) to \(B_-\), but
both incidences still point from a source port into a tail state.

## Role-preserving cross pairing

Let reciprocal sewing identify the tail sectors and source sectors through
nondegenerate pairings

\[
P_H:\mathcal H_-\longrightarrow\mathcal H_+^*
\]

and

\[
P_U:\mathcal U_-\longrightarrow\mathcal U_+^*.
\]

The combined pairing is block diagonal:

\[
P=
\begin{pmatrix}
P_H&0\\
0&P_U
\end{pmatrix}.
\]

Cross-adjointness requires

\[
PA_-=A_+^*P.
\]

The upper-right block of the left side is

\[
P_HB_-,
\]

while the upper-right block of the right side is zero. The lower-left blocks
give

\[
B_+^*P_H=0.
\]

If \(P_H\) is nondegenerate, then

\[
B_+=B_-=0.
\]

Thus nonzero reciprocal forward forcing is incompatible with
cross-adjointness under a role-preserving pairing.

## Reflection is not arrow reversal

Analytic reflection performs operations such as

\[
z\longmapsto-\overline z
\]

and exchanges the two valuation sectors. It does not automatically turn the
typed arrow

\[
\mathcal U\longrightarrow\mathcal H
\]

into

\[
\mathcal H\longrightarrow\mathcal U.
\]

The latter is dualization or adjunction, not ordinary sector transport.
Treating a reflected copy of \(B\) as \(B^*\) erases variance.

## Anti-diagonal pairing obstruction

One might instead try an anti-diagonal pairing that identifies a source port
in one sector with a tail state in the other. A nondegenerate such pairing
would require compatible dimensions and topologies.

At finite cutoff, the constant source channel has rank one while the retained
tail–seam state has rank growing with the label set. In completion, the tail is
infinite-dimensional. Therefore a rank-one source port cannot be the dual of
the complete tail state.

This is the same capacity obstruction previously found for fixed boundary
jets. Adjoint completion needs a state-bearing dual port whose effective rank
grows with the tail.

## Candidate full-history reservoir

The moving seam history is the smallest already constructed source object with
the required growing rank. A viable incidence pattern would be

\[
\mathcal H_{\mathrm{seam}}
\overset{B_-}{\longrightarrow}
\mathcal H_{\mathrm{tail}}
\]

together with

\[
\mathcal H_{\mathrm{tail}}
\overset{B_+^*}{\longrightarrow}
\mathcal H_{\mathrm{seam}}.
\]

The common endpoint trace is insufficient; the full history maps must be used.
Their graph domains and completion topology are part of the adjointness claim.

## Required categorical constructor

The missing operation is not another sector copy. It is a contravariant
constructor

\[
\mathfrak D:
(\mathcal U\overset B\longrightarrow\mathcal H)
\longmapsto
(\mathcal H\overset{B^\dagger}\longrightarrow\mathcal U)
\]

carrying:

- the source pairings;
- variance reversal;
- domain transport;
- boundary traces;
- completion topology;
- an involutivity cell.

Fourier–Tate sewing may implement this constructor only if these components
are derived explicitly. Equality of scalar functional equations is not enough.

## Finite matrix compiler

At cutoff \(X\), retain four separately typed matrices:

\[
B_{+,X}^{\mathrm{forward}},
\qquad
B_{-,X}^{\mathrm{forward}},
\qquad
B_{+,X}^{\dagger},
\qquad
B_{-,X}^{\dagger}.
\]

Test whether reciprocal sewing supplies comparison cells

\[
B_{-,X}^{\dagger}=B_{+,X}^*
\]

and

\[
B_{+,X}^{\dagger}=B_{-,X}^*
\]

in the declared source metrics. Do not identify a forward matrix with an
adjoint matrix merely because their scalar entries are conjugate.

## Hostile tests

The proposal fails under any of the following:

1. reciprocal sewing preserves arrow direction only;
2. the adjoint candidate factors through the rank-one constant port;
3. scalar traces agree while typed domains differ;
4. adjointness requires a cutoff-dependent whitening metric;
5. finite adjoints exist but their graph limits do not;
6. the full-history reservoir has an escaping partner at infinity;
7. two factorization paths give equal endpoint matrices but incompatible
   residue flags.

## Verdict

The doubled tail system currently contains two controlled forward evolutions,
not a conservative adjoint pair. Reciprocal analytic symmetry is necessary but
does not reverse incidence variance. The next construction must derive a true
adjoint-completion functor, most plausibly through the full seam-history
reservoir. Without it, selfadjointness and Lagrangian-domain selection cannot
begin.
