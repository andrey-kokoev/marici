# 1086 — The Physical Hexagon Degenerates Through a Filtered Cospan

## Record

Entry 1085 established the support-level degeneration of the physical
three-site hexagon at total energy.  The existing occurrence, soft-Rees, and
rank-twelve calculations in Entries 329--333, 353, 366, and 367 determine
the coefficient-level architecture.

Sequence claim: `seqclaim-e627e62f21a198aac165b02b`.

## Occurrence-resolved degeneration

The six Bunch--Davies Leray germs form a canonical \(C_3\)-equivariant
family.  Over each marked Cut, its two lower-denominator occurrences do not
become equal copies.  They give two unequal nonzero Kummer classes

\[
\kappa_{ij|jk}\ne\kappa_{ij|ki},
\qquad
\kappa_{ij|jk}+\kappa_{ij|ki}=\kappa_{ij}^{\rm sewn}.
\]

The individual endpoint periods depend on an unprinted regulator hierarchy,
but the relative occurrence quotient and its sewn rank-one Kummer period
line are canonical.  Thus occurrence forgetting is a derived addition map,
not identification of two equal classes.

## Extension through soft support

At either site-soft branch, Entry 353 gives the Smith/Rees transition

\[
(1,2,2)\longrightarrow(1,2,2t).
\]

The ordinary special fiber has rank two, while the missing direction survives
at the next Rees grade.  Hence the filtered rank remains three.  The only
new factor is the already frozen soft Cartier normal \(t\); there is no new
support or torsion prime.

## Full coefficient comparison

The logarithmic total-energy image and Cut--nearby image are both rank three,
but Entry 367 proves

\[
\dim(L_{\log}+L_{\rm Cut})=5,
\qquad
L_{\log}\cap L_{\rm Cut}=\langle e_6\rangle.
\]

Therefore strict commutation or equality of coefficient images is false.
Their canonical relation is the filtered cospan

\[
L_{\log}
\longleftarrow
\mathcal C_{\rm cond}
\longrightarrow
L_{\rm Cut},
\]

whose common \(e_6\) line is the second-Rees bridge.  The elliptic nearby
line belongs only to \(L_{\log}\); the Cut--nearby commutator has zero
infinity-Gysin image.

## Deutsch--Popperian verdict

The stronger claim

\[
\boxed{
\text{the physical hexagon degenerates by a strict map to one generic
scattering Cut coefficient object}
}
\]

is falsified.  The surviving narrower statement is

\[
\boxed{
\text{the physical hexagon degenerates through an occurrence-resolved,
soft-Rees filtered conductor cospan.}
}
\]

This strengthens filtered H2 while rejecting its strict-image version:
the same carrier and comparison calculus relate distinct coefficient layers,
rather than forcing those layers to coincide.

## Classification

- carrier: existing total-energy, Cut, coordinate-soft, and occurrence
  incidence data;
- Tate/Kummer data: unequal occurrence classes and canonical sewn line;
- shared bridge: the second-Rees \(e_6\) line;
- elliptic data: separate Legendre nearby line on the logarithmic side;
- generic scattering Cut flag: not the degeneration object;
- new carrier datum: none.

## Evidence

- Entries 229, 329, 330, 333, 353, 366, 367, 1083, and 1085;
- `research/benincasa/physical-hexagon-total-energy-cospan.json`;
- the exact Rust/Smith/cyclic certificates cited by those entries.

## Next falsifier

Test the simultaneous double-soft point and the conductor/elliptic
intersections for the complete cospan.  A new torsion prime, irreducible
support factor, or loss of the common \(e_6\) line would push the architecture
toward H3.  Closure using only the two soft normals and the existing Legendre
node would further support filtered H2.
