import pytest

from test_cases.Calculator import Calculator
from test_cases.test_calculator import get_datas


@pytest.fixture(scope="class")
def initcalc_class():
    print("\nsetup")
    calc = Calculator()
    yield calc
    print("\nteardown")


@pytest.fixture(params=get_datas()['int_datas'], ids=get_datas()['ids'])
def get_add_datas(request):
    return request.param


@pytest.fixture(params=get_datas()['float_datas'], ids=get_datas()['float_ids'])
def get_add_datas1(request):
    return request.param


@pytest.fixture(params=[[1, 1, 1.0], [1, -1, -1.0], [-1, -1, 1.0],
                        [0, 2, 0], [2, 0, 'None'], [999, -999, -1.0], [0.04, 0.1, 0.4],
                        [-0.1, -0.1, 1.0], [0.1, -0.1, -1.0], [-0.1, 0.1, -1.0], [99.0, -1000.0, -0.099]],
                ids=['正整数', '正负', '负负', '除数为零', '被除数为零', '大数',
                     'float1', 'float2', 'float3', 'float4', 'float5'])
def get_div_datas(request):
    return request.param


def pytest_collection_modifyitems(session, config, items: list):
    print('搜集所有测试用例方法')
    items.reverse()
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def pytest_addoption():
    pass