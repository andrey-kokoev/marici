-- Apply after vendor_customer_proposal.sql. For a simple Ramsey graph,
-- select one proposal per unordered party pair within the graph instance.
CREATE VIEW proposal_edge_sign AS
SELECT id,
       CASE WHEN vendor_mode IS NULL OR customer_mode IS NULL THEN NULL
            WHEN vendor_mode = customer_mode THEN '+' ELSE '-' END AS edge_sign
FROM proposal_answers;
