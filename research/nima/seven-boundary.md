# Seven-point boundary support search

## Question

Does a locally admissible sparse support force an unwanted positive triangle monomial?

## Claim boundary

Search all supports of cardinality at most four among the 42 seven-point triangulations. This is not exhaustion of all 2^42 supports. Values are Boolean, so no coefficient-lifting conclusion is inferred.

For each support, the checker tests all 63 local rectangle cross-products. For a passing support it collects all triangle factors appearing in its positive monomials. Every such factor must be nonzero. It then checks whether any excluded triangulation uses only those factors. Absence of an extra triangulation gives a Boolean lift by setting exactly the collected factors to one.

The complete counts by support cardinality are: zero, 1 tested and 1 admitted; one, 42 and 42; two, 861 and 735; three, 11480 and 7112; four, 111930 and 42770. Every admitted support passes triangle closure. Thus 50660 admitted supports lift as Boolean points, out of 124314 supports tested.

## Disposition

No support-closure obstruction exists within the declared cardinality bound. Larger supports and arbitrary nonzero coefficients on these supports remain untested. Ideal equality remains a distinct result. Rather than treating continued cardinality sampling as a global argument, the next test should formulate which faces of the triangle exponent cone are induced by setting triangle coordinates zero; failure of that face criterion would locate a genuine boundary-lifting obstruction.
