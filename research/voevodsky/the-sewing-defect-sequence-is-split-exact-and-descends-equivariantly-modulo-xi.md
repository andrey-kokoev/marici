# The sewing-defect sequence is split exact and descends equivariantly modulo Xi

## Question

Does the phase-space defect quotient introduce a new extension, closure, or coherence obstruction before the Evans/Xi class is tested?

## Claim boundary

No. The graph inclusion and defect map form a canonically split exact sequence. The splitting is continuous, Fourier-equivariant, and remains exact for holomorphic families after quotienting by the Xi ideal. Therefore every remaining obstruction is carried by the particular Evans defect class, not by the ambient quotient construction.

## Split defect sequence

Let \(H\) be the complete response space and \(T:H\to H\) the unitary quarter turn. Define

$$
i_T:H\to H\oplus H,
\qquad
i_Tx=(x,Tx),
$$

and

$$
d_T:H\oplus H\to H,
\qquad
d_T(x,y)=y-Tx.
$$

Then

$$
d_Ti_T=0,
$$

$$
\ker d_T=\operatorname{ran}i_T,
$$

and \(d_T\) is surjective. Hence

$$
0\longrightarrow H
\xrightarrow{i_T}
H\oplus H
\xrightarrow{d_T}
H
\longrightarrow0
$$

is exact.

## Canonical splitting

Define

$$
r:H\oplus H\to H,
\qquad r(x,y)=x,
$$

and

$$
s:H\to H\oplus H,
\qquad s(h)=(0,h).
$$

They satisfy

$$
ri_T=I_H,
\qquad
d_Ts=I_H,
$$

and the chain-homotopy decomposition

$$
\boxed{
i_Tr+sd_T=I_{H\oplus H}.}
$$

Indeed,

$$
(x,y)=(x,Tx)+(0,y-Tx).
$$

Thus the sequence is continuously split on every declared Hilbert, Schwartz, relative-history, and strong-dual rung on which \(T\) acts continuously.

## Fourier equivariance

Let the simultaneous boundary quarter turn be

$$
\mathbb T_\partial(x,y)=(Tx,Ty).
$$

Then

$$
\mathbb T_\partial i_T=i_TT,
$$

and

$$
d_T\mathbb T_\partial=T d_T.
$$

Therefore the quotient identification

$$
(H\oplus H)/\operatorname{Graph}(T)
\simeq H
$$

is canonical and quarter-turn equivariant.

## Holomorphic families

Apply the construction pointwise to \(\mathcal O(H)\). Because all maps are continuous and constant in \(z\), one obtains a split exact sequence of \(\mathcal O\)-modules:

$$
0\to\mathcal O(H)
\to\mathcal O(H\oplus H)
\to\mathcal O(H)\to0.
$$

The same explicit splitting works after passing to the Xi-divisor quotient:

$$
0\to
\frac{\mathcal O(H)}{\tau\mathcal O(H)}
\to
\frac{\mathcal O(H\oplus H)}{\tau\mathcal O(H\oplus H)}
\to
\frac{\mathcal O(H)}{\tau\mathcal O(H)}
\to0.
$$

No tensor-exactness theorem is needed; exactness follows directly from the surviving formulas for \(r\) and \(s\).

## Evans class

For a holomorphic Evans boundary pair

$$
e(z)=(e_-(z),e_+(z)),
$$

the complete obstruction is

$$
\operatorname{Def}_{\rm Ev}(z)
=d_Te(z)
=e_+(z)-Te_-(z).
$$

Its divisor class is

$$
[\operatorname{Def}_{\rm Ev}]
\in
\mathcal O(H)/\tau\mathcal O(H).
$$

Chain promotion is equivalent to

$$
[\operatorname{Def}_{\rm Ev}]=0.
$$

All shell and multiplicity-jet equations are coordinate evaluations of this one class.

## Relation to the fresh owner worksheet

Aspect's new worksheet leaves the authoritative \(U_{\rm G4}\) and pairings empty while admitting the candidate ordered-pair source carrier `ThetaPair`. The split sequence shows that completing that carrier or the boundary quotient creates no additional abstract extension class. Once \(U_{\rm G4}\) is supplied, its difference from the constructed crossing maps directly to the same defect coordinate.

## Disposition

The ambient sewing-defect complex is canonically split, topologically closed, Fourier-equivariant, and remains split modulo Xi. It has no hidden cohomological obstruction. The sole nonzero datum that can remain is the concrete Evans defect class, whose vanishing is exactly the RH-bearing source-placement theorem.