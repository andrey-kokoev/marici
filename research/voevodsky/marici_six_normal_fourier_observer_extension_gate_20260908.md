# Six-normal and full-Fourier observer extension gate

Date: 2026-09-08

## What composes formally

Prior research proves that the complete Fourier observer is injective on the codiagonalized projective translated-theta source. The new construction supplies six jointly separating short-normal observers on the marked endpoint/conormal source sector.

For two observer families on the **same source**, adjoining the second family to an already jointly faithful first family preserves joint faithfulness. This categorical theorem is now checked in

`research/voevodsky/agda/DGPyramidObserverFamilyExtension.agda`.

Thus, once both families are transported to one admitted source object, the combined Fourier-plus-six-normal family is algebraically jointly faithful. The normal observers add typed endpoint detection without weakening Fourier faithfulness.

## First exact missing arrow

The two existing faithfulness statements are not yet on the same source:

- Fourier faithfulness is proved on the projective translated-theta packet;
- six-normal rank is proved on the complete framed endpoint/conormal source sector.

The bordered Xi bridge identifies the endpoint **target lines** and their incidence rows. It does not yet give an equivalence or split monomorphism between these two source objects. Therefore directly taking the product of their observer families would be an untyped combination.

The required datum is a source transport

\[
T:\mathcal S_{\theta}^{\mathrm{adm}}
\longrightarrow\mathcal S_{\mathrm{endpoint}}
\]

or a common source `S` mapping to both, together with a conservative return on the declared admissible subobject. In the Agda interface this is `SourceTransport`, carrying

\[
T^{-}T^{+}=1.
\]

After it is supplied, `pullbackPreservesJointFaithfulness` transports the six-normal family to the theta source and `extensionPreservesJointFaithfulness` combines it with the full Fourier family.

## Completion boundary

Even that composition proves algebraic point separation only. Prior research explicitly shows that full Fourier injectivity does not provide a continuous recovery map or Hilbert lower frame bound. RH-strength completion still requires a uniform observer margin on compact off-critical parameter sets and the independently defined positivity cone.

## Current result

The finite six-normal block is complete, and the categorical combination theorem is machine-checked. The next concrete construction is not another normal target. It is the common-source transport from the translated-theta admissible source into the framed endpoint source, preserving the bordered Xi incidence and completion energy.
