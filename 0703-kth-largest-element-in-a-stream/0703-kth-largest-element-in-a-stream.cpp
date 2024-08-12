class KthLargest {
public:
    int x, K;
    map<int,int> mp;
    map<int,int>::iterator iter;
    KthLargest(int k, vector<int>& nums) {
        K = k;
        x=0;
        for(int i : nums)mp[-i]++;
        iter = mp.begin();
        while(iter != mp.end()){
            x+=(iter->second);
            if(x>=k || next(iter,1) == mp.end()) break;
            iter++;
        }
    }
    
    int add(int val) {
        mp[-val]++;
        if(mp.size()==1){
            iter = mp.begin();
            x = iter->second;
        }
        else if(val >= -iter->first) x++;
        
        while(x<K){
            iter++;
            x += iter->second;
        }
        while(x-iter->second>=K){
            x-=iter->second;
            iter--;
        }
        return -(iter->first);
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */