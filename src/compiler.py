class Compiler:
    def __init__(self):
        pass

    def compile(self, filename, debug=False):
        with open(filename, 'r', encoding="utf8") as f:
            keywords = {
                "fi": 0x01,
                "fii": 0x02,
                "ft": 0x03,
                "tf": 0x04,
                "th": 0x05,
                "ih": 0x06,
                "fit": 0x07,
                "fifth": 0x08,
                "stack": 0x09,
                "quit": 0x0A
            }

            program = f.read()
            tokens = program.split()
            bytecode = bytes([keywords[b] for b in tokens])
            if debug:
                print(f"\033[92m\033[1mTokens\033[0m: {tokens}")
                print(f"\033[92m\033[1mBytecode\033[0m: {bytecode}")
            return bytecode