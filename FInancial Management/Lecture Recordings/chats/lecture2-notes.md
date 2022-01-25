# Present value or Discounting techniques

- PV of single amount (lump sum)
	- PV = FV/(1+i)^n
	or
	- PV = FV * PVIF_(i%,n years)
	
-  PV  of annuity (deffered)
	- PV = A * [((1+i)^n-1) / i(1+i)^n]
	or
	- PV = A * PVIF_(i%, n years)
	
- PV of annuity (due)
	- PV = A * [((1+i)^n-1) / (i(1+i)^n)] * (1+i)
	or
	- PV = (A * PVIF_(i%, n years)) * (1+i)
	
- PV of perpetuity (Infinite period)
	- PV = A/i
	- amount of  annuity growing is same
	- not applicable if  we already know  the number of years

- PV of ferowing annuity
	- amount of annuity growing is not same
	- PV = A * (1+g) * [1-{(1+g)/(1+i)}^n]/(i-g)
	
- PV of uneven cash flows
	- PV = A_1/(1+i)^1 + A_2/(1+i)^2 + A_3/(1+i)^3 + ... + A_n/(1+i)^n
	
g:is growth rate