class Solution:

    @staticmethod
    def findJudge0(N: int, trust: [int, int]) -> int:
        """1224 ms, 23.8 MB"""

        trust_table = [[0 for _ in range(N)] for _ in range(N)]

        for relationship in trust:
            index_one, index_two = [index - 1 for index in relationship]
            trust_table[index_one][index_two] = 1

        for index, row in enumerate(trust_table):
            if sum(row) == 0:
                everybody = sum([row_[index] for row_ in trust_table])
                if everybody == N - 1:
                    return index + 1
        return -1

    @staticmethod
    def findJudge(N: int, trust: [int, int]) -> int:
        """824 ms, 17.3 MB"""

        edges_in, edges_out = [0] * N, [0] * N

        for relationship in trust:
            index_one, index_two = relationship[0] - 1, relationship[1] - 1
            edges_out[index_one] += 1
            edges_in[index_two] += 1

        for index in range(N):
            if edges_out[index] == 0 and edges_in[index] == N - 1:
                return index + 1

        return -1
