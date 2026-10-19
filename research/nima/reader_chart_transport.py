"""Complete reader-field chart coordinates with explicit source contexts.

No scalar averaging, new native operation, or identification of independent
reader assignments with one coherent native history is performed.
"""
from copy import deepcopy
from fractions import Fraction as F
from anchored_contact_comparisons import R,restore,binding_digest


def mix(matrix,rows):
    assert len(matrix)==8 and len(rows)==8 and all(len(r)==36 for r in rows)
    return [[sum((R(F(a))*rows[k][j] for k,a in enumerate(row) if F(a)),R())
             for j in range(36)] for row in matrix]


def validate(packet,contexts,reader_rows,native_chart,transitions):
    assert packet['schema']=='marici.nima.contextual-reader-chart.v1'
    assert packet['contexts']==contexts and packet['contextDigest']==binding_digest(contexts)
    assert packet['readerRows']==reader_rows and sorted(reader_rows)==list(range(4))
    assert packet['nativeChart']==native_chart
    assert (native_chart,packet['chart']) in transitions
    raw=packet['values'];assert len(raw)==8 and all(len(row)==36 for row in raw)
    rows=[[restore(x) for x in row] for row in raw]
    source=mix(transitions[native_chart,packet['chart']],rows)
    assert all(x==0 for row in source[4:] for x in row),'outside the four-reader coarse image'
    return source


def encode(fields,contexts,reader_rows,native_chart,chart,transitions):
    assert len(fields)==4 and all(len(row)==36 for row in fields)
    assert sorted(reader_rows)==list(range(4))
    source=[[R() for _ in range(36)] for _ in range(8)]
    for field,row in zip(fields,reader_rows):source[row]=list(field)
    values=mix(transitions[chart,native_chart],source)
    packet={'schema':'marici.nima.contextual-reader-chart.v1','contexts':deepcopy(contexts),
            'contextDigest':binding_digest(contexts),'readerRows':list(reader_rows),
            'nativeChart':native_chart,'chart':chart,
            'values':[[x.record() for x in row] for row in values]}
    validate(packet,contexts,reader_rows,native_chart,transitions)
    return packet


def decode(packet,contexts,reader_rows,native_chart,transitions):
    source=validate(packet,contexts,reader_rows,native_chart,transitions)
    return [source[row] for row in reader_rows]


def transition(packet,target,contexts,reader_rows,native_chart,transitions):
    validate(packet,contexts,reader_rows,native_chart,transitions)
    assert (target,packet['chart']) in transitions
    rows=[[restore(x) for x in row] for row in packet['values']]
    out=deepcopy(packet);out['chart']=target
    out['values']=[[x.record() for x in row] for row in mix(transitions[target,packet['chart']],rows)]
    validate(out,contexts,reader_rows,native_chart,transitions)
    return out
