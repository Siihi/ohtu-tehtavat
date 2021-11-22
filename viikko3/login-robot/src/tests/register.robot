*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command And Create User

*** Test Cases ***
Register With Valid Username And Password
	Input Credentials  test  testtest1
	Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
	Input Credentials  kalle  testtest1
	Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
	Input Credentials  aa  testtest1
	Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
	Input Credentials  test  test
	Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
	Input Credentials  test  testtesttest
	Output Should Contain  Password only has letters

*** Keywords ***
Input Register Command And Create User
	Create User  kalle  kalle123
	Input Register Command
