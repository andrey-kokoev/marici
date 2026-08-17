# Central-Flip Finite Normal Form and Ringed Realization Split

## Correction to the gate

Entry 346 treated d_central_flip as one wholly missing block. That boundary
is too coarse. Entries 120 and 121 already prove its finite
cellular/coefficient normal form on the positive D03 corner.

The source occurrence carrier is the two-route Koszul diamond

\[
R\langle F_{03}\rangle\xrightarrow{(x_3,-x_1)^T}
R\langle Z_3,Z_1\rangle\xrightarrow{(x_1,x_3)}
R\langle v_{10}\rangle,
\]

and not either single route. Its normalized filtered comparison retains the
occurrence extension and repeated-normal excess, with relative rank profile
\((1,2,1)\). The LCM/Alexander--Whitney cap, both Tor grades, and filtered
Bockstein square are integral and explicit.

Finite-free duality also gives the canonical extension by zero of the
v10-corner cochains. The complete occurrence Koszul--Cech map, including its
one-variable terms, identifies the resulting coefficient class with

\[
+\left[\frac{1}{x_1x_3u_0u_1u_3u_5}\right]\otimes[dX_{03}].
\]

This is the supported v10 corner of the local Cousin trace, not the complete
road trace.

## Actual split obstruction

The remaining central-flip block factors into two genuinely missing typed
operations:

1. d_central_flip_ringed_span: a normalization-provenanced marked spatial
   correspondence with projections p and q and an extraordinary trace;
2. d_central_flip_pc_purity: identification of the finite dual corner with
   the actual ringed PC extraordinary costalk.

Literal D03 pullback cannot provide the first map: entry 105 proves that it
sends the filtration Yoneda class to zero while the local Cousin trace is
nonzero. Nor can common-base Laurent localization identify the supported
corner with the complete road object: the corner Koszul complex becomes
contractible while the complete road augmentation remains nonzero.

Thus the current theorem is neither global nonexistence nor mere coefficient
underdetermination. The finite normal form exists and is forced; its spatial
six-functor provenance and PC purity are absent.

Read-only delegation evidence: run-20cecbd5adfc47c7bf29f6051c0d288e and
run-d88aa0ddc5e842d4a07e6ee0405c1bf1.
