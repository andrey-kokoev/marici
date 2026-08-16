# Literal Pair-Support No-Go and the External Log-Gysin Correspondence Gate

Date: 2026-08-15  
Status: falsified for a direct support-preserving realization of the
projective-SNC pair strata in the literal entry-143 face-indexed complex.
Extraordinary/log-BM or cdh correspondences with new overlap objects remain
possible and are the required next geometry. No graph admission is claimed.

## Result

Entry 206 constructs the canonical integral augmented SNC/Tate carrier bridge.
Its middle degree has three pair-intersection generators. Including their
three reflected mates gives six labelled pair objects. The four Boolean
normal states on each object produce the necessary
\[
6\cdot 4=24
\]
pair/normal rows.

Entry 143, however, has generators only of the form \([S,H]\), where \(S\) is
a noncrossing \(K_6\) face and \(H\subseteq S\). The three physical long roads
are
\[
D_{14},\quad D_{03},\quad D_{25}.
\]
Every distinct pair crosses. Exhaustive enumeration of the \(K_6\) face
poset gives face counts
\[
(1,9,21,14)
\]
in dimensions \(0,1,2,3\), and exactly zero faces containing any long-road
pair. Consequently all 24 necessary source states have zero legal literal
entry-143 target summands.

The SNC pair differential is the cyclic incidence matrix \(R-I\), which has
rank two and a unit \(2\times2\) minor. Each two-normal Boolean top also has
two nonzero singleton boundary terms, with their second differential
cancelling integrally. A zero direct assignment therefore erases these
required rows; it does not derive them. Whether an extraordinary
corridor-valued image closes the resulting chain equations is outside this
no-go's scope.

Rotation cycles the three crossing pairs and reflection fixes one road while
exchanging the other two, so the obstruction is \(D_3\)-stable. The two-top
coefficient bridge of entries 205--206 repairs the integral generic-top
carrier but does not create the missing support objects.

## Scoped no-go

There is no direct support-preserving realization of the projective-SNC
pair-intersection Boolean packet in the existing literal entry-143
\([S,H]\) diagram. The demanded 24 rows cannot be obtained by relabeling pair
strata as ordinary \(K_6\) faces, and a zero assignment does not realize the
required nonzero data.

This does **not** rule out the requested full-log excess-Gysin
correspondence. Such a correspondence necessarily lies outside the ordinary
face-indexed category.

## Minimal additional datum

For every unordered long-road pair \((i,j)\), adjoin a genuine external
overlap object \(W_{ij}\) and a correspondence
\[
\Gamma_{ij}^{!,\log}\longrightarrow C_\bullet(q_k)\subset F_B/F_V
\]
with:

1. proper/log-BM or nearby-cycle source legs carrying normalization and
   conductor provenance;
2. the reflected mate of every pair object, with the forced polarity action;
3. four Boolean occurrence/normal states on every labelled pair object,
   together with the independently retained multiplicity/Tor data;
4. restriction maps to both adjacent long-facet packets;
5. Beck--Chevalley maps realizing both nonzero SNC and normal boundaries;
6. a support comparison to the complementary marked corridor \(q_k\);
7. endpoint framing and \(D_3\)/reflection coherence.

Only after these external objects and maps are constructed is there an
intrinsic 24-row matrix to solve. The endpoint/Q mapping fiber,
\(p_{\partial,Q}\), its Bockstein, \(D_8\), and Jordan coherence therefore
remain undefined.

## Certificate

- `research/voevodsky/check_p2_snc_literal_pair_support_no_go.rs`
- SHA-256:
  `0562d912ed7c7eb9a78a9354a8f2cce39dd8a7e24be049f87fa0f643745af428`

Validation:

- `rustfmt --edition 2021 --check`: passed;
- `rustc --edition=2021 -D warnings -O`: passed;
- linked runtime assertions and JSON emission: passed;
- temporary executable: removed;
- `git diff --check`: required before commit.

## Outcome contract

~~~json
{
  "claim": "The 24 reflected-pair/Boolean source rows required by the projective-SNC bridge have no legal direct target summands in entry143 because every pair of physical long roads crosses; the only direct support-preserving assignment is zero, which erases rather than realizes the nonzero SNC and Boolean boundary data.",
  "status": "falsified_scoped_direct_literal_pair_support_realization",
  "scope": "direct support-preserving maps into the existing entry143 [S,H] face-indexed complex only; external extraordinary, log-BM, cdh, or nearby-cycle overlap correspondences are not ruled out",
  "evidence": {
    "k6_face_counts": [1, 9, 21, 14],
    "crossing_long_pairs": 3,
    "reflected_pair_objects": 6,
    "boolean_states_per_pair_object": 4,
    "required_pair_rows": 24,
    "legal_literal_entry143_rows": 0,
    "pair_incidence_rank": 2,
    "pair_incidence_saturated": true,
    "normal_top_boundary_nonzero": true,
    "normal_square_d2_zero": true,
    "D3_reflection_stable": true,
    "two_top_bridge_repairs_support": false,
    "physical_mapping_fiber": "unconstructed"
  },
  "checker_sha256": "0562d912ed7c7eb9a78a9354a8f2cce39dd8a7e24be049f87fa0f643745af428",
  "next_required_map": "Construct external W_ij/Gamma_ij^{!,log} objects with proper/log-BM provenance, reflected pair objects, four Boolean states, multiplicity/Tor data, adjacent-facet Beck-Chevalley maps, and a support comparison to the complementary q_k corridor."
}
~~~
