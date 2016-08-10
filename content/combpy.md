Title: Python中用itertools实现排列和组合
Date: 2016-05-08 19:20
Modified: 2015-05-08 19:30
Category: Python
Tags: itertools
Authors: Kai Wang
Slug: post1
Summary: A simple example of the usage of itertools

实现一个列表（或者说一个数组）的排列组合是一个写脚本处理数据时很常见的小问题。在python中可以通过itertools生成器简单实现这个功能。不用废话，直接用代码说话。

# 1. 组合（combination）

	#! /usr/bin/env python
	# -*- coding=utf-8 -*-
	import itertools
	
	list1 = ['a','b','c']
	list2 = []
	
	for i in range(1,len(list1)+1):
	    iter = itertools.combinations(list1,i)
	    list2.append(list(iter))
	    
	print(list2)
	
 打印的结果是
 
	[[('a',), ('b',), ('c',)], [('a', 'b'), ('a', 'c'), ('b', 'c')], [('a', 'b', 'c')]]
	
# 2. 排列（permutation）

	#! /usr/bin/env python
	# -*- coding=utf-8 -*-
	import itertools
	
	list1 = ['a','b','c']
	list2 = []
	
	for i in range(1,len(list1)+1):
	    iter = itertools.permutations(list1,i)
	    list2.append(list(iter))
	
	 
	print(list2)
 
 打印的结果是
 
	[[('a',), ('b',), ('c',)], [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')], [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]]
	
以上两个例子中，list1是列表还是字符串都可以达到同样的效果。