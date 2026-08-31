# A local source boundary value exists, but full continuation authority does not

Earlier source work supplies the universal negative-imaginary energy
prescription.  For the triple-incidence parameter it induces

\[
p\mapsto p-i(\epsilon_1+\epsilon_2+3\epsilon_3),
\qquad \epsilon_i>0.
\]

Thus current mutable state contains a source-authorized **local boundary-value
germ** at \(p=0\). It does not yet contain a transported twisted thimble or a
global contour for the continued sheets.

The evidence now separates three statements:

1. the literal positive chain does not support the triple-incidence nearby line;
2. nonliteral branches require analytic continuation;
3. the local \(p-i0\) side is source-authorized, but its deck/Čech-compatible
   Picard--Lefschetz transport and physical covector have not been constructed.

The five-site deck audit is the strongest guardrail: only the source-positive
sheet is regular on the positive ray.  The other 31 continued sheets hit
uncancelled positive-real poles and explicitly require an independently
specified contour.  That audit explicitly does not choose such a contour and
therefore does not assign scalar periods.

So the valid implication is

\[
\text{local source boundary side}
\not\Rightarrow
\text{nonzero twisted physical period}.
\]

The triple-incidence nearby line remains without a physical period until the
positive Cayley--Menger germ is transported over a transverse \(p\)-disk, its
Picard--Lefschetz variation and \(\mu_2\) character are computed, and the
result passes deck and wall/Čech compatibility.

Artifact:

- `research/nima/checkers/check_cosmology_analytic_continuation_authority_gate.py`
- `research/nima/results/cosmology_analytic_continuation_authority_gate.json`
