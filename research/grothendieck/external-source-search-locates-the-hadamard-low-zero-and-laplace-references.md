# External source search locates the Hadamard, low-zero, and Laplace references

## Question

Which publication-level sources can anchor the remaining paired-Hadamard citation contract?

## Search authority

The operator explicitly authorized shell-based external search for this action. Crossref metadata was queried through its public API. NIST DLMF pages were attempted but returned HTTP 403 and were not treated as inspected evidence.

## Located sources

### Centered xi function and Hadamard material

Kevin Broughan, *Equivalents of the Riemann Hypothesis*, Cambridge University Press, 2017, DOI

`10.1017/9781108178266`.

Chapter 6 is titled “The Riemann Xi Function,” pages 37–61, DOI

`10.1017/9781108178266.006`.

Crossref verifies the book, chapter title, publisher, date, and page range. The chapter text was not available through the metadata endpoint, so the exact theorem or equation containing the paired product still needs inspection.

### Rigorous low-ordinate exclusion

Dave Platt and Tim Trudgian, “The Riemann hypothesis is true up to `3·10^12`,” *Bulletin of the London Mathematical Society* 53(3), 2021, pages 792–797, DOI

`10.1112/blms.12460`.

An open author manuscript was located as arXiv `2004.09765`. Its Theorem 1 states that RH is true up to height `3,000,175,332,800`, meaning that the lowest `12,363,153,437,138` nontrivial zeros have real part `1/2`. This directly and vastly exceeds the required exclusion `|Im rho|<=1/2`.

### Laplace transform uniqueness

David Vernon Widder, *The Laplace Transform*, Princeton Mathematical Series 6, Princeton University Press; electronic DOI

`10.1515/9781400876457`.

Crossref verifies author, title, publisher, and DOI. The exact uniqueness and interchange theorem numbers remain to be inspected in the book.

### Zero-count formula candidate

Dieter Wolke, “On the Explicit Formula of Riemann–von Mangoldt, II,” *Journal of the London Mathematical Society* 28(3), 1983, pages 406–416, DOI

`10.1112/jlms/s2-28.3.406`.

This is a publication-level zero-count reference candidate. The specific bound needed here is only `N(T)=O(T log T)`, but the paper text was not inspected.

## Evidence boundary

Metadata establishes bibliographic identity, not theorem content. The Broughan, Widder, and Wolke locators remain candidates until the relevant statements and hypotheses are read. Platt–Trudgian Theorem 1 was inspected in the open arXiv manuscript and now supplies the low-height verification.

No unreviewed RH proof or preprint was admitted. Crossref returned several such items; they were excluded.

## Acceptance test

A source-complete citation packet must add exact theorem, equation, or page locators showing:

- the even xi product or enough Hadamard data to derive it;
- the stated zero-count growth;
- verified RH through a height exceeding `1/2`;
- Laplace uniqueness and an interchange theorem with matching absolute-integrability hypotheses.

## Disposition

Use these four publications as the bounded bibliography shortlist. Obtain their text or operator-supplied excerpts before marking the analytic bridge source-complete.