# -*- coding: utf-8-*-
"""
类的接口--抽象基类
"""
import abc

__author__ = 'george'
__date__ = '2018-09-26'


class CacheBase(metaclass=abc.ABCMeta):
    """
    提供全局的接口抽象基类(给缓存的子类扩展)
    """
    cached = {}

    @abc.abstractmethod
    def get(self, key):
        raise NotImplemented

    @abc.abstractmethod
    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    def get(self, key):
        return self.cached[key]

    def set(self, key, value):
        '''
        设置key，value，保存到基类的cached
        :param key:
        :param value:
        :return:
        '''
        self.cached[key] = value

    def getall(self):
        for key in self.cached.keys():
            print(f'key:{key} --> value:{self.cached[key]}')

redis_cache = RedisCache()
# 设置key:value键值对
redis_cache.set('name', 'tom')
redis_cache.set('name', 'jack')
#获取存储的值
redis_cache.getall()