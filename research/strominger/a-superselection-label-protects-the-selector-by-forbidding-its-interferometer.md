# A Superselection Label Protects the Selector by Forbidding Its Interferometer

## Correction to the apparent repair

Adding a strict superselection label does produce a nontrivial projector (P)
commuting with every admitted endomorphism. But this same rule forbids the
off-diagonal preparation and complementary readout maps needed to observe the
controlled metaplectic sign.

For a two-label object, the protected algebra is block diagonal. A relative
phase (Z) commutes with (P), whereas a coherent swap (X) and a
complementary Hadamard port (H) satisfy

\[
[Z,P]=0,
\qquad
[X,P]\ne0,
\qquad
[H,P]\ne0.
\]

Thus a strict superselection label solves preservation only by removing the
interference experiment.

## The required categorical object

The four-capability instrument cannot be one closed endomorphism algebra. It
requires three separately typed roles:

```text
preparation object --preparation port--> selector object
selector object ----protected core----> selector object
selector object ----readout port------> observation object
```

Only protected-core endomorphisms must commute with (P). Preparation and
readout are typed morphisms with different boundaries; requiring them to lie
in the commutant would erase their purpose.

This is a compositional distinction, not a chronological one. The roles are
fixed by domains, codomains, and allowed factorization positions.

## Refined theorem

No single unital operation algebra can simultaneously satisfy all three
claims:

1. every operation commutes with a nontrivial selector projector;
2. the algebra prepares coherent superpositions across selector sectors;
3. the algebra performs a complementary coherence readout.

The minimal repair is therefore not merely a larger labelled object. It is a
typed instrument category containing a protected endomorphism algebra plus
source-authorized preparation and observation ports that are not promoted to
arbitrary internal controls.

## New frontier

The magnetic source must supply this factorization as one constructor packet.
Supplying (P) alone gives an inert superselection rule. Supplying an
off-diagonal port alone destroys protection if it is closed under unrestricted
internal composition. The missing law must declare both the port boundaries
and the protected core.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/selector_protection_manipulation_role_split_checks.py
```
