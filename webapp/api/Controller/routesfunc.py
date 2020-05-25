from Model.basic import check, auth
from Object.users import user
from Object.actions import action
import json

def getauth(cn, nextc):
    err = check.contain(cn.pr, ["pass"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = auth.gettoken(cn.pr["pass"])
    return cn.call_next(nextc, err)

def myauth(cn, nextc):
    err = check.contain(cn.hd, ["token"], "HEAD")
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.hd = err[1]
    err = auth.verify(cn.hd["token"])
    return cn.call_next(nextc, err)

def signup(cn, nextc):
    err = check.contain(cn.pr, ["email", "password1", "password2"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = user()
    err = use.register(cn.pr["email"], cn.pr["password1"], cn.pr["password2"])
    cn.private["user"] = use

    return cn.call_next(nextc, err)

def signin(cn, nextc):
    err = check.contain(cn.pr, ["email", "password1"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = user()
    err = use.login(cn.pr["email"], cn.pr["password1"])
    cn.private["user"] = use

    return cn.call_next(nextc, err)

def authuser(cn, nextc):
    err = check.contain(cn.hd, ["usrtoken"], "HEAD")
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.hd = err[1]

    use = user()
    err = use.verify(cn.hd["usrtoken"])
    cn.private["user"] = use

    return cn.call_next(nextc, err)

def gettoken(cn, nextc):
    err = check.contain(cn.pr, [])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = cn.private["user"]
    err = use.gettoken()
    return cn.call_next(nextc, err)

def createdoc(cn, nextc):
    err = check.contain(cn.pr, ["company", "name"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = action(1)
    err = use.create(cn.pr["company"], cn.pr["name"])
    err = use.ret_bin(True)
    return cn.call_next(nextc, err)


def sendtok(cn, nextc):
    err = check.contain(cn.pr, ["to", "curr", "date", "amount"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    err = [True, {"transaction" : {"type": "send", "amount": cn.pr["to"], "curr": cn.pr["curr"], "to": cn.pr["to"], "date": int(cn.pr["date"])}}, None]
    return cn.call_next(nextc, err)

def wallet(cn, nextc):
    err = [True, {"tokens": {"eth": 1.00000214, "ex2": 23.0000002}, "transactions": [{"type": "send", "amount": 2.23, "curr": "eth", "to": "eliot.courtel@wanadoo.fr", "date": 1589487889}, {"type": "send", "amount": 0.523, "curr": "eth", "to": "jhlauret@gmail.com", "date": 1589487889 }]}, None]
    return cn.call_next(nextc, err)

def walletcred(cn, nextc):
    err = [True, {"public": "uijbszdkjbsdojbsd", "private": "XXXXXXxxx"}, None]

    return cn.call_next(nextc, err)
