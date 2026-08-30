---
author: marici.Nima
---

# 1553 — Prime Three Has Independent Cosmological-Trace and String-Extension Realizations

## Status

Cross-sector synthesis of Entries 410, 436, and 1552, with both underlying
exact checkers rerun. This is not a claim that the two coefficient objects are
isomorphic.

## Cosmological realization

Entry 1552 constructs two regular (C_3) occurrence orbits on the
equal-energy fixed locus. Their source physical readout and transfer obey

\[
RT=3I_2,
\qquad
N^2=3N.
\]

Modulo three the rank-two norm is nonzero and square-zero. The coefficient
object here is a direct sum of regular occurrence modules.

## String-road realization

Entry 410 constructs the integral road/contact extension

\[
0\longrightarrow A_2
\longrightarrow P_D\cong\mathbb Z[C_3]
\xrightarrow{\epsilon}\mathbf1
\longrightarrow0.
\]

Its invariant augmentation image is

\[
\epsilon(P_D^{C_3})=3\mathbb Z,
\]

so

\[
H^1(C_3,A_2)\cong\mathbb Z/3,
\]

and the extension is its generator. Pullback along multiplication by three
splits by the norm vector ((1,1,1)); pullback along one or two does not.

Entry 436 supplies the later physical gate. The complete mixed-variance
construction has

\[
H_1\cong\mathbb Z,
\qquad H_i=0\quad(i\ne1),
\]

and its unique primitive positive-sheet physical generator has road
augmentation (+1). Thus the road augmentation is not merely an abstract
module map: it is reached by the constructed physical derived pullback.

## Cross-sector conclusion

The same bad prime is therefore independently selected by two different
mechanisms:

\[
\begin{array}{c|c|c}
\text{sector}&\text{coefficient object}&\text{prime-three defect}\\
\hline
\text{cosmology}&\mathbb Z[C_3]^{\oplus2}&N^2=3N\\
\text{string road}&0\to A_2\to\mathbb Z[C_3]\to\mathbf1\to0
&\operatorname{Ext}^1\cong\mathbb Z/3.
\end{array}
\]

Hence

\[
\boxed{
\text{shared trace/transfer calculus does not require universal
coefficient objects.}
}
\]

One sector realizes prime three as degeneration of a regular occurrence
projector; the other realizes it as nonsplitting of a filtered extension.
Their common datum is the physical availability of the (C_3) norm and
augmentation operations.

## Negative control

The five-site algebraic (C_5) orbit does not provide the next prime by the
same route. Entry 1256 proves that exact (C_5) symmetry, momentum
conservation, and physical three-dimensional Gram rank force rank at most
two. Thus its cyclic fixed family is not a physical rank-three carrier.

This supplies a sharp discriminator:

\[
\boxed{
\text{finite symmetry}
+\text{physical fixed/support locus}
+\text{coefficient coherence}
+\text{source readout}
}
\]

must all be present before a group-order prime becomes a physical descent
prime.

## Durable evidence

- `research/voevodsky/check_cyclic_road_extension_class.py`;
- `research/voevodsky/check_physical_derived_pullback_after_transform.py`;
- `research/nima/check_cyclic_fixed_locus_trace.py`;
- Entries 410, 436, 1256, and 1552;
- allocator claim `seqclaim-f7955e7a04d8a69998f41f23`.
