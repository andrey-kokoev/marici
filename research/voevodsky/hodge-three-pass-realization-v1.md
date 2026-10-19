# Three-pass realization: first source-map test

## Question

Operator proposal: main-dimension to codimension succeeds, return succeeds, but the next conversion fails. Test this against actual Hodge interfaces, using the sustained-capability standard in ledger 4322, rather than assigning M/C names to arbitrary matrices.

Active SCC obligations: route/recovery compatibility first; readout descent second. No physical time is assigned to composition order. This is a new bounded audit; main Hodge net and fixed sixfold are unchanged.

## Claim boundary and issue-level test

- Problem: identify a repeat-realization defect that excludes an algebraic representative of the fixed rational Hodge class.
- Conjecture under test: the conventional dimension/codimension conversion or cycle-class/representative conversion can succeed twice but fail on its third pass at the class level.
- Rivals: duality makes repetition automatic; a representative changes only by an invisible kernel element; a partial capability loses information not present in cohomology.
- Risky consequence: a nonzero third-pass defect must survive class comparison, not merely a particular representative or implementation.
- Strongest test: type Poincare duality and the actual cycle-class map, then test section recovery and a known algebraic kernel control.
- Disposition: the two conventional class-level interpretations cannot yield the proposed third-pass failure. A source-derived witness-sensitive partial realization remains unspecified, not refuted. No Hodge verdict follows.

## 1. Dimension/codimension: Poincare duality is repeatable

For smooth projective complex X of dimension n, the canonical topological interpretation is

    M = H_{2(n-p)}(X,Q), C = H^{2p}(X,Q),
    c = PD: M -> C, r = PD^{-1}: C -> M.

Here p is complex codimension; the chain dimensions are real. Neither carrier is a physical main space. These maps satisfy rc=id and cr=id, hence crc=c. For n=6,p=3 both degrees are six, but the homology/cohomology types remain distinct.

This applies to every rational class, not only algebraic ones. Restricting C to rational Hodge classes and M to its inverse image does not change the conclusion. Poincare duality is therefore not an algebraic realization constructor or a third-pass detector.

## 2. Cycle-class conversion: a successful section already repeats

Use the actual algebraic interface

    A = CH^p(X)_Q, H = Hdg^p(X,Q), c = cl: A -> H,
    I = im(c).

A section r:I -> A satisfies cr=id_I. Such a Q-linear section exists abstractly by choosing basis lifts; it is neither canonical nor an algorithm for discovering algebraic representatives. No section on all H is assumed.

For every a in A,

    crc(a)=c(a).

For every h in I,

    rcr(h)=r(h).

Thus both three-pass recovery equations hold on the known image. Fourfold reductions agree as ordinary vector-space maps. This says nothing about richer witness-consuming coherences.

Starting from the selected Hodge class alpha reverses the order: alpha --r?--> A --c--> H --r?--> A. If the first step really constructs an algebraic representative and c returns alpha, the same stateless rule r can be used again. Failure of a later implementation cannot undo the first representative's algebraicity. Existence of that first lift on alpha is precisely the unresolved question, not a consequence of the notation.

## 3. A known algebraic control against exact representative recovery

Let E be a complex elliptic curve, O its origin, and P a non-torsion point. The degree-zero divisor D=[P]-[O] determines a nonzero element of Pic(E) tensor Q = CH^1(E)_Q, but cl(D)=0. The identification Pic^0(E) with E and degree description of H^2(E,Q) are imported standard facts.

Every Q-linear section of cl has r(0)=0, so rc(D)=0 is not D. Nevertheless crc(D)=0=c(D), and D is an actual algebraic divisor. Therefore requiring recovery of every original Chow representative from its cohomology class already rejects legitimate p=1 algebraic cycles. This is a control on a different X, not a counterexample on the selected sixfold.

The formal exact model c(x,y)=x, r(t)=(t,0) reproduces this kernel mechanism; its second coordinate is not claimed to be computed elliptic Chow data. An independent faithful reader of y distinguishes the changed representative, but cannot descend to H.

## 4. How a genuine third-step failure can occur

For partial maps, let M contain (value, available) and (value, exhausted). Let c be defined only on the available state, and r return the exhausted state. Then c followed by r succeeds; the next c is undefined. The value readout returns unchanged, but the full capability state does not.

This is an exact finite counterexample to inferring repeatability from readout return. It is NOT a Hodge model, and no resource flag is supplied by the fixed variety. In a linear total model, a witness-sensitive c that does not descend through the returned readout can likewise have crc != c; that tests a different interface from cl.

The first missing object for this branch is a source-derived partial realization operation on algebraic/Hodge packets, with a specified domain and retained witness state. Its acceptance test is concrete: every algebraic cycle must admit a packet with two compatible uses, while every packet over the fixed alpha fails. Requiring one chosen algorithm to fail, or requiring exact recovery of all Chow representatives from H, does not meet this test. Stop this branch until such source data are supplied; do not invent a resource budget to force failure.

## Verification and disposition

The companion dependency-free checker enumerates all functions between two two-element sets and verifies crc=c whenever rc=id or cr=id. It checks an exact rational split-surjection model, a deliberately bad return, and the partial capability example. These are finite regression controls for the general proofs above, not computations of the sixfold's Chow group. No proof-assistant closure or new geometric constructor is claimed.

Sources: ledger 4322; hodge-cycle-map-scope-v1.md; hodge-cycle-packet-dictionary-v1.md; hodge-explicit-sixfold-candidate-v1.md. The requested three-pass attack has been tested at its two standard source bindings and localized to the missing enriched operation. Neither Hodge nor universal all-cycle invariance is proved or disproved.
