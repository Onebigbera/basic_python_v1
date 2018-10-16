"""
pickle 模块
    pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。
    pickle模块只能在python中使用，python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化，

    pickle序列化后的数据，可读性差，人一般无法识别。
    pickle中常见的几种方法:
    pickle.dump()
        pickle.dump(obj, file[,protocol])
          序列化对象，并将结果数据流写入到文件对象中。参数protocol是序列化模式，默认值为零，表示以文本形式序列化，

    pickle.load()
          反序列化对象(解析对象)，从文件中将序列化的对象读取出来，返回数据对象


    pickle.dumps()
         直接将Python中的对象序列化，返回一个bytes对象

    pickle.loads()
        直接从bytes对象中读取序列化的信息，而非从文件中读取。



"""

import pickle
