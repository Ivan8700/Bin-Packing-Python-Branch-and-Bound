# Bin-Packing-Python-Branch-and-Bound
## This is a B&amp;B algorithm implementation for the bin packing problem.  
**<ins> The problem :</ins>** Given 'n' items of size (0,1] , assign the items to bins of size at most 1 such that the amount of bins used will be minimal.  
That's a NP problem and the algorithm which I used to solve it is the 'Branch & bound' algorithm.  
**<ins> Initialization :</ins>** assign 'n' empty bins.  
For each node the upper bound will be calculated using the 'Best Fit' algorithm which schedules the item in the first bin which it can be scheduled to, if non exist - create a new bin and schedule it there.  
For each node the lower bound will be calculated using the max{OPT,amount_of_bins_created} bound which compares 'OPT - sum of items' and 'amount_of_bins_created already created in the node'.  
After the calculation of the bounds - if the subtree of the node might generate a better solution in the future, create 'n' sons which correspond to 'assign the next job in order of the input in every other bin and check the solution'.  

Although the algorithm gives always an optimal solution, it is pretty slow compared to other algorithm with Complexity run-time up to O(n^n) (strictly less but obviously still an exponential run-time).


