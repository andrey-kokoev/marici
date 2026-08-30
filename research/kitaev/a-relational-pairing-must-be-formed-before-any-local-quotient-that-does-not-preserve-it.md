# A relational pairing must be formed before any local quotient that does not preserve it

## Question

When does separate completion of two local sector objects destroy a
relational witness that an outer sewing operation needs?

## Exact descent theorem

Let

\[
q_+:V_+\longrightarrow Q_+,
\qquad
q_-:V_-\longrightarrow Q_-
\]

be surjective local completion or quotient maps, with kernels \(K_+\) and
\(K_-\). Let

\[
\beta:V_+\times V_-\longrightarrow\mathbb C
\]

be a bilinear or sesquilinear relational pairing.

There exists a unique pairing

\[
\overline\beta:Q_+\times Q_-\longrightarrow\mathbb C
\]

satisfying

\[
\beta=\overline\beta\circ(q_+\times q_-)
\]

if and only if

\[
\beta(K_+,V_-)=0
\]

and

\[
\beta(V_+,K_-)=0.
\]

This is the exact criterion for whether relational sewing may occur after
local quotient completion.

## Proof

Necessity is immediate. If \(k_+\in K_+\), then \(q_+(k_+)=0\), so any
descended pairing must satisfy

\[
\beta(k_+,v_-)=\overline\beta(0,q_-(v_-))=0.
\]

The second condition is identical.

For sufficiency, define

\[
\overline\beta(q_+(v_+),q_-(v_-))=\beta(v_+,v_-).
\]

The two annihilation conditions make this independent of representatives.
Surjectivity gives uniqueness.

## Irrecoverability theorem

If either annihilation condition fails, no later operation depending only on
\((Q_+,Q_-)\) can reconstruct \(\beta\). Two source pairs differing by a
discarded kernel vector have identical local completed states and different
relational values.

Adding more computation after the quotient does not help. The missing datum
is not computational complexity; it is absent from the functor's input.

This is the formal meaning of retaining an occurrence key until the outer
mate.

## Common-kernel character

Suppose a shared source module \(V\) has two local observations

\[
L_+:V\longrightarrow Q_+,
\qquad
L_-:V\longrightarrow Q_-.
\]

Any character vector

\[
k\in\ker L_+\cap\ker L_-
\]

is invisible to every downstream construction factoring through

\[
(L_+,L_-):V\longrightarrow Q_+\oplus Q_-.
\]

An outer witness can detect \(k\) only if an additional source map \(R\)
satisfying

\[
Rk\ne0
\]

is retained before local totalization.

## Architecture-selection rule

This yields a precise choice between two topologies.

### Local-totalization topology

Complete each sector first and then sew:

\[
V_+\times V_-
\longrightarrow
Q_+\times Q_-
\longrightarrow
Q_{\rm global}.
\]

This is valid only when every required global pairing descends through the
local quotients.

### Relational-first topology

Retain each local carrier and its witness, form the cross relation, and only
then complete:

\[
(V_+,V_-,\beta)
\longrightarrow
Q_{\rm relational}.
\]

This is required whenever \(\beta\) is nonzero on a local kernel.

Aspect's shorthand \(2(2+1)+1\) describes this second pattern: two local
witness–mate systems retain their shared occurrence key, and one outer mate
consumes the relation. The notation is architectural rather than a universal
dimension count.

## Theta/Clark application

The two reciprocal theta sectors have local scalar and endpoint projections,
while the mixed-sheet Green numerator contains an alternating cross
polarization. That cross term is a reflection coboundary and carries an
oriented transverse jet.

If either local quotient discards the even–odd occurrence label on which this
alternating form depends, the cross polarization cannot be reconstructed
from the two completed scalar sectors.

Therefore the signed Clark construction must test descent before quotienting:

\[
\beta(K_+,V_-)=0,
\qquad
\beta(V_+,K_-)=0.
\]

If these identities fail, the mixed numerator and the signed kernel form must
be assembled on the unquotiented two-sector carrier. Separate positive
completion of each sector is then structurally premature.

## Radical warning

For a signed kernel form, the local radical of one restricted sector need not
be radical for the complete cross-sector form. A vector \(k_+\) may satisfy

\[
\beta_+(k_+,V_+)=0
\]

while

\[
\beta_{\rm cross}(k_+,V_-)\ne0.
\]

Quotienting by the local radical would destroy a globally nondegenerate
hyperbolic pair.

Hence the radical must be computed after assembling every source-authorized
cross term. Radical formation and relational sewing do not generally
commute.

## Smallest finite hostile

Let \(V_+=V_-=\mathbb R^2\), and let each local quotient retain only the first
coordinate:

\[
q_\pm(x,y)=x.
\]

Define

\[
\beta((x,y),(u,v))=yv.
\]

Both second-coordinate vectors vanish locally, but their cross pairing is
nonzero. No function of the retained coordinates \(x,u\) can recover \(yv\).

This is the minimal exact model of a relational character erased by both
local completions.

## Scalar comparison is insufficient

Two local scalar outputs may agree, and their post hoc product or correlation
may be computable, while the coherent cross pairing remains absent. A
classical comparison of quotient values is not the same constructor as a
bilinear form on the pre-quotient carriers.

Aspect's coherent parity experiment operationalizes this difference:
irreversible local record formation destroys the joint visibility, whereas
coherent retention and uncomputation restore it.

## Completion-stable form

For cutoff families, descent must hold uniformly and naturally:

\[
\beta_N(K_{+,N},V_{-,N})=0,
\qquad
\beta_N(V_{+,N},K_{-,N})=0,
\]

with compatible quotient maps and a closed limiting pairing.

Approximate annihilation is not exact descent. If the residual tends to zero
without a uniform bound, the limiting pairing may still be discontinuous or
lose its occurrence key.

## Disposition

The order of construction is now decided by an exact kernel test. Local
completion may precede global sewing only for pairings that annihilate every
local kernel. Otherwise the cross relation must be formed first.

For theta, the next finite calculation is to evaluate the mixed Green or
signed Clark form on the local radicals of the two sector trace maps. A
single nonzero value forces relational-first completion.

## Claim boundary

This packet proves the abstract descent theorem and gives a conditional theta
application. It does not yet compute the actual theta local radicals or their
mixed pairing.
