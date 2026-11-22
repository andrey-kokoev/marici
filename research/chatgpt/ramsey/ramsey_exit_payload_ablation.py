"""Ablate exit-flag support upstream of actual retained payload composition. Native registry unchanged. Test source scope, and whether composition itself spends a reused operand."""
from ramsey_exit_three_successor_probes import exits,PACKETS,RetainedSuccessorLedger,D,json

def run():
    ledger=RetainedSuccessorLedger(PACKETS);primitive={p[0][2]:p for p in ledger.root.paths};cache={}
    def pool(labels):
        k=tuple(sorted(labels));
        if k not in cache:cache[k]=ledger.retain_path_payload(tuple(primitive[e] for e in k),[1]*len(k))
        return cache[k]
    records=[]
    for bind in exits():
        f,g=bind['typed_order'];blocks=bind['blocks'];active=set(blocks[f]+blocks[g]);full=active|set(blocks[9]);assert full==set(primitive);rows=[]
        for row in bind['rows']:
            a,b=row['arc'];s=a[1]+next(iter({'A','B'}-{a[1]}));tests=[]
            for policy in ('selected','edge_once','arrows'):
                for with9 in (False,True):
                    offered=full if with9 and policy!='selected' else active
                    # Branch after a: first offer; second offer on the s branch only.
                    left=pool([a]);right=pool(offered);two=ledger.compose_payloads(left,right);ws=lambda z:{tuple(e[2] for e in p) for p in z.paths};ab=(a,s) in ws(two);assert (a,b) in ws(two);rev=False;same_operand=None
                    if ab:
                        # Explicit adapter withdraws 14 after one use under edge_once.
                        next_offer=pool(offered-{s,s[::-1]}) if policy=='edge_once' else right
                        three=ledger.compose_payloads(two,next_offer);rev=(a,s,s[::-1]) in ws(three);parents,_=ledger.deconstruct_payload(three);assert parents[0] is two and parents[1] is next_offer;same_operand=right is next_offer
                    assert ab==(with9 and policy!='selected') and rev==(with9 and policy=='arrows');tests.append(dict(policy=policy,with9=with9,first_cross=ab,reverse=rev if ab else None,reused_operand=same_operand))
            rows.append(tests)
        records.append(dict(binding=bind['binding'],rows=rows))
    return records
if __name__=='__main__':
    out=run();print(out[0]['rows'][0]);(D/'ramsey_exit_payload_ablation.json').write_text(json.dumps(out)+'\n')
