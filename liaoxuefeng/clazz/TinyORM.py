#!/usr/bin/env python3
# encoding: utf-8
"""
@file: TinyORM.py
@user: muyi-macpro
@time: 2018/4/6 下午5:10
@desc: 几行代码实现的tiny orm 廖师傅非常精彩
"""


# 期待用户定义user类来操作数据库中user表

# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()


# 保存数据库表的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 定义Model的元类，修饰了Model
# 在ModelMetaclass中，一共做了几件事情：
#   排除掉对Model类的修改；
#   在当前类（比如User）中查找定义的类的所有属性，
#       如果找到一个Field属性，就把它保存到一个__mappings__的dict中，
#       同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
#   把表名保存到__table__中，这里简化为表名默认为类名。
class ModelMetaclass(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Model':
            return type.__new__(mcs, name, bases, namespace)

        print('Found model: %s' % name)
        mappings = dict()
        for k, v in namespace.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            namespace.pop(k)

        namespace['__mappings__'] = mappings  # 保存属性和列的映射关系
        namespace['__table__'] = name  # 假设表名和类名一致
        return type.__new__(mcs, name, bases, namespace)


# 当用户定义一个class User(Model)时，
# Python解释器首先在当前类User的定义中查找metaclass，
# 如果没有找到，就继续在父类Model中查找metaclass，
# 找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


if __name__ == '__main__':
    class User(Model):
        # 定义类的属性到列的映射：
        id = IntegerField('id')
        name = StringField('username')
        email = StringField('email')
        password = StringField('password')

    # 创建一个实例：
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')

    print(u.__mappings__)
    print(u.id)
    # 保存到数据库：
    u.save()

    pass
