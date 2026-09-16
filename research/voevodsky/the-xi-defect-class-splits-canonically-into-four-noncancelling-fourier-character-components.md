# The Xi defect class splits canonically into four noncancelling Fourier-character components

## Question

Can the single quotient class \([e_+-Te_-]\) be decomposed into independently testable pieces, and can cancellation occur between different Fourier characters?

## Claim boundary

Yes, it decomposes canonically by the four character projectors of the order-four response operator. Xi-divisibility holds exactly componentwise, and orthogonal character sectors cannot cancel one another. Reality pairs the \(i\) and \(-i\) sectors but does not erase them on the parity-complete carrier.

## Character projectors

Let

$$
\mu_4=\{1,-1,i,-i\}.
$$

For \(\lambda\in\mu_4\), define

$$
P_\lambda
=\frac14\sum_{j=0}^3\lambda^{-j}T^j.
$$

Since \(T^4=I\), these satisfy

$$
P_\lambda^2=P_\lambda,
\qquad
P_\lambda P_\mu=0\quad(\lambda\ne\mu),
$$

$$
\sum_{\lambda\in\mu_4}P_\lambda=I,
\qquad
TP_\lambda=\lambda P_\lambda.
$$

Because \(T\) is unitary, the projectors are orthogonal on the response Hilbert rung.

## Defect decomposition

For

$$
D=e_+-Te_-,
$$

define

$$
D_\lambda=P_\lambda D.
$$

Then

$$
D=\sum_{\lambda\in\mu_4}D_\lambda,
$$

and explicitly

$$
\boxed{
D_\lambda
=P_\lambda e_+-\lambda P_\lambda e_-.
}
$$

Thus each component compares outgoing and incoming traces in one Fourier character:

$$
P_\lambda e_+
\mathrel{?}
\lambda P_\lambda e_-.
$$

## Xi quotient

The projectors are constant continuous operators, so they preserve the Xi ideal:

$$
P_\lambda\bigl(\tau\mathcal O(H)\bigr)
\subseteq\tau\mathcal O(H).
$$

Therefore

$$
[D]=0
\quad\Longleftrightarrow\quad
[D_\lambda]=0
\text{ for every }\lambda,
$$

or equivalently

$$
D_\lambda=\tau h_\lambda
$$

for four holomorphic character-valued quotient sections.

The quotient splits:

$$
\frac{\mathcal O(H)}{\tau\mathcal O(H)}
\cong
\bigoplus_{\lambda\in\mu_4}
\frac{\mathcal O(H_\lambda)}
{\tau\mathcal O(H_\lambda)}.
$$

## No cross-character cancellation

On the Hilbert rung,

$$
\|D\|^2
=\sum_\lambda\|D_\lambda\|^2.
$$

Hence a nonzero defect in one character sector cannot be cancelled by a defect in another. Likewise, prime or endpoint scalarization must not sum character sectors before the Xi-divisibility test.

## Reality

For the declared Real structure, complex conjugation exchanges

$$
H_i\longleftrightarrow H_{-i}
$$

and preserves \(H_{\pm1}\). Thus a real Evans family satisfies a conjugacy relation between \(D_i\) and \(D_{-i}\). One may test one of the pair and its Real conjugate, but neither sector vanishes merely from reality.

On the old even Sonin carrier, only \(H_{\pm1}\) survive. On the parity-complete oriented carrier, all four sectors must be retained.

## Explicit projector test

For any shell and jet, compute

$$
D_\lambda^{(j)}(z_0)
=
\frac14\sum_{r=0}^3
\lambda^{-r}T^r
\partial_z^jD(z_0).
$$

One nonzero component rejects Evans membership. Conversely, vanishing through the multiplicity in every sector is equivalent to the original vector-valued jet family.

## Source-level interpretation

The even sectors test cosine/trivial-character response, while the odd sectors test sine/sign-character response. Through Mellin diagonalization their transport factors are the four parity/Tate branches already normalized. Thus the defect quotient now has a characterwise local-factor presentation with no phase ambiguity.

## Disposition

The final Xi obstruction is not one opaque vector. It is the direct sum of four canonical Fourier-character defect classes

$$
[D_\lambda]
=
[P_\lambda e_+-\lambda P_\lambda e_-].
$$

They are independently Xi-divisible and cannot cancel across characters. This provides the cheapest sectorwise falsification test once the authoritative Evans boundary pair is exposed.