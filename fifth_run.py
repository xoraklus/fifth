#!/usr/bin/env python3

from src.compiler import Compiler
from src.vm import FifthVM
from src.fifth_repl import Fifth
import sys

if len(sys.argv) >= 2:
    compiler = Compiler()
    bytecode = compiler.compile(sys.argv[1])
    vm = FifthVM(bytecode=bytecode)
    vm.run()
else:
    repl = Fifth([])
    repl.run()
