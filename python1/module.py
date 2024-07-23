import theater_module

theater_module.price(3)
theater_module.price_morning(10)
theater_module.price_soldier(7)

import theater_module as mv

mv.price(2)
mv.price_morning(5)
mv.price_soldier(0)

from theater_module import *
price(2)
price_morning(8)
price_soldier(9)


from theater_module import price,price_morning
#price_soldier(9)

from theater_module import price_soldier as price
price(2)

import byme
byme.sign()