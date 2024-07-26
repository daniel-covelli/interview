import { Bst } from "../../src/class/bst";
import { NodeClass } from "../../src/class/node";


describe('sum module', () => {
    test('adds 1 + 2 to equal 3', () => {
        const tree = new Bst(new NodeClass(1))
      expect(tree.root).toBe(3);
    });
  });