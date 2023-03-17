# k < m, k < n

def amigtele(m, n, k):
    if (k < m) and (k < n):
        mM = m
        nN = 0
        print(mM, nN)
        mM = m - n
        nN = n
        print(mM, nN)
        if k in (mM, nN):
            return mM, nN
        else:
            amigtele(mM, nN, k)
        return mM, nN
print(amigtele(5, 3, 2))

def amigures(m, n, k, mm=0):
    if (k < m) and (k < n) and (mm < m):
        mM = mm
        nN = n
        print(mM, nN)
        if (m - mM) >= n:
            mM += n
            nN = 0
        else:
            nN = n - (m - mM)
            mM = m
        print(mM, nN)
        if k in (mM, nN):
            return mM, nN
        else:
            amigures(m, n, k, mM)
        return mM, nN
print(amigures(5, 3, 1))