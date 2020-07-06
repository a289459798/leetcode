#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data = {}
        for key, v in enumerate(nums):
            if v not in data:
                data[v] = 0
            data[v] += 1
        # sort
        result = []
        i = 0
        for key, v in data.items():
            max = v
            for key2, v2 in data[key:].items():
                if max < v2:
                    max = v2
            result[i] = max
            i += 1
        print(result)
    
    def topKFrequent2(self, nums, k):

        t = {}
        for k, v in enumerate(nums):
            t = self.add(t, v)
        print(t)

    def add(self, t, data):
        if t:
            if t['key'] == data:
                t['data'] += 1
            else:
                print(t)
                if t['child'][0] and t['child'][0]['key'] == data:
                   t['child'][0]['data'] += 1
                elif t['child'][1] and t['child'][1]['key'] == data:
                   t['child'][1]['data'] += 1
                elif t['child'][0] and not t['child'][1]:
                    t['child'][1] = self.add(t['child'][1], data)
                else:
                    t['child'][0] = self.add(t['child'][0], data)
        else :
            t = {'key': data, 'data': 1, 'child': [{}, {}]}
        return t

Solution().topKFrequent2([2,2,1,1,1,3, 4, 5, 6, 7], 2)