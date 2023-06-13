from copy import deepcopy
class Node:
    def __init__(self,lower_bound,upper_bound,bins,sum_in_each_bin,height,child):
        self.lower_bound=lower_bound;
        self.upper_bound=upper_bound;
        self.bins=bins;
        self.sum_in_each_bin=sum_in_each_bin;
        self.height=height;
        self.child=child;
        self.amount_of_bins=0;
        self.calculating_list=[];
        self.sum_bins_calculation_list=[];
    def calculateUpperBound(self,input_array):
        self.calculating_list=deepcopy(self.bins[:]);
        self.sum_bins_calculation_list=self.sum_in_each_bin[:];
        i=self.height;
        for x in input_array[self.height:]:
            for q in range(0,len(input_array)):
                if(self.sum_bins_calculation_list[q] + x<=1):
                    self.calculating_list[q][i+1]=x;
                    self.sum_bins_calculation_list[q]+=x;
                    break;
            i+=1;
        cnt=0;
        for x in self.sum_bins_calculation_list:
            if (x>0):
                cnt+=1;
        self.upper_bound=cnt;
                
    def calculateLowerBound(self,opt):
        cnt=0;
        for x in self.sum_in_each_bin:
            if(x>0):
                cnt+=1;
        if (cnt>opt):
            return cnt;
        return opt;
            
    def addItemToBin(self,item,item_index):
        if(self.sum_in_each_bin[self.child]+item<=1):
            self.bins[self.child][item_index]=item;
            self.sum_in_each_bin[self.child]+=item;
    
