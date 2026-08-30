# Carrier categorical self-realization falsifier

## Type-correct formulation

A Carrier object and an entire category are not ordinarily objects of the
same type.  The candidate construction is instead an indexed semantic
functor

\[
(\mathcal C,\Sigma)
\longmapsto
\mathbf{Marici}(\mathcal C,\Sigma)
=
\int_{\sigma\in\mathbf S_{\mathcal C}}
\mathbf{Int}_{\mathcal C}(\sigma).
\]

Here \(\mathbf S_{\mathcal C}\) is the category of admitted source records,
\(\mathbf{Int}_{\mathcal C}(\sigma)\) is the interface category generated over
one record, and the integral is the Grothendieck construction assembling all
fibers and their reindexing maps.

Objects include coefficient lenses, supported objects, boundary conditions,
and readout interfaces.  Morphisms include restriction, localization,
transport, degeneration, and pairing.  Higher cells retain comparison
homotopies and structured failures of coherence.

## Strong reconstruction conjecture

The strongest conjecture says that the generated system determines its input:

\[
\boxed{
(\mathcal C,\Sigma)
\simeq
\operatorname{Rec}
\mathbf{Marici}(\mathcal C,\Sigma).
}
\]

Equivalently, the construction is faithful on admissible Carrier/source
pairs.

## First falsifier: readout-only reconstruction fails

Flavor supplies an exact counterexample to reconstruction from observable
values alone.  Distinct sparse presentations can have identical weak-basis
invariants, while the loop phase changes or ceases to exist after a general
weak-basis rotation.  Thus the physical readout functor identifies objects
that remain different in the presentation groupoid.

Likewise, a single frozen Bell analyzer maps a multidimensional photon
coefficient fiber to one scalar record.  It cannot reconstruct the coefficient
ray without the source amplitude.

Therefore

\[
\boxed{
\text{readout algebra alone does not reconstruct the Carrier/interface.}
}
\]

This is not a defect.  A physical readout is expected to be a quotient.

## Surviving conjecture: source-indexed Yoneda completeness

Let \(\mathcal P\) be the predeclared family of all authorized probes,
including internal transport and coherence probes as well as terminal physical
readouts.  Define

\[
Y_{\mathcal P}(A)
=
\bigl(P(A)\bigr)_{P\in\mathcal P}.
\]

The surviving conjecture is

\[
\boxed{
Y_{\mathcal P}\text{ is jointly faithful on the source-indexed interface
category.}
}
\]

It does not require any one readout to distinguish all objects.  It requires
the complete authorized family of probes, with provenance and transport
retained, to distinguish morphisms and reconstruct objects up to typed
equivalence.

Physical readouts form a terminal quotient of this richer semantic nerve:

\[
\mathbf{Int}_{\mathcal C,\Sigma}
\xrightarrow{Y_{\mathcal P}}
\widehat{\mathcal P}
\longrightarrow
\mathbf{Record}.
\]

## Finite matrix test

For a finite admitted subcategory with morphism basis \(m_1,\ldots,m_r\) and
probe family \(P_1,\ldots,P_s\), construct the probe matrix

\[
A_{ij}=P_i(m_j).
\]

The joint-faithfulness gate is

\[
\operatorname{rank}A=r
\]

after quotienting only by predeclared typed equivalences.  A kernel vector is
a concrete invisible morphism.

The audit must then classify every kernel direction:

1. declared gauge or presentation equivalence;
2. internal but physically unreadable lens coordinate;
3. missing authorized probe;
4. genuinely indistinguishable Carrier structure.

Cases 3 and 4 falsify the current probe completeness claim.  Adding a probe
is admissible only when independently generated from source structure; a
kernel-targeted projector is prohibited.

## First bounded targets

1. **Flavor:** assemble weak-basis invariants together with chart-transition
   and stabilizer probes.  Confirm that physical readouts alone have a kernel,
   then test whether the full source-indexed groupoid nerve removes it.
2. **Bell:** compare one analyzer with the predeclared analyzer family on the
   rank-two Ward fiber.  Determine the smallest authorized separating family.
3. **Cosmology:** compare the generic coefficient system with all published
   Leray and residue probes.  Any invisible supported costalk is a precise
   missing-probe obstruction.
4. **Theta:** treat the complete generalized-Laguerre tower as the vertical
   self-probe family.  A finite negative coefficient falsifies admissibility;
   failure of the whole tower to distinguish spectral measures falsifies
   reconstruction.

## Deutsch--Popperian statement

The Marici system does not claim that everything observable determines
everything that exists.  It claims that everything admitted as distinct is
distinguishable by some legal source-generated probe:

\[
\boxed{
A\not\simeq B
\Longrightarrow
\exists P\in\mathcal P:\ P(A)\not\simeq P(B).
}
\]

If two allegedly different structures agree under every legal probe, the
program must either identify them or exhibit a new source-derived probe.  It
may not preserve the distinction by assertion alone.

