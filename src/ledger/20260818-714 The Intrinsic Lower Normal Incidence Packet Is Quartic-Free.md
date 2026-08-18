---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 714 — The Intrinsic Lower Normal Incidence Packet Is Quartic-Free

## Frozen packet

Entries 709--712 reduce the only unresolved signed lower-normal branch to:

1. the minus quadratic pair residue;
2. the repeated plus quadratic pair residue;
3. the mixed triple costalk on \(\eta^2=T_2\);
4. the constant oriented incidence coefficients
   \((1/2,-1/2,1/2)\).

For a quadratic Kummer family, the intrinsic Gauss--Manin pole divisor is
contained in the union of its leading-coefficient and discriminant divisors.
The triple cover adds its two leading coordinate factors and binary-quadratic
discriminant.

## Complete divisor audit

On the homogeneous base the two pair leading coefficients are

\[
A_-=(\ell_2\ell_3)^2,
\qquad
A_+=(\ell_1\ell_4)^2.
\]

Their second-normal discriminant coefficients are, up to units,

\[
C_- =\ell_1\ell_2^2\ell_3^2\ell_4,
\qquad
C_+ =\ell_1^2\ell_2\ell_3\ell_4^2.
\]

The mixed triple cover has leading coordinate factors \(X_2,X_3\) and
discriminant

\[
\operatorname{Disc}(T_2)=\ell_1\ell_2\ell_3\ell_4.
\]

Exact polynomial gcd gives

\[
\boxed{
\gcd(\mathcal Q,A_-)
=\gcd(\mathcal Q,A_+)
=\gcd(\mathcal Q,C_-)
=\gcd(\mathcal Q,C_+)=1,}
\]

and likewise

\[
\boxed{
\gcd(\mathcal Q,X_2X_3\operatorname{Disc}(T_2))=1.}
\]

The incidence coefficients are nonzero constants and introduce no pole
divisor.

## Narrow conclusion

\[
\boxed{
\text{the complete intrinsic signed lower-normal Kummer/incidence packet
has no }\mathcal Q\text{ support}.}
\]

Therefore the lower deletion branch does not generate the homogeneous
quartic through its pair connections, mixed triple cover, or their canonical
incidence. Producing \(\mathcal Q\) would require an additional
source-derived comparison with a larger pushforward or physical integration
chain. It cannot be inferred from this local packet.

This does not prove that every possible derived pushforward of the generic
lower family is quartic-free. It closes the intrinsic pair--triple normal
mechanism frozen in Entries 706--712.

## Classification

- carrier: unchanged marked energy/Cayley--Menger incidence;
- coefficient systems: pair and triple Kummer objects;
- singular support: soft and signed-energy divisors;
- \(\mathcal Q\): absent;
- new carrier datum: none.

## Evidence

- `research/benincasa/check_lower_normal_incidence_q_support.py`;
- Entries 698, 706, 707, 709, 711, and 712;
- allocator claim `seqclaim-7a6f80535936ca97e30ac744`.

## Next falsifier

Retire the intrinsic lower-normal branch as a home for \(\mathcal Q\). Return
to the full marked top-sector relative Gauss--Manin object and test the first
remaining typed location: an extension coefficient involving the physical
integration-chain/Gysin local system. Any new comparison must be derived from
that relative source; no map from the lower packet may be fitted post hoc.
