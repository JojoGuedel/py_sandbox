from decimal import Decimal

class NumberType():
    pass

class Prime():
    def __init__(self):
        self._primes = [2]
    
    def _gen_primes(self, target: int):
        while self._primes[-1] ** 2 <= target:
            self._primes.append(self.next(self._primes[-1]))
    
    def primes(self):
        p = 0
        i = 0

        while True:
            if len(self._primes) > i + 1:
                p = self._primes[i + 1]
            else:
                p = self.next(p)

            i += 1
            yield p

    def next(self, current: int):
        if current < 2:
            return 2

        self._gen_primes(current)
        
        while True:
            current += 1

            if current in self._primes:
                return current

            for p in self.primes():
                if p ** 2 > current:
                    return current

                if current % p == 0:
                    break
    
    def factorize(self, number: int):
        factors = []

        for p in self.primes():
            while number % p == 0:
                number /= p
                yield p
            
            if p ** 2 > number:
                yield number
                return

            if number == 1:
                return
            
def factorize(number: Decimal):
    factors: list[Decimal] = []
    c: Decimal = 2
    while number > 1:
        if number % c == 0:
            number = Decimal(number) / Decimal(c)
            factors.append(c)

        else:
            c += 1
    
    return factors

if __name__ == "__main__":
    prime1 = Prime()
    prime2 = Prime()
    
    p = prime1.next(100000000)
    print(p)

    print([i for i in prime1.factorize(p)])
    print([i for i in prime2.factorize(p)])
    print(factorize(p))