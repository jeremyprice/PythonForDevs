
import sys

def show_sizeof(x):
    print type(x), sys.getsizeof(x)

show_sizeof(None)
show_sizeof(3)
show_sizeof(2**63)
show_sizeof(102947298469128649161972364837164)
show_sizeof(918659326943756134897561304875610348756384756193485761304875613948576297485698417)
show_sizeof(321.12345434567654323456789)
show_sizeof(12<20)
show_sizeof('string')
show_sizeof('a bigger string than the one above')
show_sizeof(['item01', 'item02', 'item03'])
show_sizeof(['item01', 'item02', 'item03', 'item04', 'item05', 'item06'])
