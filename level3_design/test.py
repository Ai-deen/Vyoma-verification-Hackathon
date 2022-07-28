# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge,  FallingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk_i))

    dut.data_i.value = 0x456474456747FFA21234
    yield Timer(1, units="ns")
    dut.key_load.value = 1
    yield Timer(1, units="ns")
    dut.data_i.value = 0x1234123412341234 
    yield Timer(1, units="ns")
    dut.key_load.value = 0 
    yield Timer(1, units="ns")
    dut.data_load.value = 1
    yield Timer(1, units="ns")
    dut.data_load.value = 0
    yield Timer(1, units="ns")

    #330 data_i = 80'hFFFFFFFF_FFFFFFFF_FFFF ; key_load = 1; // Key
    #10  data_i = 64'h00000000_00000000      ; key_load = 0; data_load = 1; // Plaintext
    #10  data_load = 0;
    #330 data_i = 80'h00000000_00000000_0000 ; key_load = 1; // Key
    #10  data_i = 64'hFFFFFFFF_FFFFFFFF      ; key_load = 0; data_load = 1; // Plaintext
    #10  data_load = 0;
    #330 data_i = 80'hFFFFFFFF_FFFFFFFF_FFFF ; key_load = 1; // Key
    #10  data_i = 64'hFFFFFFFF_FFFFFFFF      ; key_load = 0; data_load = 1; // Plaintext
    #10  data_load = 0;
    dut_output = dut.data_o.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
