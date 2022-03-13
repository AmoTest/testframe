from ddt import ddt, data, unpack, file_data
import unittest

@ddt
class test_02(unittest.TestCase):

    #单组元素
    @data(1, 2, 3)
    def test_02_a(self, value):
        print(value)

    #多组数据，未拆分
    @data([1 ,2], [3, 4])
    def test_02_b(self, value):
        print(value)

    #多组数据，拆分
    @data([1, 2], [3, 4])
    @unpack
    def test_02_c(self, value1, value2):
        print("----------------")
        print(value1 , value2)

    #多个列表字典未拆分
    @data([{"name": "peter"}, {"age": 15}, {"addr": "chengdu"}])
    def test_02_d(self, value):
        print("----------------")
        print('d->多个列表字典未拆分：{}'.format(value))

    #多个列表字典拆分
    @data([{"name": "peter"}, {"age": 15}, {"addr": "chengdu"}])
    @unpack
    def test_02_e(self, value1, value2, value3):#data里的数据key必须与字典的key保持一致
        print("----------------")
        print('e->多个列表字典拆分:{}{}{}'.format(value1, value2, value3))

    @data({"name": "peter", "age": 15, "addr": "chengdu"})
    def test_02_f(self, value):
        print("----------------")
        print("f->单个字典未拆分:{}".format(value))

    @data({"name": "peter", "age": 15, "addr": "chengdu"})
    @unpack
    def test_02_g(self, name, age, addr):
        print("----------------")
        print("g->单个字典拆分:{}{}{}".format(name, age, addr))

    @data({"name": "peter", "age": 15, "addr": "chengdu"},{"name": "elvis", "age": 18, "addr": "hangzhou"})
    @unpack
    def test_02_h(self, name, age, addr):
        print("----------------")
        print("h->多个字典拆分:{}{}{}".format(name, age, addr))

    test_data = [{"name": "peter", "age": 15, "addr": "chengdu"}, {"name": "elvis", "age": 18, "addr": "hangzhou"}]
    @data(*test_data) # *号为解包，ddt会按逗号分隔，将数据拆分（不需要@unpack装饰器了）
    def test_02_i(self, value):
        print("----------------")
        print("i->多个字典拆分:{}".format(value))

if __name__ == "__main__":

    unittest.main()
