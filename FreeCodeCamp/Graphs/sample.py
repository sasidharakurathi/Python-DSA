# class Solution:
    # def findJudge(self, n: int, trust: list[list[int]]) -> int:
    #     t = len(trust)
    #     incoming = [0] * (n + 1)
    #     outgoing = [0] * (n + 1)

    #     # Step 1: count incoming & outgoing
    #     for i in range(t):
    #         incoming[trust[i][1]] += 1
    #         outgoing[trust[i][0]] += 1

    #     # Step 2: check for judge
    #     for i in range(1, n + 1):
    #         if incoming[i] == n - 1 and outgoing[i] == 0:
    #             return i

    #     return -1
    
#     def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
#         if n == 1:
#             return n
        
#         graph = self.buildGraph(trust)
#         trust_hashmap = {}
        
#         for node , edges in graph.items():
#             for edge in edges:
#                 if edge not in trust_hashmap:
#                     trust_hashmap[edge] = 1
#                 else:
#                     trust_hashmap[edge] += 1
                    
#                 if trust_hashmap[edge] == n-1:
#                     if not graph.get(edge , None):
#                         return edge
                    
        
#         # print(trust_hashmap)
#         return -1
        
#     def buildGraph(self , trust):
#         graph = {}

#         for node1 , node2 in trust:
#             if node1 not in graph:
#                 graph[node1] = [node2]
#             else:
#                 graph[node1].append(node2)
        
#         return graph
    
# s = Solution()
# print(s.findJudge(2 , [[1,2]]))
# print(s.findJudge(3 , [[1,3] , [2,3]]))
# print(s.findJudge(3 , [[1,3],[2,3],[3,1]]))
