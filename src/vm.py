class FifthVM:
    def __init__(self, bytecode):
        self.stack = []
        self.bytecode = bytecode
        self.counter = 0

    def error(self, type_e, msg):
        raise type_e(msg)
    
    def pop(self):
        return self.stack.pop()

    def push(self, val):
        self.stack.append(val)

    def run(self):
        while self.counter < len(self.bytecode):
            opcode = self.bytecode[self.counter]
            self.counter += 1

            if opcode == 0x01:
                self.push(1)
            elif opcode == 0x02:
                self.push(0)
            elif opcode == 0x03:
                if len(self.stack)>=1:
                    x = self.pop()
                    self.push(x*2)
                else:
                    self.error(RuntimeError, "'ft' needs atleast 1 item on the stack.")
            elif opcode == 0x04:
                if len(self.stack)>=2:
                    x = self.pop()
                    y = self.pop()
                    self.push(y+x)
                else:
                    self.error(RuntimeError, "'tf' needs atleast 2 items on the stack.")
            elif opcode == 0x05:
                if len(self.stack)>=2:
                    x = self.pop()
                    y = self.pop()
                    self.push(y-x)
                else:
                    self.error(RuntimeError, "'th' needs atleast 2 items on the stack.")
            elif opcode == 0x06:
                if len(self.stack)>=1:
                    top = self.stack[-1]
                    self.push(top)
                else:
                    self.error(RuntimeError, "'ih' needs atleast 1 item on the stack.")
            elif opcode == 0x07:
                if len(self.stack)>=1:
                    x = self.pop()
                    print(x)
                else:
                    self.error(RuntimeError, "'fit' needs atleast 1 item on the satck.")
            elif opcode == 0x08:
                if len(self.stack)>=1:
                    x = self.pop()
                    print(chr(x))
                else:
                    self.error(RuntimeError, "'fifth' needs atleast 1 item on the stack.")
            elif opcode == 0x09:
                print(self.stack)
            elif opcode == 0x0A:
                print("Program stopped execution forcefully via 'quit'")
                break
            else:
                self.error(KeyError, f"Unknown keyword: {opcode}")