-- SQLite, fresh database. Treat a proposal as one fixed set of terms.
PRAGMA foreign_keys = ON;
CREATE TABLE party (id TEXT PRIMARY KEY NOT NULL);
CREATE TABLE proposal (
    id INTEGER PRIMARY KEY,
    vendor TEXT NOT NULL REFERENCES party(id),
    customer TEXT NOT NULL REFERENCES party(id),
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_price_usd_cents INTEGER NOT NULL CHECK(unit_price_usd_cents >= 0),
    CHECK(vendor <> customer)
) STRICT;
CREATE TRIGGER fixed_terms BEFORE UPDATE ON proposal BEGIN
    SELECT RAISE(ABORT, 'changed terms require a new proposal');
END;
CREATE TABLE choice (
    proposal_id INTEGER NOT NULL REFERENCES proposal(id),
    source_side TEXT NOT NULL CHECK(source_side IN ('vendor','customer')),
    mode TEXT NOT NULL CHECK(mode IN ('+','-')),
    PRIMARY KEY(proposal_id,source_side)
) WITHOUT ROWID;
-- Domain of assertions; existence here is not evidence of assent or refusal.
CREATE VIEW rels AS
WITH side(s) AS (VALUES ('vendor'),('customer')), sign(m) AS (VALUES ('+'),('-'))
SELECT p.id AS proposal_id,s AS source_side,m AS mode,
       CASE s WHEN 'vendor' THEN vendor ELSE customer END AS source_party
FROM proposal p CROSS JOIN side CROSS JOIN sign;
CREATE VIEW proposal_answers AS
SELECT p.id, v.mode AS vendor_mode, c.mode AS customer_mode
FROM proposal p
LEFT JOIN choice v ON v.proposal_id=p.id AND v.source_side='vendor'
LEFT JOIN choice c ON c.proposal_id=p.id AND c.source_side='customer';
