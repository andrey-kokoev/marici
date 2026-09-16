# The finite metaplectic G4 sewing interface reduces to four character-phase comparisons

## Question

After constructing the order-four radial lift, what remains to build an intertwiner with the retained Fourier--Poisson sewing on a finite multiplicity-free packet?

## Claim boundary

Only four unit-modulus character comparisons remain. This exactly classifies finite unitary intertwiners and reduces source identification to phase normalization on the four eigendirections. It does not choose those phases or handle completed character multiplicities.

## Two order-four representations

Let \(W_{\rm FP}\) act on the finite retained Fourier packet \(X_{\rm FP}\), and let \(\widetilde W_u\) act on the finite metaplectic radial packet \(\widetilde X_{\rm rad}\). Both decompose multiplicity-freely as

$$
X_{\rm FP}=\bigoplus_{\lambda\in\mu_4}X_\lambda,
\qquad
\widetilde X_{\rm rad}=\bigoplus_{\lambda\in\mu_4}\widetilde X_\lambda,
$$

where

$$
\mu_4=\{1,-1,i,-i\}.
$$

Let \(P_\lambda\) and \(\widetilde P_\lambda\) be the canonical character projectors.

## Intertwiner classification

A map

$$
C:X_{\rm FP}\longrightarrow\widetilde X_{\rm rad}
$$

satisfies

$$
CW_{\rm FP}=\widetilde W_uC
$$

if and only if

$$
C P_\lambda
=
\widetilde P_\lambda C
$$

for every \(\lambda\). Since each character space is one-dimensional, choose normalized vectors \(e_\lambda\) and \(\widetilde e_\lambda\). Every intertwiner has the unique form

$$
C e_\lambda
=c_\lambda\widetilde e_\lambda.
$$

It is unitary exactly when

$$
|c_\lambda|=1
$$

for all four characters. Hence the finite unitary interface is a \(U(1)^4\)-torsor before source normalization.

## Source normalization tests

The external identification is fixed once four independent source comparisons determine these phases. The required tests can be taken as:

1. vacuum normalization in the \(\lambda=1\) sector;
2. endpoint orientation in the \(\lambda=-1\) sector;
3. one oriented support-to-character Fourier coefficient in the \(\lambda=i\) sector;
4. sharp/Real conjugacy, which then forces the \(\lambda=-i\) coefficient from the \(i\) coefficient.

With normalized Real bases, the last condition has the form

$$
c_{-i}=\overline{c_i}.
$$

Thus only three independent phases remain before applying the source tests, and the vacuum condition fixes one immediately.

## Completion boundary

If the completed carrier has multiplicity spaces \(M_\lambda\), scalar phases are replaced by unitary maps

$$
C_\lambda:M_\lambda\longrightarrow\widetilde M_\lambda.
$$

Matching spectra then no longer gives a finite phase problem. Prime/grade labels, cutoff naturality, and the response cocycle must identify these multiplicity maps.

## Disposition

On every finite multiplicity-free packet, the formerly impossible G4 sewing comparison is reduced to four character phases, with Real structure relating the two odd phases. The next executable source check is one normalized coefficient in each independent character sector; no arbitrary global intertwiner remains to be guessed.