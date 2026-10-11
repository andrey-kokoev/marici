# Explicit identity-arrow contract for the WG assembly comparison

## Proposed convention

This is an explicit proposed assembly interface, not a claim that every existing WG relation already carries identities. It separates object registration, structural arrows, selected generation and retained execution history.

### Objects and identity terms

An object A and an identity arrow id_A:A->A are different typed records. Draw a dot for A; use AA only as shorthand for its distinguished identity record when that record is present. A nullary dot/name does not by itself prove an arbitrary proposition or supply an inhabitant of R(A,A).

For the structural assembly carrier we propose a **reflexive directed graph**: each registered object has a supplied distinguished unit. Object registration must construct/retain that unit through a declared operation. If a category is later claimed, composition and unit laws must also be supplied. A reflexive graph alone does not provide them.

WG's general transition relation R remains separate. R need not contain identities even if the structural carrier does. For example a Boolean-flip relation has no edge from false to false. A retained empty history is not automatically an R-edge.

## What an AB record entails

A structural directed arrow record f:A->B must contain or resolve:

- its own occurrence ID;
- its source and target object IDs;
- the declared structural unit records id_A and id_B.

In this proposed identity-complete interface, admitting AB therefore requires both AA and BB. If this is the first introduction of B, the introduction operation must supply B and its unit; these must not be guessed from a rendered segment. The closure may be performed atomically, but its additions remain recorded.

It does not require BA, another parallel AB occurrence, a triangle, or an inverse. Even if A=B, a loop occurrence is not identified with id_A merely because its endpoints agree. Preserve its occurrence identity and any nontrivial witness/history.

A bare undirected segment has neither a declared arrow direction nor categorical unit data until an adapter provides them. It must not be silently read as a pair of directed arrows.

## Admission table

| Input record | Guaranteed | Not guaranteed |
|---|---|---|
| Bare geometric dot A | A marked point | A typed unit or witness of arbitrary R(A,A) |
| Registered assembly object A | A and distinguished AA under this proposed interface | Any outgoing nonidentity arrow |
| Registered structural AB | A, B, AA, BB and this AB occurrence | BA or any face filling |
| Both AB and BA | Both directions and their endpoints/units | Inverse laws or a two-arrow history equal to the empty one |
| Composable AB and BC | A matched boundary; A,B,C and their units | Composite AC without an admitted composition operation |
| Constructed AC from AB,BC | The composite and its retained parents | Equality with an independently supplied AC without a comparison witness |
| A triangle witness | A specified comparison of its named boundary routes | A Euclidean filled membrane or volume without a realization rule |

## Counting and history

Count separately: objects, distinguished units, nonidentity arrow occurrences, retained execution steps, and higher witnesses. A four-object complete directed simple carrier has four units and twelve nonidentity arrows, sixteen structural arrows in total. This does not change older counts explicitly excluding units or equate them with coefficient-matrix transfer counts.

Executing an identity-valued step may increase history length even when the endpoint and composite arrow are unchanged. Do not count unit availability as an executed transition or erase an executed transition because its value is a unit.

## Consequence for WG once/twice

The common initial package should explicitly contain A and AA, rather than using AA interchangeably with a dot. Each pass must report newly introduced objects, units, arrow occurrences and higher witnesses separately.

If promotion makes a first-pass package E into a second-level object [E], its identity id_[E] is a new level-typed unit. It is not one of the internal AA records of E. The promotion must retain E and introduce the higher unit explicitly. Likewise a full-turn minus sign on a coefficient fiber is not replaced by an identity merely because the base endpoint returns.

This contract makes pass depth and identity availability auditable; it does not select the missing physical promotion or identify its outputs with particles.

## Prior-source boundary

Read `research/nima/atomic-proposition-seed.md`: its nullary dot initializes a syntax but does not provide a proposition proof, and repeated selected steps can retain nonempty histories with unchanged endpoints. Read the WG Layer 1/2 definitions as distinguished in `wg-once-twice-particle-audit.md`: arbitrary witness relations have no automatic unit/composition structure. This note proposes the additional structural interface explicitly rather than attributing it to the bare WG type.
