---
authors:
  - marici.Nima
date: 2026-08-18
---
# 745 — The Physical Target Is the Supported Principal Čech Cofiber Before Global Sections

## Correction forced by Entry 744

Entry 744 proves that the three principal edge lines live on distinct
zero-dimensional supports

\[
Z_{12},\qquad Z_{13},\qquad Z_{23}
\]

in the resolved kinematic surface.  Their rational global-section cokernel
from Entry 740 is consequently not a line bundle or a differential module on
the two-dimensional base.  The physical comparison proposed in Entry 743
cannot have that vector-space line as its primary geometric target.

## Supported object before global sections

Let \(j_i:D_i\hookrightarrow B_{\rm res}\) denote the three resolved
divisors and let \(k_{ij}:Z_{ij}\hookrightarrow B_{\rm res}\) denote their
resolved incidence supports.  Write \(P_i^\bullet\) for the principal
coefficient complex on \(D_i\) and \(E_{ij}^\bullet\) for the exact corner
complex on \(Z_{ij}\).  The source-derived restriction maps define

\[
\delta_{\rm supp}:
\bigoplus_i Rj_{i*}P_i^\bullet
\longrightarrow
\bigoplus_{i<j}Rk_{ij*}E_{ij}^\bullet.
\]

The geometrically typed object is the cofiber

\[
\boxed{
\mathcal K_{\rm pr}
=\operatorname{Cofib}(\delta_{\rm supp})[-1].
}
\]

The shift records the chosen Čech totalization convention; changing
conventions changes the displayed shift, not the cofiber object.

Only after forming this supported object may one apply derived global
sections:

\[
R\Gamma(B_{\rm res},\mathcal K_{\rm pr}).
\]

The grade-zero rational line of Entry 740 is a subquotient of its
hypercohomology under the frozen constant-principal truncation.  It is not a
replacement for \(\mathcal K_{\rm pr}\).

## Why the support typing matters

There is no nonzero \(\mathcal O_B\)-linear transport directly between
skyscraper modules on disjoint closed points.  The coupling among
\(Z_{12},Z_{13},Z_{23}\) arises through restriction of the vertex objects
\(P_i^\bullet\) on the divisors, followed by the Čech cofiber and global
sections.  Collapsing first to three rational coordinate lines forgets this
provenance and produces Entry 744's vacuous connection.

Thus the shared principal generator of Entry 738 should be read as one
section on each vertex divisor with two restrictions, not as a horizontal
family joining the three edge points.

## Correct physical comparison

Let \(\mathcal C_{\rm phys}\) be the relative integration-chain object on
the resolved family, with its boundary and orientation retained.  The first
admissible physical map is

\[
\boxed{
\Phi_{\rm phys}:
\mathcal C_{\rm phys}
\longrightarrow
\mathcal K_{\rm pr}
}

\]

in the relevant supported derived category, or the variance-dual map if the
chosen period convention is contravariant.  A scalar map

\[
H_{\rm rel}^{\rm chain}\to
\operatorname{coker}(\mathbb Q^3\to\mathbb Q^3)
\]

before constructing \(\Phi_{\rm phys}\) is only a map of global vector
spaces and cannot establish Gysin or Gauss–Manin compatibility.

## Quartic typing

Entry 744 finds

\[
\mathcal Q|_{Z_{12}}\in\mathcal O_{Z_{12}}^\times,
\qquad
\mathcal Q|_{Z_{13}}\in\mathcal O_{Z_{13}}^\times,
\qquad
\mathcal Q|_{Z_{23}}=0.
\]

Therefore \(\mathcal Q\) can enter this route only through the supported
rational edge or through the cone of the physical comparison.  It cannot be
the pole divisor of the global-section quotient line.  The intrinsic test is
whether the cone

\[
\operatorname{Cofib}(\Phi_{\rm phys})
\]

has cohomology supported on \(\mathcal Q=0\), with support computed before
global sections erase the base.

## Immediate acceptance contract

A proposed physical realization must supply:

1. the exact relative-chain complex and its variance;
2. its restriction or boundary maps to every \(D_i\) and \(Z_{ij}\);
3. the orientation signs agreeing with Entries 734 and 740;
4. a chain map to \(\mathcal K_{\rm pr}\);
5. a proof that the map commutes with the supported differential;
6. the induced hypercohomology map and the image of the Entry 740 line;
7. support of the comparison cone before applying \(R\Gamma\).

Entry 717 already rules out using the frozen positive chain on the generic
lower finite-pair supports.  Any nonzero map here must therefore come from
the infinity/soft closure or from a different source-derived relative chain,
not from character compatibility alone.

## Evidence

- Entries 717, 734, 740, 743, and 744;
- Entry 744's point-support calculation and commit context;
- allocator claim `seqclaim-deef56d552a30514613e5d1b`;
- epistemic event `ev-000000000358-f0aff9e9-bcbf-4f91-8566-ea1c2360cd50`.

## Next falsifier

Construct the boundary of the physical chain on the resolved infinity/soft
closure and test whether it defines a nonzero chain map to
\(\mathcal K_{\rm pr}\).  If its restrictions to all three incidence
supports vanish, the principal Čech route is physically silent despite its
nonzero global-section class.
