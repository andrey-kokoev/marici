# Poisson Sewing of Prime Exclusion Generates the Full Ramanujan Packet

## The proposed strict square

The preceding result reduced the scalar analytic obstruction to the primitive
prime current. A tempting next step was to prove its tempered realization
prime by prime and then assemble the result multiplicatively.

This would require additive Fourier--Poisson sewing to preserve the separate
prime-exclusion channels. The smallest two-prime quotient decides whether it
does.

## Prime exclusions modulo six

Work on \(\mathbb Z/6\mathbb Z\) with the unnormalized discrete Fourier
transform

\[
\widehat f(k)
=
\sum_{a\bmod6}f(a)e^{-2\pi iak/6}.
\]

The prime-2 exclusion is

\[
f_2(a)=\mathbf 1_{2\nmid a}.
\]

Because it has period two, its transform is supported only at
\(k=0,3\):

\[
\widehat f_2=(3,0,0,-3,0,0).
\]

The prime-3 exclusion is

\[
f_3(a)=\mathbf 1_{3\nmid a}.
\]

Its transform is supported only at \(k=0,2,4\):

\[
\widehat f_3=(4,0,-2,0,-2,0).
\]

Their product is the unit-residue indicator

\[
f_6=f_2f_3=\mathbf 1_{(a,6)=1}.
\]

Its transform is

\[
\widehat f_6(k)
=
e^{-2\pi ik/6}+e^{-10\pi ik/6}
=
2\cos(\pi k/3),
\]

so

\[
\widehat f_6=(2,1,-1,-2,-1,1).
\]

The modes \(k=1,5\) are absent from both individual prime packets but appear
in their product. They are genuine mixed-prime Fourier channels.

## General squarefree cutoff

For squarefree \(Q\), define

\[
f_Q(a)=\mathbf 1_{(a,Q)=1}.
\]

Its Fourier transform is the Ramanujan sum

\[
\widehat f_Q(k)
=
c_Q(k)
=
\sum_{\substack{a\bmod Q\\(a,Q)=1}}
e^{-2\pi iak/Q}.
\]

Although \(f_Q\) factors pointwise into prime exclusions, its Fourier image
is a convolution of the embedded prime Fourier packets. That convolution
generates characters whose denominators involve several primes at once.

Therefore additive Poisson sewing and multiplicative prime decomposition do
not commute primewise. Their correct comparison retains the full residue and
character packet.

## Categorical consequence

The missing connected-realization square cannot be a strict product of local
prime squares. Before scalarization it must pass through

\[
\mathbb Z/Q\mathbb Z
\quad\longleftrightarrow\quad
\widehat{\mathbb Z/Q\mathbb Z}
\]

at every squarefree cutoff, with compatible transition maps as \(Q\)
grows. The inverse-limit carrier is the profinite residue space, while its
Fourier dual is the torsion character space.

The primitive scalar current remains the only analytic divisor obstruction
in the right sector. But a source-level proof of its temperedness must retain
the complete Ramanujan packet long enough for mixed-prime Fourier
cancellations to occur.

## Relation to the multi-tower language

Three structures are distinct:

1. the multiplicative Fock tower creates prime occupations;
2. the additive residue tower carries Poisson transport;
3. the Ramanujan comparison tower records their mixed character incidence.

The comparison tower is not a scalar coherence cell. It has its own growing
family of residue-character states. Scalar primitive density is obtained only
after totalizing this tower.

## Hard obstruction

The finite calculation explains why primewise estimates repeatedly failed to
reach RH. The missing cancellation is cross-prime and additive-dual. However,
retaining all Ramanujan modes does not itself prove temperedness. One still
needs a completion theorem showing that the compatible finite packets act
continuously on the half-normalized boundary rigging.

This is now the smallest honest target:

> Prove a cutoff-uniform tempered bound for the completed Ramanujan packets
> derived from integer endpoint incidence and Poisson sewing.

## Falsifier

A proposed construction fails if it:

- retains only one scalar per prime;
- predicts no \(k=1,5\) modes at \(Q=6\);
- scalarizes before Fourier transport;
- uses incompatible residue refinements as \(Q\) grows;
- or obtains boundedness only after inserting a zeta zero-free estimate.

