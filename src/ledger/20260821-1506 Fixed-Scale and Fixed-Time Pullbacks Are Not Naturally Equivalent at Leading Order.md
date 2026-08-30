# 1506 — Fixed-Scale and Fixed-Time Pullbacks Are Not Naturally Equivalent at Leading Order

## Status

Primary-source finite falsifier of Entry 1504's proposed natural equivalence.

## Frozen spectra

Easther, Kinney, and Peiris compare the leading boundary-EFT and new-physics-hypersurface spectra. With

\[
y_i=\frac{k}{a_iH_i},
\]

the fixed-time boundary result is [astro-ph/0505426, Eqs. (1)–(2)]

\[
\frac{P_{\rm BEFT}(k)}{P_{\rm BD}(k)}
=
1+\beta\frac{H_i}{M}y_i\sin(2y_i).
\]

For the fixed-physical-scale prescription [Eq. (3)],

\[
\frac{P_{\rm NPH}(k)}{P_{\rm BD}(k)}
=
1+\frac{1}{2y_c}
\sin\!\left(\frac{2y_c}{1-\epsilon}\right),
\]

where \(y_c\) is evaluated at \(k=aM\) and is only weakly scale dependent in slow roll.

Their qualitative behaviors disagree:

- BEFT amplitude grows linearly with \(k\), and its phase is proportional to \(k\);
- NPH amplitude decreases toward short wavelengths, and its modulation is effectively logarithmic in \(k\).

## Attempted comparison map

The source itself tests whether boundary-hypersurface independence can reconcile the two sectors by allowing

\[
\beta=\beta(y_i).
\]

In de Sitter space the invariance equation is [Eq. (15)]

\[
\frac{d}{dy_i}
\left[
y_i\beta(y_i)\sin(2y_i)
\right]
=0.
\]

Its solution is [Eq. (16)]

\[
\boxed{
\beta(y_i)
=
\frac{\beta_0}{y_i\sin(2y_i)}.
}
\]

This is not a regular change of presentation:

1. it has poles wherever \(\sin(2y_i)=0\);
2. near the UV cutoff those poles signal breakdown of the effective expansion;
3. in slow roll it reproduces the order and logarithmic amplitude dependence of NPH but not its periodicity;
4. the source notes that a self-consistent construction would require introducing the second physical scale \(H\) into the EFT expansion.

## Result

\[
\boxed{
\text{fixed-scale NPH}
\not\simeq
\text{fixed-time BEFT}
\quad
\text{within the frozen regular leading boundary coefficient system}.
}
\]

The obstruction is coefficient-theoretic rather than a new carrier incidence. Both constructions can live over the mode–time incidence carrier of Entry 1504, but their pullbacks carry inequivalent coefficient objects.

An approximate reconciliation is possible only after a nontrivial coefficient extension involving:

- hypersurface-running couplings;
- additional \(H/M\) dependence;
- control of the pole divisor \(\sin(2y)=0\);
- recovery of the missing NPH phase/periodicity.

None is supplied by a mere carrier reparameterization.

## Update to the common-core conjecture

This is a clean cosmological instance of H2:

\[
\boxed{
\text{shared incidence carrier and comparison calculus}
+
\text{sector-specific coefficient systems}.
}
\]

It is negative evidence for H1. The same carrier does not force identical coefficients or observables.

## Next falsifier

Construct the full boundary renormalization/transport object over the incidence carrier and ask whether its regular horizontal sections reproduce the NPH coefficient system without poles or fitted phase data.

Failure would establish that NPH and BEFT are genuinely different coefficient sectors. Success would identify the missing comparison object, but would not turn the NPH section into a universal spacetime boundary.

## Provenance

- R. Easther, W. H. Kinney, and H. Peiris, *Boundary Effective Field Theory and Trans-Planckian Perturbations: Astrophysical Implications*, arXiv:astro-ph/0505426, Eqs. (1)–(3), (14)–(28).
- Ledger sequence claim: seqclaim-1e061f1f85e66422eac9a91d.
- Epistemic graph event: ev-000000001633-89e162f1-9b4a-40fe-bf95-2d97a060930a.
