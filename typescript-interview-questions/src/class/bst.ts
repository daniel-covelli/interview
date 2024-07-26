import { NodeClass } from "./node";


export class Bst {
  public root?: NodeClass;

  constructor(root?: NodeClass) {
    this.root = root;
  }

  public insert(val: number) {
    if (this.root === undefined) {
      return (this.root = new NodeClass(val));
    }

    function bst(val: number, node?: NodeClass) {
      if (node === undefined) return;

      // no duplicate insertions
      if (node.val === val) return;

      if (node.val > val && node.left === undefined) {
        console.log('insertLeft');
        node.left = new NodeClass(val);
        return;
      }

      if (node.val < val && node.right === undefined) {
        console.log('insertRight');
        node.right = new NodeClass(val);
        return;
      }

      bst(val, node.left);
      bst(val, node.right);
    }

    bst(val, this.root);
  }
}
