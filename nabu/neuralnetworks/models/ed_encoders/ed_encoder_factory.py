'''@file ed_encoder_factory.py
contains the EDEncoder factory'''

from . import listener, dummy_encoder, dblstm, dnn, listener_ps, \
bottleneck_encoder, bldnn, hotstart_encoder, stack_encoder

def factory(encoder):
    '''get an EDEncoder class

    Args:
        encoder: the encoder type

    Returns:
        an EDEncoder class'''

    if encoder == 'listener':
        return listener.Listener
    if encoder == 'listener_ps':
        return listener_ps.ListenerPS
    elif encoder == 'dummy_encoder':
        return dummy_encoder.DummyEncoder
    elif encoder == 'dblstm':
        return dblstm.DBLSTM
    elif encoder == 'dnn':
        return dnn.DNN
    elif encoder == 'bottleneck_encoder':
        return bottleneck_encoder.BottleneckEncoder
    elif encoder == 'bldnn':
        return bldnn.BLDNN
    elif encoder == 'hotstart_encoder':
        return hotstart_encoder.HotstartEncoder
    elif encoder == 'stack_encoder':
        return stack_encoder.StackEncoder
    else:
        raise Exception('undefined encoder type: %s' % encoder)
