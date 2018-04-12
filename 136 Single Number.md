# 136:Single Number

## Request

Given an array of integers, every element appears *twice* except for one. Find that single one.

**Note:**
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Solution

    class Solution {
    	public int singleNumber(int[] nums) {
    
            Map map = new HashMap();
    
            for (int i = 0; i < nums.length; i++){
    
                if( map.get(nums[i]) == null) map.put(nums[i],1);
    
                    else map.remove(nums[i]);
    
            }
    
            Iterator<Integer> i = map.keySet().iterator();
    
            while(i.hasNext()){
    
                int re = ((Integer)i.next()).intValue();
    
                return re;
    
            }
            return 0;
    }

However, this takes extra memory. So still try to find out a better solution.

Time complexity is O(n) , Space complexity is O(n)

## Better way

XOR — 0 ^ N = N , N ^ N = 0,just all ^ and get answer.

## 