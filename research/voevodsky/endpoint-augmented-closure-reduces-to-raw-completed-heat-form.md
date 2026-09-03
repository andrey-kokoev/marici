# Endpoint-augmented closure reduces to the raw completed-heat form

## Question

After adjoining the independent endpoint coordinate, what remains to prove for closability and semiboundedness of the remainder-localizer form?

## Claim boundary

The augmented form splits as the raw completed-heat form plus a bounded positive endpoint block. Therefore its closability and semiboundedness reduce exactly to those of the raw completed-heat form on the order bulk. No additional endpoint cross term remains. The raw form is not proved closable or semibounded here.

## Augmented carrier

The graph completion is

\[
\mathcal H_E
=
\mathcal H_{\rm ord}
\oplus
\mathbb C_E.
\]

Write vectors as \((f,z)\). The endpoint coordinate is independent after completion.

## Block form

Let

\[
\alpha_h=e^{h/4}-1.
\]

The natural extension of the remainder form is

\[
q_E((f,z),(g,w))
=
q_H(f,g)
+
\alpha_h\overline zw,
\]

where \(q_H\) has kernel

\[
K_H(a,b)
=
H(a+b)-H(a+b+h).
\]

In block notation,

\[
q_E
=
\begin{pmatrix}
q_H&0\\
0&\alpha_h
\end{pmatrix}.
\]

There is no source cross term: on the original graph vectors \((f,L_Ef)\), this evaluates to

\[
q_H(f)+\alpha_h|L_Ef|^2
=
q_R(f).
\]

## Closability equivalence

The endpoint block is bounded on \(\mathbb C_E\). A direct-sum form with one bounded closed block is closable exactly when the other block is closable. Hence

\[
q_E\text{ is closable}
\quad\Longleftrightarrow\quad
q_H\text{ is closable on }\mathcal H_{\rm ord}.
\]

If \(q_H\) closes, then

\[
\overline q_E
=
\overline q_H
\oplus
\alpha_h|z|^2.
\]

## Semiboundedness equivalence

Since \(\alpha_h>0\), the endpoint block introduces no negative direction. Therefore \(q_E\) has a global lower bound exactly when \(q_H\) does. The least lower constant of the augmented form is the lower constant of the raw block, truncated against zero if necessary.

## Consequence

The endpoint problem is completely localized:

- it obstructed closability on the unaugmented carrier;
- graph completion turned it into an independent positive bounded block;
- it no longer participates in the remaining closure residual.

The live mathematical problem is now

`closable_semibounded_raw_completed_heat_form_on_H_ord`.

This is sharper than asking again for a joint endpoint--gamma--prime domain.

## Disposition

The endpoint-augmented carrier is constructed and its block form is typed. The first unresolved object is the closure and lower bound of \(q_H\) on the order completion. Source--Weil comparison and RH remain unproved.

## Verification

- `research/voevodsky/checkers/check_endpoint_augmented_block_form.py`
- `research/voevodsky/results/endpoint_augmented_block_form.json`
