# CP-selector physical16 rank (WP347)

## Lift to the faithful flavor quotient

Use a local nondegenerate `physical16` chart

\[
(z_1,\ldots,z_{15},j),
\]

where the (z_i) are CP-even and (j) is CP-odd. The WP327 spontaneous shell
imposes

\[
j^2=c_0^2,
\]

and an admitted positive orientation bias would refine it to (j=c_0).

Each constraint has rank one. Even after orientation selection, the selected
family retains all fifteen CP-even coordinates. The operation therefore
selects a proper CP component conditionally but not a distinguished
`physical16` point.

## Hostile pair

The checker constructs two exact chart points with the same (j=c_0) and
different (z_1). They satisfy the same shell, orientation, thermal-domain,
and calibrated CP readouts while remaining distinct points of the faithful
flavor quotient.

This is the first-nonfaithful-arrow diagnosis: `physical16 -> CP coordinate ->
domain preparation -> detector record`.

The first projection already erases fifteen physical directions. No downstream
domain tower or detector calibration can restore them.

## Disposition

The CP programme supplies a genuine partial selector, not merely a texture
rigidifier. Its magnitude and orientation remain conditional on source inputs,
and it cannot answer the full flavor-selector objective without new operations
constraining the fifteen CP-even coordinates.

Run `uv run --with sympy python
research/flavor/checkers/wp347_cp_selector_physical16_rank.py` to regenerate the
exact rank audit.
