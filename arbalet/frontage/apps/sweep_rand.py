#!/usr/bin/env python


from ._generator import gen_sweep_rand
from .colors import Colors
from json import loads


class SweepRand(Colors):

    def __init__(self):
        Colors.__init__(self, gen_sweep_rand)
        self.PARAMS_LIST['uapp'] = ['african', 'gender', 'teddy', 'warm']

    def handle_message(self, data, path=None): # noqa
        if not self.LOCK_WS.acquire_write(2):
            print('Wait for RWLock for too long in WS...Ignoring data')
            return
        if data is not None:
            params = loads(data)
            if params['uapp'] in self.PARAMS_LIST['uapp']:
                self.process_params(params)
                self.create_generator()
        self.LOCK_WS.release()