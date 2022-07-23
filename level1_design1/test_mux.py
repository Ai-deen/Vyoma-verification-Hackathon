# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux_basic1(dut):
    """Test for mux12"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    A=1
    B=2
    inp_sel=13 

    dut.inp12.value=A
    dut.inp13.value=B
    dut.sel.value=inp_sel

    await Timer(2, units='ns')

    dut._log.info(f'A={A:03} B={B:03} SEL={inp_sel:05} EXPECT={B:03} DUT={int(dut.out.value):05}')

    assert dut.out.value == B, "Test failed, because selected input was inp13 and expected output was {B} but the output from DUT is {OUT} ".format(B=dut.inp13.value, OUT=dut.out.value)

@cocotb.test()
async def test_mux_basic2(dut):
    """Test for mux30"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    C=1
    inp_sel=30
    dut.inp30.value=C
    dut.sel.value=inp_sel

    await Timer(2, units='ns')

    dut._log.info(f'C={C:03} SEL={inp_sel:05} EXPECT={C:03} DUT={int(dut.out.value):05}')

    assert dut.out.value == C, "Test failed, because selected input was inp30 and expected output was {C} but the output from DUT is {OUT} ".format(C=dut.inp30.value, OUT=dut.out.value)


@cocotb.test()
async def test_mux(dut):
    """Test for all mux values """

    cocotb.log.info('##### CTB: Develop your test here ########')

    for i in range(31):
        inp_sel = i
        dut.sel.value=inp_sel
        
        A0 = random.randint(0, 3)
        A1 = random.randint(0, 3)
        A2 = random.randint(0, 3)
        A3 = random.randint(0, 3)
        A4 = random.randint(0, 3)
        A5 = random.randint(0, 3)
        A6 = random.randint(0, 3)
        A7 = random.randint(0, 3)
        A8 = random.randint(0, 3)
        A9 = random.randint(0, 3)
        A10 = random.randint(0, 3)
        A11 = random.randint(0, 3)
        A12 = random.randint(0, 3)
        A13 = random.randint(0, 3)
        A14 = random.randint(0, 3)
        A15 = random.randint(0, 3)
        A16 = random.randint(0, 3)
        A17 = random.randint(0, 3)
        A18 = random.randint(0, 3)
        A19 = random.randint(0, 3)
        A20 = random.randint(0, 3)
        A21 = random.randint(0, 3)
        A22 = random.randint(0, 3)
        A23 = random.randint(0, 3)
        A24 = random.randint(0, 3)
        A25 = random.randint(0, 3)
        A26 = random.randint(0, 3)
        A27 = random.randint(0, 3)
        A28 = random.randint(0, 3)
        A29 = random.randint(0, 3)
        A30 = random.randint(0, 3)
        
        dut.inp0.value = A0
        dut.inp1.value = A1
        dut.inp2.value = A2
        dut.inp3.value = A3
        dut.inp4.value = A4
        dut.inp5.value = A5
        dut.inp6.value = A6
        dut.inp7.value = A7
        dut.inp8.value = A8
        dut.inp9.value = A9
        dut.inp10.value = A10
        dut.inp11.value = A11
        dut.inp12.value = A12
        dut.inp13.value = A13
        dut.inp14.value = A14
        dut.inp15.value = A15
        dut.inp16.value = A16
        dut.inp17.value = A17
        dut.inp18.value = A18
        dut.inp19.value = A19
        dut.inp20.value = A20
        dut.inp21.value = A21
        dut.inp22.value = A22
        dut.inp23.value = A23
        dut.inp24.value = A24
        dut.inp25.value = A25
        dut.inp26.value = A26
        dut.inp27.value = A27
        dut.inp28.value = A28
        dut.inp29.value = A29
        dut.inp30.value = A30

        if inp_sel == 0 :
            await Timer(2, units='ns')
            dut._log.info(f'A0={A0:03} SEL={inp_sel:05} EXPECT={A0:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A0, "Test failed, because selected input was inp0 and expected output was {A0} but the output from DUT is {OUT} ".format(A0=dut.inp0.value, OUT=dut.out.value)
        elif inp_sel == 1 :
            await Timer(2, units='ns')
            dut._log.info(f'A1={A1:03} SEL={inp_sel:05} EXPECT={A1:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A1, "Test failed, because selected input was inp1 and expected output was {A1} but the output from DUT is {OUT} ".format(A1=dut.inp1.value, OUT=dut.out.value)
        elif inp_sel == 2 :
            await Timer(2, units='ns')
            dut._log.info(f'A2={A2:03} SEL={inp_sel:05} EXPECT={A2:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A2, "Test failed, because selected input was inp2 and expected output was {A2} but the output from DUT is {OUT} ".format(A2=dut.inp2.value, OUT=dut.out.value)
        elif inp_sel == 3 :
            await Timer(2, units='ns')
            dut._log.info(f'A3={A3:03} SEL={inp_sel:05} EXPECT={A3:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A3, "Test failed, because selected input was inp3 and expected output was {A3} but the output from DUT is {OUT} ".format(A3=dut.inp3.value, OUT=dut.out.value)
        elif inp_sel == 4 :
            await Timer(2, units='ns')
            dut._log.info(f'A4={A4:03} SEL={inp_sel:05} EXPECT={A4:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A4, "Test failed, because selected input was inp4 and expected output was {A4} but the output from DUT is {OUT} ".format(A4=dut.inp4.value, OUT=dut.out.value)
        elif inp_sel == 5 :
            await Timer(2, units='ns')
            dut._log.info(f'A5={A5:03} SEL={inp_sel:05} EXPECT={A5:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A5, "Test failed, because selected input was inp5 and expected output was {A5} but the output from DUT is {OUT} ".format(A5=dut.inp5.value, OUT=dut.out.value)
        elif inp_sel == 6 :
            await Timer(2, units='ns')
            dut._log.info(f'A6={A6:03} SEL={inp_sel:05} EXPECT={A6:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A6, "Test failed, because selected input was inp6 and expected output was {A6} but the output from DUT is {OUT} ".format(A6=dut.inp6.value, OUT=dut.out.value)
        elif inp_sel == 7 :
            await Timer(2, units='ns')
            dut._log.info(f'A7={A7:03} SEL={inp_sel:05} EXPECT={A7:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A7, "Test failed, because selected input was inp7 and expected output was {A7} but the output from DUT is {OUT} ".format(A7=dut.inp7.value, OUT=dut.out.value)
        elif inp_sel == 8 :
            await Timer(2, units='ns')
            dut._log.info(f'A8={A8:03} SEL={inp_sel:05} EXPECT={A8:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A8, "Test failed, because selected input was inp8 and expected output was {A8} but the output from DUT is {OUT} ".format(A8=dut.inp8.value, OUT=dut.out.value)
        elif inp_sel == 9 :
            await Timer(2, units='ns')
            dut._log.info(f'A9={A9:03} SEL={inp_sel:05} EXPECT={A9:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A9, "Test failed, because selected input was inp9 and expected output was {A9} but the output from DUT is {OUT} ".format(A9=dut.inp9.value, OUT=dut.out.value)
        elif inp_sel == 10 :
            await Timer(2, units='ns')
            dut._log.info(f'A10={A10:03} SEL={inp_sel:05} EXPECT={A10:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A10, "Test failed, because selected input was inp10 and expected output was {A10} but the output from DUT is {OUT} ".format(A10=dut.inp10.value, OUT=dut.out.value)
        elif inp_sel == 11 :
            await Timer(2, units='ns')
            dut._log.info(f'A11={A11:03} SEL={inp_sel:05} EXPECT={A11:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A11, "Test failed, because selected input was inp11 and expected output was {A11} but the output from DUT is {OUT} ".format(A11=dut.inp11.value, OUT=dut.out.value)
        elif inp_sel == 12 :
            await Timer(2, units='ns')
            dut._log.info(f'A12={A12:03} SEL={inp_sel:05} EXPECT={A12:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A12, "Test failed, because selected input was inp12 and expected output was {A12} but the output from DUT is {OUT} ".format(A12=dut.inp12.value, OUT=dut.out.value)
        elif inp_sel == 13 :
            await Timer(2, units='ns')
            dut._log.info(f'A13={A13:03} SEL={inp_sel:05} EXPECT={A13:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A13, "Test failed, because selected input was inp13 and expected output was {A13} but the output from DUT is {OUT} ".format(A13=dut.inp13.value, OUT=dut.out.value)
        elif inp_sel == 14 :
            await Timer(2, units='ns')
            dut._log.info(f'A14={A14:03} SEL={inp_sel:05} EXPECT={A14:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A14, "Test failed, because selected input was inp14 and expected output was {A14} but the output from DUT is {OUT} ".format(A14=dut.inp14.value, OUT=dut.out.value)
        elif inp_sel == 15 :
            await Timer(2, units='ns')
            dut._log.info(f'A15={A15:03} SEL={inp_sel:05} EXPECT={A15:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A15, "Test failed, because selected input was inp15 and expected output was {A15} but the output from DUT is {OUT} ".format(A15=dut.inp15.value, OUT=dut.out.value)
        elif inp_sel == 16 :
            await Timer(2, units='ns')
            dut._log.info(f'A16={A16:03} SEL={inp_sel:05} EXPECT={A16:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A16, "Test failed, because selected input was inp16 and expected output was {A16} but the output from DUT is {OUT} ".format(A16=dut.inp16.value, OUT=dut.out.value)
        elif inp_sel == 17 :
            await Timer(2, units='ns')
            dut._log.info(f'A17={A17:03} SEL={inp_sel:05} EXPECT={A17:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A17, "Test failed, because selected input was inp17 and expected output was {A17} but the output from DUT is {OUT} ".format(A17=dut.inp17.value, OUT=dut.out.value)
        elif inp_sel == 18 :
            await Timer(2, units='ns')
            dut._log.info(f'A18={A18:03} SEL={inp_sel:05} EXPECT={A18:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A18, "Test failed, because selected input was inp18 and expected output was {A18} but the output from DUT is {OUT} ".format(A18=dut.inp18.value, OUT=dut.out.value)
        elif inp_sel == 19 :
            await Timer(2, units='ns')
            dut._log.info(f'A19={A19:03} SEL={inp_sel:05} EXPECT={A19:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A19, "Test failed, because selected input was inp19 and expected output was {A19} but the output from DUT is {OUT} ".format(A19=dut.inp19.value, OUT=dut.out.value)
        elif inp_sel == 20 :
            await Timer(2, units='ns')
            dut._log.info(f'A20={A20:03} SEL={inp_sel:05} EXPECT={A20:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A20, "Test failed, because selected input was inp20 and expected output was {A20} but the output from DUT is {OUT} ".format(A20=dut.inp20.value, OUT=dut.out.value)
        elif inp_sel == 21 :
            await Timer(2, units='ns')
            dut._log.info(f'A21={A21:03} SEL={inp_sel:05} EXPECT={A21:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A21, "Test failed, because selected input was inp21 and expected output was {A21} but the output from DUT is {OUT} ".format(A21=dut.inp21.value, OUT=dut.out.value)
        elif inp_sel == 22 :
            await Timer(2, units='ns')
            dut._log.info(f'A22={A22:03} SEL={inp_sel:05} EXPECT={A22:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A22, "Test failed, because selected input was inp22 and expected output was {A22} but the output from DUT is {OUT} ".format(A22=dut.inp22.value, OUT=dut.out.value)
        elif inp_sel == 23 :
            await Timer(2, units='ns')
            dut._log.info(f'A23={A23:03} SEL={inp_sel:05} EXPECT={A23:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A23, "Test failed, because selected input was inp23 and expected output was {A23} but the output from DUT is {OUT} ".format(A23=dut.inp23.value, OUT=dut.out.value)
        elif inp_sel == 24 :
            await Timer(2, units='ns')
            dut._log.info(f'A24={A24:03} SEL={inp_sel:05} EXPECT={A24:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A24, "Test failed, because selected input was inp24 and expected output was {A24} but the output from DUT is {OUT} ".format(A24=dut.inp24.value, OUT=dut.out.value)
        elif inp_sel == 25 :
            await Timer(2, units='ns')
            dut._log.info(f'A25={A25:03} SEL={inp_sel:05} EXPECT={A25:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A25, "Test failed, because selected input was inp25 and expected output was {A25} but the output from DUT is {OUT} ".format(A25=dut.inp25.value, OUT=dut.out.value)
        elif inp_sel == 26 :
            await Timer(2, units='ns')
            dut._log.info(f'A26={A26:03} SEL={inp_sel:05} EXPECT={A26:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A26, "Test failed, because selected input was inp26 and expected output was {A26} but the output from DUT is {OUT} ".format(A26=dut.inp26.value, OUT=dut.out.value)
        elif inp_sel == 27 :
            await Timer(2, units='ns')
            dut._log.info(f'A27={A27:03} SEL={inp_sel:05} EXPECT={A27:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A27, "Test failed, because selected input was inp27 and expected output was {A27} but the output from DUT is {OUT} ".format(A27=dut.inp27.value, OUT=dut.out.value)
        elif inp_sel == 28 :
            await Timer(2, units='ns')
            dut._log.info(f'A28={A28:03} SEL={inp_sel:05} EXPECT={A28:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A28, "Test failed, because selected input was inp28 and expected output was {A28} but the output from DUT is {OUT} ".format(A28=dut.inp28.value, OUT=dut.out.value)
        elif inp_sel == 29 :
            await Timer(2, units='ns')
            dut._log.info(f'A29={A29:03} SEL={inp_sel:05} EXPECT={A29:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A29, "Test failed, because selected input was inp29 and expected output was {A29} but the output from DUT is {OUT} ".format(A29=dut.inp29.value, OUT=dut.out.value)
        elif inp_sel == 30 :
            await Timer(2, units='ns')
            dut._log.info(f'A30={A30:03} SEL={inp_sel:05} EXPECT={A30:03} DUT={int(dut.out.value):05}')
            assert dut.out.value == A30, "Test failed, because selected input was inp30 and expected output was {A30} but the output from DUT is {OUT} ".format(A30=dut.inp30.value, OUT=dut.out.value)


    
