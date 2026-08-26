# Response authority is a connection on a context-indexed state family

## Problem

A fixed readout determines a value in one context. A response law compares nearby source states, epochs, calibrations, or experimental frames.

Those states generally live in different fibers. Before subtraction, differentiation, replay, or composition is meaningful, the fibers must be identified by an authorized transport.

Therefore the missing first-jet constructor is a connection.

## Context-indexed state

Let \(c\) range over contexts such as:

- calibration epoch;
- detector configuration;
- authority epoch;
- generator basis;
- nuisance model;
- reference frame;
- software schema version.

Let \(X_c\) be the source-state fiber and \(Y_c\) the readout fiber at context \(c\). A context-local instrument is

\[
F_c:X_c\longrightarrow Y_c.
\]

A captured observation supplies

\[
x_c\in X_c,
\qquad
y_c=F_c(x_c)\in Y_c.
\]

It does not identify \(X_c\) with \(X_{c'}\) or \(Y_c\) with \(Y_{c'}\).

## Connection data

A comparison between contexts requires transports

\[
P^X_{c\to c'}:X_c\longrightarrow X_{c'}
\]

and

\[
P^Y_{c\to c'}:Y_c\longrightarrow Y_{c'}.
\]

The discrete covariant response is the naturality defect

\[
\nabla_{c\to c'}F
=
F_{c'}P^X_{c\to c'}
-
P^Y_{c\to c'}F_c.
\]

When this defect vanishes, the instrument commutes with the declared context transport.

When it does not vanish, the defect is a real response or calibration change. It cannot be inferred from the endpoint values alone.

## Why a zero-jet cannot construct the connection

Suppose only \(F_c(x_c)\) and \(F_{c'}(x_{c'})\) are known. Many transports \(P^X,P^Y\) can relate the fibers while reproducing the same endpoints.

Consequently:

- fixed templates do not determine coupling derivatives;
- captured calibration records do not determine phase-update laws;
- serialized authority claims do not determine current admissibility;
- matching output bytes do not determine constructor coherence.

The connection is additional source structure.

## Optical epoch witness

Aspect's dual-clock interlock supplies an exact finite example. The fixed ordered record \((1,2)\) is compatible with:

- source \(17\) in epoch \(0\);
- source \(1\) after a phase-frame shift.

The ambiguity is not detector noise. The two claims use different fiber identifications.

A separately certified zero reference constructs the live phase transport. Without it, cross-epoch source attribution is undefined.

## Cross-run splice

Suppose a physical record is produced in context \(c_0\), but decoded using a map admitted only in context \(c_1\).

Each marginal component may be valid:

- source preparation;
- physical record;
- calibration;
- decoder;
- claimant.

The composed claim can still be false because the diagram lacks a common transport witness.

The required square is

\[
P^Y_{c_0\to c_1}F_{c_0}
=
F_{c_1}P^X_{c_0\to c_1}.
\]

Cross-run splicing uses one side of this equation without proving the other.

## Live authority as a connection

Sontag's twin-world theorem is the same structure with authority fibers.

A portable closure carries captured data and an authority claim. Invocation occurs in the current target epoch. The live authority observer supplies the transport from the captured request context to the current execution context.

A stale epoch means the required transport is not admitted. Copying the closure does not refresh it because copying a fiber value does not construct a connection.

## Flavor instrumentation

A fixed HHH detector template lives in one phenomenological context. A portal source response requires transport from \((\lambda_s,z)\) into:

1. generator basis weights;
2. event kinematics;
3. detector templates;
4. nuisance-bearing likelihood bins.

Each arrow is a connection component. Public downstream classifiers and fixed likelihood templates do not reconstruct the missing upstream transports.

An executable surrogate repository defines a choice-relative connection. It becomes an admitted physical instrument only when a publication-bound manifest and validation join identify it with the experimental context.

## Coherence

For three contexts \(c_0,c_1,c_2\), connection composition requires

\[
P_{c_1\to c_2}P_{c_0\to c_1}
=
P_{c_0\to c_2}
\]

on the declared domain.

A nonzero loop defect is contextual holonomy. It records calibration drift, schema migration ambiguity, or authority rebinding failure.

Coherence cannot be fitted from matching final readouts. It requires source-authorized comparison cells.

## Constructor contract

A response-bearing system must declare:

1. context base;
2. source and readout fibers;
3. transport maps;
4. temporal and authority scope;
5. connection coherence;
6. calibration reference;
7. naturality residual;
8. smallest splice falsifier.

A value-only record lacks the type required for response claims.

## Finite falsifier

Use two contexts with identical captured record \(y\) and two different source transports:

\[
P_A^X=I,
\qquad
P_B^X=R,
\]

where \(R\ne I\), while the decoder transport is held fixed.

If both paths reproduce the released endpoint but assign different current sources, the endpoint does not determine the connection.

A conforming compiler rejects the cross-context claim until one transport is independently certified.

## Disposition

A first jet is a value plus a rule for comparing neighboring fibers. In context-dependent systems, that rule is a connection.

Response authority is therefore not stored in the observation. It resides in the source-authorized transport that makes variation, replay, and composition well-typed.
