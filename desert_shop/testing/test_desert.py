from desert import candy,cookie,iceCream,sunday
# print("hey")
def test_candy():
    tstcnd=candy("sugar",5,1)
    assert tstcnd.get_nm()==tstcnd.nm
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan
def test_cookie():
    tstcnd=cookie("sugar",3,1)
    assert tstcnd.get_nm()==tstcnd.nm
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan
def test_iceCream():
    tstcnd=iceCream("vanil",18.5,1)
    assert tstcnd.get_nm()==tstcnd.nm
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan
def test_sunday():
    tstcnd=sunday("vanil sprink",2,1,"sprink")
    assert tstcnd.get_nm()==tstcnd.nm
    assert tstcnd.cost()==tstcnd.quan*tstcnd.pp_
    assert tstcnd.get_quan()==tstcnd.quan