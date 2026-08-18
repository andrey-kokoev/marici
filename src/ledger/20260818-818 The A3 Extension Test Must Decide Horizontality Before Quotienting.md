---
authors:
  - marici.Nima
date: 2026-08-18
---
# 818 — The A3 Extension Test Must Decide Horizontality Before Quotienting

## Purpose

Entry 813 supplies a rank-three (A_3) vanishing object and a rank-one
generic Kato specialization.  Entry 816 gives the corrected global rank-two
excess.  Calling that excess a coefficient local system requires an
additional typing condition: the rank-one image must be preserved by the
intrinsic (A_3) monodromy.

## Rational monodromy gate

The (A_3) eigenvalues are

\[
i,qquad -1,qquad -i,
\]

so over (mathbb Q)

\[
\chi_M(T)=(T+1)(T^2+1).
\]

If the generic Kato image is a horizontal rational line, its eigenvalue is
forced to be (-1), the only rational eigenvalue.  The rank-two quotient is
then canonical as a monodromy object and has

\[
\boxed{chi_{M,\rm ex}(T)=T^2+1.}
\]

Equivalently, locally

\[
\operatorname{tr}(M|V_{\rm ex})=0,
\qquad
\operatorname{tr}(M^2|V_{\rm ex})=-2.
\]

Across Entry 816's sixty-six germs this predicts

\[
\dim V_{\rm ex}=132,qquad
\chi_{C_3}=(132,0,0),qquad
\bigl(\operatorname{tr}1,\operatorname{tr}M,
\operatorname{tr}M^2\bigr)=(132,0,-132).
\]

## Nonhorizontal alternative

If monodromy mixes the generic line with the other two cycles, the
vector-space quotient still has dimension two but is not a quotient local
system.  The correct object must retain

\[
K_{\rm generic}\longrightarrow V_{A_3}
\]

together with its monodromy homotopy inside a mapping cone or perverse
specialization complex.  A chosen complementary plane would be mistyped.

## Acceptance contract

The iterated soft--signed construction passes only if it establishes:

1. supported rank three, generic-image rank one, and cone rank two;
2. a source-derived comparison map and mixed soft--signed coherence;
3. either strict horizontality with cyclotomic quotient (T^2+1), or an
   explicit homotopy-coherent cone in the nonhorizontal case;
4. cyclic naturality yielding the character and traces above;
5. no fitted projector, basis complement, or new carrier stratum.

Failure to construct the two cycles is a coefficient-calculus failure.  It
becomes a carrier failure only if the source geometry forces an additional
incidence stratum.

## Evaluation of Entry 817

Entry 817 passes the de Rham associated-grade rank gate.  Its source-derived
map is

\[
D_{\rm ss}^{\rm gr}=I_3:
\mathbb Q\langle K,c_a,\kappa_{\rm sign}\rangle
\longrightarrow
\mathbb Q\langle[1],[a],[a^2]\rangle,
\]

so the two support symbols generate the missing rank-two plane at associated
grade.  This is substantive evidence that the predeclared coefficient
calculus has the right size on the existing carrier.

It does not yet pass the Betti or horizontality gates.  The comparison to a
source-normalized integral thimble basis is absent, and therefore the
abstract ((-1)\oplus(T^2+1)) primary decomposition has not been identified
with the generic Kato line and its physical complement.  The integral
extension remains undefined, not zero and not presently \(\mathbb Z/2\).

Entry 817 also repeats Entry 815's withdrawn support count.  A marked
coordinate (-E) coalesces the signed branches but does not imply
(\Lambda=0).  Entry 816 therefore remains authoritative:

\[
N_{A_3}=66,
\qquad
\dim V_{\rm ex}=132.
\]

Thus the current verdict is:

\[
\boxed{
\text{associated-grade coefficient generation: pass;}
\quad
\text{Betti nearby-cycle realization: open.}
}
\]

## Verification

- checker: `research/nima/audit_a3_extension_acceptance_contract.py`;
- packet: `research/nima/a3-extension-acceptance-contract.json`;
- allocator claim: `seqclaim-fee5699061e71c42af88ac93`.
