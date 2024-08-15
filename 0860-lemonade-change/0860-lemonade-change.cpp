class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int a=0,b=0;
        for(int i : bills){
            if(i == 5) a++;
            else if(i==10){
                if(a){
                    a--;
                }
                else{
                    return false;
                }
                b++;
            }
            else if(i==20){
                if(a&&b){
                    a--;
                    b--;
                }
                else if(a>=3){
                    a-=3;
                }
                else return false;
            }
        }
        return true;
    }
};