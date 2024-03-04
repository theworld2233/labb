import z3

## Construct two 32-bit integer values.  Do not change this code.
a = z3.BitVec('a', 32)
b = z3.BitVec('b', 32)
u_avg = z3.UDiv(a + b, 2)
s_avg = (a + b) / 2
az33 = z3.ZeroExt(1, a)
bz33 = z3.ZeroExt(1, b)
real_u_avg = z3.Extract(31, 0, z3.UDiv(az33 + bz33, 2))

as33 = z3.SignExt(1, a)
bs33 = z3.SignExt(1, b)
real_s_avg = z3.Extract(31, 0, (as33 + bs33) / 2)
def printable_val(v, signed):
    if type(v) == z3.BitVecNumRef:
        if signed:
            v = v.as_signed_long()
        else:
            v = v.as_long()
    return v

def printable_model(m, signed):
    vals = {}
    for k in m:
        vals[k] = printable_val(m[k], signed)
    return vals

def do_check(msg, signed, avg, real_avg):
    e = (avg != real_avg)
    print("Checking", msg, "using Z3 expression:")
    print("    " + str(e).replace("\n", "\n    "))
    solver = z3.Solver()
    solver.add(e)
    ok = solver.check()
    print("  Answer for %s: %s" % (msg, ok))

    if ok == z3.sat:
        m = solver.model()
        print("  Example:", printable_model(m, signed))
        print("  Your average:", printable_val(m.eval(avg), signed))
        print("  Real average:", printable_val(m.eval(real_avg), signed))