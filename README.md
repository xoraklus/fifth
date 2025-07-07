# fifth

A minimal project featuring a compiler, VM, and REPL with basic commands.

# Features

- Compiler for the language
- VM to execute bytecode (hexadecimal representation)
- REPL
- Minimal command set

# Installation

```bash
git clone https://github.com/xoraklus/fifth.git
cd fifth
```

Optionally, you can create a virtual environment:

```bash
python -m venv venv

source venv/bin/activate # Windows: venv\Scripts
\activate
```

# Usage

```bash
# Start the REPL (primary way to use the language)
python fifth_run.py

# Compile and run a program
python fifth_run.py path/to/your/source_file.fifth # It is compiled by the compiler and ran by a VM
```

## Commands (language instruction set)

- `fi`: Push 1 to the stack
- `fii`: Push 0 to the stack
- `ft`: Pop a value x, push x * 2 to the stack
- `tf`: Pop a values x and y, push y + x to the stack
- `th`: Pop a values x and y, push y - x to the stack
- `ih`:  Duplicate top stack value
- `fit`: Pop a value x, print x to the console
- `fifth`: Pop a value x, print x as character to the console
- `quit`: Quit the REPL / Stop program execution
- `stack`: Output the stack

### Examples:

Example 1:
```bash
python fifth_run.py
>>> fi
>>> fi
>>> tf
>>> ft 
>>> ft
>>> ft
>>> ft
>>> ft
>>> fi
>>> tf
>>> stack
[65]
>>> fifth
A
>>> quit
# REPL exited
```

Example 2:
We have src.fifth:
```fifth
fi fi tf ft ft ft ft ft fi tf stack fifth quit
```

We run it:
```bash
python fifth_run.py src.fifth
[65]
A
Program stopped execution forcefully via 'quit'
```
# License

[MIT License](LICENSE)
