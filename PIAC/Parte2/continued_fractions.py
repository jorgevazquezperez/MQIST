#!/usr/bin/env python

import contfrac as cf

def main():

    x = 0.1562

    coefficients = list(cf.continued_fraction(x))

    print("Components (also called coefficients):")
    print(coefficients)

    print("\nArithmetical expression:")
    print(cf.arithmetical_expr(coefficients))

    print("\nConvergents:")
    for i, conv in enumerate(list(cf.convergents(x))):
        print(f"{i}th convergent: {conv}")

if __name__ == '__main__':
    main()