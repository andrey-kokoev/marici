"""Paired SQLite control: explicit decline vs absence of an interest match."""
import sqlite3


def run():
    with sqlite3.connect(':memory:') as db:
        db.executescript('''
        CREATE TABLE customer(id TEXT PRIMARY KEY, wants TEXT NOT NULL);
        CREATE TABLE product(id INTEGER PRIMARY KEY, category TEXT NOT NULL);
        CREATE TABLE decline(c TEXT, p INTEGER, PRIMARY KEY(c,p));
        CREATE VIEW pair_view AS SELECT customer.id AS c, product.id AS p,
            wants=category AS interest,
            EXISTS(SELECT 1 FROM decline d WHERE d.c=customer.id AND d.p=product.id) AS declined
            FROM customer CROSS JOIN product;
        CREATE VIEW unknown_preference AS SELECT c,p FROM pair_view WHERE interest=0 AND declined=0;
        ''')
        db.executemany('INSERT INTO customer VALUES (?,?)',zip(('Ada','Ben','Cy'),'TCT'))
        db.executemany('INSERT INTO product VALUES (?,?)',enumerate('TTCCKKJTTT',1))
        def rows(q):return tuple(db.execute(q))
        positive='SELECT c,p FROM pair_view WHERE interest ORDER BY c,p';outside=positive.replace('WHERE interest','WHERE interest=0');original=rows(positive),rows(outside)
        for explicit in (False,True):
            if explicit:db.execute("INSERT INTO decline VALUES ('Ada',7)")
            assert (rows(positive),rows(outside))==original
            def lookups():return (rows("SELECT p FROM decline WHERE c='Ada' ORDER BY p"),rows('SELECT c FROM decline WHERE p=7 ORDER BY c'))
            before=lookups();n=rows('SELECT COUNT(*) FROM unknown_preference')[0][0];assert before==((((7,),),(('Ada',),)) if explicit else ((),()))
            assert (len(original[0]),len(original[1]),n)==(12,18,18-int(explicit))
            db.execute('CREATE INDEX reverse_decline ON decline(p,c)');assert before==lookups();db.execute('DROP INDEX reverse_decline')
            print('explicit decline:',explicit,'positive / outside / unknown:',12,18,n,'Ada -> products; P7 -> customers:',before)
if __name__=='__main__':run()
