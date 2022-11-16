# Linear structure

- Stack
- Queue

# Tree

- Thread search tree （ 3个值 2个指针一个节点，整个连通）

  ![Thread Search Tree](/Users/Isacclee/Documents/Study/se/OUT/Review/Thread Search Tree.png)

## Trie tree
208


# Heap

- 数组 ，从1 开始存 [i/2]为父，2i 左 2i+1右
- d-heap

# Algorithm

## Sort

### Insert Sort

对要插入的元素 挪动前面的每一位 查到正确位置

``` c
voidInsertionSort( ElementTypeA[ ], intN ) 

{

      int j, P; 

      ElementType  Tmp; 

      for (P = 1; P < N; P++ ) { 

  Tmp = A[ P ];  /* the next coming card */

  for (j = P; j > 0 && A[ j - 1 ] > Tmp; j-- ) 

        A[j ] = A[ j - 1 ]; 

        /* shift sorted cards to provide aposition 

                       for the new coming card*/

  A[ j ] = Tmp; /* place the new card at the proper position */

      }  /* end for-P-loop */

}

```

## lower bond

O(N+I) I = number of inversion -> average inversion i  = n(n-1)/4

-> sort algorithm just swap adjacement requires N2 on average

## Shell

找hk ，对 隔了hk的 排序

```c
void Shellsort( ElementType A[ ], int N ) 
{ 
      int  i, j, Increment; 
      ElementType  Tmp; 
      for ( Increment = N / 2; Increment > 0; Increment /= 2 )  
	/*h sequence */
	for ( i = Increment; i < N; i++ ) { /* insertion sort */
	      Tmp = A[ i ]; 
	      for ( j = i; j >= Increment; j - = Increment ) 
		if( Tmp < A[ j - Increment ] ) 
		      A[ j ] = A[ j - Increment ]; 
		else 
		      break; 
		A[ j ] = Tmp; 
	} /* end for-I and for-Increment loops */
}
```

一般是相对为素数或者 hk = 2^k === Hibbard 序列 复杂度一般不是纯n2 是n的几分之几次，比如hibbard  ：avg 5/4 worst 3/2

Sedgewick's sequence 比较屌 avg 7/6 ,worst4/3

### Heap sort

num of comparison 2NlogN - O(NloglogN)



# Interesting:
141.