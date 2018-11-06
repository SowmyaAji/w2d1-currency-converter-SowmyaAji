
import pytest
from currency_converter import convert

def test_currency_convert ():

    assert convert([("USD", "USD", 1)], 1, "USD", "USD") == 1
    assert convert([("USD", "USD", 1)], 2, "USD", "USD") == 2


def test_two_currencies():
    assert round(
        convert([("USD", "EUR", 0.74)], 1, "EUR", "USD"), 2) == 1.35
    assert round(
        convert([("USD", "EUR", 0.74)], 1, "USD", "EUR"), 2) == 0.74

def convert_many_currencies ():

    
    assert round(
        convert([("EUR", "JPY", 145.949)], 1, "EUR", "JPY"), 2) == 145.949
    assert round(
        convert(["EUR", "JPY", 145.949],150,"JPY","EUR"),2)==1.027
    assert round(
        convert([("USD","INR",72.86)],2,"USD","INR"),2)==145.72
    assert round(
        convert([("USR","INR",72.86)],100, "INR","USD"),2)==1.37
   
def raise_error ():
    rates = [("USD", "CNY",6.9)]
    with pytest.raises(ValueError):
        convert(rates,10, 'CNY','MXN')
    
    


    
    


 