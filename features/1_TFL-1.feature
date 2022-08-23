@FIELD-593
Feature: BDD Explore for import test result

	#*Steps to reproduce:*
	#
	## 
	## step 2
	#
	#*What you should see:*
	#
	#* expectation 1
	#
	#*What you actually see:*
	#
	#* observation 1
	@TEST_TFL-1 @TESTSET_TFL-2
	Scenario: Distract one number from the other
		Given have number 9
		When take away 4
		Then result is 5
