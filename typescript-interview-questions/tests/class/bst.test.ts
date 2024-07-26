import {Bst} from '../../src/class/bst';
import {NodeClass} from '../../src/class/node';

describe('bst class', () => {
  test('insert', () => {
    const tree = new Bst(new NodeClass(1));
    tree.insert(2);
    expect(tree.root).not.toBeUndefined();
    expect(tree.root?.val).toBe(1);
    expect(tree.root?.right?.val).toBe(2);
  });
});
