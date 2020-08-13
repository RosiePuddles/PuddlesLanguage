[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-water.svg)](https://forthebadge.com)  

[![GitHub version](https://badge.fury.io/gh/RosiePuddles%2FPuddlesLanguage.svg)](https://badge.fury.io/gh/RosiePuddles%2FPuddlesLanguage)  
# PuddlesLanguage!  
  
I, for some still unknown reason to me, decided to write my own coding language over the end of lockdown and this is what came out of it. It's still being worked on  
> **Please note!!** > It doesn't work very well but, I'm still working on it to improve it  
# Contents  
- [Documentation](#Documentation)  
   - [Variables](#Variables) 
   - [sfloat and dfloat rules](#sfloat-and-dfloat-rules)
# Documentation  
[(Back to top)](#Contents)  
### Variables  
> Currently there is only a 'var' variable for all types of variables. Others are being added  
  
#### Assignment
To assign a variable, use the general form below

```
<varibale type> <variable name> :: <value> [; <extra information]
```
The <code>&lt;extra information&gt;</code> is only required for <code>sfloat</code> and <code>dfloat</code>
#### int
An integer variable. If the user attempts to assign a <code>float</code> to an <code>int</code> variable, it will return an error, but assign the rounded <code>float</code> to the <code>int</code> variable  
<details>  
  <summary>Example</summary> 
  
   #### Integer assignment to an <code>int</code> variable 
 ```
int example_variable :: 5
log example_variable
```
 ```
5
```
---
   #### Float assignment to an <code>int</code> variable 
 ```
int example_variable :: 9.37
log example_variable
```
 ```
9
```
 </details>  
  
#### float
A float variable. If the user assigns an <code>int</code> to a <code>float</code> variable, it will be changed into a float with one decimal place
<details>  
  <summary>Example</summary> 
  
   #### Float assignment to an <code>float</code> variable 
 ```
int example_variable :: 3.14159
log example_variable
```
 ```
3.14159
```
---
   #### Integer assignment to an <code>float</code> variable 
 ```
int example_variable :: 7
log example_variable
```
 ```
7.0
```
 </details>  

#### sfloat
A float variable with a set number of significant figures. The number of significant figures is alterable. This will impact the number of significant figures returned from any numerical operation
#### dfloat  
#### bool  
#### string  
#### char

### sfloat and dfloat rules
The code assumes that, for any sfloat or dfloat, it can be written as the sfloat value &pm;5&times;10<sup>n</sup> where n is an integer. This value is the uncertainty.
#### Adding two or more sfloats or dfloats
When adding the special floats, the values of the special floats are added together and returned as a float value. If the user...

[![forthebadge](https://forthebadge.com/images/badges/cc-0.svg)](https://forthebadge.com)