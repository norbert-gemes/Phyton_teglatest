def tv(a: int, b: int, c: int) -> float:
    TV: float = a * b * c
    return TV


def ta(a: int, b: int, c: int) -> int:
    TA: int = 2 * (a * b + a * c + b * c)
    return TA


def main() -> None:
    print('Téglatest térfogat, felszín!')

    a: int = int(input('Adja meg a téglatest első oldalát: '))
    b: int = int(input('Adja meg a téglatest második oldalát: '))
    c: int = int(input('Adja meg a téglatest harmadik oldalát: '))

    térfogat: float = tv(a, b, c)
    felszín: int = ta(a, b, c)
    print(f'A téglatest térfogata: {térfogat} cm^3')
    print(f'A téglatest felszíne: {felszín} cm^2')


if __name__ == '__main__':
    main()
