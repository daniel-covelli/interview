import {longestSubstring} from '../src/longest-substring';

describe('longestSubstring without repeating characters', () => {
  test('finds max subset for normal case', () => {
    expect(longestSubstring('banana')).toBe('ban');
  });

  test('finds singular character when all values are the same', () => {
    expect(longestSubstring('bbbbb')).toBe('b');
  });

  test('returns empty string if empty string is passed', () => {
    expect(longestSubstring('')).toBe('');
  });

  test('returns character if character is passed', () => {
    expect(longestSubstring('a')).toBe('a');
  });
});
