# Porter Stemmer algorithm

- [C](VC)^{m}[V]

- condition part also may also contains : 
	- `*s` : stem ends with s
	- `*v*` : stem contains vowel
	- `*d` : stem ends with a double consonant
	- `*o` : stem ends with cvc, where the second c is not W, X, Y.

- step 1a : deals with plural and past participles
	- sses -> ss
	- ies -> i
	- ss -> ss
	- s -> 

- step 1b
	- (m>0) eed -> ee
	- (*v*)ed -> 
	- (*v*)ing -> 
	
- step 2
	- ~~ional~~ -> e
	- ~~al~~
	- ~~i~~
	- ~~li~~
	- ~~ation~~ -> e
	- ~~ion~~ -> e
	- ~~or~~ 
	- ~~ism~~ 
	- ~~ness~~ 
	- ~~iti~~ -> e

- step 3
	- ~~ate~~
	- ~~ative~~
	- ~~ize~~
	- ~~iti~~
	- ~~al~~
	- ~~ful~~
	- ~~ness~~

- step 4
	- ~~al~~
	- ~~ance~~
	- ~~ence~~
	- ~~er~~
	- ~~able~~
	- ~~ic~~
	- ~~ion~~
	- ~~ou~~
	- ~~ism~~
	- ~~iti~~
	- ~~ate~~
	- ~~ement~~
	- ~~ent~~
	- ~~ant~~
	- ~~ible~~

- step 5a
	- (m>1) e ->
	- (m=1 and not *o) e ->

- step 5b 
	- (m > 1 and *d and *L) -> single letter