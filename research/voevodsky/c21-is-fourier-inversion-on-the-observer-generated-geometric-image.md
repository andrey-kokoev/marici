# C21 is Fourier inversion on the observer-generated geometric image

## Question

Does the reverse presentation map from semilocal geometry to the source observer have an analytic realization?

## Claim boundary

Yes on the essential image of the integrated regular scaling representation. This does not define an inverse on arbitrary cutoff, prolate, or affiliated geometric operators.

Let

$$
U_S^{\mathrm{obs}}:\mathsf{Obs}_S\longrightarrow\mathsf{Geom}_S^{\mathrm{obs}}
$$

be the integrated representation corestricted to its essential image. Under Fourier transform on the abelian scaling group \(C_S\),

$$
\mathcal F_{C_S}U_S(h)\mathcal F_{C_S}^{-1}=M_{\widehat h}.
$$

For \(T\in\mathsf{Geom}_S^{\mathrm{obs}}\), let \(\sigma_T\) be its Fourier multiplier, defined by

$$
\mathcal F_{C_S}T\mathcal F_{C_S}^{-1}=M_{\sigma_T}.
$$

The reverse constructor is

$$
C_{21}(T)=\mathcal F_{C_S}^{-1}(\sigma_T).
$$

If \(T=U_S(h)\), then \(\sigma_T=\widehat h\), so

$$
C_{21}(U_S(h))=h.
$$

Conversely,

$$
U_S(C_{21}(T))=T
$$

for every \(T\) in the observer-generated essential image. Injectivity follows from

$$
U_S(h)=0
\Longrightarrow
\widehat h=0
\Longrightarrow
h=0.
$$

## Disposition

Both \(C_{12}\) and \(C_{21}\) have analytic realizations on the observer-generated source/geometric equivalence. The reverse map is Fourier inversion of the represented multiplier, not an assumed abstract chart inverse. Extension beyond the essential image is not claimed.