# Data Structure and Algorithm

## Self-introductiong
    我是閔慈!這裡是我的學習筆記!


## Helpers:
1. CS50 : [CS50 YouTube](https://www.youtube.com/channel/UCcabW7890RKJzL968QWEykA)
2. Debug : Spyder
3. Test way : eval
4. Recurrsive : [費氏數列](https://emn178.pixnet.net/blog/post/91987861)
5. Markdown : [超好用Markdown筆記](http://xianbai.me/learn-md/index.html) 
6. 如果你的ipynb檔一直在Github上Reload失敗 : [不如試試這個吧!免安裝](https://nbviewer.jupyter.org/) 
7. Jupyter Notebook快捷鍵 - Part1: [Jupyter Notebook 快捷轉換code和markdown](https://blog.csdn.net/qq_35423500/article/details/79565146)
8. Jupyter Notebook快捷鍵 - Part2: Control + / => 註解
 
## Data Structure & Algorithm:
+ Week1-Linkedlist: [Linkedlist](Week1/Linkedlist.ipynb)、[Linkedlist參考圖片](Week1/Linked-list1.png)
+ Week2-Stack & Queue: [Stack&Queue](Week2/Stack&Queue學習歷程&流程圖.ipynb)、[Stack&Queue流程圖](Week2/Stack&Queue.png)
+ Week3-Set: [Set](https://github.com/mandy331/Data-Structure_PythonNote/blob/master/Week3/Set.py)
+ Week4-Insertion Sort: [Insertion Sort](https://github.com/mandy331/Data-Structure_PythonNote/blob/master/Week4/InsertionSort.py)、[InsertionSort流程圖](Week4/InsertionSort.png)
+ Week4-Quick Sort: [QuickSort](Week4/QuickSort學習歷程&流程圖.ipynb)、[QuickSort流程圖](https://github.com/mandy331/Data-Structure_PythonNote/blob/master/Week4/QuickSort.png)
+ Week7-Heap Sort: [HeapSort](Week7/HeapSort流程圖&說明.ipynb)、[HeapSort流程圖](Week7/HeapSort.png)
+ Week7-Merge Sort: [MergeSort](Week7/MergeSort流程圖&說明.ipynb)、[MergeSort流程圖](Week7/MergeSort.png)
+ Week8-Binary Search Tree: [BinarySearchTree](Week8/BinarySearchTree學習歷程&流程圖.ipynb)、[BST流程圖](Week8/BinarySearchTree.png)、[BinarySearchTree功能說明](Week8/BinarySearchTree功能說明.md)
+ Week10-Hash Table: [HashTable](Week10/HashTable學習歷程&流程圖.ipynb)、[HashTable流程圖](Week10/HashTable.png)
+ Week12-Breadth First Search & Depth First Search: [BFS&DFS](Week12/BFS&DFS的學習歷程&流程圖.ipynb)、[BFS流程圖](Week12/BFS.png)、[DFS流程圖](Week12/DFS.png)


## Final Exam CheatSheet:
1. Linkedlist:
+ 功能: 查詢、新增、刪除
+ 元素: Node(儲存value. next pointer). Linkedlist(head. length)
+ 情況:
    + 查詢(get(self, idx)):
        + 1. idx不在範圍裡:return None 
        + 2. idx在範圍裡，就走訪到idx: return value
    + 新增(addAtHead(x), addAtTail(x), addAtIndex(idx, x)): 
        + 1. addAtHead. addAtTail: 
            + 若length == 0: 新增於head
        + 2. addAtIndex:
            + idx不在範圍裡: pass
            + 加在頭: addAtHead
            + 加在尾: addAtTail
            + 加中間: 走訪到idx前一個
    + 刪除(deleteAtIndex(idx)):
        + 1. idx不在範圍裡: pass
        + 2. linkedlist的長度為0: pass
        + 3. 刪開頭(idx == 0):
            + 當length == 1，刪第一個
            + 當length > 1
        + 4. 刪尾巴(idx == length - 1 and length>=2)
        + 5. 刪中間
