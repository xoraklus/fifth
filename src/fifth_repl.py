class Fifth:
    def __init__(self, stack=None):
        self.stack = stack if stack is not None else []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def run(self):
        while True:
            cmd = input(">>> ")
            if cmd == "fi":
                self.push(1)
            elif cmd == "fii":
                self.push(0)
            elif cmd == "ft":
                if len(self.stack) >= 1:
                    x = self.pop()
                    self.push(x * 2)
                else:
                    print("'ft' needs atleast 1 item on the stack.")
                    pass
            elif cmd == "tf":
                if len(self.stack) >= 2:
                    x = self.pop()
                    y = self.pop()
                    self.push(y+x)
                else:
                    print("'tf' needs atleast 2 items on the stack.")
                    pass
            elif cmd == "th":
                if len(self.stack) >= 2:
                    x = self.pop()
                    y = self.pop()
                    self.push(y-x)
                else:
                    print("'th' needs atleast 2 items on the stack.")
                    pass
            elif cmd == "ih":
                if len(self.stack) >= 1:
                    top = self.stack[-1]
                    self.push(top)
                else:
                    print("'ih' needs atleast 1 item on the stack.")
            elif cmd == "fit":
                if len(self.stack) >= 1:
                    x = self.pop()
                    print(x)
                else:
                    print("'fit' needs atleast 1 item on the stack.")
                    pass
            elif cmd == "fifth":
                if len(self.stack) >= 1:
                    x = self.pop()
                    print(chr(x))
                else:
                    print("'fifth' needs atleast 1 item on the stack.")
                    pass
            elif cmd == "quit":
                raise KeyboardInterrupt("quit")
            elif cmd == "stack":
                print(self.stack)
            else:
                print(f"Unsupported command: {cmd}")
                pass
