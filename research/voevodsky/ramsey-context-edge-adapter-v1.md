# Coherent role-fiber edge adapters are not standard PN-law transport

## Candidate and input policy

Following the strict restriction obstruction, test a context-indexed comparison instead of literal equality of restricted roles. The prospective contract is `contracts/ramsey-context-edge-adapter-attempt.v1.json`, frozen with checker and revision-19 port input at `scc-freezes/ramsey-context-edge-adapter-v1.39bdb24e3feb2dbc.json` before testing.

Write C=0 and M=1. For source and target charts a,b and a shared world vertex v, define

    T_ab(v,r) = r XOR role_a(v) XOR role_b(v).

This keeps v fixed. It is the unique permutation of the two-element fiber carrying the actual source role to the actual target role. Each edge adapter records both parent port identities and its support; the full records and parent-triangle permits remain in the digest-pinned input. No two-M law is imposed on an edge or vertex.

## Successful restriction and coherence cells

Every T_ab is invertible, with inverse T_ba. Restriction to a vertex is evaluation of the same formula. On a triple intersection,

    T_bc(v,T_ab(v,r)) = r XOR role_a(v) XOR role_c(v) = T_ac(v,r).

The two occurrences of role_b cancel. This holds on both fiber values, not just the occupied role. It preserves different context assignments rather than claiming they are equal.

The checker covers all 20,736 independently eligible four-face chart choices, 497,664 edge-fiber checks and 165,888 triple-vertex checks. Altering one flip or erasing a parent context is rejected.

## The independent law gate fails for a uniform extension

A coherent role-fiber bijection need not preserve the standard PN predicate on arbitrary triangle role assignments. In the concrete source-bound pair of ports (chart 0, face 0) and (chart 1, face 0), sorted triangle coordinates have flip mask (1,1,0). The occupied roles (1,0,1) map to (0,1,1); both have two M vertices, as required by their separate input certificates.

But the same fiber map sends (1,1,0) to (0,0,0). The former satisfies the standard two-M predicate; the latter does not. Thus this adapter is not a uniform automorphism of the standard PN role-assignment domain.

This counterexample tests a stronger extension to all role assignments. It does **not** invalidate the selected pair's two independent permits, nor prove that descent of fixed-context ports requires such a uniform extension. That distinction is why the parent conjecture remains open.

One may always transport the predicate by pullback:

    Permit_b^transport(y) := Permit_a(T_ba(y)).

This is coherent by the same cancellation law, but is generally not the target's standard two-M predicate. Calling it the standard sector law would change the problem. All eight assignments were checked for the inverse/pullback identity.

## Native boundary and next obligation

These are explicit finite role-fiber adapters, not yet actual native WG comparison derivations. `NativeTableRules.agda` requires an equivalence of the package value types and alignment of their values for `compare-kind`, with resolved source and target premises. Revision 19 admits full records as String-valued atoms. A Boolean fiber bijection is not itself such a comparison of the full record packages. Native P retention alone does not fill this gap.

The next construction must choose and declare a structured role-context interface retaining the full parent records, bind that interface to independently admitted source inputs, and provide actual native comparison/restriction derivations. It must explicitly choose between fixed-context certificate pairs and transported predicates; it may not identify the latter with standard PN laws. Triple-vertex comparison cells must then be derived at that exact package type, not inferred from this Boolean calculation.

Verification: the frozen SCC challenge passes; `results/ramsey-context-edge-adapter-v1.json` contains counts, hostile controls and the explicit law counterexample. This is a runtime audit over the earlier input artifact, not a fresh sector replay or kernel proof. General descent, physical role motion, whole-space admission and forcing are not established. No net revision, graph publication or Git checkpoint is made.
