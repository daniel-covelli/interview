import {NodeClass} from './node';

export class Bst {
  root?: NodeClass;

  constructor(root?: NodeClass) {
    this.root = root;
  }

  private nullCheck(val: number) {
    if (this.root === undefined) {
      this.root = new NodeClass(val);
      return true;
    }
    return false;
  }

  // Run time 0(log n)
  public insert(val: number) {
    if (this.nullCheck(val)) return;

    function dfs(val: number, node?: NodeClass) {
      if (node === undefined) return;

      // no duplicate insertions
      if (node.val === val) return;

      if (node.val > val && node.left === undefined) {
        node.left = new NodeClass(val);
        return;
      }

      if (node.val < val && node.right === undefined) {
        node.right = new NodeClass(val);
        return;
      }

      if (val < node.val) {
        dfs(val, node.left);
      } else {
        dfs(val, node.right);
      }
    }

    dfs(val, this.root);
  }

  // Run time 0(n)
  public balance() {
    function bstToInOrderArray(node?: NodeClass): number[] {
      if (node === undefined) return [];

      const left = bstToInOrderArray(node.left);
      const right = bstToInOrderArray(node.right);

      return [...left, node.val, ...right];
    }

    function buildBalancedBst(arr: number[]) {
      const len = arr.length;
      if (len === 0) return undefined;

      const middle = Math.floor(len / 2);
      const root = new NodeClass(arr[middle]);

      root.left = buildBalancedBst(arr.slice(0, middle));
      root.right = buildBalancedBst(arr.slice(middle + 1));

      return root;
    }

    const sortedArray = bstToInOrderArray(this.root);
    this.root = buildBalancedBst(sortedArray);
  }

  // Run time 0(n)
  public bstToArray() {
    if (!this.root) return [];

    const results = [];
    let level: (NodeClass | undefined)[] = [this.root];

    while (level.length) {
      const newLevel = [];

      for (const next of level) {
        results.push(next?.val);

        if (next && (next.left || next.right)) {
          newLevel.push(next.left);
          newLevel.push(next.right);
        }
      }

      level = newLevel;
    }

    return results;
  }
}
