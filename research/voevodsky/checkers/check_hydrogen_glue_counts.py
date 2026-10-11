"""Two explicitly conditional neutron-as-glue placements, with exact arrow costs.
An electron INTERFACE is supplied, not an electron's internal tetrahedral complex.
Glue is first tested as a typed identity factorization. Its failure to change
boundary semantics is a result, not an isotope or particle identification.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json

from check_proton_merkle_reassembly import verify as verify_focus, weight, times, plus, ZERO, ONE, cycle_list

BASE=Path(__file__).resolve().parents[1]
FOCUS=BASE/'results/proton_merkle_store.json'
CASES=('H1-boundary-prototype','H2-nuclear-glue','H2-interface-glue')

def digest(record): return sha256(b'marici.hydrogen-glue-counts.v1\0'+json.dumps(record,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def wire(source,target): return {'source':list(source),'target':list(target),'weight_real':'1','weight_imag_sqrt3':'0'}
def sorted_rows(rows): return sorted(rows,key=lambda r:(r['source'],r['target']))

def network(source,case,width=36):
    if case not in CASES: raise ValueError('unsupported case')
    labels=sorted({tuple(r['source'][1:]) for r in source if r['source'][0]=='raw'})
    if type(width) is not int or not 1<=width<=len(labels): raise ValueError('interface width')
    rows=deepcopy(source)
    if case=='H2-nuclear-glue':
        # Factor G as I_36 G while retaining every original G coefficient.
        for r in rows:
            if r['source'][0]=='local': r['target'][0]='nuclear-glue'
        rows += [wire(('nuclear-glue',)+p,('aligned',)+p) for p in labels]
    for p in labels[:width]:
        raw=('raw',)+p; electron=('electron-boundary',)+p
        if case=='H2-interface-glue':
            middle=('interface-glue',)+p
            rows += [wire(raw,middle),wire(middle,electron)]
        else: rows.append(wire(raw,electron))
        rows.append(wire(electron,raw))
    core=['raw','local']+(['nuclear-glue'] if case=='H2-nuclear-glue' else [])+['aligned','raw']
    attachment=['raw']+(['interface-glue'] if case=='H2-interface-glue' else [])+['electron-boundary','raw']
    return sorted_rows(rows),core,attachment

def path_matrix(rows,route):
    # Composition follows the named stage protocol, not arbitrary recurrent walks.
    by_pair=defaultdict(list)
    for r in rows: by_pair[r['source'][0],r['target'][0]].append(r)
    first=by_pair[route[0],route[1]]
    result={(tuple(r['target'][1:]),tuple(r['source'][1:])):weight(r) for r in first}
    for u,v in zip(route[1:],route[2:]):
        outgoing=defaultdict(list)
        for r in by_pair[u,v]: outgoing[tuple(r['source'][1:])].append((tuple(r['target'][1:]),weight(r)))
        next_result=defaultdict(lambda:ZERO)
        for (middle,initial),a in result.items():
            for final,b in outgoing[middle]: next_result[final,initial]=plus(next_result[final,initial],times(b,a))
        result={k:v for k,v in next_result.items() if v!=ZERO}
    return result

def positive_protocol_cover(rows,route):
    by_source=defaultdict(list)
    for i,r in enumerate(rows): by_source[tuple(r['source'])].append(i)
    used=set(); weights=[]
    def walk(start,current,step,value,edges):
        if step==len(route)-1:
            if current==start:
                if value[1]!=0 or value[0]<=0: raise ValueError('nonpositive closed protocol contribution')
                weights.append(value[0]); used.update(edges)
            return
        for i in by_source[current]:
            r=rows[i]
            if r['target'][0]==route[step+1]: walk(start,tuple(r['target']),step+1,times(weight(r),value),edges+[i])
    for start in sorted({tuple(r['source']) for r in rows if r['source'][0]==route[0]}): walk(start,start,0,ONE,[])
    return used,weights

def construct(focus):
    _,source=verify_focus(focus); objects={}; nets=[]
    def put(rec): key=digest(rec); objects[key]=rec; return key
    for case in CASES:
        rows,core,attachment=network(source,case)
        arrows=[put({'kind':'arrow',**r}) for r in rows]
        nets.append(put({'kind':'protocol-network','case':case,'interface_width':36,'arrows':arrows,
                         'core_protocol':core,'attachment_protocol':attachment}))
    root=put({'kind':'two-glue-hypotheses','focus':focus['root'],'networks':nets,
              'electron_interior':'not constructed; common additional cost E',
              'interface_contract':'36 separately typed channels; identity matching each way',
              'glue_contract':'typed identity factorization; not an independent neutral carrier'})
    return {'schema':'marici.hydrogen-glue-store.v1','focus':focus,'objects':objects,'root':root}

def verify(packet):
    if set(packet)!={'schema','focus','objects','root'} or packet['schema']!='marici.hydrogen-glue-store.v1': raise ValueError('schema')
    focus_report,source=verify_focus(packet['focus']); store=packet['objects']
    def get(ref):
        if ref not in store or digest(store[ref])!=ref: raise ValueError('missing object or hash mismatch')
        return store[ref]
    root=get(packet['root'])
    if root.get('kind')!='two-glue-hypotheses' or root.get('focus')!=focus_report['root'] or len(root['networks'])!=3: raise ValueError('focus/case binding')
    expected_contract={'kind':'two-glue-hypotheses','focus':focus_report['root'],'networks':root['networks'],
              'electron_interior':'not constructed; common additional cost E',
              'interface_contract':'36 separately typed channels; identity matching each way',
              'glue_contract':'typed identity factorization; not an independent neutral carrier'}
    if root!=expected_contract: raise ValueError('undeclared contract')
    target={(tuple(r['target'][1:]),tuple(r['source'][1:])):weight(r) for r in source if r['source'][0]=='aligned'}
    labels=sorted({i for i,j in target}); identity={(p,p):ONE for p in labels}; reports=[]
    for case,ref in zip(CASES,root['networks']):
        net=get(ref)
        if set(net)!={'kind','case','interface_width','arrows','core_protocol','attachment_protocol'} or net['kind']!='protocol-network' or net['case']!=case or net['interface_width']!=36: raise ValueError('network declaration')
        rows=[]
        for ref in net['arrows']:
            a=get(ref)
            if set(a)!={'kind','source','target','weight_real','weight_imag_sqrt3'} or a['kind']!='arrow': raise ValueError('arrow schema')
            rows.append({k:v for k,v in a.items() if k!='kind'})
        expected,core,attachment=network(source,case)
        if rows!=expected or net['core_protocol']!=core or net['attachment_protocol']!=attachment: raise ValueError('not the declared glue construction')
        keys=[(tuple(r['source']),tuple(r['target'])) for r in rows]
        if len(set(keys))!=len(keys): raise ValueError('duplicate endpoint occurrence')
        if path_matrix(rows,core)!=target or path_matrix(rows,attachment)!=identity: raise ValueError('boundary observable changed')
        core_used,core_weights=positive_protocol_cover(rows,core)
        interface_used,interface_weights=positive_protocol_cover(rows,attachment)
        if core_used|interface_used!=set(range(len(rows))) or sum(core_weights)!=1 or sum(interface_weights)!=36: raise ValueError('incomplete pruning cover')
        reports.append({'case':case,'known_arrow_count':len(rows),'complete_count':f'{len(rows)} + E',
                        'core_arrows':len(core_used),'attachment_arrows':len(interface_used),
                        'core_return':'N','attachment_return':'I_36','core_positive_cycles':len(core_weights),
                        'attachment_positive_cycles':len(interface_weights),
                        'protocol_scoped_fixed_weight_pruning_minimal':True})
    return reports

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def main():
    focus=json.loads(FOCUS.read_text(encoding='utf-8')); packet=construct(focus); reports=verify(packet)
    _,source=verify_focus(focus)
    checks={'H1_1908_plus_unknown_electron_interior':reports[0]['known_arrow_count']==1908,
            'nuclear_glue_1944_plus_same_unknown_interior':reports[1]['known_arrow_count']==1944,
            'interface_glue_1944_plus_same_unknown_interior':reports[2]['known_arrow_count']==1944,
            'both_placements_add_36_known_arrows':all(r['known_arrow_count']-reports[0]['known_arrow_count']==36 for r in reports[1:]),
            'all_three_have_same_boundary_returns':all((r['core_return'],r['attachment_return'])==('N','I_36') for r in reports),
            'each_declared_protocol_pair_is_pruning_minimal':all(r['protocol_scoped_fixed_weight_pruning_minimal'] for r in reports),
            'both_locations_are_distinct_typed_graphs':packet['objects'][packet['root']]['networks'][1]!=packet['objects'][packet['root']]['networks'][2]}
    widths=[]
    for width in (1,6,12,36):
        counts=[len(network(source,c,width)[0]) for c in CASES]
        widths.append({'interface_width':width,'counts_plus_E':counts})
    checks['counts_depend_on_declared_interface_width']=all(r['counts_plus_E']==[1836+2*r['interface_width'],1872+2*r['interface_width'],1836+3*r['interface_width']] for r in widths)
    # At width 36 the two increments agree; narrower interfaces separate them.
    checks['same_full_width_cost_does_not_identify_glue_location']=widths[0]['counts_plus_E'][1]!=widths[0]['counts_plus_E'][2]
    bad=deepcopy(packet); root=deepcopy(bad['objects'][bad['root']]); ref=root['networks'][1]; net=deepcopy(bad['objects'][ref]); net['arrows'].pop(); new=digest(net); bad['objects'][new]=net; root['networks'][1]=new; bad['root']=digest(root); bad['objects'][bad['root']]=root
    checks['rehashed_missing_glue_arrow_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); root=deepcopy(bad['objects'][bad['root']]); ref=root['networks'][2]; net=deepcopy(bad['objects'][ref]); net['core_protocol']=net['attachment_protocol']; new=digest(net); bad['objects'][new]=net; root['networks'][2]=new; bad['root']=digest(root); bad['objects'][bad['root']]=root
    checks['protocol_substitution_rejected']=rejected(lambda:verify(bad))
    checks['serialized_glue_packet_reverifies']=verify(json.loads(json.dumps(packet)))==reports
    result={'schema':'marici.hydrogen-glue-count-check.v1','passed':all(checks.values()),'checks':checks,'cases':reports,'width_controls':widths,
            'root':packet['root'],'focus_file_sha256':sha256(FOCUS.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'disposition':'Both identity-glue placements increase typed support without changing the declared observables. Neither establishes a distinct isotope. Electron interior E remains unconstructed; numbers are protocol costs, not atomic masses.'}
    out=BASE/'results'; (out/'hydrogen_glue_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (out/'hydrogen_glue_counts.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
