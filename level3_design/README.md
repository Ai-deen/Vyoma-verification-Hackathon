# PRESENT Encryptor Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![Screenshot (137)](https://user-images.githubusercontent.com/105343698/182112046-8dcb142f-1b6b-4023-8e16-9ea27a3c368d.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Verilog_Present module here) which takes in 16 bit hexadecimal input and a 4 bit key.

The values are assigned to the input port using 
```
    input = 0x23
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0x5
    dut.public_key.value = key
    yield Timer(1, units="ns")
```

The assert statement is used for comparing the encryptor's output to the expected value.

The following error is seen:
```
assert dut.encrypt_data.value == 0b1110, f'Test failed, Expected Encrypted Data is different from the Output data.Expected data = {0b1110},DUT = {int(dut.encrypt_data.value)}'
```
## Test Scenario-1 **(Important)**
- Test Inputs:
```
    input = 0x1
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")   
```
- Expected Output: Expected data = 4
- Observed Output in the DUT:DUT = 0

Output mismatches for the above inputs proving that there is a design bug

## Test Scenario-2 **(Important)**
- Test Inputs:
```
    input = 0x45
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")   
```
- Expected Output: Expected data = 7
- Observed Output in the DUT:DUT = 5

Output mismatches for the above inputs proving that there is a design bug

## Test Scenario-3 **(Important)**
- Test Inputs:
```
    input = 0x2
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns")  
```
- Expected Output: Expected data = 8
- Observed Output in the DUT:DUT = 0

Output mismatches for the above inputs proving that there is a design bug


## Test Scenario-4 **(Important)**
- Test Inputs:
```
    input = 0x41
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns") 
```
- Expected Output: Expected data = 7
- Observed Output in the DUT:DUT = 5

Output mismatches for the above inputs proving that there is a design bug

## Test Scenario-5 **(Important)**
- Test Inputs:
```
    input = 0xA
    dut.hexadecimal_input.value = input
    yield Timer(1, units="ns")
    key = 0xD
    dut.public_key.value = key
    yield Timer(1, units="ns") 
```
- Expected Output: Expected data = 14
- Observed Output in the DUT:DUT = 0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug - 1
According to the instructions,a Bug has been inserted in the design

```
    always @(*)
    begin
      xor_public[3]<=endata[3] & publ_key[3];           // XOR operation of encrypted data and public key
      xor_public[2]<=endata[2] & publ_key[2];           
      xor_public[1]<=endata[1] & publ_key[1];
      xor_public[0]<=endata[0] & publ_key[0];
    
   
      xor_private[3]<=xor_public[3] & prvi_key[3];     // XOR operation of data and private key
      xor_private[2]<=xor_public[2] & prvi_key[2];
      xor_private[1]<=xor_public[1] & prvi_key[1];
      xor_private[0]<=xor_public[0] & prvi_key[0]; 
```
The XOR symbol(^) has been replaced with AND symbol(&) and so the design is made buggy.

## Design Bug - 2
According to the instructions,a Bug has been inserted in the design

```
      privatekey_out[3] <= private_key[3]&grey_out[3];              // XOR operation with private key
      privatekey_out[2] <= private_key[2]&grey_out[2];
      privatekey_out[1] <= private_key[1]&grey_out[1];
      privatekey_out[0] <= private_key[0]&grey_out[0];

      encrypt_out[3] <= privatekey_out[3]&publ_key[3];              // XOR operation with public key
      encrypt_out[2] <= privatekey_out[2]&publ_key[2];
      encrypt_out[1] <= privatekey_out[1]&publ_key[1];
      encrypt_out[0] <= privatekey_out[0]&publ_key[0];  
```
The XOR symbol(^) has been replaced with AND symbol(&) and so the design is made buggy.


## Design Test
Updating the design and re-running the test makes the tests fail.

![Screenshot (138)](https://user-images.githubusercontent.com/105343698/182117016-166314a3-a385-4a53-8cde-76390c9e8783.png)

The updated design is checked in as encryp_decryp_buggy.v

## Verification Strategy

The buggy design should fail all the test cases which passed through the original design without any problem.

## Is the verification complete ?

Yes,the verification is complete as there as the buggy design failed all the tests.
