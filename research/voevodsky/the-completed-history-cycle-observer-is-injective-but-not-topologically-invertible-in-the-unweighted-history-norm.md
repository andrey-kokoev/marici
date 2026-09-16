# The completed history-cycle observer is injective but not topologically invertible in the unweighted history norm

## Question

Does algebraic faithfulness of

\[
\mathcal O_D=(\widehat B_D,\widehat Z_D)
\]

already make the completed helical presentation a homeomorphic equivalence for
the source projective topology and the ambient target topology
\(L^2(\mathbb R_+)\oplus\mathcal Z_{D,\exp}\)?

## Answer

No. The history channel is strongly smoothing on translated edges. Along forest
edges escaping to large logarithmic position, the cycle coordinate is zero and
the history norm tends to zero after source-seminorm normalization. Thus the
observer is injective but not bounded below in the ambient history-plus-chord
topology.

## Escaping forest-edge sequence

Fix a source seminorm

\[
q_\delta(c)=\sum_e|c_e|e^{\delta W(e)}.
\]

The fixed-ratio translated-shell graph has forest edges \(e_n\) with interval
supports \([A_n,B_n]\) escaping to \(+\infty\). Let

\[
c_n=e^{-\delta W(e_n)}\mathbf e_{e_n}.
\]

Then

\[
q_\delta(c_n)=1,
\qquad
Z_Dc_n=0,
\]

because \(e_n\) belongs to the chosen forest.

The history column has the form

\[
b_{e_n}(s)=
\int_{A_n}^{B_n}
\Phi_1(v)\Phi_1(v+s+D)\,dv.
\]

The explicit completed atom is

\[
\Phi_1(u)=
 e^{u/2}(2\pi^2e^{4u}-3\pi e^{2u})e^{-\pi e^{2u}}.
\]

It decays faster than \(e^{-Nu}\) for every \(N>0\). By Cauchy--Schwarz,

\[
\|b_{e_n}\|_2
\leq
\|\Phi_1\mathbf1_{[A_n,B_n]}\|_2\,\|\Phi_1\|_2,
\]

up to the harmless fixed translation \(D\). The first factor decays
superexponentially as \(A_n\to\infty\). Multiplication by the source
normalization \(e^{-\delta W(e_n)}\leq1\) cannot prevent decay. Hence

\[
\|\widehat B_Dc_n\|_2\longrightarrow0,
\qquad
Z_Dc_n=0,
\qquad
q_\delta(c_n)=1.
\]

## Consequence

There is no constant \(C_\delta\) such that

\[
q_\delta(c)
\leq C_\delta
\bigl(\|\widehat B_Dc\|_2+z_\delta(Z_Dc)\bigr)
\]

for all source vectors. Therefore the inverse of \(\mathcal O_D\) on its image
is not continuous when that image receives the subspace topology from the
unweighted \(L^2\) history target and the projective chord target.

This does not contradict injectivity. It is the standard distinction between
zero kernel and a positive lower observability bound: the sequence is
asymptotically invisible without containing an actually invisible nonzero
vector.

## Interpretation for the helix

The completed observer image supports a canonical algebraic inverse, but not a
topological inverse in the ambient unweighted-history topology. Consequently:

- the helix is algebraically reversible on the realized observer image;
- it is not a bicontinuous Fréchet/Hilbert helix with the current ambient target
  topology;
- finite cutoffs can be exactly reconstructible while reconstruction condition
  numbers diverge.

## Admissible repairs

There are three distinct repairs.

1. **Transport the source topology to the image.** Give
   \(\operatorname{im}\mathcal O_D\) the final topology defined by the
   seminorms \(q_\delta(\mathcal O_D^{-1}x)\). This makes the map a
   homeomorphism by construction, but does not derive an independent physical
   observer norm.
2. **Weight the history target.** Add output seminorms that compensate for the
   translated-atom decay. Their weights must be source-derived and compatible
   with seam transport.
3. **Retain a discrete forest port as well as the chord port.** Recording every
   edge coefficient makes reconstruction projectively bounded, but turns the
   observer into a coordinate copy of the source rather than a compressed
   physical trace.

## Claim boundary

The argument uses the recorded translated-shell source, an escaping sequence of
forest edges, and the explicit superexponential completed atom. It concerns the
unweighted \(L^2\) history topology. It does not rule out a stronger
source-derived history rigging, a transported image topology, or a different
seam-invariant complete observer family.

## Verdict

\[
\boxed{
\mathcal O_D\text{ is algebraically faithful but not topologically invertible
in }L^2\oplus\mathcal Z_{D,\exp}.}
\]

The next helix layer must therefore be a rigged/projective presentation, not an
unweighted Hilbert presentation.
