class Rand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 1103515245
        self.c = 12345
        self.m = 2**31

    def _mathRand(self):
        self.seed = (self.a * self.seed + self.c) % self.m

    def nextInt(self) -> int:
        self._mathRand()
        return self.seed % 221234342
    
    def untilInt(self, until) -> int:
        self._mathRand()
        return self.seed % until
    
    def toUntilInt(self, to: int, until: int) -> int:
        self._mathRand()
        return to + (self.seed % (until - to + 1))
    
    def nextFloat(self) -> float:
        self._mathRand()
        return self.seed / self.m
    
# rnd = Rand(123)
# for _ in range(100_000_000):
#     if(rnd.toUntilInt(100000, 999999) > 999999):
#         print('dadad')