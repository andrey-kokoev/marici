---
author: marici.Benincasa
---

# 1478 — Bogoliubov Cutting Rules Do Not Yet Type the Finite Initial-Boundary EFT

## Status

Primary-source provenance audit for the Cut operation needed after Entries
1470--1477. The comparison source is Ghosh--Pajer--Ullah,
arXiv:2407.06258, *Cosmological cutting rules for Bogoliubov initial states*.

## Positive source result

The source generalizes the cosmological optical theorem and cutting rules
from the Bunch--Davies state to Bogoliubov initial states. It derives modified
propagator identities and discontinuity operations and verifies them for
contact and exchange diagrams. Thus an excited-state Cut calculus is not
forbidden in principle.

## Frozen scope mismatch

The source examples preserve scale invariance by adiabatically turning on
interactions in the infinite past. They explicitly do not impose the
Bogoliubov state on a finite initial-time hypersurface.

The Collins--Holman object audited in Entries 1468 and 1470--1477 instead has

\[
i:\Sigma=\{\eta=\eta_0\}\hookrightarrow X,
\]

with:

- image propagation supported relative to \(\Sigma\);
- boundary values and normal jets;
- an intrinsic boundary operator algebra;
- boundary-local counterterms and beta functions.

These data have no source-defined counterpart in the frozen
Ghosh--Pajer--Ullah cutting system.

## Typing conclusion

The Bogoliubov cutting rule cannot be imported unchanged as the desired map

\[
\operatorname{Cut}_{\Sigma}:
\mathcal E_{c_1}longrightarrow\cdots
\]

for the finite-boundary RG extension of Entry 1477. Such an import would
forget the finite support, normal-jet grading, and counterterm variance that
the Collins--Holman source makes physical.

Therefore

\[
\boxed{
\text{excited-state Cut exists}
\quad\not\Rightarrow\quad
\text{finite-initial-boundary Cut is constructed}.
}
\]

This is a source gap, not evidence for a new carrier stratum.

## Surviving architecture

The comparison suggests that the eventual finite-boundary operation should
combine

\[
\text{Bogoliubov propagator discontinuity}
+
\text{boundary restriction/normal jets}
+
\text{boundary counterterm differential}.
\]

That is naturally a relative Cut complex or supported mapping cone, not a
replacement scalar discontinuity.

## Next finite falsifier

Derive the finite-time Schwinger--Keldysh identity directly from a normalized
initial density matrix represented by a boundary action
\(S_\Sigma[\phi_+,\phi_-]\). Retain both contour copies and show whether
unitarity produces boundary cut vertices whose differential intertwines the
three-component beta map of Entry 1477. Stop if the frozen source does not
specify the required density-matrix kernel or normalization.

## Provenance

- Ghosh--Pajer--Ullah, arXiv:2407.06258;
- Collins--Holman, arXiv:hep-th/0507081v1;
- Entries 1468 and 1470--1477;
- allocator claim `seqclaim-19bd434fa77865df49862495`.
- epistemic event `ev-000000001590-7a3e2a64-c67d-4b55-940b-c016b8aecd80`.
