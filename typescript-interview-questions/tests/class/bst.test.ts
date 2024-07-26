import {Bst} from '../../src/class/bst';
import {NodeClass} from '../../src/class/node';

describe('bst class', () => {
  describe('insert method', () => {
    test('insert into undefined root', () => {
      const tree = new Bst();
      tree.insert(199);

      expect(tree.root?.val).toBe(199);
    });

    test('basic insert', () => {
      const tree = new Bst(new NodeClass(1));
      tree.insert(0);
      tree.insert(2);
      tree.insert(3);
      tree.insert(-1);

      expect(tree.root?.val).toBe(1);
      expect(tree.root?.left?.val).toBe(0);
      expect(tree.root?.left?.left?.val).toBe(-1);
      expect(tree.root?.left?.right).toBeUndefined();
      expect(tree.root?.right?.val).toBe(2);
      expect(tree.root?.right?.left).toBeUndefined();
      expect(tree.root?.right?.right?.val).toBe(3);
      expect(tree.root?.right?.right?.left).toBeUndefined();
      expect(tree.root?.right?.right?.right).toBeUndefined();
    });

    test('create unbalanced bst', () => {
      const tree = new Bst(new NodeClass(100));
      tree.insert(99);
      tree.insert(98);
      tree.insert(97);
      tree.insert(96);

      expect(tree.root?.val).toBe(100);
      expect(tree.root?.left?.val).toBe(99);
      expect(tree.root?.right).toBeUndefined();
      expect(tree.root?.left?.left?.val).toBe(98);
      expect(tree.root?.left?.right).toBeUndefined();
      expect(tree.root?.left?.left?.left?.val).toBe(97);
      expect(tree.root?.left?.left?.right).toBeUndefined();
      expect(tree.root?.left?.left?.left?.left?.val).toBe(96);
      expect(tree.root?.left?.left?.left?.right).toBeUndefined();
      expect(tree.root?.left?.left?.left?.left?.left).toBeUndefined();
      expect(tree.root?.left?.left?.left?.left?.right).toBeUndefined();
    });

    test("doesn't add duplicates", () => {
      const tree = new Bst(new NodeClass(100));
      tree.insert(99);
      tree.insert(99);

      expect(tree.root?.val).toBe(100);
      expect(tree.root?.left?.val).toBe(99);
      expect(tree.root?.right).toBeUndefined();
      expect(tree.root?.left?.left).toBeUndefined();
      expect(tree.root?.left?.right).toBeUndefined();
    });
  });

  describe('balance method', () => {
    test('will do nothing if root is undefined', () => {
      const tree = new Bst();
      tree.balance();

      expect(tree.root).toBeUndefined();
    });

    test('will balance a left-skewed bst', () => {
      const tree = new Bst(new NodeClass(100));
      tree.insert(99);
      tree.insert(98);
      tree.insert(97);
      tree.insert(96);
      tree.balance();

      expect(tree.root?.val).toBe(98);
      expect(tree.root?.left?.val).toBe(97);
      expect(tree.root?.right?.val).toBe(100);
      expect(tree.root?.left?.left?.val).toBe(96);
      expect(tree.root?.left?.right).toBeUndefined();
      expect(tree.root?.left?.left?.left).toBeUndefined();
      expect(tree.root?.left?.left?.right).toBeUndefined();
      expect(tree.root?.right?.left?.val).toBe(99);
      expect(tree.root?.right?.right).toBeUndefined();
      expect(tree.root?.right?.left?.left).toBeUndefined();
      expect(tree.root?.right?.left?.right).toBeUndefined();
    });

    test('will balance a right-skewed bst', () => {
      const tree = new Bst(new NodeClass(0));
      tree.insert(1);
      tree.insert(2);
      tree.insert(3);
      tree.balance();

      expect(tree.root?.val).toBe(2);
      expect(tree.root?.left?.val).toBe(1);
      expect(tree.root?.right?.val).toBe(3);
      expect(tree.root?.left?.left?.val).toBe(0);
      expect(tree.root?.left?.right).toBeUndefined();
      expect(tree.root?.left?.left?.left).toBeUndefined();
      expect(tree.root?.left?.left?.right).toBeUndefined();
      expect(tree.root?.right?.left).toBeUndefined();
      expect(tree.root?.right?.right).toBeUndefined();
    });

    test('will return a perfect bst', () => {
      const tree = new Bst();

      for (let i = 1; i < 8; i++) {
        tree.insert(i);
      }
      tree.balance();

      expect(tree.bstToArray()).toEqual([4, 2, 6, 1, 3, 5, 7]);
    });
  });

  describe('bstToArray method', () => {
    test('will return the array representation of a normal bst', () => {
      const tree = new Bst(new NodeClass(2));
      tree.insert(1);
      tree.insert(3);
      tree.insert(4);
      tree.insert(-1);
      expect(tree.bstToArray()).toEqual([2, 1, 3, -1, undefined, undefined, 4]);
    });

    test('will return the array representation of a skewed bst', () => {
      const tree = new Bst(new NodeClass(100));
      tree.insert(50);
      tree.insert(23);
      tree.insert(-1);

      expect(tree.bstToArray()).toEqual([
        100,
        50,
        undefined,
        23,
        undefined,
        -1,
        undefined,
      ]);
    });
  });

  describe('delete method', () => {
    test('will delete a leaf node', () => {
      const tree = new Bst(new NodeClass(1));
      tree.insert(2);
      tree.delete(2);

      expect(tree.bstToArray()).toEqual([1]);
    });

    test('will delete a non-leaf node', () => {
      const tree = new Bst();

      for (let i = 1; i < 8; i++) {
        tree.insert(i);
      }
      tree.balance();

      tree.delete(6);

      expect(tree.bstToArray()).toEqual([4, 2, 7, 1, 3, 5, undefined]);
    });

    test('will delete a the root node', () => {
      const tree = new Bst();

      for (let i = 1; i < 8; i++) {
        tree.insert(i);
      }
      tree.balance();

      tree.delete(4);
      expect(tree.bstToArray()).toEqual([5, 2, 6, 1, 3, undefined, 7]);
    });
  });
});
