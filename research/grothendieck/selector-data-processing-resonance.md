# Selector data-processing inequality for resonance spectra

## Theorem

Let `c:G->X` be a selector on a finite group and let `f:X->Y` be any
deterministic post-processing. Put `d=f compose c`. Then

`Stab_R(c) subset Stab_R(d)`.

Taking normal cores gives

`K_c subset K_d`.

The resonance monotonicity theorem therefore yields

`R(K_c) | R(K_d)` and `U(K_d) subset U(K_c)`.

Thus deterministic coarse-graining can only enlarge the terminal invisible
kernel and can only shrink the compatible power--Mackey operation system.
An injective post-processing on the image of `c` preserves both exactly.

## Strict C6 chain

On `G=C6`, start with the fully labelled selector `c(g)=g`, post-process to
parity, then post-process to the constant selector. The terminal kernels have
orders

`1 < 3 < 6`,

their radical resonance labels are

`1 | 3 | 6`,

and their spectra are respectively all indices, indices prime to three, and
indices prime to six. All inclusions are strict on indices 1 through 24.

## Interpretation and scope

This is a coefficient-side data-processing law. Information loss makes more
deck transformations invisible, which creates more quotient constraints and
removes arithmetic operations. It does not say that post-processing is a
physical constructor and does not provide any relative-chain pushforward.
