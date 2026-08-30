# Interacting rank-26 support audit

Date: 2026-08-24  
Actor: `marici.Benincasa`

## Scope and typing

This packet inventories only independently frozen supports of the homogeneous
three-site scalar one-loop system.  It distinguishes:

- ordinary restriction of the typed rank-26 quotient;
- logarithmic nearby cycles of the rank-12 marked-relative system;
- coefficient lattices on resolved exceptional charts;
- pairing with the physical relative cycle.

Equal ranks across these columns would not identify the objects, and unequal
ranks do not by themselves define a comparison cone.

## Current matrix

| Support | Frozen Carrier datum | Typed coefficient evidence | Physical readout evidence | Current classification |
|---|---|---|---|---|
| Generic nonsoft locus | Energy/Cut carrier | Literal source is cyclic in rank 26; tested connection algebra is `Mat_26`; replicated across fibers and primes | Positive Bunch--Davies period gives a nonzero dual covector, hence a cyclic dual for the tested full matrix algebra | Generic scalar contextual faithfulness supported through Gauss--Manin transport |
| Total energy `E_T=0` | Existing signed/total-energy divisor | Tangent rank-26 source closure has rank 7 and generates `Mat_7`; transverse control returns rank 26. Independently, the marked rank-12 logarithmic nearby object has `N^2=0`, `rank N=4`, Jordan type `J2^4+J1^4` | Any nonzero dual covector is cyclic on the tested rank-7 tangent system; compatibility with the physical nearby-cycle pairing remains open | Existing support; tangent faithfulness survives on the retained grade, but nearby cycles remain unconstructed |
| Triangle/Gram wall | Existing triangle wall | Nima's rank-26 computation gives rank 12 on the wall versus rank 26 nearby; moving-wall quotient collapses and low/high filtration grades exchange | Physical chain pairing remains outside the collapse certificate | Existing support; owned by Nima's triangle-wall adapter lane and not recomputed here |
| Component-soft loci | Existing soft divisors | Tangent closures have ranks `(20,20,24)`. The `X2` and `X3` systems generate full matrix algebras. The `X1` system is the maximal parabolic `0 -> M16_deleted -> M20 -> Q4 -> 0`; `M16_deleted=P->bP`, and `Res_g23` recovers `Q4`. The five ordinary marked residues see rank 10 of `M16_deleted`; their first tangent scores raise this to rank 16. Occurrence transport remains exact `20 -> 20` | The complete admissible marked-residue plus first-score family recovers all 20 algebraic directions. Physical cycle activation remains a separate open gate | Existing soft localization calculus plus a sector-specific nonsplit coefficient extension; contextual faithfulness survives for the complete algebraic port family |
| Marked tangency | Existing marked-wall blowup | One-step conductor/Rees lattice resolves the radial/tangent poles; no fitted support is needed | No source-normalized interacting physical pairing in this packet | Existing coefficient support |
| Radial all-soft chart | Existing signed-energy and soft strict transforms | All denominators arise from frozen strict transforms; no leftover irreducible exceptional factor | Physical activation is separately constrained by relative-cycle data | No new Carrier support at the audited grade |
| Landau supports | Independently derived Landau/critical loci | No complete rank-26 specialization or supported cone in the current packet | Not tested | Open |
| Elliptic degeneration | Existing elliptic coefficient family over total energy | Rank-12 elliptic line degenerates by nearby cycles; no new carrier divisor. Its embedding into the rank-26 total-energy specialization is unconstructed | Physical relative-chain compatibility remains open | Sector-specific coefficient degeneration on existing support |

## Nonduplication boundary

The triangle-wall calculation and its labelled quotient adapter belong to
`marici.Nima`.  This lane may consume its declared ranks and maps but must not
reconstruct an alternative adapter and treat agreement as authority.

## Highest-information next construction

The next object is not another absolute rank census.  It is the total-energy
Rees/nearby specialization

\[
\psi_{E_T}(\mathcal M_{26}),
\]

retaining the rank-seven direct source closure, the moving-wall normal, and all
five occurrence-labelled marks.  Its specialization triangle must be computed
before asking whether the physical score ports remain jointly faithful.

The known rank-twelve nilpotent system is a smaller marked localization sector.
It can constrain the answer only after a source-derived deletion/localization
map from the five-mark rank-twenty-six union is constructed.  Such a map is not
currently present and must not be inferred from a rank comparison.

If this comparison cannot be derived from the existing localization and
moving-wall maps, the next independent lane is component-soft rank-26
specialization.  A rank discrepancy alone will not authorize a fitted map.

## Source artifacts

- `research/benincasa/rank26-connection-algebra.json`
- `research/benincasa/rank26-total-energy-direct-specialization.json`
- `research/benincasa/full-marked-total-energy-nilpotent.json`
- `research/benincasa/marked-soft-support-certificate.json`
- `research/benincasa/rank26-labelled-component-soft-specialization.json`
- `research/benincasa/rank26-soft-occurrence-transport.json`
- `research/benincasa/rank26-tangent-support-closure.json`
- `research/benincasa/rank26-tangent-support-algebra.json`
- `research/benincasa/x1-soft-parabolic-deletion-image.json`
- `research/benincasa/x1-soft-residue-quotient-port.json`
- `research/benincasa/x1-soft-joint-marked-residue-ports.json`
- `research/benincasa/marked-tangency-support-certificate.json`
- `research/benincasa/marked-radial-support-certificate.json`
- `research/nima/rank26-triangle-wall-collapse.json`
