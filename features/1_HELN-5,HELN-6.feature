@HELN-8
Feature: Test Execution for Test Plan HELN-7

	@TEST_HELN-5
	Scenario: Add two positive numbers
		Given have number 3
		When add 2
		Then result 5
	@TEST_HELN-6
	Scenario: Add a number and zero
		Given any first number is 0
		When another number 6
		Then result 6
