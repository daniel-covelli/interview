export class NodeClass {
  public val: number;
  public left?: NodeClass;
  public right?: NodeClass;

  constructor(val: number, left?: NodeClass, right?: NodeClass) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
