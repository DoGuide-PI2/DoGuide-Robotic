from queue import Queue
from socket import ALG_SET_AEAD_ASSOCLEN
from exchange import Exchange

defaults = {
    'queue': {
        'queue': {
            'passive': False,
            'durable': True,
            'exclusive': False,
            'autoDelete': False,
            'nowait': False
        },
        'consumer': {
            'noLocal': False,
            'noAck': False,
            'exclusive': False,
            'nowait': False
        }
    },
    'exchange': {
        'exchange': {
            'passive': False,
            'durable': True,
            'autoDelete': True,
            'internal': False,
            'nowait': False
        },
        'queue': {
            'passive': False,
            'durable': True,
            'exclusive': False,
            'autoDelete': True,
            'nowait': False
        },
        'consumer': {
            'noLocal': False,
            'noAck': False,
            'exclusive': False,
            'nowait': False
        }
    },
    'rpc': {
        'queue': {
            'passive': False,
            'durable': True,
            'exclusive': False,
            'autoDelete': True,
            'nowait': False
        },
        'consumer': {
            'noLocal': False,
            'noAck': False,
            'exclusive': False,
            'nowait': False
        }
    }
}

def queue(name, server):
    conf = defaults['queue']
    conf['server'] = server

    return Queue(name, conf)


def exchange(name, server):
    conf = defaults['exchange']
    conf['server'] = server

    return Exchange(name, conf)