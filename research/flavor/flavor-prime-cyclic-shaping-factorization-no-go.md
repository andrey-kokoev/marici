# Prime-cyclic shaping forces factorized rotations

Work package: WP602  
Owner: marici.Figueiredo

## Generalized question

WP601 closes diagonal \(Z_5\) shaping for one pair of \(D_5\) doublets. The
mechanism is linear algebra over a finite field and extends to every prime
cyclic rotation group.

Let the common rotation charge be a nonzero vector
\(w=(w_1,w_2)\in\mathbb F_p^2\). Let a mixed monomial have nonzero exponent
charge \(e=(e_1,e_2)\). Its invariance means

\[
e\mathbin{\cdot}w=0.
\]

Because the orthogonal complement of a nonzero vector in
\(\mathbb F_p^2\) is one-dimensional, \(e\) is proportional to
\((w_2,-w_1)\).

## Exact tradeoff

Add a diagonal shaping charge \(q=(q_1,q_2)\). It forbids the mixed monomial
when \(e\mathbin{\cdot}q\ne0\). Using the proportionality above,

\[
e\mathbin{\cdot}q\ne0
\quad\Longleftrightarrow\quad
\det(w,q)\ne0.
\]

The determinant condition says exactly that \(w\) and \(q\) form a basis of
\(\mathbb F_p^2\). Their generated action therefore contains independent
rotations of the two multiplets.

Independent rotations restore componentwise generalized CP. If angular
extrema are indexed as \((m_1\pi/p,m_2\pi/p)\), compose bare CP with the
independent rotation powers \((m_1,m_2)\) modulo \(p\). This fixes both
components. Thus every diagonal shaping charge that removes an existing mixed
invariant also removes the intended common-CP obstruction.

The checker exhausts all nonzero two-component rotation charges, all invariant
mixed charge vectors and every shaping vector for primes
\(3,5,7,11,13\). It finds no violation. The finite census is a regression
witness; the one-dimensional-orthogonal-complement argument proves the stated
prime-order theorem.

## Disposition

The diagonal shaping branch is closed for two multiplets over prime cyclic
rotation groups. A viable source architecture must instead use an operation
that does not enlarge the admitted action to independent component rotations:

- a non-diagonal non-abelian product-selection rule;
- gauge or geometric locality with an explicit absence-of-contact theorem;
- collective breaking in which no single admitted coupling restores the
  forbidden operator or factorized rotations.

This result still supplies no physical instrument. Any successor must descend
to `physical16` and expose its protecting interaction through a calibrated
threshold record.

## Reproduction

Run:

    uv run --offline python research/flavor/checkers/wp602_prime_cyclic_shaping_factorization_no_go.py

The generated result is
research/flavor/results/wp602_prime_cyclic_shaping_factorization_no_go.json.
