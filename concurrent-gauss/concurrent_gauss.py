from copy import deepcopy
import multiprocessing
from multiprocessing import shared_memory
import array
import threading
from concurrent.futures import ThreadPoolExecutor

class ConcurrentGauss:
    def __init__(self, A, b, pool) -> None:
        self.A = A
        self.b = b
        self.len = len(A)
        self.n = [[0 for _ in range(self.len + 1)] for _ in range(self.len)]
        self.m = [0 for _ in range(self.len)]
        self.M = deepcopy(A)
        for idx, x in enumerate(b):
            self.M[idx].append(x)
        self.thread_pool = pool

    def A_op(self, i, k):
        self.m[k] = self.M[k][i] / self.M[i][i]

    def B_op(self, i, j, k):
        self.n[k][j] = self.M[i][j] * self.m[k]

    def C_op(self, j, k):
        self.M[k][j] -= self.n[k][j]
        
    def resolve(self):
        for i in range(self.len - 1):
            with ThreadPoolExecutor(max_workers=self.thread_pool) as executor:
                futures = [executor.submit(self.A_op, i, j) for j in range(i + 1, self.len)]
                for future in futures:
                    future.result()

            with ThreadPoolExecutor(max_workers=self.thread_pool) as executor:
                futures = [executor.submit(self.B_op, i, j, k) 
                           for k in range(i + 1, self.len) 
                           for j in range(i, self.len + 1)]
                for future in futures:
                    future.result()

            with ThreadPoolExecutor(max_workers=self.thread_pool) as executor:
                futures = [executor.submit(self.C_op, j, k) 
                           for k in range(i + 1, self.len) 
                           for j in range(i, self.len + 1)]
                for future in futures:
                    future.result()
        return self.M
    
    def to_diagonal(self):
        for i in range(self.len-1, -1, -1):
            for j in range(self.len-1, i, -1):
                self.M[i][self.len] -= self.M[i][j] * self.M[j][self.len]
                self.M[i][j] = 0
            self.M[i][self.len] /= self.M[i][i]
            self.M[i][i] = 1
        
        return self.M
        