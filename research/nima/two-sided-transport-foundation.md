# Two-sided transport before port operators

## 1. Primitive data and licensed motion

Let A,B be types and F : A -> B -> U a family of types of incidences. A term of F(a,b) is an incidence witness, not automatically an identification or a transport operator.

Given paths p : a=a' and q : b=b', define

L_p^b := transport (lambda x. F(x,b)) p : F(a,b) -> F(a',b),
R_q^a := transport (lambda y. F(a,y)) q : F(a,b) -> F(a,b').

Transport along a path is an equivalence, with inverse transport along its inverse path. Noninvertible directed operations require additional data; they cannot silently be treated as these transports.

## 2. The fundamental square

For z : F(a,b), define the comparison type

Square_F(p,q,z) :=
  (R_q^{a'}(L_p^b(z)) = L_p^{b'}(R_q^a(z))).

There is a canonical term beta_F(p,q,z) of this type. Proof: identity elimination on p and then q reduces the statement to z=z, inhabited by refl_z. This is a written HoTT argument, not a machine-checked certificate in this packet. At arbitrary paths the equality is propositional, not generally judgmental. At two reflexivity paths the chosen witness computes to reflexivity.

Function extensionality packages the pointwise beta into equality of the two composite functions. No univalence axiom is needed for the basic pointwise construction. Univalence matters when a licensed equivalence is to be represented as an identity of types.

## 3. The proposed diagonal formula

For A=B and D(x):=F(x,x), a path p:a=b gives

transport_D(p) : F(a,a) -> F(b,b).

There are canonical pointwise comparisons

transport_D(p)(z) = R_p^b(L_p^a(z)),
transport_D(p)(z) = L_p^b(R_p^a(z)).

Both follow by path induction on p. Thus the notation for the licensing datum should be p:a=b followed by transport_D(p), rather than writing an arbitrary incidence F(a,b) as if it were a function.

## 4. Where nontriviality can actually live

Canonical interchange does not generate an obstruction: for a genuine dependent family, beta already exists. Nontrivial transport around loops (monodromy) is compatible with this coherent square. It must not be confused with a failure of commutation.

If another comparison eta(p,q,z) is supplied, its discrepancy relative to beta is the loop

eta(p,q,z) concatenated with inverse(beta(p,q,z))

at the left-hand composite output. Whether that loop is null is a higher identity question. Such a discrepancy needs the additional eta; it is not forced by regrouping. Moreover a candidate eta required to agree with refl on reflexivity and be uniformly dependent on p,q faces path-induction constraints. A nontrivial filler at one fixed square is not automatically a coherent global alternative.

If F takes values in sets, identity types inside each fibre are propositions, so any two pointwise fillers coincide. To retain distinct fillers one must allow higher fibres, such as groupoids. If the motions are independently supplied directed maps rather than path transports of one F, existence of an interchange filler becomes an additional axiom or proof obligation.

## 5. Concrete bounded semantic illustrations

The checker supplies two separate models, not a purported full implementation of HoTT:

1. Base group C2 in each coordinate and fibre set C2 x C2, with left/right flips of the respective coordinates. These give nontrivial monodromy yet commute exactly. The diagonal action flips both coordinates. This is a finite action model of a set-valued family over the classifying groupoids; it is not a failure of coherence.
2. Fibre groupoid BC2. Natural automorphisms of its identity functor are the central elements of C2, giving two distinct choices of comparison at a fixed identity square. The identity is the canonical reflexive choice; the other is extra comparison data, not a canonical defect. This example illustrates higher fibre information, not an admissible globally normalized alternative transport rule.

## 6. Architecture consequence

The abstract port net remains an execution representation. Beneath it, specify incidence families, licensed motions, and typed route comparisons. A later interpretation must map port operations into those data and prove preservation; the existing net core does not yet provide such a semantics. In particular, irreversible payload quotienting is not justified merely by path transport.

The scalar-field conventions do not enter any of this construction.

Checker: `research/nima/checkers/check_two_sided_transport_models.py`.
Result: `research/nima/results/two-sided-transport-models.json`.
