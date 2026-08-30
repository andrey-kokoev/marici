# RH index typing separates spectral displacement, refinement, composition, and time

## No temporal interpretation is designated

The current RH construction does not designate any variable or arrow as
physical time. Four structures that can receive a temporal interpretation in
another realization must first remain separately typed here.

## Spectral displacement

The spectral base is a complex domain \(S\) with coordinate \(s\). A path

\[
\gamma:[0,1]\longrightarrow S
\]

is a geometric probe of a connection. Its parameter \(\lambda\) is an
arbitrary path coordinate. Reparameterizing \(\lambda\) does not change
parallel comparison. No temporal role for \(\lambda\) is currently declared.

On the critical seam one may write \(s=1/2+it\). Within the present
construction, \(t\) denotes spectral height. A temporal interpretation would
require an additional realization map.

## Cutoff refinement

Prime cutoffs form a directed index category. An arrow \(X\to Y\) means that
the labelled packet at cutoff \(X\) is included or refined into the packet at
cutoff \(Y\). No chronological order is part of this arrow as currently typed.

Limits over this category are completion statements. Identifying them with
long-time limits would require a separate functor.

## Constructor composition

A constructor word

\[
F\circ C_r\circ\cdots\circ C_1
\]

is algebraic composition in a typed partial category. Its order records domain
and dependency constraints. It does not assert chronological execution unless
a separate temporal realization functor is supplied.

## Chain degree

In an incidence cone

\[
V\oplus H\xrightarrow{D}B,
\]

the two positions are chain degrees. The differential records incidence
mismatch. No temporal semantics for the differential or contracting homotopy
has been supplied.

## Operative versus static coherence

The earlier word `dynamic` was intended only to distinguish a coherence
morphism or natural transformation from a declared equality of objects. That
word is too temporally suggestive here. The corrected term is `operative
coherencer`:

- it is a typed morphism acting on retained comparison ports;
- it may be natural over spectral and cutoff index categories;
- it carries no physical-time semantics without an additional realization.

A genuine dynamical interpretation would require an additional functor from a
time category into the RH construction. No such functor has been supplied, but
the present typing does not prohibit one.

## Full-fiber test for a temporal realization

Let

\[
q:V\longrightarrow G_{\mathcal T}
\]

be the current target-relative germ quotient, and let

\[
\tau:V\longrightarrow\mathcal P
\]

be a proposed realization into physical processes. The existing germ remains
faithful for the enlarged target family exactly when \(\tau\) is constant on
every full \(q\)-fiber:

\[
q(v)=q(w)
\Longrightarrow
\tau(v)=\tau(w).
\]

If this holds, \(\tau\) factors through the existing germ and adds an
interpretation without adding source distinctions. If it fails, temporal
realization is a genuinely new target operation and the marked germ must be
refined before that realization is admitted.

This is the precise answer to whether time was already implicit. Some temporal
realizations may factor through the present structure; others may detect a
fiber direction the present RH target family intentionally discarded. The
current mathematics alone does not choose between them.

## Correct connection equation

Let \(A_X(s)\,ds\) be a determinant-line connection one-form. Along a spectral
path \(\gamma\), parallel comparison satisfies

\[
\frac{dT_X}{d\lambda}
=
A_X(\gamma(\lambda))
\gamma'(\lambda)
T_X(\lambda).
\]

Its conformal scale obeys

\[
\log\rho_X(1)-\log\rho_X(0)
=
\operatorname{Re}
\int_\gamma A_X(s)\,ds.
\]

This is geometric parallel comparison on parameter space. Calling it temporal
evolution would require an additional realization that identifies the path
category with physical processes.

## DPC verdict

The RH categorical machinery is temporally uncommitted as currently defined.
Spectral paths, cutoff refinements, constructor words, and chain degrees are
four different index types. A physical-time claim requires a new
source-authorized realization functor and cannot be inferred from the existing
notation; neither is it excluded by that notation.

`check_rh_target_relative_marked_germ.py` verifies both cases: one proposed
temporal realization factors through the existing joint signature, while a
second reads a discarded hidden fiber and therefore forces germ refinement.
