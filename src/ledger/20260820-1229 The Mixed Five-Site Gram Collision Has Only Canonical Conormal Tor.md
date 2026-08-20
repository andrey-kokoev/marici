# Entry 1229 — The Mixed Five-Site Gram Collision Has Only Canonical Conormal Tor

## Integral weighted model

Analyze

\[
F_i=F_j,
\qquad
\det H=0
\]

without dividing by $\det H$. Introduce the forced Gram Kummer coordinate and finite roots

\[
\det H=\lambda^2,
\qquad
Y_k=\lambda y_k,
\qquad
Y_k^2=F_k.
\]

At a generic pair collision with $Y_i+Y_j$ a unit, define

\[
\varepsilon
=
Y_i-Y_j
=
\frac{F_i-F_j}{Y_i+Y_j}.
\]

## Strict-transform walls

The two colliding marked walls have strict transforms

\[
q_+=\lambda X+\varepsilon,
\qquad
q_-=\lambda X-\varepsilon.
\]

They generate the ideal

\[
\boxed{(q_+,q_-)=(\varepsilon,\lambda X)}.
\]

Their Jacobian in $(\lambda,\varepsilon)$ is

\[
-2X.
\]

Therefore the collision is transverse for generic $X\neq0$.

## Deeper signed-energy restriction

On $X=0$, the separation symbol $\lambda X$ vanishes. Derived restriction of the two-term Koszul complex then produces exactly the canonical rank-one conormal Tor associated with the already declared signed-energy embedding.

There is no additional kernel or coefficient class beyond

\[
\text{Gram nearby cycle}
\otimes^{L}
\text{marked incidence}
\otimes^{L}
\text{signed-energy conormal layer}.
\]

## Gram deck action

The Gram involution acts by

\[
(\lambda,Y_i,Y_j)
\longmapsto
(-\lambda,-Y_i,-Y_j).
\]

Hence

\[
q_\pm\longmapsto-q_\pm.
\]

The marked divisors and their logarithmic differentials are fixed; the factor $-1$ is a unit. The external Gram Kummer character remains a separate coefficient factor.

Thus

\[
\boxed{
\text{mixed Gram/pair collision}
=
\text{existing weighted Gram, incidence, and conormal calculus}.
}
\]

No coefficient excess and no new carrier datum occur in this local model.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_mixed_gram_pair_collision.rs`
- `research/benincasa/results/five-site-mixed-gram-pair-collision.json`

## Next falsifier

Assemble Entries 1226–1229 over all ten labelled edge pairs and their cyclic occurrence multiplicities. Verify compatibility on triple overlaps $F_i=F_j=F_k$ and compute the resulting higher Čech differential. A surviving class must be classified as a Kummer-character coefficient extension; failure of the already frozen intersection maps would be required for a carrier-level obstruction.
