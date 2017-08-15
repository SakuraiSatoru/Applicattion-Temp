using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace test
{
    public class BinaryTreeNode<T> {
        private T data; //数据元素
        private BinaryTreeNode<T> left, right; //指向左、右孩子结点的链
        public BinaryTreeNode(){
            left = right = null;
        }
        //构造有值结点
        public BinaryTreeNode(T d) {
            data = d;
            left = right = null;
        }
        public T Data {
            get { return data; }
            set { data = value; }
        }
        public BinaryTreeNode<T> Left {
            get { return left; }
            set { left = value; }
        }
        public BinaryTreeNode<T> Right {
            get { return right; }
            set { right = value;}
        }

        //中根次序遍历二叉树(递归算法）
        public void TraversalInOrder(List<T> sql) {
                BinaryTreeNode<T> q = this.Left;
                if (q != null)
                    q.TraversalInOrder(sql);
                sql.Add(this.Data);
                q = this.Right;
                if (q != null)
                    q.TraversalInOrder(sql);
        }
        
        public void check(List<int> sql){
            int i,k;
            k=0;
            for(i=1;i<sql.Count;i++)

            {
            if(sql[i+1] > sql[i])
            {
                k=k+1;
            }
            if(k==sql.Count)
            Console.WriteLine("是搜索二叉树");
            }
        }


        }

        //二叉树结点类
    public class BinaryTree<T> {
        protected BinaryTreeNode<T> root; //指向二叉树的根结点
        public BinaryTreeNode<T> Root {
            get { return root; }
            set { root = value; }
        }
        public BinaryTree() { //构造空二叉树
            root = null;
        }
    }



        

        

  

}
