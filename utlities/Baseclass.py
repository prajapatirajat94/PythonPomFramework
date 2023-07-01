import pytest


@pytest.mark.usefixtures("init_driver")
class BaseClass():
    pass


# below method you need to add in Base Class to for parametrize and pass it into test_e2e.py file method
# (self,getData)
# here params support tupples and dictionary data type
@pytest.fixture(params=[("Rajat@gmail.com", "Rsting123"), ("kjl@gmail.com", "Rsting123")])
def getData(request):
    return request.param

# or you can use in params dictionary
# @pytest.fixture(params=[{"firstname":"Rajat@gmail.com", "password":"Rsting123" },
#                         { "firstname":"kjl@gmail.com","password":"Rsting123"}])
# def getData(request):
#     return request.param
