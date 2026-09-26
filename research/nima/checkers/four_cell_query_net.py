"""Attributed linear query net: EB/FB -> two VALUEs; VALUE/READ -> ANSWER.
A query consumes its own value. Reuse requires an explicit new source/copy policy.
"""
from copy import deepcopy
from four_cell_port_net import Net, ARITY
ARITY.update({'VALUE': ('p',), 'READ': ('p','o'), 'ANSWER': ('p',)})

class QueryNet(Net):
    def enabled(self):
        self.validate()
        result=[]
        for n,(kind,_) in self.nodes.items():
            peer,port=self.wires[n,'p']
            other=self.nodes[peer][0]
            if port=='p' and ((kind=='EB' and other=='FB') or
                             (kind=='VALUE' and other=='READ')):
                result.append((n,peer))
        return result

    def step(self,pair):
        if pair not in self.enabled():
            raise ValueError('inactive or consumed pair')
        a,b=pair
        kind,x=self.nodes[a]
        _,y=self.nodes[b]
        if kind=='EB':
            if x['family']!=y['family'] or x['members'] & y['members'] or x['pole']+y['pole']!=0:
                raise ValueError('invalid cancellation pair')
            peers=[self.wires[a,'o'],self.wires[b,'o']]
            replacements=[('VALUE',deepcopy(x)),('VALUE',deepcopy(y))]
        else:
            if x['family']!=y[0]:
                raise ValueError('query family mismatch')
            peers=[self.wires[b,'o']]
            replacements=[('ANSWER',deepcopy(x))]
        if any(n in pair for n,_ in peers) or len(set(peers))!=len(peers):
            raise ValueError('invalid boundary')
        for n in pair:
            for p in ARITY[self.nodes[n][0]]:
                endpoint=(n,p)
                if endpoint in self.wires:
                    peer=self.wires.pop(endpoint)
                    del self.wires[peer]
            del self.nodes[n]
        for (kind,payload),peer in zip(replacements,peers):
            n=self.add(kind,payload)
            self.link((n,'p'),peer)
        self.validate()

    def meanings(self):
        """Live denotation of queued queries and completed answers, by named OUT."""
        self.validate()
        result={}
        for n,(kind,label) in self.nodes.items():
            if kind!='OUT':continue
            peer,port=self.wires[n,'p']
            agent,payload=self.nodes[peer]
            if agent=='READ':
                peer,port=self.wires[peer,'p']
                agent,payload=self.nodes[peer]
                if agent not in ('EB','FB','VALUE'):
                    raise ValueError('unsupported waiting query')
            elif agent!='ANSWER':
                raise ValueError('unsupported output')
            if label[0]!=payload['family'] or label in result:
                raise ValueError('ambiguous boundary')
            result[label]=(tuple(sorted(payload['members'])),payload['pole'],payload['value'])
        return result

    def completed(self):
        return sum(kind=='ANSWER' for kind,_ in self.nodes.values())

def construct_queries(records):
    net=QueryNet()
    for family in sorted({r['family'] for r in records.values()}):
        pair=[]
        for kind,suffix in (('EB','E_B'),('FB','F_B')):
            label=(family,kind)
            node=net.add(kind,records[family+'_'+suffix])
            query=net.add('READ',label)
            out=net.add('OUT',label)
            net.link((node,'o'),(query,'p'))
            net.link((query,'o'),(out,'p'))
            pair.append(node)
        net.link((pair[0],'p'),(pair[1],'p'))
    net.validate()
    return net
