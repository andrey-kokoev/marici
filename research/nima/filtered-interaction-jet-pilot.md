# Filtered Interaction and Probing Depth: Jet Pilot

## Finite-depth model

Represent an object probed through depth \(d\) by its jet

\[
\tau_d f\in A_d=k[x]/(x^{d+1}).
\]

Interaction is multiplication.  Exact truncation naturality holds:

\[
\boxed{
\tau_d(fg)=	au_d\bigl((\tau_df)(\tau_dg)\bigr).
}
\]

Thus two objects known through a common depth can interact without consulting
unprobed coefficients.  If their certified depths differ, the unconditional
result is certified only through the smaller depth.

## Residue as the next coherence channel

At depth two, write

\[
u=u_0+u_1x+u_2x^2,
\qquad
v=v_0+v_1x+v_2x^2.
\]

The first omitted interaction grade is

\[
\boxed{B(u,v)=u_1v_2+u_2v_1,}
\]

the coefficient of \(x^3\).  It is not an arbitrary log entry.  With the
degree-three line viewed as a square-zero \(A_2\)-bimodule, exact calculation
gives the Hochschild cocycle law

\[
u\cdot B(v,w)-B(u\star v,w)
+B(u,v\star w)-B(u,v)\cdot w=0.
\]

Retaining \(B\) reconstructs multiplication through depth three, and the
lifted product is strictly associative.  Hence the coherence residue is
precisely the data required to extend interaction by one probing level.

This realizes the proposed two-channel operation:

\[
(u,r_u)\widehat\star(v,r_v)
=
\left(
u\star v,
u_0r_v+r_uv_0+B(u,v)
\right).
\]

The first component is the current-depth value; the second is the accumulated
next-depth coherence channel.

## Catch-up gate

Catch-up is not automatic.  The two states

\[
f_1=1,
\qquad
f_2=1+x^2
\]

have the same depth-one jet but different depth-two interactions with a generic
partner.  No operation receiving only \(\tau_1f\) can decide which extension
is correct.

Therefore a shallower object reaches a partner's greater depth only if it has
a source-defined extension law, recurrence, propagator, or new causal input.
Otherwise interaction projects to the common minimum depth.

## What the pilot establishes

The Operator's conjecture has an exact mathematical realization:

\[
\boxed{
\text{probing depth}=\text{filtration level},
\qquad
\text{residue}=\text{next-grade extension cocycle}.
}
\]

Interaction composes both current values and their accumulated residues.
Higher coherence is not metaphorical here: it is the cocycle identity required
for associative continuation.

The pilot does not establish that physical time equals jet depth or that all
Carrier interactions use this particular filtration.  The next test is to
locate the same cocycle law in an existing source-derived Marici filtration—
preferably the alternating-fusion normal jets or a nearby-cycle/Rees complex.

## Existing Marici interaction gate

Grothendieck's Phase-I operation-inventory closure prevents a universal
interpretation of the pilot.  None of the five admitted multiplication
candidates is simultaneously Carrier-level, coefficient-neutral, total,
equivariant, unital, and distributive.  Connected edge sewing is a genuine
Carrier operation only after compatible boundary interfaces are marked; the
coherent all-even external product lives in a framed coefficient sector.

Therefore the phrase ``when two objects meet'' must be typed as a partial
operation

\[
\mu_{p,q}:X_p\times Y_q\dashrightarrow Z
\]

defined only for compatible ports \(p,q\).  The filtered conjecture applies
only after \(\mu_{p,q}\) is admitted and shown to preserve the filtration:

\[
\tau_d\mu_{p,q}(X,Y)
=
\tau_d\mu_{p,q}(\tau_dX,\tau_dY).
\]

No matched port is a type error, not a coherence residue.  A matched port with
incomplete depth uses the common minimum or a source-derived catch-up map.
Only then can its next-grade failure define a cocycle such as \(B\).

The strongest surviving formulation is consequently:

\[
\boxed{
\text{matched ports}
+\text{common certified filtration}
\longrightarrow
\text{value composition}+	ext{higher coherence residue}.
}
\]

Certificate:
`research/nima/checkers/check_filtered_interaction_jet_pilot.py`
