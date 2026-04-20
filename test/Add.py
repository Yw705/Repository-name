# top = top

import cocotb
from spade import SpadeExt
from cocotb.triggers import Timer

@cocotb.test
async def test_2(dut):
    s = SpadeExt(dut)

    s.i.a = "1"
    s.i.b = "1"
    await Timer(10, units="ns")
    s.o.assert_eq("2")

@cocotb.test
async def test_4(dut):
    a = SpadeExt(dut)

    a.i.a = "2"
    a.i.b = "2"
    await Timer(10, units="ns")
    a.o.assert_eq("4")    