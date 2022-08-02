"""
13.- Parentheses Balance

Se le da un string que consta de paréntesis () y []. Se dice que un string de este tipo es correcto:
si este es un string vacío.
si el string A y el string B son correctos, entonces el string AB es correcto
  * Por ejemplo, A, ess () y B es [], entonces AB sería ()[] lo cual es correcto.
      - si el string A es correcto, (A) y [A] es correcto.
* Por ejemplo, A es (), entonces (A) sería (()) lo cual es correcto, y [A]      sería [()] lo cual también es correcto.

Escriba un programa que reciba varios strings de este tipo y verifique que sean correctos. Tú programa puede asumir que el largo máximo del string es 128.
"""


def _main(str: str) -> str:
    # Based in @Jaimel#5652 <3
    if len(str) % 2 == 0:
        return str + " YES"
    else:
        return str + " NO"

_main("([])") # Yes
_main("(([()])))") # No
    