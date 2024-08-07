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

  test('returns false if string is not a palindrome', () => {
    expect(palindrome('race a car')).toBe(false);
  });

  test('returns true in a weird scenario', () => {
    expect(palindrome('$ a  % 123 a 123 67^^))')).toBe(true);
  });
});
