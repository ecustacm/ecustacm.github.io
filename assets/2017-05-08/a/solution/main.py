from fractions import Fraction
from copy import deepcopy

z_val = {}

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b / gcd(a, b)


class PolyTerm(object):
    def __init__(self, frac=Fraction(0, 1)):
        self.coef = frac
        self.a = [] # a_i^j sub & pow [ [1, 2], [2, 1], ...  ]

    def mul_coef(self, frac):
        self.coef *= frac

    def inner_sort(self):
        self.a = sorted(self.a, reverse=False)

    def out(self):
        print("coef: %s, term: %s" % (self.coef, self.a))


class Poly(object):
    def __init__(self):
        self.poly = []

    def mul_coef(self, coef):
        for term in self.poly:
            term.mul_coef(coef)

    def mul_ai(self, sub):
        new_poly = deepcopy(self.poly)

        for term in new_poly:
            find = False
            for a in term.a:
                if a[0] == sub:
                    find = True
                    a[1] += 1
                    break

            if not find:
                term.a.append([sub, 1])
                term.inner_sort()
        self.poly = new_poly

    def add_poly(self, polyb):
        ret_poly = Poly()

        all_terms = []
        ret_terms = []
        for terma in self.poly:
            all_terms.append(terma)

        for termb in polyb.poly:
            all_terms.append(termb)

        ll = len(all_terms)
        for i in range(ll):
            for j in range(i+1, ll):
                sta = set([ (s, p) for s, p in all_terms[i].a ] )
                stb = set([ (s, p) for s, p in all_terms[j].a ] )

                if sta == stb:
                    all_terms[i].coef = all_terms[i].coef + all_terms[j].coef
                    all_terms[j].coef = 0

        for term in all_terms:
            if term.coef != 0:
                ret_terms.append(term)

        ret_poly.poly = deepcopy(ret_terms)
        return ret_poly


    def get_poly(self):
        ret = deepcopy(self.poly)
        return ret

    def out(self):
        for term in self.poly:
            term.out()
        print("poly end")


def get_z_val(n):
    """
    https://en.wikipedia.org/wiki/Cycle_index
    """
    global z_val

    if n in z_val:
        return deepcopy(z_val[n])

    if n == 0:
        one = PolyTerm(Fraction(1.0))
        poly = Poly()
        poly.poly = [one]
        z_val[n] = deepcopy(poly)
        return z_val[n]

    res = Poly()
    for i in range(1, n+1):
        v1 = get_z_val(n - i)
        v = deepcopy(v1)

        v.mul_ai(i)

        res = res.add_poly(v)

    res.mul_coef(Fraction(1, n))
    z_val[n] = deepcopy(res)
    return z_val[n]


def func(n, m):
    poly_n = get_z_val(n)
    poly_m = get_z_val(m)
    # poly_n.out()
    # poly_m.out()

    ret_poly = Poly()

    for terma in poly_n.poly:
        for termb in poly_m.poly:
            new_term = PolyTerm()
            new_term.coef = terma.coef * termb.coef


            for ta in terma.a:
                for tb in termb.a:
                    sa = ta[0]
                    pa = ta[1]

                    sb = tb[0]
                    pb = tb[1]
                    ll = lcm(sa, sb)
                    new_term.a.append([ll, (sa * sb * pa * pb / ll)])
            ret_poly.poly.append(new_term)

    return ret_poly



def subs(term, v):
    total = 1
    for a in term.a:
        total *= v**a[1]
    return term.coef * total


def answer(w, h, s):
    poly = func(w, h)
    total = 0

    for term in poly.poly:
        total += subs(term, s)
    return str(total)


def table():
    for i in range(1, 11):
        for j in range(1, 11):
            if i * j > 25:
                continue

            ans = answer(i, j, 2)
            s = "ans[%s][%s] = %s;" % (i, j, ans)
            print(s)



def main():
    with open("out", "w") as f:

        for i in range(1, 11):
            for j in range(1, 11):
                if i * j > 25:
                    continue

                ans = answer(i, j, 2)
                s = "%s\n" % (ans)
                f.write(s)


if __name__ == "__main__":
    table()
    # main()
