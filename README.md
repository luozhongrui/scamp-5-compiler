# scamp-5-compiler

## Prerequisite

**1. Build a local Docker image.**

```shell
make docker-build
```

<span style="color: yellow; font-size: 24px;">&#x26A0;</span> For Windows User:
Before building the docker image, make sure that the docker/entrypoint.sh file is formatted in Linux/Unix format (with the terminator \n instead of \r\n)

**2. Activate the Docker environment.**

```shell
make activate
```

### Delimiters

|                 |    Delimiter     |
| :-------------: | :--------------: |
|      comma      |     **`,`**      |
|      point      |     **`.`**      |
|      colon      |     **`:`**      |
|  single quote   |     **`'`**      |
|      quote      |     **`"`**      |
|   parentheses   | **`(`**, **`)`** |
| square brackets | **`[`**, **`]`** |

### Arithmetic, Relational, and Logical Operators

|                |                         Operator                         |
| :------------: | :------------------------------------------------------: |
|    addition    |                         **`+`**                          |
|  subtraction   |                         **`-`**                          |
| multiplication |                         **`*`**                          |
|   assignment   |                         **`=`**                          |
|   relational   | **`<`**, **`<=`**, **`!=`**, **`>=`**, **`>`**, **`==`** |
|    logical     |              **`and`**, **`or`**, **`not`**              |

### Reserved Words

- Declaration: `def`
- Flow-of-control: `while`, `if`, `else`, `for`

### Identifiers

An identifier is a sequence of letters and digits beginning with a letter. Identifiers are case-sensitive; that is, **gura**, **Gura**, and **GURA** are treated as different identifiers. Note that reserved words CANNOT be used as identifiers.

### Integer Constants

A sequence of one or more digits. An integer that begins with the digit 0 **and** consists of a sequence of octal digits is treated as an **octal** integer; otherwise, the sequence of digit(s) is treated as a **decimal** integer.
