# Exact Gaussian criterion for safe early pushforward

After one global Gaussian step, write the covariance as

\[
V'=
\begin{pmatrix}
A'&C'\\
C'^T&B'
\end{pmatrix}.
\]

Early internal pushforward followed by a reset to (B_0) replaces this by

\[
V'_{\rm reset}=A'\oplus B_0.
\]

For a second Gaussian interaction whose observed output row has blocks ((X,Y)), the difference between retained-memory and reset observed covariances is

\[
\Delta A_2
=
Y(B'-B_0)Y^T
+XC'Y^T
+YC'^TX^T.
\]

Consequently

\[
\boxed{
\Delta A_2=0\text{ for every second Gaussian interaction}
\Longleftrightarrow
B'=B_0\text{ and }C'=0.
}
\]

Sufficiency is immediate.  Necessity follows by first choosing (X=0) and varying (Y), which forces (B'=B_0), then varying (X,Y), which forces (C'=0) by polarization.

For Gaussian states, (C'=0) is exactly factorization of the observed and internal characteristic functions.  The additional condition (B'=B_0) says the internal factor is the same reset state used by the reduced channel.  This is the precise Markov/product stratum on which early Cut pushforward commutes with later temporal composition.
