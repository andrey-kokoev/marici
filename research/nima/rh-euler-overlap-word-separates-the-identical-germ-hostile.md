# The Euler-overlap word separates the identical-germ hostile

## Two bordered candidate packets

Fix one constructor-closed pre-scalar marked germ \(g\). It contains the full
currently declared analytic synthesis, primitive and square incidence,
archimedean and zero-frequency ports, reciprocal transports, and cutoff
bonding data.

Let \(E_g(s)\) be its labelled Euler reconstruction on the source chamber

\[
\Re s>1.
\]

The actual bordered packet is

\[
P=(g,\sigma),
\]

where \(\sigma\) is the global theta section. Define the reciprocal-even
polynomial

\[
H(s)=
1+
\frac{256}{3}
s(s-1)
\left(s-\frac12\right)^2.
\]

The hostile bordered packet is

\[
P_H=(g,H\sigma).
\]

The two packets have exactly the same pre-scalar marked germ. The multiplier
is applied only to the candidate determinant section after every germ port has
been constructed. It also preserves reciprocal reflection and the three
normalizations at \(0\), \(1/2\), and \(1\).

It is hostile because it has zeros at \(1/4\) and \(3/4\). Those zero values
are used only to certify that the alternative changes the divisor, not to
distinguish its source authority.

## Source-derived constructor word

The Tate source already authorizes two maps on the Euler chamber:

1. reconstruct \(E_g\) from the labelled Euler packet;
2. restrict the proposed global theta section to the same chamber.

Their difference is the overlap residual

\[
W_{\mathrm E}(g,\tau)
=
\tau|_{\Re s>1}-E_g.
\]

This is a constructor word from source data and the candidate section port. It
does not inspect the divisor.

For the actual packet, Tate's Mellin overlap identity gives

\[
W_{\mathrm E}(P)=0.
\]

For the hostile packet,

\[
W_{\mathrm E}(P_H)
=
(H-1)E_g.
\]

At \(s=2\),

\[
H(2)=385.
\]

The Euler reconstruction is nonzero there, so the hostile residual is
nonzero. The packets are separated in the absolutely convergent Euler chamber,
before either inserted zero is evaluated.

## Categorical consequence

The immediate pre-scalar germ is intentionally divisor-blind. Once a candidate
global section is adjoined, constructor congruence closure must include the
Euler-overlap word. The actual and hostile bordered packets then lie in
different full fibers.

This gives the exact answer to Deutsch's hostile-pair test:

- identical current germ data can support two proposed scalar continuations;
- the source-derived overlap constructor rejects the hostile continuation;
- therefore arbitrary divisor insertion is not a source-preserving operation.

## Scope boundary

This result establishes source-section rigidity, not RH. It excludes changing
the divisor while claiming the same source germ. It does not prove that the
unique actual source section lacks off-seam zeros.

The remaining explanatory problem is internal: find a source law that makes
an off-seam zero of the already rigid actual section impossible. Repeating the
hostile multiplier test cannot solve that problem.

## DPC verdict

The present germ calculus does contain a pre-zero discriminator for external
hostile divisor insertion. The discriminator is exact Euler–theta overlap.
The calculus still contains no zero-confinement explanation for the unique
actual section.

## Verification

`check_rh_euler_overlap_hostile_pair.py` verifies identical pre-scalar germ
signatures, reciprocal symmetry, preserved anchor normalizations, the hostile
divisor change, zero actual overlap residual, and nonzero hostile overlap
residual at \(s=2\).
