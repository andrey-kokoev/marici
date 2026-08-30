# The infinite Clark jet is one Hardy–Fock boundary object

## Question

Can the source authorize all spectral jets coherently without appending an
unbounded list of derivative sensors after observing the multiplicity of a
zero?

## Factorially normalized jet

Fix a parameter center \(z_0\) and a radius \(r>0\) on which the source
family is holomorphic. Define

\[
j_k(q)
=
\frac{r^k}{k!}\partial_z^kG(q,z_0),
\qquad k\ge0.
\]

The infinite jet is the sequence

\[
J_rG(q)=(j_0(q),j_1(q),\ldots).
\]

If \(G(q,\cdot)\) belongs to the Hardy space on the parameter disk, Parseval
gives the exact identity

\[
\sum_{k=0}^\infty
\frac{r^{2k}}{(k!)^2}
\left|\partial_z^kG(q,z_0)\right|^2
=
\frac{1}{2\pi}
\int_0^{2\pi}
\left|G(q,z_0+re^{i\theta})\right|^2d\theta.
\]

Thus the factorially weighted infinite jet is not an arbitrary collection of
sensors. It is the coefficient representation of one analytic boundary
function.

## Exact bounded shift dynamics

The source flow and all of its spectral derivatives satisfy

\[
(\partial_q+s)\partial_z^kG
+ki\,\partial_z^{k-1}G
=-\partial_z^kf.
\]

After factorial normalization,

\[
(\partial_q+s)j_k+ir\,j_{k-1}=-g_k,
\]

where

\[
g_k=\frac{r^k}{k!}\partial_z^kf
\]

and \(j_{-1}=0\).

Let \(S\) be the unilateral shift

\[
(Sj)_k=j_{k-1}.
\]

Then the entire prolongation is one bounded equation on
\(\ell^2(\mathbb N_0)\):

\[
(\partial_q+s)J_rG+ir\,S J_rG=-J_rf.
\]

Since \(\|S\|=1\), the nilpotent matrices at finite jet order converge to a
bounded Fock-type connection of norm \(r\). The troublesome factor \(k\) has
been exactly absorbed by the Taylor normalization.

## Germ faithfulness

If every component of \(J_rF(z_0)\) vanishes, then every derivative of the
holomorphic function \(F\) vanishes at \(z_0\). Hence \(F\) vanishes
identically on the connected parameter neighborhood.

Therefore one authorized infinite jet observes zeros of every finite
multiplicity without choosing the jet order after the fact. The only
remaining kernel is the zero analytic germ.

This is qualitative faithfulness. It does not supply a uniform lower bound
for a sequence of nonzero germs whose Hardy norms tend to zero.

## Translation is coherent but radius-losing

Parameter translation acts on the whole Taylor packet by the exponential of
the derivative connection. On a fixed Hardy disk, differentiation and
translation toward the boundary are not uniformly bounded at the same
radius.

The natural object is therefore a scale of nested disks:

\[
0<r<R<\operatorname{dist}(z_0,\partial\Omega).
\]

Cauchy estimates make translation and differentiation continuous from the
\(R\)-disk norm to the \(r\)-disk norm. A single fixed-radius Hilbert space is
too rigid for the full holomorphic constructor. The correct completion is a
Hardy–Fock rigging over radii, or equivalently the compact-open holomorphic
topology expressed in factorial jet coordinates.

On a compact parameter set \(K\) inside an open sector, one may choose a
uniform outer radius below the distance from \(K\) to the sector boundary.
The radius necessarily collapses as the compactum approaches a boundary or
singularity.

## Endpoint trace lifts to the Hardy packet

The source-native endpoint estimate controls \(G(0,z)\) by the scale-flow
graph energy at each parameter. Integrating that estimate around the
parameter circle and using the Hardy identity yields a jet-valued endpoint
bound:

\[
\|J_rG(0)\|_{\ell^2}^2
\le
C_K
\int_0^\infty
\|J_r(G+f)(q)\|_{\ell^2}^2\,dq,
\]

provided the pointwise graph estimate is uniform on the circle.

Thus the scale-flow trace and the spectral-jet observation are compatible in
one mixed topology:

- Sobolev or graph regularity in \(q\);
- Hardy–Fock regularity in \(z\).

This is the minimal abstract topology in which the full odd jet can reach the
endpoint continuously.

## Sheet action

The Clark coefficient \(a\) multiplies the odd first-jet coordinate and,
more generally, fixes the sheet orientation of the jet connection. Reversing
\(a\) conjugates the sign of the appropriate odd sector while preserving the
Hardy norm.

The positive jet norm is sheet-even, as every defect energy must be. The
signed jet vector retains the representation data needed for coherent sewing.
Discarding it after computing its norm returns to scalar equivalence and
loses constructor equivalence.

## Operational promotion criterion

Aspect's coherent sewing experiment supplies the correct interpretation. A
jet coefficient becomes an operative port only if parameter translation or
another calibrated constructor acts coherently on the whole packet.
Coefficientwise readout followed by classical comparison does not realize
the shift representation.

In the analytic model, the promotion test is:

1. the Taylor packet is derived from one source germ;
2. translation acts by the coherent jet representation;
3. truncation maps commute with the source flow;
4. the completed endpoint trace is continuous in the radius rigging.

## Hostile fixtures

### Unnormalized jets

Using \(\partial_z^kG\) directly leaves coupling coefficients \(k\), producing
an unbounded weighted shift on plain \(\ell^2\). Declaring this the completed
state without a domain is invalid.

### Fixed-radius translation

Demanding every holomorphic translation be bounded on one fixed-radius Hardy
space fails near its boundary. The repair is a nested-radius rigging, not an
invented uniform bound.

### Coefficientwise fake state

An arbitrary \(\ell^2\) sequence need not be the jet of the declared source
class if its radius and analytic compatibility are not fixed. Treating every
sequence as admissible can introduce false PBH modes.

### Qualitative faithfulness without uniform stability

The functions

\[
F_N(z)=N^{-1}z
\]

have nonzero first jets and are germ-faithful at every finite \(N\), while
their Hardy–Fock norm tends to zero. Completion-stable observability still
requires a normalized source lower bound.

## Disposition

There is a canonical abstract infinite-jet completion: the factorial Taylor
packet in a Hardy–Fock radius rigging. It converts the entire source-derived
Jordan tower into a bounded unilateral-shift connection and makes endpoint
trace continuity compatible with all finite multiplicities.

The remaining source-bearing gate is narrower:

1. establish that the completed theta/Tate family belongs to this mixed
   scale-flow and Hardy–Fock topology on sector compacts;
2. identify the jet-valued boundary output inside the colligation;
3. derive the passive defect identity;
4. prove a normalized observability margin that survives cutoff completion.

## Claim boundary

This packet proves an abstract Hardy-space and jet-normalization theorem. It
does not establish the required theta Hardy bounds, a global disk crossing
the sector boundary, passive sewing, or a uniform observability constant.
