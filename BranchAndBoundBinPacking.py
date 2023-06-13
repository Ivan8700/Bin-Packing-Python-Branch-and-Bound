from Node import Node
import math
import time
import random;
def printSolution(best_solution,bin_status,sum_status,opt,sum):
    print("The best solution is with value : " + str(best_solution));
    output='';
    i=1;
    for x in bin_status:
        if(sum_status[i-1]>0):
            output += "Bin number " + str(i) + "\n";
            output += "{ "
            for key,value in x.items():
                output += "(" + str(value) + " , " + str(key) + "), ";
            output += "} \n";
            output+= "with summation " + str(sum_status[i-1]) + "\n";
            i+=1;
            print(output);
            del output;
            output = '';
    print("Solution has " + str(best_solution) + " bins");
    print("OPT is bound by : " + str(opt));
    print("The sum of items is : " + str(sum));
    print("Time taken function is {} seconds" .format(time.time() - start_time))
            

best_solution=-1;
bin_status_of_best_solution=[];
sum_status_of_bin=[];
input_array = [];
bins=[];
sum_in_each_bin=[];
option_to_input=int(input("Enter 0 - to receive input from input.txt file, 1 - to manually insert, 2 - random jobs : "));
if(option_to_input==0):
    input_file=open('inputs/input1.txt');
    n=int(input_file.readline());
else:
    n = int(input("Enter amount of jobs "));
print("Enter the items you want to pack, the items are of size (0,1] : ");
sum=0;
for x in range(0,n):
    if (option_to_input==0):
        k=float(input_file.readline())
    elif (option_to_input==1):
        k=(float(input()));
    else:
        k=random.uniform(0.0001,1);
    sum+=k;
    input_array.append(k);
    bins.append({});
    sum_in_each_bin.append(0);
start_time = time.time();
order = [];
root= Node(math.ceil(sum),len(input_array),bins,sum_in_each_bin,0,0);
order.append(root);
best_solution=len(input_array);
#Algorithm start
cnt=0;
while(len(order)!=0):
    using_node=order.pop(0); #dfs order
    if(cnt!=0):
        using_node.addItemToBin(input_array[using_node.height],(using_node.height+1));
    #print(using_node.bins); //print the node that you are calculating bounds for
    using_node.calculateUpperBound(input_array)
    if(best_solution>using_node.upper_bound):
        best_solution=using_node.upper_bound;
        bin_status_of_best_solution=using_node.calculating_list;
        sum_status_of_bins=using_node.sum_bins_calculation_list;
    using_node.calculateLowerBound(math.ceil(sum))
    if(using_node.upper_bound==math.ceil(sum)):
        break
    if(using_node.lower_bound < best_solution and using_node.lower_bound != using_node.upper_bound):
        if(cnt==0):
            order.insert(0,Node(-1,-1,bins,sum_in_each_bin,0,0));
        else:
            for num in range(1,len(input_array)+1):
                order.insert(0,Node(-1,-1,bins,sum_in_each_bin,using_node.height+1,len(input_array)-num))
    cnt+=1;

printSolution(best_solution,bin_status_of_best_solution,sum_status_of_bins,math.ceil(sum),sum);


