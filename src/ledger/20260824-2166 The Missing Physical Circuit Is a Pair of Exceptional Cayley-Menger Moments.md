---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2166 — The Missing Physical Circuit Is a Pair of Exceptional Cayley--Menger Moments

## Derived target

Entry 2165 leaves the exceptional parity-check row

\[
\lambda_{\rm exc}=(\widehat y,-2\widehat q)
\]

over the projectivized all-soft Cayley--Menger family. Let
\(\Gamma_{\rm exc}\) denote the projectivized specialization of the complete
Bunch--Davies relative chain, retaining its source orientation, Kummer
branch, marked boundaries, and deck character. Let

\[
\omega_{\rm exc}
=
\frac{d_{\rm rel}\widehat a\wedge d_{\rm rel}\widehat b}{W}
\]

stand for the corresponding exceptional coefficient form, with all frozen
marked factors understood.

Linearity of the current pairing forces the physical covector to be

\[
\boxed{
\Lambda_{\rm BD}
=
\left(I_y,-2I_q\right),
}
\]

where

\[
I_y
=
\int_{\Gamma_{\rm exc}}\widehat y\,\omega_{\rm exc},
\qquad
I_q
=
\int_{\Gamma_{\rm exc}}\widehat q\,\omega_{\rm exc}.
\]

If the pair is finite and nonzero, its kernel is

\[
\boxed{
\mathcal L_{\rm phys}
=
\mathbb Q\langle(2I_q,I_y)\rangle.
}
\]

## Interpretation

The missing cosmological analogue of Strominger's primitive parity-check
vector is therefore not another algebraic kernel census. It is a
source-normalized pair of exceptional Cayley--Menger moments.

The ratio

\[
\zeta_{\rm BD}=\frac{I_y}{I_q}
\]

is naturally a projective period coordinate. Nothing derived so far forces
it to be a universal rational constant; it may vary over the exceptional
external-direction base.

## Acceptance contract

The pair defines a physical circuit only after proving:

1. convergence or a source-fixed renormalized value for both moments;
2. independence from the weighted lift used to reach the all-soft
   exceptional divisor;
3. compatibility with the weight-three projective Kummer cocycle;
4. cyclic transport among the three labelled occurrences;
5. nonvanishing of \((I_y,I_q)\);
6. compatibility with the physical deck character and relative-boundary
   orientation.

Failure of lift independence means the Tor packet is physically
underselected. A varying but well-defined \(\zeta_{\rm BD}\) gives a
sector-specific physical period line, not a universal integer circuit.

## Finite next computation

Construct a two-master relative reduction for the numerator insertions

\[
\widehat y\,\omega_{\rm exc},
\qquad
\widehat q\,\omega_{\rm exc}.
\]

Derive their Gauss--Manin connection and boundary values in one external
projective chart. The first falsifier is whether they span a rank-one or
rank-two period system:

- rank one with constant rational ratio: Strominger-like universal circuit;
- rank one with nonconstant algebraic ratio: canonical varying line;
- rank two: physical selector remains a genuine two-component period;
- undefined moments: frozen-source activation fails.

## Status

- exceptional coefficient packet: established;
- physical covector formula: derived conditionally from current pairing;
- moment values and lift independence: uncomputed;
- new Carrier datum: none.

## Evidence

- Entries 828--835 and 2160--2165
- research/benincasa/exceptional-bd-moment-covector.md
- allocator claim seqclaim-ec5e664094c5d59a2d9fc3db
