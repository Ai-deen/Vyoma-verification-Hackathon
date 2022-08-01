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

@cocotb.test()
def run_test_1(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    input = 0x1
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")

    cocotb.log.info(f'DUT INPUT={dut.hexadecimal_input.value}')
    cocotb.log.info(f'DUT KEY={dut.public_key.value}')
    cocotb.log.info(f'DUT ENCRYPT_DATA={dut.encrypt_data.value}')
    assert dut.encrypt_data.value == 0b0100, f'Test failed, Expected Encrypted Data is different from the Output data.Expected data = {0b0100},DUT = {dut.encrypt_data.value}'


@cocotb.test()
def run_test_2(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    input = 0x45
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")

    cocotb.log.info(f'DUT INPUT={dut.hexadecimal_input.value}')
    cocotb.log.info(f'DUT KEY={dut.public_key.value}')
    cocotb.log.info(f'DUT ENCRYPT_DATA={dut.encrypt_data.value}')
    assert dut.encrypt_data.value == 0b0111, f'Test failed, Expected Encrypted Data is different from the Output data.Expected data = {0b0111},DUT = {dut.encrypt_data.value}'


@cocotb.test()
def run_test_3(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    input = 0x2
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")

    cocotb.log.info(f'DUT INPUT={dut.hexadecimal_input.value}')
    cocotb.log.info(f'DUT KEY={dut.public_key.value}')
    cocotb.log.info(f'DUT ENCRYPT_DATA={dut.encrypt_data.value}')
    assert dut.encrypt_data.value == 0b1000, f'Test failed, Expected Encrypted Data is different from the Output data.Expected data = {0b1000},DUT = {dut.encrypt_data.value}'

@cocotb.test()
def run_test_4(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    input = 0x41
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")

    cocotb.log.info(f'DUT INPUT={dut.hexadecimal_input.value}')
    cocotb.log.info(f'DUT KEY={dut.public_key.value}')
    cocotb.log.info(f'DUT ENCRYPT_DATA={dut.encrypt_data.value}')
    assert dut.encrypt_data.value == 0b0111, f'Test failed, Expected Encrypted Data is different from the Output data.Expected data = {0b0111},DUT = {dut.encrypt_data.value}'


@cocotb.test()
def run_test_5(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    input = 0xA
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")

    cocotb.log.info(f'DUT INPUT={dut.hexadecimal_input.value}')
    cocotb.log.info(f'DUT KEY={dut.public_key.value}')
    cocotb.log.info(f'DUT ENCRYPT_DATA={dut.encrypt_data.value}')
    assert dut.encrypt_data.value == 0b1110, f'Test failed, Expected Encrypted Data is different from the Output data.Expected data = {0b1110},DUT = {dut.encrypt_data.value}'

    
