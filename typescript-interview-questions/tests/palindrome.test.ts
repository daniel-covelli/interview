import {palindrome} from '../src/palindrome';

describe('palindrome', () => {
  test('returns true if string is a valid palindrome', () => {
    expect(palindrome('ava')).toBe(true);
  });

  test('returns true with a string that contains special characters', () => {
    const s = 'A man, a plan, a canal: Panama';

    expect(palindrome(s)).toBe(true);
  });

  test('returns true if string is only whitespace', () => {
    expect(palindrome(' ')).toBe(true);
  });
});
