# -*- coding:utf-8 -*-
import pytest

from testcases.Calculator import Calculator


class TestCalculator:

    def setup_class(self):
        self.calc = Calculator()
        print('setup_class:首次执行测试类调用 ', '\n开始测试')

    def teardown_class(self):
        print('teardown_class：所有测试用例测试结束后调用', '\n测试结束')

    def setup(self):
        print('setup: 每条测试用列开始时调用', '\n开始计算')

    def teardown(self):
        print('teardown: 每条测试用例结束时调用', '\n计算结束')

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [1, -1, 0], [-1, -1, -2],
                                            [0, 2, 2], [999, -999, 0], [0.04, 0.1, 0.14]],
                             ids=['正整数', '正负', '负负', '零数', '大数', 'float'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        print(f'预期结果:{expect},实际输出:{result}')
        assert expect == result
        # if expect == result:
        #     print('预期结果=实际结果，测试通过')
        # else:
        #     print('预期结果!=实际结果，测试失败')

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 1.0], [1, -1, -1.0], [-1, -1, 1.0],
                                            [0, 2, 0], [2, 0, 'None'], [999, -999, -1.0], [0.04, 0.1, 0.4]],
                             ids=['正整数', '正负', '负负', '除数为零', '被除数为零', '大数', 'float'])
    def test_div(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
            result1 = round(result, 2)
            print(f'预期结果:{expect},实际输出:{result1}')
            assert expect == result1
            # if expect == result:
            #     print('预期结果=实际结果，测试通过')
            # else:
            #     print('预期结果!=实际结果，测试失败')
        except ZeroDivisionError as e:
            print(f'出现错误{e},被除数为0，无法计算，测试通过')


if __name__ == "__main__":
    pytest.main(['-vs', './test_calculator.py'])
