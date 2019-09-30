```Welcome Screen
Insert card
Enter PIN
Validate PIN
IF PIN is valid
	Enter amount
	IF amount is valid [amount <= total limit && amount <= total available balance]
	Parse amount
	# Amount should be divisible of available notes
	# If amount is 1000 there should available two 500 notes
	# or single note of 1000
	IF Parse amount is done
		Deduct withdrawing amount from total balance
		Withdraw amount
		Withdraw receipt
	ELSE If amount parsing failed
		prompt for enter amount again.
```
