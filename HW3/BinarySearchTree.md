## BinarySearchTree
> BinarySearchTree簡介

+ Binary Search Tree和Binary Tree的不同是，Binary Search Tree是有排序過的Binary Tree。

+ 必須符合CurrentNode.left.val <= CurrentNode.val < CurrentNode.right.val
+ 由TreeNode所組成，每一個TreeNode一定要紀錄value. left(左節點). right(右節點)。
+ 有新增、搜尋、刪除、替換四大必備功能。
+ 讀BST有三種不同走訪方法：
    + Preorder : root => left => right (我使用的是這個)
    + Inorder : left => root => right
    + Postorder : left => right => root
+ BST的缺點是容易不平衡，最糟的情況是退化成Linked-list，WorstCase會變成O(n)，所以Red Black Tree的出現就是在BST的基礎上加以改良，Red Black Tree能夠在insertNode的時候，隨時讓Tree保持平衡，那麼搜尋時間就會穩定維持O(logn)。

> BinarySearchTree功能說明
+ 新增: 在Tree中新增節點，新增的標準如下 =>
    + 當節點的value小於等於root.value時，則新增在root.left。
    + 當節點的value大於root.value時，則新增在root.right。
    + 這次設計的比較特別的是，假設我想在Tree1這棵已建好的樹裡新增Node，我依照上述標準新增在Tree1後，BST Function本身的self.root也會同時被更新成Tree1。
+ 搜尋: 搜尋符合特定值的節點，並回傳離root最近的Node。
    + 假設要搜尋Tree1裡的某一個值，我會先從Tree1開始(Current)，只要符合上述標準，Current會依序向下移動，碰到以下兩種情況就會停止。
    + 搜尋成功: Current.val == 特定值，就回傳Current。
    + 搜尋失敗: Current is None，代表搜尋失敗，回傳None。
+ 刪除: 刪除符合特定值的節點，此次是重新建立BST。
    + 只要Tree中符合特定值都會一起刪掉，所以會打亂原本的BST結構，因此這次是重新建立BST，並覆蓋掉原本的BST。
    + 在特定測資下，新建的BST的高度不會超過原BST的樹高。
    + 新建的BST的root是選擇所有數值的中間點數值，因此能在特定測資下保持新建樹高不大於原樹高的規定。
+ 修改: 修改符合特定值的節點，將其一併換成新的值，此次也是是重建BST。
    + 只要Tree符合特定值的都會一起替換成新的值，也會打亂原本的BST結構，因此這次也是重新建立BST，並覆蓋掉原本BST。
    + 在特定測資下，新建的BST的高度不會超過原BST高度。
    + 新建的BST的root是選擇所有數值的中間點數值，因此能特定測資下保持新建樹高不大於原樹高的規定。

> 參考連結
+ [我自己寫的BinarySearchTree作業](HW3/BinarySearchTree.ipynb)

+ [Binary Search Tree: Intro(簡介)](http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html)
  
+ [a simple implementation of a Binary Search Tree in Python](https://gist.github.com/jakemmarsh/8273963)

+ [Binary Tree and Binary Search Tree in Data Structure](https://www.youtube.com/watch?time_continue=1&v=7vw2iIdqHlM&feature=emb_logo)

+ [Binary Trees : Introduction and Traversal Algorithms](https://www.youtube.com/watch?v=6oL-0TdVy28)

