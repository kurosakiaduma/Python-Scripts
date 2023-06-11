def appendAndDelete(s: str, t: str, k: int) -> str:
    """
    Determines whether it is possible to convert string `s` to string `t` in exactly `k` operations.
    An operation can be either appending a character to the end of the string or deleting the last character of the string.

    :param s: The initial string.
    :type s: str
    :param t: The desired final string.
    :type t: str
    :param k: The exact number of operations that must be performed.
    :type k: int
    :return: Returns 'Yes' if it is possible to convert `s` to `t` in exactly `k` operations, otherwise returns 'No'.
    :rtype: str
    """
    for _ in range(len(t)):                
        if s[_] == t[_]:
            
            if _ == (len(t)-1) and _ == (len(s)-1):
                return "Yes"
        
            elif _ == (len(s)-1):
                k -= len(t[_+1:])
                if k >= 2*len(s) or k % 2 == 0:
                    return "Yes"
                else:
                    return "No"
                
            elif _ == (len(t)-1):
                k -= len(s[_+1:])
                if k >= 2*len(t) or k % 2 == 0:
                    return "Yes"
                else:
                    return "No"
            
            else:
                pass
        
        else:
            print(f"{k} {len(t[_:])} len{(s[_:])}")
            k -= len(t[_:])+len(s[_:])
            if k == 0:
                return "Yes"
            elif k > 0:
                if not(s[:_]):
                    return "Yes"
                else:
                    if k == len(s[:_]) * 2:
                        return "Yes"
                    return "No"
            else:
                return "No" 