# Gaussian dual injectivity on an exponential form space

## Question

Can Gaussian convolution remain injective on the larger dual forced by endpoint exponential control, rather than only on tempered distributions?

## Claim boundary

Injectivity is proved for the candidate weighted dual \(H_{-\beta}\). The actual Bargmann intertwiner, combined-form dual identification, and graph-orthogonality equation remain unverified.

## Candidate form dual

Let

\[
H_\beta=L^2(\mathbb R,e^{\beta|x|}dx).
\]

Under the unweighted pairing, its Hilbert dual is represented by

\[
H_{-\beta}=L^2(\mathbb R,e^{-\beta|x|}dx).
\]

Elements of \(H_{-\beta}\) can have exponential growth and need not be tempered. Fourier-multiplier injectivity on tempered distributions is therefore insufficient.

## Injectivity theorem

For \(t>0\), let

\[
G_t(x)=e^{-x^2/(4t)}.
\]

Convolution by \(G_t\) is injective on \(H_{-\beta}\).

Take \(f\in H_{-\beta}\) and define

\[
h(y)=f(y)e^{-y^2/(4t)}.
\]

Cauchy--Schwarz gives \(h\in L^1\), because

\[
\int e^{\beta|y|-y^2/(2t)}dy<\infty.
\]

The convolution identity is

\[
(G_t*f)(x)
=
e^{-x^2/(4t)}
\int h(y)e^{xy/(2t)}dy.
\]

The bilateral Laplace transform

\[
L_h(z)=\int h(y)e^{zy}dy
\]

is entire: Gaussian damping dominates every fixed exponential direction. If \(G_t*f=0\) on the real axis, then \(L_h\) vanishes on the real axis. The identity theorem gives \(L_h\equiv0\). On the imaginary axis, \(L_h\) is the Fourier transform of \(h\); Fourier uniqueness yields \(h=0\), hence \(f=0\).

This argument does not divide by the rapidly decaying Gaussian Fourier multiplier and therefore survives the larger exponential dual.

## Categorical consequence

Let \(T\) be the positive operator representing the combined graph inner product. If graph-orthogonality to all Gaussian translates can be written as

\[
(Tf)*\widetilde G_t=0
\]

and \(Tf\in H_{-\beta}\), injectivity implies \(Tf=0\). If \(T\) has zero kernel on the quotient domain, then \(f=0\). Thus coherent states are total in the graph topology, making their inclusion conservative for form positivity.

The required arrows are:

The first map is induced by the graph operator \(T\); the second is convolution by \(\widetilde G_t\):

\[
D(Q)
\longrightarrow
H_{-\beta}
\longrightarrow
\operatorname{Fun}(\mathbb R).
\]

Injectivity of the second arrow is now available. The first arrow and the identification of translate pairing with convolution remain source-dependent.

## Remaining typed gates

1. Construct the explicit Bargmann intertwiner for endpoint, gamma, and prime rows.
2. Identify the actual combined form dual as a subspace of \(H_{-\beta}\), with its pairing.
3. Prove \(Tf\in H_{-\beta}\) for every graph-domain element.
4. Derive graph orthogonality as the stated Gaussian convolution.
5. Control the completed labelled-prime row and differentiated tails.
6. Prove the substantive positive section.

## Disposition

The dual-injectivity objection is not intrinsic to exponential growth. A fixed Gaussian remains injective on the natural exponential Hilbert dual by an entire Laplace-transform argument. The topology bracket is now concentrated in the intertwining and dual-identification cells, not in Gaussian injectivity itself.

## Verification

- `research/voevodsky/gaussian-dual-injectivity-exponential-form-space-v1.json`
- `research/voevodsky/checkers/check_gaussian_dual_injectivity_exponential_form_space.py`
- `research/voevodsky/results/gaussian_dual_injectivity_exponential_form_space.json`
