---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2178 — Contact Infinity Is Route Loss on Restriction but Interference on the Cartier Grade

## Compactified contact normals

Compactify two labelled contact denominators by

\[
\ell_j=\frac{\widehat\ell_j}{s_j},
\qquad
\ell_k=\frac{\widehat\ell_k}{s_k}.
\]

Then

\[
C_j=\frac{s_j}{\widehat\ell_j},
\qquad
C_k=\frac{s_k}{\widehat\ell_k},
\]

and Entry 2176's strict route packet becomes

\[
(A,B)
=
\frac{s_js_k}{\widehat\ell_j\widehat\ell_k}(8,-8).
\]

## Ordinary restriction

On either contact-infinity divisor,

\[
s_j=0
\qquad\text{or}\qquad
s_k=0,
\]

ordinary restriction gives

\[
\boxed{(A,B)|_{D_\infty}=(0,0).}
\]

Thus the displayed scalar routes undergo route loss at external infinity.
The vanishing order is one on a single component and two at the normal-
crossing corner (s_j=s_k=0).

## Cartier associated grade

The common factor (s_js_k) is source-derived by the reciprocal contact
product. Removing only that Cartier factor gives

\[
\boxed{
\operatorname{gr}_{(s_js_k)}(A,B)
=
\frac1{\widehat\ell_j\widehat\ell_k}(8,-8).
}

This is nonzero and remains in the kernel of the sum readout. Therefore the
first nonvanishing normal grade preserves destructive interference even
though ordinary boundary restriction sees route loss.

The normal exponents are integral, so their scalar normal monodromy is
trivial. The information is filtered/Cartier data, not a new branch
character.

## Mechanism classification

The two descriptions are not contradictory:

\[
\boxed{
\begin{aligned}
\text{ordinary boundary value}&:\text{ route loss},\\
\text{first nonzero Cartier grade}&:\text{ destructive interference}.
\end{aligned}
}
\]

This is the contact-packet analogue of the recurring Marici distinction
between an ordinary pullback and a supported or filtered secondary class.

## Physical boundary

Contact infinity is a compactification boundary of the external coefficient
base. Entry 2178 does not show that the Bunch–Davies physical family reaches
or pairs with its Cartier grade. A physical activation requires a
source-derived asymptotic family or relative-chain specialization. Without
that map, the filtered interference class is algebraically present but
physically unselected.

## Evidence

- Entries 2176–2177
- `research/benincasa/checkers/contact_infinity_cartier_interference.rs`
- allocator claim `seqclaim-805d0b866cd067475a55212d`
