# AVL Tree Implementation Documentation

This repository contains an implementation of an **AVL Tree** with the following key components:

- **`AVLNode` Class**: Represents a single node in the AVL tree.
- **`AVLTree` Class**: Represents the AVL tree itself, containing nodes and methods for managing the tree.

## `AVLNode` Class

The `AVLNode` class defines the structure and behavior of a node in the AVL tree. Below is an overview of its methods:

### **Constructor (`__init__`)**
Initializes the node with:
- A **key** and **value**.
- References to the left child, right child, parent, and height.

---

### **Node Accessors**
- **`get_left` / `get_right`**: Returns the left or right child of the node. If the child is `None`, returns a virtual node.
- **`get_parent`**: Returns the parent node if it exists; otherwise, returns `None`.
- **`get_key` / `get_value`**: Returns the key or value of the node. If the node is virtual or `None`, returns `None`.
- **`get_height`**: Returns the height of the node. If the node is virtual, returns `-1`.
- **`is_real_node`**: Returns `True` if the node is real (not virtual); otherwise, returns `False`.

---

### **Node Operations**
- **`delete_node_only`**: Deletes the node by adjusting pointers in the tree. Calls:
  - **`successor`**: Finds the in-order successor of the node using the `min` helper function.
  - **`min`**: Finds the minimum node in the subtree. The complexity is \(O(\log n)\).

- **`balance_factor`**: Computes the balance factor (difference in height between the left and right child) of the node. Complexity: \(O(1)\).

- **`update_height`**: Updates the node's height based on its children. Complexity: \(O(1)\).

---

## `AVLTree` Class

The `AVLTree` class implements the AVL tree structure and provides methods to manipulate and query the tree.

### **Constructor (`__init__`)**
Initializes the AVL tree with:
- A root node (`None` initially).
- Size of the tree (`0` initially).

---

### **Tree Operations**

#### **Search**
- **`search(key)`**: Searches for a node with the given key in the tree.
- Complexity: \(O(\log n)\) in the worst case.

#### **Insert**
- **`insert(key, value)`**: Inserts a node with the given key and value into the tree. Balances the tree after insertion.
- Uses helper methods:
  - **`balance_factor`**
  - **`update_height`**
  - **`left_rotation` / `right_rotation`**
- Complexity: \(O(\log n)\).

#### **Delete**
- **`delete(node)`**: Deletes the given node and balances the tree.
- Uses:
  - **`delete_node_only`**
  - **`left_rotation` / `right_rotation`**
- Complexity: \(O(\log n)\).

#### **Conversion to Array**
- **`avl_to_array()`**: Converts the tree into a sorted array using an in-order traversal.
- Complexity: \(O(n)\).

#### **Get Size**
- **`size()`**: Returns the number of nodes in the tree. Uses the `avl_to_array` helper. Complexity: \(O(n)\).

#### **Split**
- **`split(node)`**: Splits the tree into two subtrees based on the given node:
  - The left subtree contains all keys less than the node's key.
  - The right subtree contains all keys greater than the node's key.
- Uses the **`join`** operation for reconstruction.
- Complexity: \(O(\log n)\).

#### **Join**
- **`join(other_tree, key, value)`**: Merges the current tree with another tree using a new node (key, value) as the root.
- Adjusts the tree balance using rotations.
- Complexity: \(O(\log n)\).

#### **Get Root**
- **`get_root()`**: Returns the root of the tree. Complexity: \(O(1)\).

---

### **Rotations**
- **`left_rotation(node)` / `right_rotation(node)`**:
  - Balances the tree by rotating nodes left or right.
  - Updates the heights of the affected nodes.
  - Complexity: \(O(1)\).

---

### **Helper Functions**
- **`min(node)`**: Finds the minimum node in the subtree rooted at the given node.
  - Complexity: \(O(\log n)\).

- **`successor(node)`**: Finds the in-order successor of the given node.
  - Complexity: \(O(\log n)\).

---

## **Complexity Summary**

| Operation                  | Complexity    |
|----------------------------|---------------|
| Search                     | \(O(\log n)\) |
| Insert                     | \(O(\log n)\) |
| Delete                     | \(O(\log n)\) |
| Convert to Array           | \(O(n)\)      |
| Get Size                   | \(O(n)\)      |
| Split                      | \(O(\log n)\) |
| Join                       | \(O(\log n)\) |
| Rotations                  | \(O(1)\)      |
| Min / Successor            | \(O(\log n)\) |

---

## **Experimental Results**

### **Split Analysis**
The cost of splitting is influenced by the cost of performing `join` operations. Since AVL trees maintain a height difference of at most 1 between subtrees, the cost of a `join` operation is low on average.

#### **Key Observations**
1. **Random Splits:**  
   The average cost of a `join` operation ranges between **2 and 3**.
2. **Maximal Split Cost:**  
   For maximal splits (e.g., splitting on the largest node in the left subtree), the process involves repeated `join` operations while traversing to the root. This results in higher costs, but they are still \(O(\log n)\) due to the height constraint.

---

### **Table: Experimental Costs**

| Split ID | Random Join Cost | Maximal Join Cost | Average Join Cost (Maximal Split) |
|----------|------------------|-------------------|-----------------------------------|
| 12       | 3.1              | 5                 | 2.66                              |
| 13       | 2.72             | 5                 | 2.3                               |
| 15       | 2.54             | 5                 | 2.76                              |
| 17       | 3.066            | 6                 | 3.230                             |
| 19       | 2.705            | 7                 | 3.2                               |
| 22       | 3.052            | 5                 | 3.166                             |

---

### **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-repo-url>/AVLTree.git
   cd AVLTree
