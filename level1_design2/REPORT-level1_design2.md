# seq_detect_1011 Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![Screenshot (135)](https://user-images.githubusercontent.com/105343698/182013279-7290cf47-f277-44cc-b48b-d0404a071e4d.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes in 1-bit inputs and with time gap and detects 1011 pattern

The values are assigned to the input port using 
```
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
```

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1, f'Sequence 1011 is not detected due to error...'
```
## Test Scenario **(Important)**
- Test Inputs: 
```
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
```
- Expected Output: dut.seq_seen.value == 1 i.e EXPECT=1
- Observed Output in the DUT: DUT=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;              //here next_state should be SEQ_1
        else
          next_state = SEQ_10;   
```
For the seq_detect_1011 design, the ``next_state`` in ``SEQ_1`` should be ``SEQ_1`` instead of ``IDLE`` as in the design code.

## Test Scenario **(Important)**
- Test Inputs: 
```
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
```
- Expected Output: dut.seq_seen.value == 1 i.e EXPECT=1
- Observed Output in the DUT: DUT=0


## Design Bug
Based on the above test input and analysing the design, we see the following

```
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;            //hereee it should be seq10
      end
```
For the seq_detect_1011 design, the ``next_state`` in ``SEQ_101`` should be ``SEQ_10`` instead of ``IDLE`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![Screenshot (136)](https://user-images.githubusercontent.com/105343698/182013584-0f082a39-bf93-49d7-98de-09c3e542e86d.png)

The updated design is checked in as seq_detect_1011_fix.v

## Verification Strategy

The design should not recognize 1011011 pattern even if it has 1011 pattern in it.
All type of input patterns which contain 1011 sequence should pass. 
All of these tests should pass to verify that the code is working properly. 

## Is the verification complete ?

Yes,the verification is complete as there are no errors declared and it passes through all the tests.
