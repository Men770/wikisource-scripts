rev = {
    1 : "א", 
    2 : "ב", 
    3 : "ג", 
    4 : "ד", 
    5 : "ה", 
    6 : "ו", 
    7 : "ז", 
    8 : "ח", 
    9 : "ט", 
    10 : "י", 
    20 : "כ", 
    30 : "ל", 
    40 : "מ", 
    50 : "נ", 
    60 : "ס", 
    70 : "ע", 
    80 : "פ", 
    90 : "צ", 
    100 : "ק", 
    200 : "ר", 
    300 : "ש", 
    400 : "ת"
}

q = {
    270 : "ער",
    272 : "ערב",
    275 : "ערה",
    304 : "דש",
    344 : "שדמ"
}

def toGStr(n):
    if n in q:
        return q[n]
    s = ""
    if n >= 100:
        while n > 500:
            s += 'ת'
            n -= 400
        s += rev[n // 100 * 100]
        n = n % 100
    if n == 15:
        s += 'טו'
    elif n == 16:
        s += 'טז'
    else:
        if n > 9: s += rev[n // 10 * 10]
        if n % 10 != 0: s += rev[n % 10]
    return s
