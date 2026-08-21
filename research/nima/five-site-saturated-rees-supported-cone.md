# The Saturated Rees Cone Is the Canonical 45-Divisor Principal-Parts Module

The deck-saturated first-Rees attachment is multiplication by reciprocal
marked equations. For one principal divisor \(D=(q=0)\), its sheaf model is

\[
0\longrightarrow\mathcal O
\longrightarrow\mathcal O(D)
\longrightarrow\mathcal O_D(D)
\longrightarrow0.
\]

Thus it is an isomorphism off \(D\), and its cone is the canonical rank-one
principal-parts/Gysin line on \(D\). No fitted supported summand is needed.

## Edge blocks

For edge \(i\), the collapse kernel carries \(\chi_i\), while the normal
coefficient \(1/y_i\) also carries \(\chi_i\). Their product is invariant:

\[
\chi_i\otimes\chi_i=\mathbf1.
\]

The five edge residues therefore contribute five trivial lines.

## Boundary-pair blocks

Each unordered boundary pair \(\{i,j\}\) has four translated marked
divisors. Its residue packet is the inflated regular representation

\[
\mathbf1\oplus\chi_i\oplus\chi_j\oplus\chi_i\chi_j.
\]

Summing the ten boundary pairs and five edge blocks gives

\[
\boxed{
15\,\mathbf1
+4\sum_i\chi_i
+\sum_{i<j}\chi_i\chi_j,
}
\]

of total rank

\[
15+5\cdot4+10=45.
\]

This is exactly the character representation of the 45 geometric marked
components on \(E_T=0\).

At intersections of these divisors, further derived structure is only the
exterior conormal algebra of the declared normal-crossing embedding. Hence
the saturated supported cone introduces

- no new carrier support;
- no new Kummer character;
- no excess beyond canonical principal parts and conormal Tor.

This closes the occurrence/Rees lane at total energy. The unresolved generic
problem is now genuinely the twisted de Rham cohomology of the deck-saturated
marked complement and its physical relative cycle, not an occurrence or
support defect.

Artifacts:

- `research/nima/check_five_site_saturated_rees_supported_cone.py`
- `research/nima/results/five-site-saturated-rees-supported-cone.json`
