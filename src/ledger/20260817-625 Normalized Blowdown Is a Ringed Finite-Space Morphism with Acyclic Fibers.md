---
id: 423
date: 2026-08-17
title: Normalized Blowdown Is a Ringed Finite-Space Morphism with Acyclic Fibers
---

# Normalized Blowdown Is a Ringed Finite-Space Morphism with Acyclic Fibers

Entry 422 geometrized the PC/Čech target. The normalized barycentric
blowdown of Entry 396 now lifts canonically to a morphism of ringed finite
spaces on the marked connector.

Let
\[
\pi:\widetilde{\mathfrak P}_{03}\longrightarrow\mathfrak P_{\rm PC}
\]
send every expanded face to its old face, replacing the exceptional label
\(E\) by the blown-up center \(\{D03,x_1\}\). Give the source the pulled-back
structure sheaf
\[
\mathcal O_{\widetilde{\mathfrak P}_{03}}
=\pi^{-1}\mathcal O_{\rm PC}.
\]
Then every stalk map
\[
\mathcal O_{\pi(\widetilde S,\widetilde H)}
\longrightarrow
\mathcal O_{\widetilde S,\widetilde H}
\]
is the identity on the same prescribed localization ring. The blowdown is
therefore a morphism of ringed finite spaces without introducing a new
coefficient map.

This definition is compatible with the occurrence loading. Entry 396's
source coefficient at a flag is the label of the blowdown of its initial
face. Hence deleting an initial flag vertex produces exactly the same LCM
quotient before and after \(\pi\). The executable audit reruns the complete
seven-triangle Morse identity and verifies
\[
\pi_*d=d\pi_*
\]
on \(H_{\rm Morse}\), \(\widetilde\xi\), and \(q_J\), with the primitive
\([\mathrm{top},D03]\) roof retained.

## Fiber acyclicity

Every blowdown fiber is a singleton except over a face containing the
blown-up center. The unique nontrivial fiber is the V-shaped poset
\[
h<h_{D03},\qquad h<h_{x_1}.
\]
Its augmented cellular complex is
\[
\mathbb Z^2\xrightarrow{
\begin{pmatrix}
-1&-1\\1&0\\0&1
\end{pmatrix}}
\mathbb Z^3\xrightarrow{(1,1,1)}\mathbb Z.
\]
Coning to \(h\) gives an explicit integral contraction. Therefore every
fiber has reduced homology zero, with unit contraction coefficients.

It follows that
\[
\boxed{L\pi_!=\pi_!}
\]
on the pulled-back marked coefficient packet: derived left Kan extension
has no higher fiber terms. Its counit is the primitive normalized blowdown
map already computed in Entry 396.

Rotating the marked construction supplies the other two road centers, and
the full Čech assembly of Entry 398 glues them without additional fiber
homology.

## Boundary

This closes the ringed finite-space projection prerequisite of Entry 348.
The source ringed space here carries the pulled-back finite PC structure
sheaf. It is not yet identified with the raw algebraic log-DNC structure
sheaf; that is the later algebraization comparison.

The remaining finite six-operation datum is the relative dualizing/Thom
trace for \(\pi\). The acyclic fibers and oriented exceptional interval
strongly constrain it, but its degree and orientation must be checked
against the Tor-one suspension rather than inferred from contractibility.

The executable audit is
\`research/voevodsky/check_ringed_normalized_blowdown.py\`.
