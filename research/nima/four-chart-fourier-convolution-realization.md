# Four-chart Fourier/convolution realization of Catalan channel monomials

The previous scalar Mellin model could not identify channel rotation with physical Fourier transport because Fourier transform is not an automorphism of convolution multiplication. It exchanges two products:

\[
\mathcal F(f*g)=(\mathcal Ff)(\mathcal Fg),
\qquad
\mathcal F(fg)=(\mathcal Ff)*(\mathcal Fg)
\]

with the fixed normalization convention.

This supplies the four-chart realization directly. Define chart products

\[
\mu_0=*,\qquad
\mu_1=\cdot,\qquad
\mu_2=*,\qquad
\mu_3=\cdot.
\]

Choose one channel atom `a_d` for every polygon diagonal and define its chart transports recursively by

\[
a_{q d}^{(i+1)}=\mathcal F a_d^{(i)},
\]

where `q` rotates channel labels by a quarter polygon turn. For a triangulation `T`, set

\[
R_i(T)=\mu_i\bigl(a_d^{(i)}:d\in q^iT\bigr).
\]

Then the convolution theorem gives the exact intertwining squares

\[
\mathcal F R_i(T)=R_{i+1}(qT).
\]

After four steps,

\[
\mathcal F^4R_0(T)=R_0(q^4T)=R_0(T).
\]

Thus the total successor is semidirect: Fourier advances the analytic presentation while quarter rotation advances the channel labels. This is the same structural form as the eight-lattice relation

\[
q\,u=\rho(u)\,q.
\]

Rooted-subtree gluing remains multiplicative, but its analytical product is chart-typed rather than incorrectly frozen to convolution in all four phases.

A faithful concrete model can use tagged Schwartz atoms, retaining one channel coordinate per diagonal. Removing those tags requires a separate linear-independence theorem for the selected physical atoms; it is not needed for the typed intertwining law.

`check_four_chart_fourier_product_intertwiner.py` verifies all four squares and four-step closure on every triangulation at `n=4,8,12`, totaling 67,720 Fourier-step checks.
