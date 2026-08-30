# Theta additive-time positivity requires a coupled source completion

Status: prospective source gate; no Riemann-hypothesis claim

## Typed target

The live reflection object is the additive-time pair

\[
K_{t_0}(s,u)=\Theta(t_0+s+u),
\qquad
K^+_{t_0}(s,u)=-\partial_t\Theta(t_0+s+u).
\]

Positivity of both kernels is the ordinary-plus-shifted Stieltjes hierarchy.
It produces the positive multiplication/Jacobi operator after taking the GNS
radical quotient.  The smooth reflected compression \(P_+C_kRP_+^*\) is a
different operator and is already excluded by its excessively sparse
Fredholm spectrum.

## The source obstruction appears before any large determinant

The completed inverse-Laplace source decomposes schematically as

\[
\Theta=K_{\rm endpoint}+K_{\rm gamma}+K_{\rm prime}.
\]

The endpoint term is

\[
K_{\rm endpoint}(t)=e^{t/4}=e^{-t(-1/4)}.
\]

Its ordinary additive-time kernel is rank-one positive, but its shifted
kernel is

\[
-\partial_t e^{(t_0+s+u)/4}
=-\frac14e^{(t_0+s+u)/4},
\]

which is negative already on a \(1\times1\) Gram matrix.  Consequently no
valid construction can declare the endpoint, gamma, and prime packets to be
orthogonal positive summands of the desired Hilbert space.

## Required completion datum

The endpoint calculation proves that the labelled pieces cannot enter the
final positive object as a direct sum of independently positive subobjects.
It does **not** decide how completion repairs them.  Two typed mechanisms
remain admissible:

1. a nonorthogonal coupled quadratic form

\[
\mathcal Q_{\rm comp}
=
\begin{pmatrix}
Q_{\rm endpoint}&C_{e\gamma}&C_{ep}\\
C_{e\gamma}^*&Q_{\rm gamma}&C_{\gamma p}\\
C_{ep}^*&C_{\gamma p}^*&Q_{\rm prime}
\end{pmatrix},
\]

   whose off-diagonal blocks are derived from the same completed theta sewing
   or functional equation; or
2. a source-derived pushforward/quotient that combines the labelled scalar
   packets *before* positivity is imposed, so the endpoint line never embeds
   as an independent final subobject.

In either case the pushed-forward scalar kernel must equal the fixed \(K\),
while its shifted form must remove the endpoint's forbidden
negative-generator direction. Only then may one take the GNS radical quotient
and read off a positive generator.

This makes the proof obligation finite in type, though not finite in rank:

1. derive the coupling or pushforward without zero locations or fitted
   positivity;
2. prove compatibility with additive-time composition;
3. prove that forgetting the source labels returns the exact fixed
   \(\Theta\);
4. prove positivity of the completed ordinary and shifted forms;
5. show that the endpoint negative line either fails to descend independently,
   belongs to the completed radical, or is canceled by a source-derived
   coupling.

## Deutsch--Popperian conjecture

\[
\boxed{
\begin{minipage}{0.82\linewidth}
The completed theta functional equation supplies a canonical
endpoint--gamma--prime sewing or pushforward. Its shifted additive-time GNS
quotient removes exactly the endpoint's negative-energy direction and leaves
a positive generator whose squared resolvent is \(H'\).
\end{minipage}}
\]

The conjecture explains why completion is mathematically active: completion
does not merely add scalar correction terms.  It provides the coherence by
which individually inadmissible source pieces can descend to one admissible
coefficient object.

## First attack: ordinary augmentation is insufficient

There is already a canonical labelled-to-scalar map,

\[
\epsilon(f_e,f_\gamma,f_p)=f_e+f_\gamma+f_p.
\]

It passes the forgetting and additive-time composition tests by linearity and
reproduces the fixed completed \(\Theta\). This does **not** establish the
conjecture. Asking whether the shifted scalar image of \(\epsilon\) is
positive is just the original RH-equivalent Stieltjes gate.

Therefore ordinary augmentation is a necessary baseline, not the missing
explanation. The conjecture remains progressive only if the completed source
supplies at least one additional independently checkable structure, such as:

- a positive dilation whose compression is the augmented scalar form;
- a source identity that factors every shifted Gram form;
- a canonical radical/coisotropic reduction that removes the endpoint
  direction before positivity is asserted; or
- a local-to-global positivity theorem whose hypotheses are separately
  verified on the completed source operations.

Without such extra structure, “completion cancels the endpoint” merely
renames the desired inequality and must not be advertised as an explanation.

## Smallest decisive attacks

- **Typing failure:** no source operation produces either a coupling or a
  labelled-to-scalar pushforward.
- **Forgetting failure:** a proposed completion does not push forward to the
  fixed \(\Theta\).
- **Composition failure:** the proposed coupling or pushforward does not
  intertwine additive-time translation.
- **Hostile-vector failure:** a source-labelled vector retains negative
  shifted norm after completion.
- **Circularity failure:** the construction needs zero ordinates, RH, or a
  posteriori choice of positive subspace.
- **Vacuity failure:** the proposed mechanism is only the known augmentation
  followed by an assertion that its image is positive.

Any one failure rejects this proposed mechanism.  Passing finite Hankel or
quadrature tests alone does not admit it.

## Candidate census and surviving lane

The existing arithmetic-sector results close four tempting global shortcuts:

| Candidate | Outcome |
|---|---|
| Smooth reflection compression \(P_+C_kRP_+^*\) | Fails the required zero density because smoothing makes the reciprocal spectrum too sparse. |
| One positive Hilbert Schur leg for the intrinsic-prime cross trace | Fails because the prime-distance term has oscillating cut density, whereas a positive Schur resolvent has fixed-sign density. |
| Ordinary endpoint--gamma--prime augmentation | Canonical and translation-compatible, but positivity of its image is the RH-equivalent assertion itself. |
| Global Weil radical quotient | Canonical and source-derived, but indefinite unconditionally; its positive descent is precisely Weil positivity. |

One noncircular construction lane survives this census.  Short-support Weil
positivity supplies unconditional local Hilbert blocks.  The new datum would
be a source-derived gluing law for those blocks:

\[
\boxed{
\text{positive local Weil blocks}
\longrightarrow
\text{prime-power edge contractions}
\longrightarrow
\text{cycle-coherent positive dilation}.}
\]

The bounded attack order is forced:

1. test the two-cell block at separation \(\log 2\);
2. if it survives, test the \(0,\log2,2\log2\) triangle, where two prime-two
   edges meet the prime-four edge;
3. test the first mixed-prime rectangle \(0,\log2,\log3,\log6\);
4. only then seek an all-prime Mackey/Adams or Markov/chordal dilation law.

The first step is not covered by the known short-support theorem. Burnol's
argument proves positivity for support in \([1/c,c]\) with sufficiently small
\(c>1\), works initially under \(c\le\sqrt2\), and explicitly requires a
further idea to reach the boundary value \(c=\sqrt2\). Two narrow packets
whose centers differ by \(\log2\) require precisely that boundary support
ratio. Thus the prime-two contraction sits at the first arithmetic contact
where unconditional local positivity stops; it is not a duplicated theorem.

Pairwise contraction is not enough: a three-cycle can have every positive
\(2\times2\) principal block and still have negative determinant.  Therefore
the triangle is the first place where a proposed *coherence law*, rather than
another scalar positivity observation, earns explanatory content.

Primary boundary source: Jean-François Burnol, *Sur les Formules Explicites
I: analyse invariante*, arXiv:math/0101068, theorem and proof on pp. 2--3.
