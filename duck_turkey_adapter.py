"""
适配器模式（Adapter）- Python 最小可运行示例。
场景：客户端只认识 Duck 接口，但手头有 Turkey 对象；通过适配器桥接。
运行: python3 duck_turkey_adapter.py
"""
from __future__ import annotations

from typing import Protocol


class Duck(Protocol):
    def quack(self) -> None: ...
    def fly(self) -> None: ...


class Turkey(Protocol):
    def gobble(self) -> None: ...
    def fly(self) -> None: ...


class MallardDuck:
    def quack(self) -> None:
        print("Quack")

    def fly(self) -> None:
        print("I'm flying")


class WildTurkey:
    def gobble(self) -> None:
        print("Gobble gobble")

    def fly(self) -> None:
        print("I'm flying a short distance")


class TurkeyAdapter:
    """把 Turkey 适配为 Duck 接口。"""

    def __init__(self, turkey: Turkey) -> None:
        self._turkey = turkey

    def quack(self) -> None:
        self._turkey.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self._turkey.fly()


def test_duck(d: Duck) -> None:
    d.quack()
    d.fly()


def main() -> None:
    duck: Duck = MallardDuck()
    turkey: Turkey = WildTurkey()
    turkey_adapter: Duck = TurkeyAdapter(turkey)

    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    test_duck(duck)

    print("\nThe TurkeyAdapter says...")
    test_duck(turkey_adapter)


if __name__ == "__main__":
    main()
