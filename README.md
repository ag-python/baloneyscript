# baloneyscript
An absurdly verbose script language.

This is primarily a demo of the ``lark`` parser module in Python

This package includes a Visual Studio Code plugin for syntax highlighting.

The compiler generates **statically linked standalone binaries**.

## Example usage

The following source file:

```
my_variable is a number with a value of 1
my_second_variable is a number with a value of 2
increment my_variable
if the value of my_variable is equal to my_second_variable
print "hooray\n"
add 5 to my_second_variable
add 10 to my_variable
subtract 5 to my_variable
if the value of my_second_variable is equal to my_variable
print "hooray again!\n"
```

Can be compiled 

```bash
python3 -m baloney compile my_source_file.bs
```

It will then have generated a binary `my_source_file.bs.bin`, which when executed will print

```
> ./my_source_file.bs.bin
hooray
hooray again!
>
```

## Variable assignment

### Numberish

```baloney
my_variable is a number with a value of 1
```

### String-like

```baloney
my_string_variable is a string with a value of "hello"
```

## Numeric operations

### Increment/Decrement

```
increment my_variable
```

```
decrement my_variable
```

### Augmented operations

```
add 5 to the value of my_variable
```

```
subtract 5 to my_variable
```

## Printing

Print a string literal, only with double-quotes

```
print "hello world"
```

Or, print the value of a variable

```
print the value of my_variable
```
