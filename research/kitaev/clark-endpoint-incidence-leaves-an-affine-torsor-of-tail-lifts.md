# Clark endpoint incidence leaves an affine torsor of tail lifts

## Question

Do the common-source Clark formulas determine the graph-valued tails needed
by the mixed Green polarization?

## Endpoint incidence

For a common holomorphic source transform (F), the two Clark endpoints are

\[
P=F+iaF',
\qquad
Q=F-iaF'.
\]

They obey the holonomic relation

\[
P-Q=ia(P+Q)'.
\]

Conversely,

\[
F=\frac{P+Q}{2},
\qquad
F'=\frac{P-Q}{2ia}.
\]

Thus the Clark pair faithfully records the first source jet when (a\ne0).
This is an endpoint theorem.

## Tail lifts

Let (mathcal S) be the common source module, (mathcal D) a half-line
graph carrier, and

\[
\tau:\mathcal D\longrightarrow\mathbb C
\]

the endpoint trace. An endpoint incidence is a map

\[
E:\mathcal S\longrightarrow\mathbb C^m.
\]

A graph-valued realization of that incidence is a lift

\[
J:\mathcal S\longrightarrow\mathcal D^m
\]

satisfying

\[
\tau^mJ=E.
\]

If one lift (J_0) exists, every other lift is

\[
J_0+N,
\]

where

\[
N:\mathcal S\longrightarrow(\ker\tau)^m.
\]

Hence compatible tail lifts form an affine torsor over

\[
\operatorname{Hom}(\mathcal S,(\ker\tau)^m).
\]

The endpoint Clark formulas choose no origin in this torsor.

## Effect on the Green relation

Let (Omega) be the alternating mixed Green form on the graph ports. Under
two kernel-valued changes of lift,

\[
J_+\mapsto J_++N_+,
\qquad
J_-\mapsto J_-+N_-,
\]

the pulled-back relation changes by

\[
\Omega(N_+,J_-)
+\Omega(J_+,N_-)
+\Omega(N_+,N_-).
\]

The previous compact-support witnesses show that these terms need not
vanish. Therefore the Green polarization is not invariant under the full
tail-lift torsor.

Scalar endpoint incidence, including its holonomic first-jet relation, cannot
determine the pulled-back Green form.

## What selects a physical lift

A physical origin in the torsor must be selected by additional source laws,
such as:

1. the exact first-order tail equation;
2. its forcing map from the labelled source;
3. decay or radiation conditions;
4. Fourier--Tate covariance;
5. bilateral reflection sewing;
6. cutoff naturality and completion continuity.

These laws may uniquely select a lift, leave a smaller torsor, or be
inconsistent. The scalar completed section cannot decide among those cases.

## Uniqueness criterion

Suppose a frozen source dynamics and boundary condition admit two lifts
(J_1,J_2). Their difference (N=J_1-J_2) lies in the endpoint kernel and
solves the homogeneous source dynamics. Therefore uniqueness is equivalent
to absence of a nonzero homogeneous, decaying, zero-endpoint tail compatible
with every covariance law.

This is the exact first audit for the theta lift. It is a boundary-value
uniqueness theorem, not an endpoint observability statement.

## Architectural consequence

There are now three distinct levels:

1. source jet incidence determines (P,Q);
2. a graph-valued lift determines the tail trajectories;
3. the alternating Green form evaluates relations between those trajectories.

Level one does not reconstruct level two. Level three is not invariant under
the unrestricted ambiguity left by level one.

## Falsifier certificate

    {
      "code": "clark_endpoint_does_not_determine_tail_lift",
      "same_endpoint_incidence": true,
      "lift_difference_in_trace_kernel": true,
      "green_relation_changed": true,
      "missing_selector": "source dynamics plus covariance and decay"
    }

## Disposition

The common Clark pair fixes the first source jet but leaves an affine torsor
of graph-valued tail lifts. The mixed Green relation is sensitive to that
torsor. The next source theorem must establish uniqueness, or classify the
residual homogeneous lift ambiguity, under the full theta tail dynamics.

## Claim boundary

This is an abstract lifting and uniqueness theorem instantiated by the known
endpoint kernel witnesses. It does not assert that the fully frozen theta
boundary-value problem has multiple lifts; that requires inserting its exact
forcing, covariance, decay, and sewing laws.
