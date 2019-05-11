from future import absolute_import, division, print_function, unicode_literals
class vector:
    def vector_add(self, v,w):
        return [v_i + v_w 
                            for v_i,v_w in zip(v,w)]

    def vector_substract(self, v,w):
            return [v_i-w_i 
                            for v_i, w_i in zip(v,w)]

    def vector_sum(self, vectors):
        result = vectors[0]
        for vector in vectors[:1]:
            result = self.vector_add(result,vector)
        return result

    def scalar_multiply(self, c,v):
        return [c * v_i for v_i in v]

    def vector_mean(self,vectors):
        n = len(vectors)
        return self.scalar_multiply(1/n, self.vector_sum(vectors))

    def dot(self,v,w):
        return sum(v_i*w_i 
                            for v_i, w_i in zip(v,w))
    
    def sum_of_squares(self, v):
        return self.dot(v,v)

    def magnitude(self,v):
        return (self.sum_of_squares(v)**1/2)

    def squared_distance(self,v,w):
        return self.sum_of_squares(self.vector_substract(v,w))


class matrix:
    def shape(self,A):
        num_rows = len(A)
        num_cols = len(A[0]) if A else 0
        return num_rows,num_cols
    
    def get_row(self,A,i):
        return A[i]

    def get_col(self,A,j):
        return [a_i[j] for a_i in A]

    def make_matrix(self,num_rows,num_cols,entry_fn):
        return [[entry_fn(i,j) 
                    for j in range(num_cols)]
                         for i in range(num_rows)]

    def is_diagonal(self,i,j):
        return 1 if i== j else 0
    
class statistics:

    def mean(self, x):
        return sum(x)/len(x)

    def median(self,v):
        n = len(v)
        sorted_v = sorted(v)
        midpoint = n//2
        if n % 2 == 1:
            return sorted_v[midpoint]
        else:
            lo = midpoint - 1
            hi = midpoint
            return(sorted_v[lo] + sorted_v[hi]/2)

    def quantile(self,x,p):
        p_index = int(p * len(x))
        return sorted(x)[p_index]
    
    def data_range(self,x):
        return max(x) - min(x)

    def de_mean(self,x):
        x_bar = self.mean(x)
        return [x_i - x_bar for x_i in x]
    
    def variance(self,x):
        n = len(x)
        deviations = self.de_mean(x)
        return vector().sum_of_squares(deviations)/(n-1)

    def standard_deviation(self,x):
        return self.variance(x)**1/2

    def interquartile_range(self,x):
        return self.quantile(x,0.75) - self.quantile(x, 0.25)

    def covariance(self,x,y):
        n=len(x)
        return(self.de_mean(x),self.de_mean(y))/(n-1)

    def correlation(self,x,y):
        stdev_x = self.standard_deviation(x)
        stdev_y = self.standard_deviation(y)
        if stedv_x > 0 and sted_y > 0:
            return self.covariance(x,y)/stdev_x/stdev_y
        else:
            return 0
