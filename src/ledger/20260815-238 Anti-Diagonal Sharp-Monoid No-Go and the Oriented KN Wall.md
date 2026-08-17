# Anti-Diagonal Sharp-Monoid No-Go and the Oriented KN Wall

## Record

Date: 2026-08-15

Status: falsified an ordinary reflection-equivariant fs-log divisor as the
missing conductor-Tor wall. The anti-diagonal wall remains canonical as an
oriented Kato--Nakayama or constructible sign-local-system direction. No
general derived/log-Borel--Moore correspondence no-go and no graph
admission are claimed.

## Relative characteristic lattice

For the product-branch characteristic map
\[
\mathbb N\longrightarrow\mathbb N^2,\qquad
1\longmapsto(1,1),
\]
the relative characteristic group is
\[
L=\mathbb Z^2/\mathbb Z(1,1)\simeq\mathbb Z_{\rm or}.
\]
With the ordered branch functional
\[
\delta(a,b)=b-a,
\]
the two branch classes are
\[
[a]=-1,\qquad [b]=+1.
\]
Branch reflection exchanges \(a\) and \(b\), hence acts on \(L\) by
\(n\mapsto-n\).

## Sharp-monoid obstruction

An effective fs-log wall would require a nonzero sharp integral submonoid
of \(L\). Compatibility with both adjacent branch restrictions would put
both \(+1\) and \(-1\) in that monoid. They are additive inverses, so
\(+1\) would be a nonzero unit, contradicting sharpness.

Equivalently, no nonzero sharp ray in \(L\) is reflection invariant:
reflection maps every positive element to its inverse. Choosing the
ordered positive ray is possible, but reflection exchanges it with the
opposite ray.

This obstruction repeats for all six ordered long-road pairs. It is
independent of coefficients and occurs before endpoint framing or the
generic-\(Q\) connector.

## Consequence for the spatial kernel

Entry326 already shows that the two ordinary Rees boundary sections cannot
produce the third primitive wall face. The present theorem additionally
shows that the missing wall cannot be repaired by adjoining one ordinary
reflection-equivariant fs-log boundary divisor.

The conductor-Tor direction is intrinsically groupified and oriented. Its
correct geometric carrier must therefore permit the sign action, for
example:

- the oriented Kato--Nakayama circle/relative interval with its
  anti-diagonal orientation local system;
- a constructible vanishing-cycle object; or
- a derived/log-Borel--Moore wall object whose relative dualizing line is
  \(\mathbb Z_{\rm or}\).

The remaining required arrow is a proper Beck--Chevalley realization from
that oriented object to the literal entry143 wall costalk, with the two
Rees-chart restrictions and entry325's principal-line evaluation. The
orientation sign is derived by the quotient lattice; it is not an
additional scalar choice.

## Executable evidence

Checker:
research/voevodsky/check_dp6_anti_diagonal_fs_log_no_go.rs

SHA-256:
0bbe93554ff15c520403246b819d43f361495f33a3fc8d269f73a297228d85f3

Fresh rustfmt --check, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used because no
repository-scoped structured-command MCP capable of invoking Rust is
exposed.

## Outcome contract

~~~json
{
  "claim": "The anti-diagonal conductor-Tor lattice has branch classes -1 and +1 and reflection n to -n. No nonzero sharp integral monoid can contain both classes or be reflection invariant, so the missing wall is not an ordinary equivariant fs-log divisor.",
  "status": "falsified_scoped_reflection_equivariant_fs_log_wall",
  "scope": "ordinary fs-log divisor/ray realization of the third wall with both branch restrictions and physical reflection; oriented KN, constructible, derived, and vanishing-cycle correspondences excluded",
  "characteristic": {
    "relative_lattice": "Z^2/Z(1,1)=Z_or",
    "class_a": -1,
    "class_b": 1,
    "branch_swap": "n to -n",
    "both_effective_classes_make_nonzero_unit": true,
    "nonzero_reflection_invariant_sharp_ray_exists": false,
    "ordered_positive_ray_exists": true,
    "reflection_preserves_ordered_positive_ray": false,
    "ordered_pairs": 6
  },
  "minimal_additional_datum": "An oriented Kato-Nakayama/constructible sign-local-system wall or derived vanishing-cycle object, with reflection acting on its orientation line and a proper Beck-Chevalley realization into the literal entry143 wall costalk.",
  "unconstructed": [
    "oriented wall six-functor correspondence",
    "proper Beck-Chevalley realization of all 72 rows",
    "endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_anti_diagonal_fs_log_no_go.rs",
  "checker_sha256": "0bbe93554ff15c520403246b819d43f361495f33a3fc8d269f73a297228d85f3"
}
~~~
