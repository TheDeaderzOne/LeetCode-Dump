# 29 ms, 97.46%, 17.5 MB memory, 10.84%

class Solution:
    def divide(self, dividend, divisor):
        quotient = 0
        newnum = abs(dividend)
        divider = abs(divisor)
        if divider != 1:
            lubbock = 0
            exponent = 1
            while lubbock == 0:
                buz = divider**exponent
                newnum -= buz
                if newnum >= 0:
                    newnum += buz
                    exponent += 1
                else:
                    newnum += buz
                    exponentlim = exponent - 1
                    lubbock = 1
            for x in range(exponentlim):
                tracker = 0
                faketracker = 0
                for _ in range(divider - 1):
                    tracker += 1
                    faketracker += divider ** (exponentlim - x)
                    if faketracker > newnum:
                        faketracker -= divider ** (exponentlim - x)
                        tracker -= 1
                        break
                if tracker != 0:
                    for _ in range(tracker):
                        quotient += divider ** (exponentlim - x - 1)
                    newnum -= faketracker

        if divider == 1:
            quotient = newnum

        if dividend > 0 and divisor < 0:
            quotient = 0 - quotient
        if dividend < 0 and divisor > 0:
            quotient = 0 - quotient
        if quotient > 2**31 - 1:
            quotient = 2**31 - 1
        if quotient < 0 - (2**31):
            quorient = 0 - (2**31)
        return quotient
