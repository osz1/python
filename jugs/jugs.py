# k < m, k < n
def jugs1(m, n, k):
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
            jugs1(mM, nN, k)

        return mM, nN


print(jugs1(5, 3, 2))


def jugs2(m, n, k, mm=0):
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
            jugs2(m, n, k, mM)

        return mM, nN


print(jugs2(5, 3, 1))
