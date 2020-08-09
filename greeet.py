'''import sass as s #aliasing 
s.message()'''


#Employee salary details

#to cal dearness allowance

def da(basic):
    da = basic * 50/100
    return da

#to cal houserent allowance
def hra(basic):
    hra = basic *20/100
    return hra

#to cal provident fund
def pf(basic):
    pf = basic * 10/100
    return pf

#to cal income tax payable by employee

def itax(gross):
    tax = gross*10/100
    return tax





