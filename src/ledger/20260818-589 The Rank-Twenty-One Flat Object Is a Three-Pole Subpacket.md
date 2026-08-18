# 589 — The Rank-Twenty-One Flat Object Is a Three-Pole Subpacket

## Correction

Entries 580--587 correctly construct and test a flat deletion-filtered object for

\[
\{q_{g_1},q_{g_2},q_{G_{12}}\}.
\]

They do not construct the complete source summand in the \(q_{G_{12}}\) sector. References there to the “physical top line” or “physical top packet” are too strong and are superseded by this scope statement.

## Frozen source comparison

Equation eq:Triangle of arXiv:2408.16386v2 has, in each \(q_{G_{12}}\)-containing term,

\[
\frac{1}{q_{g_1}q_{g_2}q_{g_3}q_{G_{12}}q_{g_{23}}}
\qquad\text{or}\qquad
\frac{1}{q_{g_1}q_{g_2}q_{g_3}q_{G_{12}}q_{g_{31}}}.
\]

The rank-twenty-one checker instead uses

\[
q_{g_1}=c+b+X_1,\quad
q_{g_2}=c+a+X_2,\quad
q_{G_{12}}=c+E.
\]

It omits

\[
q_{g_3}=a+b+X_3
\]

and, term by term, either

\[
q_{g_{23}}=c+b+X_2+X_3
\]

or

\[
q_{g_{31}}=c+a+X_3+X_1.
\]

After taking \(q_{G_{12}}=0\), these become the four-pole lower families frozen in Entry 545:

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{g_{23}}\},
\qquad
\{q_{g_1},q_{g_2},q_{g_3},q_{g_{31}}\}.
\]

The first has deletion-closed generic rank \(34\), not \(21\).

## What survives

For the declared three-pole family, the following remain valid:

- deletion ranks \((7,8,8,9,16,18,18,21)\);
- coherent injective localization maps;
- two-direction connection naturality;
- a canonical rank-one proper three-pole quotient;
- a rank-two boundary extension;
- mixed-jet flatness;
- regularity on the tested generic \(\mathcal Q=0\) fibers.

Thus

\[
\boxed{
H_{21}^{(g_1,g_2,G_{12})}
\text{ is a flat canonical three-pole subpacket.}
}
\]

## What is withdrawn

The calculations do not establish

\[
H_{21}^{(g_1,g_2,G_{12})}
=
\text{the complete physical }q_{G_{12}}\text{ summand},
\]

nor that its rank-one proper quotient is the complete physical top line.

Entry 587 therefore excludes \(\mathcal Q\)-support only from this three-pole subpacket. The independent source-level physical-chain theorem of Entry 181 remains valid.

## Classification

- defect type: scope/typing error, not an algebraic failure;
- established object: flat three-pole coefficient subpacket;
- missing source data: two denominator factors in each physical summand;
- carrier modification required: none;
- H2 status: unchanged.

## Next finite falsifier

Construct the actual five-pole pre-residue deletion object for

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{G_{12}},q_{g_{23}}\}
\]

and its cyclic \(q_{g_{31}}\) partner. Derive the literal Poincare residue along \(q_{G_{12}}=0\) into the frozen rank-34 four-pole lower module, then compare its source-master image with

\[
0\to\mathcal T_7\to\mathcal M_q^{(9)}
\xrightarrow{R_\infty}\mathbb V_{\rm ell}(-1)\to0.
\]

No projector or fitted complement is admissible.

## Evidence

- research/benincasa/marici-gm/src/bin/generic_q_pole_twisted_derham_rank.rs;
- research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs;
- research/benincasa/check_marked_relative_q.rs;
- frozen arXiv source temp/arxiv-2408.16386-source/sections/applications.tex;
- Entries 545 and 580--587.
