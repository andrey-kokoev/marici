# 1770 — The Two-Loop Character Kills the Exceptional Relative-Sign Resonance

## Frozen question

Entry 1767 found a zero-exponent relative-sign slot on the exceptional divisor
over a generic transverse \(P_6\)-wall crossing. Entry 1769 found no
corresponding exceptional residue in the source audit. The remaining question
is whether the exceptional slot descends from a supported extension class on
the original normal-crossing complement.

## Labelled characters

At a transverse \(P_6\)-\(D\) crossing, order the local meridians as
\((\gamma_{P_6},\gamma_D)\). The relative-sign algebraic target has character

\[
(-1,+1),
\]

while the resonant wall-1 source line has character

\[
(+1,-1).
\]

Thus the local Hom line has character

\[
\chi=(-1,-1).
\]

The same computation holds at a transverse \(P_6\)-\(H\) crossing, with the
wall-2 source line replacing wall 1.

## Exact local calculation

For the punctured bidisk, the rank-one local-system cochain complex is

\[
\mathbb C
\xrightarrow{(-2,-2)^T}
\mathbb C^2
\xrightarrow{(-2,2)}
\mathbb C.
\]

The differential ranks are \((1,1)\), hence

\[
H^0=H^1=H^2=0.
\]

The exceptional meridian is the product
\(\gamma_{P_6}\gamma_D\) (respectively
\(\gamma_{P_6}\gamma_H\)), so its character is \(({-1})({-1})=+1\). This
explains the exceptional zero exponent, but the acyclic two-loop complex proves
that it is a blowup-only resonance: it is not the pullback of a local
\(\operatorname{Ext}^1\) class on the original two-divisor complement.

## Narrow result

\[
\boxed{
\text{The generic transverse }P_6\text{-wall relative-sign resonance does not descend.}
}
\]

This gives an exact conceptual explanation for Entry 1769's vanishing source
residues. No new carrier stratum or supported coefficient class is generated at
generic transverse \(P_6\)-\(D\) or \(P_6\)-\(H\).

The conclusion does not cover the deeper nontransverse factors of the exact
resultants (including soft and normalization-boundary intersections), where the
normal-crossing character calculation changes.

## Durable evidence

- `research/benincasa/checkers/p6_wall_character_koszul.rs`
- `research/benincasa/results/p6-wall-character-koszul.json`
- `research/benincasa/p6-wall-character-koszul.md`

